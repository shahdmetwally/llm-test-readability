import pytest

import typed_ast._ast3 as typed_ast_internal_ast
import dict_unpacking as dict_unpacking_utils
import typed_ast.ast3 as typed_ast_ast3

def test_dict_unpacking_transformer_initialization():
    """Verify the DictUnpackingTransformer can be created from an AST module."""
    # Build an AST Module node using the typed_ast.ast3 helper.
    ast_module = typed_ast_ast3.mod()
    # Construct the transformer with the created AST module.
    transformer = dict_unpacking_utils.DictUnpackingTransformer(ast_module)

def test_dict_unpacking_transformer_visit_module():
    """Ensure DictUnpackingTransformer can visit a Module AST produced by typed_ast.ast3.parse."""
    # Source used to build the AST and initialize the transformer (unchanged input).
    source_code = "39@U3\r"

    # Initialize the transformer with the original source (as in the generated test).
    transformer = dict_unpacking_utils.DictUnpackingTransformer(source_code)

    # Parse the source into an AST Module using the typed_ast.ast3 alias.
    parsed_module = typed_ast_ast3.parse(source_code)

    # Invoke the transformer's visit_Module on the parsed AST (preserve original call sequence).
    transformed_module = transformer.visit_Module(parsed_module)

    # Basic sanity checks: should return a Module-like object and not crash.
    assert transformed_module is not None
    assert hasattr(transformed_module, "body")
    assert isinstance(transformed_module, type(parsed_module))

