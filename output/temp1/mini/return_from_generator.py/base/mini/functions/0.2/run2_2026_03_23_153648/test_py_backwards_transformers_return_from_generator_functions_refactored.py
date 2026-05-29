import pytest

import typed_ast.ast3 as typed_ast_ast3

def test_dump_accepts_none():
    """Ensure typed_ast.ast3.dump can be invoked with None (no exception raised)."""
    node = None  # represent the absent/empty AST node
    # Call the dump function with a None node to verify it accepts this input.
    typed_ast_ast3.dump(node)

