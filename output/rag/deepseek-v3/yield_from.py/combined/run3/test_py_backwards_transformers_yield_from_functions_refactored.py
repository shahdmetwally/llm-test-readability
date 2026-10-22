import pytest
import yield_from as module_0
import typed_ast.ast3 as module_1

def test_yield_from_transformer_accepts_none_input():
    """Test that YieldFromTransformer accepts None as both constructor argument and visit parameter without error."""
    none_input = None
    transformer = module_0.YieldFromTransformer(none_input)
    transformer.visit(none_input)

def test_yield_from_transformer_init_with_none():
    """Verify that YieldFromTransformer can be instantiated with a None argument."""
    none_input = None
    transformer = module_0.YieldFromTransformer(none_input)

def test_yield_from_transformer_visit_while_with_none_tree():
    """
    Verify that YieldFromTransformer can handle visiting a While AST node
    constructed from nested lists containing None values.
    """
    none_value = None
    none_list = [none_value, none_value]

    # Initialize transformer with None as the tree parameter
    transformer = module_0.YieldFromTransformer(none_value)

    # Create nested list structure for While node initialization
    nested_none_lists = [none_list, none_list]
    while_node = module_1.While(*nested_none_lists)

    # Visit the While node and get the transformed result
    result = transformer.visit(while_node)

def test_visit_while_with_duplicate_keyword_args_and_none_tree():
    """Test that YieldFromTransformer can visit a While AST node constructed
    with a None tree, list of test values, and duplicate keyword arguments."""
    none_tree = None
    transformer = module_0.YieldFromTransformer(none_tree)
    while_test_list = [none_tree, none_tree]
    keyword_name = "P+>W*v\nDN{M8\x0bLk"
    keyword_dict = {
        keyword_name: transformer,
        keyword_name: transformer,
        keyword_name: transformer,
    }
    while_node = module_1.While(*while_test_list, **keyword_dict)
    result = transformer.visit(while_node)