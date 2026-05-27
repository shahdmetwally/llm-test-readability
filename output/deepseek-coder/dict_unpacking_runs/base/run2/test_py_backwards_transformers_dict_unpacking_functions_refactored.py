import typed_ast._ast3 as ast
import dict_unpacking as dict_unpack
import typed_ast.ast3 as ast3

def test_dict_unpacking_transformer():
    # Setup
    mod = module_0.mod()  # Create a module
    transformer = module_1.DictUnpackingTransformer(mod)  # Create a transformer

    # Execution
    transformed_mod = transformer.transform(mod)  # Transform the module

    # Assertion
    assert transformed_mod == {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }

def test_dict_unpacking_transformer():
    """
    Test that DictUnpackingTransformer correctly transforms a Module node.
    """
    # Given
    source_code = "39@U3\r"
    dict_unpacking_transformer = dict_unpack.DictUnpackingTransformer(source_code)
    module_node = ast3.parse(source_code)

    # When
    transformed_module = dict_unpacking_transformer.visit_Module(module_node)

    # Then
    assert isinstance(transformed_module, ast.Module)

