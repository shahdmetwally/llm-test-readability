import typed_ast._ast3 as ast
import dict_unpacking as dict_unpack
import typed_ast.ast3 as ast3

def test_dict_unpacking_transformer_with_module_0():
    """
    Test the DictUnpackingTransformer with module_0.
    """
    # Import the modules
    mod_0 = module_0.mod()
    dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(mod_0)

    # Assert that the transformer was created successfully
    assert dict_unpacking_transformer_0 is not None

def test_dict_unpacking_transformer_with_module_1():
    """
    Test that the DictUnpackingTransformer correctly transforms a Module.
    """
    # Given
    input_string = "39@U3\r"
    dict_unpacking_transformer = dict_unpack.DictUnpackingTransformer(input_string)
    module_node = ast3.parse(input_string)

    # When
    transformed_module = dict_unpacking_transformer.visit_Module(module_node)

    # Then
    assert isinstance(transformed_module, ast.Module)

