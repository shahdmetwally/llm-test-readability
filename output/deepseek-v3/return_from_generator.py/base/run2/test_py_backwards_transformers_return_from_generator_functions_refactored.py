import pytest
import typed_ast.ast3 as typed_ast

def test_dump_handles_none_input():
    """Test that the dump function can be called with None without crashing."""
    none_input = None
    typed_ast.dump(none_input)

