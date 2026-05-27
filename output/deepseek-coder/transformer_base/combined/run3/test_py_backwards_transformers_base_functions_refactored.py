import base as base
import typed_ast._ast3 as typed_ast

def test_base_node_transformer_initialization():
    """Test that BaseNodeTransformer initializes correctly."""
    none_type = None
    base_node_transformer = base.BaseNodeTransformer(none_type)

def test_mat_mult_start_stops_correctly():
    """Test that the MatMult class correctly starts and stops a timer."""
    mat_mult = typed_ast.MatMult()
    base_import_rewrite = base.BaseImportRewrite(mat_mult)
    list_0 = [base_import_rewrite, mat_mult, base_import_rewrite]
    import_from = typed_ast.ImportFrom(*list_0)
    base_import_rewrite.visit_ImportFrom(import_from)

def test_mat_mult_import_rewrite():
    """Test that the MatMult class is correctly imported and renamed."""
    mat_mult_instance = typed_ast.MatMult()
    none_type_instance = None
    base_import_rewrite_instance = base.BaseImportRewrite(none_type_instance)
    list_instance = [none_type_instance, mat_mult_instance]
    dict_instance = {}
    import_from_instance = typed_ast.ImportFrom(*list_instance, **dict_instance)
    base_import_rewrite_instance.visit_ImportFrom(import_from_instance)

def test_import_rewrite_from_import_from():
    """Test if BaseImportRewrite correctly rewrites ImportFrom nodes."""
    module_name = "\x0bQHzaZ?\tpM/wFtV"
    base_import_rewrite = base.BaseImportRewrite(module_name)
    alias_name = "%WE}A)"
    import_from_dict = {module_name: alias_name, alias_name: alias_name, alias_name: alias_name, module_name: alias_name}
    import_from_node = typed_ast.ImportFrom(*import_from_dict, **import_from_dict)
    base_import_rewrite.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_initialization():
    """Test that the base import rewrite starts and stops correctly."""
    str_0 = "\x0bQbHzaZ?\tpM/wFtV"
    str_1 = ""
    dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0, str_1: str_0, str_0: str_0}
    import_from_0 = typed_ast.ImportFrom(*dict_0, **dict_0)
    base_import_rewrite_0 = base.BaseImportRewrite(import_from_0)
    timer_instance = base_import_rewrite_0.visit_ImportFrom(import_from_0)