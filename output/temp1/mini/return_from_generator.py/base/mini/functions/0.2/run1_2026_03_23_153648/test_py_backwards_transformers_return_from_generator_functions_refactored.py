import pytest

import typed_ast.ast3 as typed_ast_ast3

def test_dump_accepts_none_without_error():
    """Ensure typed_ast_ast3.dump can be called with None without raising an exception."""
    node = None
    # Calling dump with None should not raise; absence of exception means the test passes.
    typed_ast_ast3.dump(node)

