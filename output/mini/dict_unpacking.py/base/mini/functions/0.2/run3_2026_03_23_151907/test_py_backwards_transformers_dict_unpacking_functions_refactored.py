import pytest

import typed_ast._ast3 as ast3_private
import dict_unpacking as dict_unpacking_module
import typed_ast.ast3 as ast3

def test_dict_unpacking_transformer_initialization():
    """Ensure DictUnpackingTransformer can be instantiated with a module AST."""
    # Create a module AST node (using the typed_ast._ast3 helper).
    module_ast = ast3_private.mod()

    # Initialize the transformer that handles dict-unpacking constructs.
    transformer = dict_unpacking_module.DictUnpackingTransformer(module_ast)

    # Basic sanity checks: instance created and has expected type.
    assert transformer is not None
    assert isinstance(transformer, dict_unpacking_module.DictUnpackingTransformer)

    # If the transformer stores the module, ensure it references the same object.
    if hasattr(transformer, "module"):
        assert transformer.module is module_ast

def test_dict_unpacking_transformer_visits_module():
    """Ensure DictUnpackingTransformer can parse and visit a module from source text."""
    # Source code under test (kept exactly as in the original test)
    source_code = "39@U3\r"

    # Instantiate the transformer with the source text
    transformer = dict_unpacking_module.DictUnpackingTransformer(source_code)

    # Parse the source into an AST using the typed_ast.ast3.parse alias
    parsed_module = ast3.parse(source_code)

    # Run the transformer's visit_Module on the parsed AST (preserve call name and order)
    transformed_module = transformer.visit_Module(parsed_module)

