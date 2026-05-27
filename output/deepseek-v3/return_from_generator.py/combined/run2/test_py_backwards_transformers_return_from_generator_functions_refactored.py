import pytest
import typed_ast.ast3 as typed_ast

def test_dump_handles_none_value():
    """Test that typed_ast.ast3.dump can be called with None without raising."""
    # Call dump with None to verify it handles null input gracefully
    none_value = None
    typed_ast.dump(none_value)

