import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_with_none_node():
    """Test that YieldFromTransformer can be instantiated and visit a None node without raising."""
    # Use None as the AST node argument (edge-case: no real AST tree provided)
    none_node = None

    # Instantiate the transformer with a None tree
    transformer = yield_from.YieldFromTransformer(none_node)

    # Visiting a None node should not raise an exception
    transformer.visit(none_node)

def test_yield_from_transformer_instantiates_with_none_argument():
    """Test that YieldFromTransformer can be instantiated with None as its argument."""
    # Pass None as the argument to the transformer constructor
    none_argument = None
    transformer_instance = yield_from.YieldFromTransformer(none_argument)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """Test that YieldFromTransformer.visit() handles a While node constructed with None arguments without error."""

    # Use None as a stand-in for all node arguments
    none_value = None

    # Build the argument list for the While node (two None entries)
    while_args = [none_value, none_value]

    # Instantiate the transformer with no tree context
    transformer = yield_from.YieldFromTransformer(none_value)

    # Wrap the while_args list twice to form the positional args for While(*)
    while_constructor_args = [while_args, while_args]

    # Construct an AST While node using the None-valued arguments
    while_node = ast3.While(*while_constructor_args)

    # Visit the While node — should complete without raising
    result_node = transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """Test that YieldFromTransformer.visit() processes a While node built with None positional args and a repeated-key keyword dict."""

    none_value = None

    # Instantiate the transformer with no tree (None)
    transformer = yield_from.YieldFromTransformer(none_value)

    # Positional arguments for the While node constructor (both None)
    while_positional_args = [none_value, none_value]

    # Arbitrary auto-generated string used as keyword argument key
    keyword_key = "P+>W*v\nDN{M8\x0bLk"

    # Keyword arguments dict with repeated key mapping to the transformer instance
    while_keyword_args = {
        keyword_key: transformer,
        keyword_key: transformer,
        keyword_key: transformer,
    }

    # Construct a While AST node using the prepared positional and keyword args
    while_node = ast3.While(*while_positional_args, **while_keyword_args)

    # Visit the While node with the transformer; result captures any returned AST
    visited_result = transformer.visit(while_node)

