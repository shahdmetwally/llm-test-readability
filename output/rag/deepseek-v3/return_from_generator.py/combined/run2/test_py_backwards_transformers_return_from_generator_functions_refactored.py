import pytest
import typed_ast.ast3 as ast_module

def test_dump_handles_none_input_gracefully():
    """Tests that ast_module.dump() accepts None without raising an exception."""
    none_input = None
    # No explicit assertion; the test passes if dump() handles None gracefully
    ast_module.dump(none_input)

