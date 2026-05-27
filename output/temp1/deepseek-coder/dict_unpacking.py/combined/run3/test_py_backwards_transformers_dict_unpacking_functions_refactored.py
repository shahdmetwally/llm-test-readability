import typed_ast._ast3 as typed_ast
import dict_unpacking as dict_utils
import typed_ast.ast3 as ast3

def test_correct_initialization_of_dict_unpacking_transformer(module_with_mod_class_instance, module_1):
    dict_unpacking_transformer_instance = typed_ast.DictUnpackingTransformer(module_with_mod_class_instance)

def test_dict_unpacking_parser_with_str_literal():
    str_0 = "39@U3\r"
    dict_unpacking_transformer = dict_utils.DictUnpackingTransformer(str_0)
    var_0 = typed_ast.parse(str_0)
    typed_ast.visit(var_0,dict_unpacking_transformer)