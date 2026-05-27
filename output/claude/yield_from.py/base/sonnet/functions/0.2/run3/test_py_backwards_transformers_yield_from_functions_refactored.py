import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_with_none():
    """Test that YieldFromTransformer can be instantiated and visit() called with None input."""
    # Use None as the AST node argument (edge case: no real AST tree provided)
    none_node = None

    # Instantiate the transformer with None as the tree argument
    transformer = yield_from.YieldFromTransformer(none_node)

    # Invoke visit() with None — verifies the transformer handles a None node gracefully
    transformer.visit(none_node)

def test_yield_from_transformer_initializes_with_none_tree():
    """Test that YieldFromTransformer can be instantiated with a None AST tree node."""
    # A None value is passed as the AST tree, representing an empty or absent syntax tree
    ast_tree = None
    yield_from_transformer = yield_from.YieldFromTransformer(ast_tree)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """
    Test that YieldFromTransformer.visit() can process a While AST node
    constructed with None as its condition and body arguments without raising.
    """
    # Use None as a placeholder for missing AST child nodes
    none_value = None
    inner_list = [none_value, none_value]

    # Instantiate the transformer with no initial tree (None)
    yield_from_transformer = yield_from.YieldFromTransformer(none_value)

    # Build a While node using two lists of None values as positional args
    while_args = [inner_list, inner_list]
    while_node = ast3.While(*while_args)

    # Visit the While node; verifies the transformer handles it without error
    visited_result = yield_from_transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """
    Test that YieldFromTransformer.visit() can process an ast.While node
    constructed with None positional arguments and a dict of keyword arguments
    mapping an arbitrary string key to the transformer instance itself.
    """
    none_value = None

    # Instantiate the transformer with no tree (None root)
    transformer = yield_from.YieldFromTransformer(none_value)

    # Build positional args list: both test and body are None
    positional_args = [none_value, none_value]

    # Use an arbitrary string as the keyword argument key
    keyword_key = "P+>W*v\nDN{M8\x0bLk"

    # Build keyword arguments mapping the key to the transformer instance
    keyword_args = {
        keyword_key: transformer,
        keyword_key: transformer,
        keyword_key: transformer,
    }

    # Construct an ast.While node using the None positional args and keyword args
    while_node = ast3.While(*positional_args, **keyword_args)

    # Visit the While node; verifies that visit() handles this input without error
    result = transformer.visit(while_node)

