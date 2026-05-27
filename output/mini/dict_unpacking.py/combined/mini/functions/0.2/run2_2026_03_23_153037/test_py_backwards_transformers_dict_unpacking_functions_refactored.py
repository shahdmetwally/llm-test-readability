import pytest

import typed_ast._ast3 as typed_ast_private_ast3
import typed_ast.ast3 as typed_ast_ast3
import dict_unpacking as dict_unpacking_module

def test_dict_unpacking_transformer_can_be_constructed():
    """Ensure DictUnpackingTransformer can be instantiated with an AST module."""
    # Create an AST module (previously produced by module_0.mod()).
    ast_module = typed_ast_ast3.mod()

    # Instantiate the transformer with the AST module (previously module_1.DictUnpackingTransformer).
    transformer = dict_unpacking_module.DictUnpackingTransformer(ast_module)

def test_dict_unpacking_transformer_visits_parsed_module():
    """Ensure DictUnpackingTransformer can visit a parsed AST Module without raising."""
    # Source string is kept exactly as in the original test.
    source = "39@U3\r"

    # Instantiate the transformer with the original source.
    transformer = dict_unpacking_module.DictUnpackingTransformer(source)

    # Parse the source into an AST Module using typed_ast.ast3.parse.
    parsed = typed_ast_ast3.parse(source)

    # Run the transformer's visit_Module on the parsed module (preserve original call).
    # The test succeeds if no exception is raised.
    result = transformer.visit_Module(parsed)

