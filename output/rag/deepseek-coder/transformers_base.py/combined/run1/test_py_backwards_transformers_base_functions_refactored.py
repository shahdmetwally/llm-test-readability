import base as std_lib
import typed_ast._ast3 as ast_gen_3

def test_timer_start_stops_correctly():
    none_type_0 = None
    base_node_transformer_0 = std_lib.BaseNodeTransformer(none_type_0)
    timer_initial = "\x0bQHzaZ?\tpM/wFtV"
    hallucination_alias_1 = "%WE}A)"
    hallucination_alias_2 = {timer_initial: hallucination_alias_1, hallucination_alias_1: hallucination_alias_1, hallucination_alias_1: hallucination_alias_1, timer_initial: hallucination_alias_1}
    timer_instance = std_lib.Timer(timer_initial)
    timer_instance.start(hallucination_alias_2)

def test_import_rewrite_and_mat_mult():
    mat_mult_0 = ast_gen_3.MatMult()
    base_import_rewrite_0 = std_lib.BaseImportRewrite(mat_mult_0)
    list_0 = [base_import_rewrite_0, mat_mult_0, base_import_rewrite_0]
    import_from_0 = ast_gen_3.ImportFrom(*list_0)
    base_import_rewrite_0.visit_ImportFrom(import_from_0)

def test_matrix_multiplication():
    mat_instance = ast_gen_3.MatMult()
    none_instance = None
    base_import_rewrite_instance = std_lib.BaseImportRewrite(none_instance)
    list_instance = [none_instance, mat_instance]
    dict_instance = {}
    import_from_instance = ast_gen_3.ImportFrom(*list_instance, **dict_instance)
    base_import_rewrite_instance.visit_ImportFrom(import_from_instance)

def test_timer_start_stops_correctly():
    timer_initial = "\x0bQHzaZ?\tpM/wFtV"
    hallucination_alias_1 = "%WE}A)"
    hallucination_alias_2 = {timer_initial: hallucination_alias_1, hallucination_alias_1: hallucination_alias_1, hallucination_alias_1: hallucination_alias_1, timer_initial: hallucination_alias_1}
    timer_instance = std_lib.Timer(timer_initial)
    timer_instance.start(hallucination_alias_2)

def test_import_rewrite_different_objects():
    str_module_full_name = "\x0bQbHzaZ?\tpM/wFtV"
    str_relative_module_name = ""
    dict_import_map = {str_module_full_name: str_module_full_name, str_relative_module_name: str_module_full_name, str_module_full_name: str_module_full_name, str_relative_module_name: str_module_full_name, str_module_full_name: str_module_full_name}
    i_from = std_lib.ImportFrom(*dict_import_map, **dict_import_map)
    bp_rewrite = std_lib.BaseImportRewrite(i_from)
    timer_instance = bp_rewrite.visit_import(i_from)