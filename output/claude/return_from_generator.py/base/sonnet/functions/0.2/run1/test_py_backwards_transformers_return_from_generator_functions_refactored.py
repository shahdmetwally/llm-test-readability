import pytest
import typed_ast.ast3 as ast3

def test_dump_with_none_input():
    """Test that ast3.dump handles None as input without raising unexpectedly."""
    none_value = None
    ast3.dump(none_value)

