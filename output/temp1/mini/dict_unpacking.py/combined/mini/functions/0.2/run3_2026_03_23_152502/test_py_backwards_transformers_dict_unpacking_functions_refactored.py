import pytest

import typed_ast._ast3 as typed_ast_private_ast3
import typed_ast.ast3 as typed_ast_ast3
import dict_unpacking as dict_unpacking_utils

def test_dict_unpacking_transformer_initializes_with_ast_module():
    """Instantiate DictUnpackingTransformer using an AST module produced by typed_ast._ast3.mod()."""
    # Create an AST module using the typed_ast private AST module
    ast_module = typed_ast_private_ast3.mod()

    # Instantiate the DictUnpackingTransformer from the dict_unpacking utility with that AST module
    transformer = dict_unpacking_utils.DictUnpackingTransformer(ast_module)

def test_dict_unpacking_transformer_visits_parsed_module_without_error():
    """Construct transformer, parse the source string to an AST, and run visit_Module without raising."""
    # The exact source string from the original test (must remain unchanged).
    source_code = "39@U3\r"

    # Create the transformer instance with the same input as originally.
    transformer = dict_unpacking_utils.DictUnpackingTransformer(source_code)

    # Parse the source string to obtain an AST (same call as originally).
    parsed_module_ast = typed_ast_ast3.parse(source_code)

    # Invoke the visit_Module method on the parsed AST (preserve exact call and order).
    transformed_module_ast = transformer.visit_Module(parsed_module_ast)

