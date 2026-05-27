import yield_from as module_0
import typed_ast.ast3 as module_1

def test_yield_from_transformer_visit():
    """Test that YieldFromTransformer.visit() behaves as expected."""
    none_type = None
    yield_from_transformer = yield_from.YieldFromTransformer(none_type)
    yield_from_transformer.visit(none_type)

def test_yield_from_transformer_initialization():
    """
    Test that the YieldFromTransformer class initializes correctly.
    """
    none_type_0 = None
    yield_from_transformer_0 = module_0.YieldFromTransformer(none_type_0)

def test_timer_start_stops_correctly():
    """Test that the timer starts and stops correctly."""
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    yield_from_transformer_0 = module_0.YieldFromTransformer(none_type_0)
    list_1 = [list_0, list_0]
    while_0 = module_1.While(*list_1)
    a_s_t_0 = yield_from_transformer_0.visit(while_0)

def test_yield_from_transformer_visits_while_node_correctly():
    """
    Test that the YieldFromTransformer visits a While node correctly.
    """
    none_type = None
    yield_from_transformer = module_0.YieldFromTransformer(none_type)
    list_of_none_types = [none_type, none_type]
    string_key = "P+>W*v\nDN{M8\x0bLk"
    dict_with_string_keys = {
        string_key: yield_from_transformer,
        string_key: yield_from_transformer,
        string_key: yield_from_transformer,
    }
    while_node = module_1.While(*list_of_none_types, **dict_with_string_keys)
    result = yield_from_transformer.visit(while_node)

