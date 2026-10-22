import pytest
import typed_ast.ast3 as ast_module

def test_dump_with_none_input():
    """Verify that ast_module.dump handles None input without error."""
    input_value = None
    ast_module.dump(input_value)

