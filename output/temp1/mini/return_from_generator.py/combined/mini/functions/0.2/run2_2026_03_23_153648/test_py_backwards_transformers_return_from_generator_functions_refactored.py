import pytest

import typed_ast.ast3 as ast3

def test_dump_accepts_none_without_exception():
    """Ensure ast3.dump can be called with None without raising an exception."""
    # Keep the original literal exactly as None to verify the function handles it.
    none_value = None

    # The test will fail if ast3.dump raises an unexpected exception.
    ast3.dump(none_value)

