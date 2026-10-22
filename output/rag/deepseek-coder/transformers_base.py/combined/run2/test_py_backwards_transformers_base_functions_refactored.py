import base as base
import typed_ast._ast3 as typed_ast_ast3
import pytest

def test_base_transformer_initialization():
    """
    This test checks if an instance of BaseNodeTransformer
    can be properly initialized without raising errors.
    """
    none_type = None
    base_transformer = base.BaseNodeTransformer(none_type)

def test_base_transformer_multiplication_start():
    matrix_multiplication_0 = typed_ast_ast3.MatMult()
    base_import_rewrite_0 = base.BaseImportRewrite(matrix_multiplication_0)
    list_0 = [base_import_rewrite_0, matrix_multiplication_0, base_import_rewrite_0]
    import_from_0 = typed_ast_ast3.ImportFrom(*list_0)
    base_import_rewrite_0.visit_ImportFrom(import_from_0)

def test_mat_mult_initialization():
    mat_mult_instance = typed_ast_ast3.MatMult()
    base_import_rewrite_instance = base.BaseImportRewrite(None)
    import_from_list = [None, mat_mult_instance]
    import_from_dict = {}
    import_from_instance = typed_ast_ast3.ImportFrom(*import_from_list, **import_from_dict)
    base_import_rewrite_instance.visit_ImportFrom(import_from_instance)

def test_base_import_rewrite_visit_import_from():
    """Test BaseImportRewrite.visit_ImportFrom() functionality"""
    str_original_name = "\x0bQHzaZ?\tpM/wFtV"
    base_import_rewrite = base.BaseImportRewrite(str_original_name)
    str_renamed_name = "%WE}A)"
    dict_fake_names = {str_original_name: str_renamed_name, 
                       str_renamed_name: str_renamed_name, 
                       str_renamed_name: str_renamed_name, 
                       str_original_name: str_renamed_name}
    import_from = typed_ast_ast3.ImportFrom(list_fake_names=list(dict_fake_names.keys()), **dict_fake_names)
    base_import_rewrite.visit_ImportFrom(import_from)