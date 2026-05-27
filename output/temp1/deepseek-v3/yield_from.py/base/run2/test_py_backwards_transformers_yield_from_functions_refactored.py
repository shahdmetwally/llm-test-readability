import pytest
import yield_from as module_0
import typed_ast.ast3 as module_1

def test_yield_from_transformer_with_none_tree_and_root():
    """Test that YieldFromTransformer can be instantiated with None and visit a None tree."""
    none_tree_root = None
    transformer = module_0.YieldFromTransformer(none_tree_root)
    transformer.visit(none_tree_root)

def test_yield_from_transformer_creation_with_none_tree():
    """Test that YieldFromTransformer can be instantiated with a None tree."""
    none_tree = None
    yield_from_transformer_0 = module_0.YieldFromTransformer(none_tree)

def test_visit_while_with_multiple_child_lists():
    """Test that YieldFromTransformer can visit a While node with two child lists."""
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    yield_from_transformer_0 = module_0.YieldFromTransformer(none_type_0)
    list_1 = [list_0, list_0]  # Two identical lists for While's test and body
    while_0 = module_1.While(*list_1)  # Unpack list into While constructor args
    a_s_t_0 = yield_from_transformer_0.visit(while_0)

def test_visit_while_with_yield_from_transformer():
    """Test that YieldFromTransformer can visit a While AST node."""
    none_type_0 = None
    yield_from_transformer_0 = module_0.YieldFromTransformer(none_type_0)
    list_0 = [none_type_0, none_type_0]
    str_0 = "P+>W*v\nDN{M8\x0bLk"
    dict_0 = {
        str_0: yield_from_transformer_0,
        str_0: yield_from_transformer_0,
        str_0: yield_from_transformer_0,
    }
    while_0 = module_1.While(*list_0, **dict_0)
    a_s_t_0 = yield_from_transformer_0.visit(while_0)