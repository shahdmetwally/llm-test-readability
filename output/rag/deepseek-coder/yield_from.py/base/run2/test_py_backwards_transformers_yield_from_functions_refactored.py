import yield_from as module_0
import typed_ast.ast3 as module_1

def test_case_0():

    none_type = None  
    yield_from_transformer = module_0.YieldFromTransformer(none_type)
    yield_from_transformer.visit(none_type)

def test_case_0():

    none_input = None
    transformer = module_0.YieldFromTransformer(none_input)
    assert none_input is transformer.none_type

def test_yield_from_transformer_handles_while_statements():

    none_value = None
    none_list = [none_value, none_value]
    yield_from_transformer = module_0.YieldFromTransformer(none_value)
    nested_list = [none_list, none_list]
    while_statement = module_1.While(*nested_list)
    transform_result = yield_from_transformer.visit(while_statement)
    assert transform_result == none_value

def test_yield_from_transformer_handles_while_statements():

    none_val = None
    yield_from_transformer = module_0.YieldFromTransformer(none_val)
    empty_list = [none_val, none_val]
    string_key = "P+>W*v\nDN{M8\x0bLk"
    while_arguments = {
        string_key: yield_from_transformer,
        string_key: yield_from_transformer,
        string_key: yield_from_transformer,
    }
    while_statement = module_1.While(*empty_list, **while_arguments)
    result = yield_from_transformer.visit(while_statement)
    assert result is not None  
    assert isinstance(result, module_0.YieldFromTransformer.ReturnType)