import pytest
import typed_ast._ast3 as ast3_internal
import dict_unpacking as dict_unpacking
import typed_ast.ast3 as ast3

def test_dict_unpacking_transformer_instantiation_with_module_node():
    """Test that DictUnpackingTransformer can be instantiated with a module AST node."""
    # Create a bare module AST node to serve as input to the transformer
    module_node = ast3.mod()

    # Instantiate the transformer with the module node to verify construction succeeds
    transformer = dict_unpacking.DictUnpackingTransformer(module_node)

def test_visit_module_processes_parsed_ast_without_error():
    """Test that DictUnpackingTransformer.visit_Module processes a parsed AST module node from a source string."""

    # The raw source string used as input for parsing
    source_code = "39@U3\r"

    # Instantiate the transformer with the source code
    transformer = dict_unpacking.DictUnpackingTransformer(source_code)

    # Parse the source code into an AST module node
    parsed_module = ast3.parse(source_code)

    # Apply the transformer's visit_Module to the parsed AST
    visited_module = transformer.visit_Module(parsed_module)

