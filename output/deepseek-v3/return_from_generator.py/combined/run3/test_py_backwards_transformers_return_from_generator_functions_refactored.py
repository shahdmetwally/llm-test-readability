import pytest
import typed_ast.ast3 as typed_ast

def test_dump_handles_none():
    """
    Test that typed_ast.ast3.dump can be called with None without error.
    """
    none_input = None
    typed_ast.dump(none_input)

