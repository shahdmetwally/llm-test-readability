import pytest
import typed_ast.ast3 as ast_module

def test_dump_none_value():
    """Test that module.dump() handles None input without error."""
    none_value = None
    ast_module.dump(none_value)

