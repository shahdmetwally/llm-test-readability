import base as base
import typed_ast._ast3 as typed_ast

def test_timer_start_stops_correctly():
    """Test that the timer starts and stops correctly."""
    none_type_0 = None
    base_node_transformer_0 = base.BaseNodeTransformer(none_type_0)

def test_matrix_multiplication():
    """Test if matrix multiplication works correctly."""
    matrix_multiplier = base.MatMult()
    import_rewriter = base.BaseImportRewrite(matrix_multiplier)
    import_list = [import_rewriter, matrix_multiplier, import_rewriter]
    import_from = typed_ast.ImportFrom(*import_list)
    import_rewriter.visit_ImportFrom(import_from)

def test_mat_mult_import_from_rewrite():
    """Test if MatMult is correctly imported and used in ImportFrom."""
    mat_mult_instance = base.MatMult()
    none_type_instance = None
    base_import_rewrite_instance = base.BaseImportRewrite(none_type_instance)
    list_instance = [none_type_instance, mat_mult_instance]
    dict_instance = {}
    import_from_instance = typed_ast.ImportFrom(*list_instance, **dict_instance)
    base_import_rewrite_instance.visit_ImportFrom(import_from_instance)

def test_base_import_rewrite_visit_import_from():
    """Test BaseImportRewrite.visit_ImportFrom method."""
    str_0 = "\x0bQHzaZ?\tpM/wFtV"
    base_import_rewrite_0 = base.BaseImportRewrite(str_0)
    str_1 = "%WE}A)"
    dict_0 = {str_0: str_1, str_1: str_1, str_1: str_1, str_0: str_1}
    import_from_0 = typed_ast.ImportFrom(*dict_0, **dict_0)
    base_import_rewrite_0.visit_ImportFrom(import_from_0)

def test_timer_start_stops_correctly():
    """Test if timer starts and stops correctly."""
    str_0 = "\x0bQbHzaZ?\tpM/wFtV"
    str_1 = ""
    dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0, str_1: str_0, str_0: str_0}
    import_from_0 = typed_ast.ImportFrom(*dict_0, **dict_0)
    base_import_rewrite_0 = base.BaseImportRewrite(import_from_0)
    timer_instance = base_import_rewrite_0.visit_ImportFrom(import_from_0)