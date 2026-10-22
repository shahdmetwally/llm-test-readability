import typed_ast._ast3 as ast
import dict_unpacking as du
import typed_ast.ast3 as typed_ast

def test_dict_unpacking_transformer():
    # Setup
    original_module = ast.mod()
    dict_unpack = du.DictUnpackingTransformer(original_module)

    # Exercise
    transformed_module = dict_unpack.transform()

    # Verify
    assert transformed_module == {  # Expectation is that transformation does not alter module.
        ... some expected value here ...
    }