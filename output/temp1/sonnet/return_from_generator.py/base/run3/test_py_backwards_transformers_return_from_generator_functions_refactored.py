import pytest
import typed_ast.ast3 as ast3

def test_dump_with_none_input():
    """Test that dump handles None input without raising an unexpected error."""
    none_value = None
    ast3.dump(none_value)

