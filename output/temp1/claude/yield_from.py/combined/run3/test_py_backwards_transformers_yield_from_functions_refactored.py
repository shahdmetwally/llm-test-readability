import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_accepts_none():
    """Test that YieldFromTransformer can be instantiated with None and visit None without raising."""
    # Use None as the input to verify the transformer handles absence of an AST node gracefully
    none_input = None

    # Instantiate the transformer with None (no specific AST node context)
    transformer = yield_from.YieldFromTransformer(none_input)

    # Invoke visit with None to confirm no exception is raised
    transformer.visit(none_input)

def test_yield_from_transformer_instantiation_with_none():
    """Test that YieldFromTransformer can be instantiated with None as its argument."""
    # Pass None to verify the transformer accepts a missing/null node argument
    none_argument = None
    transformer_instance = yield_from.YieldFromTransformer(none_argument)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """Test that YieldFromTransformer.visit() handles a While node built with None arguments."""

    # Use None as a stand-in for all optional AST node fields
    none_value = None

    # Build the argument list passed to the While constructor (test=None, body=None)
    none_args = [none_value, none_value]

    # Instantiate the transformer with no tree (None)
    transformer = yield_from.YieldFromTransformer(none_value)

    # Pack the none_args list twice to satisfy While's positional parameters
    while_args = [none_args, none_args]

    # Construct a While AST node using the null arguments
    while_node = ast3.While(*while_args)

    # Visit the While node; this should complete without raising an exception
    result = transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node():
    """Test that YieldFromTransformer.visit() processes an AST While node built with None args and string keyword args."""

    # Use None as the tree argument for the transformer (no parent tree needed)
    none_arg = None

    # Instantiate the transformer with no parent tree
    transformer = yield_from.YieldFromTransformer(none_arg)

    # Positional arguments for the While node constructor (both None)
    while_positional_args = [none_arg, none_arg]

    # Keyword key used for all entries; duplicate keys mean only the last value survives in Python
    keyword_key = "P+>W*v\nDN{M8\x0bLk"

    # Keyword arguments dict for the While node (three entries with identical keys)
    while_keyword_args = {
        keyword_key: transformer,
        keyword_key: transformer,
        keyword_key: transformer,
    }

    # Construct the AST While node using the positional and keyword arguments
    while_node = ast3.While(*while_positional_args, **while_keyword_args)

    # Visit the While node with the transformer; should complete without error
    visited_result = transformer.visit(while_node)