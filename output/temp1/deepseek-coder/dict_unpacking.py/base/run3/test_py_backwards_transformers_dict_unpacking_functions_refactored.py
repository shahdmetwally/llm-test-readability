import typing
import pytest

import typed_ast._ast3 as ast
import dict_unpacking as dict_pack
import typed_ast.ast3 as ast_mod


def test_instantiate_transformers():
    """
    Test that the transformation modules are able to be 
    instantiate without raising exceptions.
    """

    # Instantiate the first transformation module
    transformer_module = typing.cast(ast_mod.Module, transformer.mod())

    # Instantiate the DictUnpackingTransformer
    dict_unpacking_transformer = dict_pack.DictUnpackingTransformer(
        transformer_module,
    )

    # Assert that we got a transformer
    assert dict_unpacking_transformer is not None, \
        "Unable to instantiate DictUnpackingTransformer"


def test_module_1_transformed_module_parses():
    import typing
    import pytest
    import typed_ast._ast3 as ast
    import dict_unpacking as dict_pack
    import typed_ast.ast3 as ast_mod

    module_code = "39@U3\r"

    # Create a transformer and transform module
    module_transformer = dict_pack.DictUnpackingTransformer(module_code)
    transformed_ast = module_transformer.visit_Module(re.parse(module_code))

    # Ensure the transformed AST parses correctly
    parsed_ast = ast_mod.parse(module_code)

    assert parsed_ast == transformed_ast