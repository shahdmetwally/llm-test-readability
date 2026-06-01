import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_with_none():
    """Test that YieldFromTransformer can be instantiated and visit() called with None input."""
    # Initialize the transformer with no source tree (None)
    none_input = None
    transformer = yield_from.YieldFromTransformer(none_input)

    # Visit a None node — verifies the transformer handles None without raising
    transformer.visit(none_input)

def test_yield_from_transformer_instantiation_with_none():
    """Test that YieldFromTransformer can be instantiated with None as the AST node argument."""
    # Pass None as the root node, representing an empty or absent AST input
    none_node = None
    transformer = yield_from.YieldFromTransformer(none_node)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """
    Test that YieldFromTransformer.visit() can process a While node
    whose test and body are constructed from None values without raising errors.
    """
    # Use None as a placeholder argument for the transformer and AST node fields
    none_value = None
    inner_list = [none_value, none_value]

    # Instantiate the transformer with no source tree (None)
    yield_from_transformer = yield_from.YieldFromTransformer(none_value)

    # Build a While node using two lists of None values as positional arguments
    while_args = [inner_list, inner_list]
    while_node = ast3.While(*while_args)

    # Visit the While node; verifies the transformer handles this input without error
    visited_result = yield_from_transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """
    Test that YieldFromTransformer.visit() handles a While node constructed
    with None positional arguments and a dict of keyword arguments that
    include non-string keys mapping to the transformer itself.
    This exercises the visitor dispatch for ast.While nodes.
    """
    none_value = None

    # Instantiate the transformer with no tree (None root)
    transformer = yield_from.YieldFromTransformer(none_value)

    # Build positional args list with two None values (test, body placeholders)
    positional_args = [none_value, none_value]

    # Use an arbitrary string as the repeated keyword argument key
    keyword_key = "P+>W*v\nDN{M8\x0bLk"

    # Construct kwargs mapping the same key multiple times to the transformer
    keyword_args = {
        keyword_key: transformer,
        keyword_key: transformer,
        keyword_key: transformer,
    }

    # Build a While AST node using the positional and keyword arguments
    while_node = ast3.While(*positional_args, **keyword_args)

    # Visit the While node — verifies the transformer can process it without error
    result = transformer.visit(while_node)