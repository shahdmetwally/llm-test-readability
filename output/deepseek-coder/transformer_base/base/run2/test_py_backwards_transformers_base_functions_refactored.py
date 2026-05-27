import base as base
import typed_ast._ast3 as typed_ast

def test_base_node_transformer_initialization():
    none_object = None
    base_node_transformer = base.BaseNodeTransformer(none_object)
    assert base_node_transformer is not None

def test_mat_mult_import_from():
    mat_mult = base.MatMult()
    base_import_rewrite = base.BaseImportRewrite(mat_mult)
    import_from_objects = [base_import_rewrite, mat_mult, base_import_rewrite]
    import_from = base.ImportFrom(*import_from_objects)
    base_import_rewrite.visit_ImportFrom(import_from)

def test_mat_mult_import_rewrite():
    mat_mult = base.MatMult()
    base_import_rewrite = base.BaseImportRewrite(None)
    import_from_list = [None, mat_mult]
    import_from_dict = {}
    import_from = base.ImportFrom(*import_from_list, **import_from_dict)
    base_import_rewrite.visit_ImportFrom(import_from)

def test_import_from_rewrite():
    str_0 = "\x0bQHzaZ?\tpM/wFtV"
    str_1 = "%WE}A)"
    dict_0 = {str_0: str_1, str_1: str_1, str_1: str_1, str_0: str_1}
    base_import_rewrite_0 = base.BaseImportRewrite(str_0)
    import_from_0 = typed_ast.ImportFrom(*dict_0, **dict_0)
    base_import_rewrite_0.visit_ImportFrom(import_from_0)

def test_import_from_base_import_rewrite():
    str_0 = "\x0bQbHzaZ?\tpM/wFtV"
    str_1 = ""
    dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0, str_1: str_0, str_0: str_0}
    import_from_0 = base.ImportFrom(*dict_0, **dict_0)
    base_import_rewrite_0 = base.BaseImportRewrite(import_from_0)
    var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    assert var_0 == expected_value