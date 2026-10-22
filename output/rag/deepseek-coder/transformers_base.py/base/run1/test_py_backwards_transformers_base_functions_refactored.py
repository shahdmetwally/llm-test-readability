import base as base_module
import typed_ast._ast3 as ast3_module

def test_base_node_transformer_initialization():
    none_type = None
    base_node_transformer = base_module.BaseNodeTransformer(none_type)
    assert isinstance(base_node_transformer, base_module.BaseNodeTransformer), "BaseNodeTransformer instantiation failed with None type input"

def test_import_from_visits_transform():
    mat_mult = base_module.MatMult()
    base_import_rewrite = base_module.BaseImportRewrite(mat_mult)
    import_from_visits = [base_import_rewrite, mat_mult, base_import_rewrite]
    import_from = ast3_module.ImportFrom(*import_from_visits)
    base_import_rewrite.visit_ImportFrom(import_from)

def test_import_visit():
    multiplication_obj = base_module.MatMult()
    none_type_var = None
    base_import_rewriter = base_module.BaseImportRewrite(none_type_var)
    import_list = [none_type_var, multiplication_obj]
    import_dict = {}
    import_from_node = ast3_module.ImportFrom(*import_list, **import_dict)
    base_import_rewriter.visit_ImportFrom(import_from_node)

def test_ast_rewrite_of_imports():
    base = base_module.BaseImportRewrite
    ast3 = ast3_module.ImportFrom
    str_alias_1 = "\x0bQHzaZ?\tpM/wFtV"
    str_alias_2 = "%WE}A)"
    dict_input_1 = {str_alias_1: str_alias_2, str_alias_2: str_alias_2, str_alias_2: str_alias_2, str_alias_1: str_alias_2}
    import_from_fixture = ast3(**dict_input_1)
    base_rewrite_instance = base(str_alias_1)
    base_rewrite_instance.visit_ImportFrom(import_from_fixture)

def test_import_from_base_import_rewrite():
    imports = {
        "base": base_module,
        "ast3": ast3_module
    }
    str_foreign = "\x0bQbHzaZ?\tpM/wFtV"
    str_local = ""
    import_statement = {
        str_foreign: str_foreign,
        str_local: str_foreign,
        str_foreign: str_foreign,
        str_local: str_foreign,
        str_foreign: str_foreign
    }
    import_from = imports["base"].ImportFrom(**import_statement)
    base_import_rewrite = imports["ast3"].BaseImportRewrite(import_from)
    resulting_import = base_import_rewrite.visit_ImportFrom(import_from)
    assert isinstance(resulting_import, str)