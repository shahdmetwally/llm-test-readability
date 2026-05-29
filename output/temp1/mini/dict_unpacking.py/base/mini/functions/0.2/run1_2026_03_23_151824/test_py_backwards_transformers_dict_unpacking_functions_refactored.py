import pytest

import typed_ast._ast3 as internal_ast3
import dict_unpacking as dict_unpacking_module
import typed_ast.ast3 as typed_ast_ast3

def test_constructs_dict_unpacking_transformer_from_ast_module():
    """Ensure we can construct a DictUnpackingTransformer for a simple AST module."""
    # Create a minimal AST module using the internal typed-ast _ast3 alias
    ast_module = internal_ast3.mod()
    # Instantiate the transformer from the dict_unpacking module alias using that AST
    transformer = dict_unpacking_module.DictUnpackingTransformer(ast_module)
    assert transformer is not None

def test_dict_unpacking_transformer_transforms_parsed_module():
    """Ensure DictUnpackingTransformer visits a parsed module without errors."""
    # Source code to be parsed and transformed (kept exactly as in original test)
    source_code = "39@U3\r"

    # Instantiate the transformer with the source (as original)
    transformer = dict_unpacking_module.DictUnpackingTransformer(source_code)

    # Parse the source into an AST using the typed_ast.ast3 alias (was module_2.parse)
    parsed_module = typed_ast_ast3.parse(source_code)

    # Apply the transformer's visit_Module to the parsed AST (preserves original call)
    transformed_module = transformer.visit_Module(parsed_module)

