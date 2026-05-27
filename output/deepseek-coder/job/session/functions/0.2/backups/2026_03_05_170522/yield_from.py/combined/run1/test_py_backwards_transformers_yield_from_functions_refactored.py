import yield_from as module_0
import typed_ast.ast3 as module_1

def test_yield_from_transformer_visit():
    """
    Test the visit method of the YieldFromTransformer class.
    """
    none_type = None
    yield_from_transformer = module_0.YieldFromTransformer(none_type)
    yield_from_transformer.visit(none_type)

def test_yield_from_transformer_initialization():
    """
    Test that the YieldFromTransformer initializes correctly.
    """
    none_type = None
    yield_from_transformer = module_0.YieldFromTransformer(none_type)

def test_yield_from_transformer_visit_while():
    """Test that the YieldFromTransformer correctly visits a While node."""
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    yield_from_transformer = module_0.YieldFromTransformer(none_type_0)
    list_1 = [list_0, list_0]
    while_0 = module_1.While(*list_1)
    a_s_t_0 = yield_from_transformer.visit(while_0)

def test_yield_from_transformer_visits_while_node_correctly():
    none_type = None
    yield_from_transformer = module_0.YieldFromTransformer(none_type)
    list_of_none_types = [none_type, none_type]
    string_key = "P+>W*v\nDN{M8\x0bLk"
    dict_of_string_keys = {
        string_key: yield_from_transformer,
        string_key: yield_from_transformer,
        string_key: yield_from_transformer,
    }
    while_node = module_1.While(*list_of_none_types, **dict_of_string_keys)
    result = yield_from_transformer.visit(while_node)

