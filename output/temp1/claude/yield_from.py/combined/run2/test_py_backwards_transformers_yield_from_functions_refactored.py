import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_with_none_node():
    """Test that YieldFromTransformer.visit() handles a None node without raising."""
    # Use None as the AST node input to test handling of missing/null nodes
    none_ast_node = None

    # Instantiate the transformer with a None tree
    transformer = yield_from.YieldFromTransformer(none_ast_node)

    # Visit the None node — should complete without error
    transformer.visit(none_ast_node)

def test_yield_from_transformer_instantiates_with_none_argument():
    """Test that YieldFromTransformer can be instantiated with None as its argument."""
    # Pass None as the constructor argument, representing an absent/optional node
    none_argument = None
    transformer_instance = yield_from.YieldFromTransformer(none_argument)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """Test that YieldFromTransformer.visit() handles a While node built with None arguments without raising."""
    # Use None as a stand-in for all AST node constructor arguments
    none_arg = None

    # Build the argument list that will be passed to the While node constructor
    while_node_args = [none_arg, none_arg]

    # Instantiate the transformer with no source tree (None)
    transformer = yield_from.YieldFromTransformer(none_arg)

    # Wrap the While args in a list to unpack into the While constructor
    while_constructor_args = [while_node_args, while_node_args]

    # Construct a While AST node using the None-filled argument lists
    while_node = ast3.While(*while_constructor_args)

    # Visit the While node — the transformer should handle it without error
    result_ast = transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node_with_repeated_keyword_transformer_args():
    """Test that YieldFromTransformer.visit() handles an ast.While node built with None positional args and transformer-valued keyword args."""

    # Use None as the tree/parent argument for the transformer
    none_value = None

    # Instantiate the transformer with no tree context
    transformer = yield_from.YieldFromTransformer(none_value)

    # Positional arguments for constructing the While node (both None)
    positional_args = [none_value, none_value]

    # A single string key reused across all keyword argument entries
    keyword_key = "P+>W*v\nDN{M8\x0bLk"

    # Keyword arguments mapping the same key to the transformer instance
    # (repeated keys are intentional — Python keeps the last assignment)
    keyword_args = {
        keyword_key: transformer,
        keyword_key: transformer,
        keyword_key: transformer,
    }

    # Construct an ast.While node using the prepared positional and keyword arguments
    while_node = ast3.While(*positional_args, **keyword_args)

    # Visit the While node with the transformer; verifies no exception is raised
    visited_result = transformer.visit(while_node)