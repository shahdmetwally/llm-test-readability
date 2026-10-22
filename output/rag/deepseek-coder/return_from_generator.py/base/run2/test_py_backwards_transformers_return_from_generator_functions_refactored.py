import typed_ast.ast3 as ast_3

def test_none_type_object_on_dump_method():
    none_value = None
    try:
        ast_3.dump(none_value)
    except Exception as e:
        assert isinstance(e, TypeError)