import pytest
import typed_ast._ast3 as typed_ast3
import dict_unpacking as dict_unpack
import typed_ast.ast3 as typed_ast3_alt

def test_dict_unpacking_transformer_initialization():
    """Verify that a DictUnpackingTransformer can be initialized with a
    module object created from the mod function."""
    module_obj = typed_ast3_alt.mod()
    dict_unpacking_transformer = dict_unpack.DictUnpackingTransformer(module_obj)

def test_dict_unpacking_transformer_visits_parsed_module_with_string_input():
    """Verify that DictUnpackingTransformer can visit a parsed module from a raw string."""
    source_code = "39@U3\r"
    transformer = dict_unpack.DictUnpackingTransformer(source_code)
    parsed_ast = typed_ast3.parse(source_code)
    result_module = transformer.visit_Module(parsed_ast)