import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_with_none_does_not_raise():
    """Test that YieldFromTransformer can be instantiated and visited with None without raising."""
    none_input = None

    # Instantiate the transformer with a None node (simulating an absent AST node)
    transformer = yield_from.YieldFromTransformer(none_input)

    # Visiting with None should complete without error
    transformer.visit(none_input)

def test_yield_from_transformer_instantiates_with_none_argument():
    """Test that YieldFromTransformer can be instantiated with None as its argument."""

    # Pass None as the argument, representing an absent or unspecified AST node
    none_argument = None
    transformer_instance = yield_from.YieldFromTransformer(none_argument)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """Test that YieldFromTransformer.visit() handles a While node constructed with None arguments without error."""

    # Use None as the placeholder value for all node arguments
    none_value = None

    # Build a list of None arguments to pass into the While node constructor
    none_args = [none_value, none_value]

    # Instantiate the transformer with no tree (None)
    transformer = yield_from.YieldFromTransformer(none_value)

    # Construct the argument list for the While AST node
    while_args = [none_args, none_args]

    # Create a While AST node using the None-valued arguments
    while_node = ast3.While(*while_args)

    # Visit the While node — should complete without raising
    result_ast = transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node_with_repeated_keyword_args():
    """Test that YieldFromTransformer.visit() processes a While node built with None positional args and repeated keyword args."""

    # Use None as placeholder for required transformer tree argument
    none_value = None

    # Instantiate the transformer with no tree context
    transformer = yield_from.YieldFromTransformer(none_value)

    # Build positional args list for the While node (both None)
    while_positional_args = [none_value, none_value]

    # Arbitrary auto-generated string used as keyword argument key
    keyword_key = "P+>W*v\nDN{M8\x0bLk"

    # Build keyword args dict mapping the key to the transformer (repeated three times)
    while_keyword_args = {
        keyword_key: transformer,
        keyword_key: transformer,
        keyword_key: transformer,
    }

    # Construct a While AST node using the positional and keyword arguments
    while_node = ast3.While(*while_positional_args, **while_keyword_args)

    # Visit the While node with the transformer; result is stored but not asserted
    visited_result = transformer.visit(while_node)

