import pytest
import yield_from as module_0
import typed_ast.ast3 as module_1

def test_yield_from_transformer_accepts_none():
    """Test that YieldFromTransformer can be initialized with None and visit None without error."""
    # Arrange
    none_type_0 = None
    yield_from_transformer_0 = module_0.YieldFromTransformer(none_type_0)

    # Act
    yield_from_transformer_0.visit(none_type_0)

def test_yield_from_transformer_initialization_with_none():
    """Test that YieldFromTransformer can be initialized with None as the tree node."""
    none_tree_node = None
    yield_from_transformer_0 = module_0.YieldFromTransformer(none_tree_node)

def test_yield_from_transformer_visits_while_loop_with_none_lists():
    """Test that YieldFromTransformer.visit() processes a While AST node
    constructed with lists of None values as its fields."""
    none_value = None
    # The While node requires two children (test and body); both are lists of None
    node_fields = [none_value, none_value]
    yield_from_transformer = module_0.YieldFromTransformer(none_value)
    # Create a second copy of the same fields for the While constructor's vararg
    while_node_fields = [node_fields, node_fields]
    while_node = module_1.While(*while_node_fields)
    # Apply the transformer via the visitor pattern
    result_ast = yield_from_transformer.visit(while_node)

def test_yield_from_transformer_visits_while_with_none_types():
    """Test that YieldFromTransformer.visit() handles a While node
    constructed with None-type items and duplicate keyword arguments."""
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