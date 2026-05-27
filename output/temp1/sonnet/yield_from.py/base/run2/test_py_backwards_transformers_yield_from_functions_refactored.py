import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_with_none():
    """Test that YieldFromTransformer can be instantiated and visit with None input without error."""
    # Use None as the AST node argument (edge case: no valid AST provided)
    none_node = None

    # Instantiate the transformer with None as the tree argument
    transformer = yield_from.YieldFromTransformer(none_node)

    # Invoke visit with None — verifies the transformer handles a None node gracefully
    transformer.visit(none_node)

def test_yield_from_transformer_instantiation_with_none():
    """Test that YieldFromTransformer can be instantiated with None as the AST node argument."""
    # Pass None as the root node, representing an empty or uninitialized transformer
    transformer = yield_from.YieldFromTransformer(None)

def test_yield_from_transformer_visits_while_node_with_none_args():
    """
    Test that YieldFromTransformer.visit() can process a While AST node
    constructed with None-containing argument lists without raising an error.
    """
    # Use None as the transformer's tree argument (no source tree provided)
    none_arg = None
    nested_none_list = [none_arg, none_arg]

    # Instantiate the transformer with no source tree
    yield_from_transformer = yield_from.YieldFromTransformer(none_arg)

    # Build a While node using the nested None list as both positional args
    while_args = [nested_none_list, nested_none_list]
    while_node = ast3.While(*while_args)

    # Visit the While node; verifies transformer handles this input gracefully
    result = yield_from_transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node_with_keyword_transformer_args():
    """
    Test that YieldFromTransformer.visit() can process an ast.While node
    constructed with None positional arguments and transformer instances
    as keyword arguments without raising an error.
    """
    none_value = None

    # Instantiate the transformer with no tree (None root)
    transformer = yield_from.YieldFromTransformer(none_value)

    # Build positional and keyword arguments for the While node
    positional_args = [none_value, none_value]
    arbitrary_key = "P+>W*v\nDN{M8\x0bLk"
    keyword_args = {
        arbitrary_key: transformer,
        arbitrary_key: transformer,
        arbitrary_key: transformer,
    }

    # Construct a While AST node using the prepared arguments
    while_node = ast3.While(*positional_args, **keyword_args)

    # Visit the While node with the transformer; result is not asserted
    result = transformer.visit(while_node)