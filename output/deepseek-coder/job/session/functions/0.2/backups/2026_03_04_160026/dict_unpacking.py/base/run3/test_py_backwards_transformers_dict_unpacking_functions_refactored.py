import typed_ast._ast3 as ast3
import dict_unpacking as dict_unpack
import typed_ast.ast3 as ast3_typed

def test_dict_unpacking_transformer_initialization():
    """
    Test that the DictUnpackingTransformer is correctly initialized with the module.
    """
    # Given
    mod = module_0.mod()

    # When
    dict_unpacking_transformer = module_1.DictUnpackingTransformer(mod)

    # Then
    assert isinstance(dict_unpacking_transformer, dict_unpack.DictUnpackingTransformer)

def test_dict_unpacking_transformer():
    """
    Test the DictUnpackingTransformer class.
    """
    # Given
    input_string = "39@U3\r"
    dict_unpacking_transformer = dict_unpack.DictUnpackingTransformer(input_string)
    parsed_module = ast3.parse(input_string)

    # When
    transformed_module = dict_unpacking_transformer.visit_Module(parsed_module)

    # Then
    assert transformed_module is not None

