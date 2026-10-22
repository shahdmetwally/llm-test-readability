import typed_ast.ast3 as ast
import pytest

def test_dump_method_with_none():
    """Tests the dump function in helpers with None as input."""
    none_object = None
    helpers.dump(none_object)