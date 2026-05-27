import pytest
import typed_ast._ast3 as ast3
import dict_unpacking as dict
import typed_ast.ast3 as ast3_unpacked

def test_case_dict_unpacking_transformer():
    """
    This test case tests the DictUnpackingTransformer's functionality using mod.
    It uses two imported modules (module_0 and module_1) and verifies their working.
    It uses a dict_unpacking_transformer instance, which creates a DictUnpackingTransformer object
    with a mod_0 instance. It verifies that no assertion fails.
    """

    # Create mod_0 and dict_unpacking_transformer_0 instances, with DictUnpackingTransformer
    mod_0 = ast3.mod()
    dict_unpacking_transformer_0 = dict.DictUnpackingTransformer(mod_0)

    # Verify no assertion fails
    assert False not in dict_unpacking_transformer_0.get_result()

test_case_dict_unpacking_transformer()

def test_dict_unpacking_transformer():
    """
    This test case checks the behaviour of DictUnpackingTransformer when used on a string.
    The transformer should transform the string into an AST tree,
    and the built-in ast parse module should correctly parse this tree.
    """
    from dict_unpacking import DictUnpackingTransformer

    # Setup variables
    input_string = "39@U3\r"  # example string for transforming into AST
    dict_unpacking_transformer = DictUnpackingTransformer()

    # Transform the input string into an AST 
    input_ast = dict_unpacking_transformer.visit_Module(ast3.parse(input_string))

    # Parse AST to evaluate the transformed string
    output_ast = ast3.parse(input_string, mode='eval')

    # Ensure transformation was successful
    assert type(input_ast) == type(output_ast)