import pytest
import typed_ast.ast3 as ast_module

def test_dump_accepts_none():
    """Verify that typed_ast's dump() function can handle a None argument."""
    none_node = None
    ast_module.dump(none_node)

