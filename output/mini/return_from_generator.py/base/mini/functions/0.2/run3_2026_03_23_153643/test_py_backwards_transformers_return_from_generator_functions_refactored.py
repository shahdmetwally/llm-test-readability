import pytest

import typed_ast.ast3 as ast3

def test_dump_none_does_not_raise_exception():
    """Smoke test: ast3.dump should accept None (no exception raised)."""
    node = None  # represent the absence of an AST node
    ast3.dump(node)

