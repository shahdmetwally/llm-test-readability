import pytest

import typed_ast._ast3 as typed_ast_private_ast3
import dict_unpacking as dict_unpacking_module
import typed_ast.ast3 as typed_ast_ast3

def test_dict_unpacking_transformer_constructs_from_parsed_module():
    """Ensure DictUnpackingTransformer can be constructed from a typed_ast parsed module."""
    # Create a parsed module object using the typed_ast._ast3 API
    parsed_module = typed_ast_private_ast3.mod()

    # Initialize the DictUnpackingTransformer with the parsed module.
    # This mirrors the original behavior: construct transformer from module object.
    dict_unpacking_transformer = dict_unpacking_module.DictUnpackingTransformer(parsed_module)

    # Basic check that the transformer was constructed
    assert isinstance(dict_unpacking_transformer, dict_unpacking_module.DictUnpackingTransformer)

def test_dict_unpacking_transformer_visits_module_without_error():
    """Ensure DictUnpackingTransformer can visit a parsed Module without raising."""
    # A short source string used both to instantiate the transformer and to parse.
    source_code = "39@U3\r"

    # Create the transformer with the source string (preserve original constructor call).
    transformer = dict_unpacking_module.DictUnpackingTransformer(source_code)

    # Parse the same source string into a Module AST (preserve original parse call).
    parsed_module_ast = typed_ast_ast3.parse(source_code)

    # Visit the parsed Module with the transformer (preserve original visit_Module call).
    transformed_module = transformer.visit_Module(parsed_module_ast)

