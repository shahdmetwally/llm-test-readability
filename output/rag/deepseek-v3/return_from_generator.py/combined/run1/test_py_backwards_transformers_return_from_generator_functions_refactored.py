import pytest
import typed_ast.ast3 as ast_module

def test_dump_with_none_argument_does_not_raise_error():
    """Verify that the dump function accepts None as an argument."""
    none_input = None
    ast_module.dump(none_input)

