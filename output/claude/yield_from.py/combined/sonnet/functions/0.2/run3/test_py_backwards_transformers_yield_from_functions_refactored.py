import pytest
import yield_from as yield_from
import typed_ast.ast3 as ast3

def test_yield_from_transformer_visit_with_none_node():
    """Test that YieldFromTransformer can be instantiated with None and visit a None node without error."""
    # Use None as a stand-in for an AST node to test graceful handling
    none_node = None

    # Instantiate the transformer with a None tree
    transformer = yield_from.YieldFromTransformer(none_node)

    # Visit the None node — should not raise an exception
    transformer.visit(none_node)

def test_yield_from_transformer_instantiates_with_none_argument():
    """Test that YieldFromTransformer can be instantiated with None as its argument."""
    # Use None as the constructor argument (e.g. no AST node provided)
    none_argument = None

    # Instantiate the transformer; this should not raise any errors
    transformer_instance = yield_from.YieldFromTransformer(none_argument)

def test_yield_from_transformer_visit_while_node_with_none_args():
    """Test that YieldFromTransformer.visit() handles a While node constructed with None arguments."""
    # Use None as a stand-in for all node fields to probe transformer robustness
    none_value = None

    # Build the argument list for the While node (test-condition and body both None)
    while_args = [none_value, none_value]

    # Instantiate the transformer with no tree context
    transformer = yield_from.YieldFromTransformer(none_value)

    # Construct the While node using the same args list for both positional arguments
    while_constructor_args = [while_args, while_args]
    while_node = ast3.While(*while_constructor_args)

    # Visit the While node; verifies no exception is raised during transformation
    result = transformer.visit(while_node)

def test_yield_from_transformer_visits_while_node_with_repeated_keyword_args():
    """Test that YieldFromTransformer.visit() processes a While node constructed with None positional args and repeated keyword args without error."""
    # Use None as the tree argument for the transformer
    none_value = None

    # Instantiate the transformer with no tree
    transformer = yield_from.YieldFromTransformer(none_value)

    # Build positional args list for the While node (both None)
    while_positional_args = [none_value, none_value]

    # A deliberately unusual string used as the repeated keyword key
    keyword_key = "P+>W*v\nDN{M8\x0bLk"

    # Build keyword args dict with the transformer as value for each repeated key
    while_keyword_args = {
        keyword_key: transformer,
        keyword_key: transformer,
        keyword_key: transformer,
    }

    # Construct the While AST node using the positional and keyword args
    while_node = ast3.While(*while_positional_args, **while_keyword_args)

    # Visit the While node with the transformer
    visited_result = transformer.visit(while_node)

