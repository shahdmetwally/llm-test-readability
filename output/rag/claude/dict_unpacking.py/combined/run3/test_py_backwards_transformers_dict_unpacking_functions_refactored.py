import pytest
import typed_ast._ast3 as ast3_internal
import dict_unpacking as dict_unpacking
import typed_ast.ast3 as ast3

def test_dict_unpacking_transformer_instantiates_with_module():
    """Verify that DictUnpackingTransformer can be instantiated with a parsed AST module."""

    # Create a bare AST module node to serve as input to the transformer
    parsed_module = ast3.mod()

    # Instantiate the transformer with the AST module — should not raise
    transformer = dict_unpacking.DictUnpackingTransformer(parsed_module)

def test_visit_module_processes_parsed_ast_without_error():
    """Test that DictUnpackingTransformer.visit_Module processes a parsed AST module without error."""

    # Arbitrary source string used as input to exercise the transformer
    source_code = "39@U3\r"

    # Instantiate the transformer with the source code identifier
    transformer = dict_unpacking.DictUnpackingTransformer(source_code)

    # Parse the source string into an AST module node
    parsed_module = ast3.parse(source_code)

    # Apply the transformer's visit_Module method to the parsed AST
    transformed_module = transformer.visit_Module(parsed_module)

