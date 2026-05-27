import pytest
import typed_ast.ast3 as ast3

def test_dump_accepts_none():
    """Call ast3.dump with None to ensure the function can be invoked with a None node."""
    # Represent the absent/empty AST node explicitly for readability.
    node = None

    # Invoke the dump function exactly as in the original test (was module_0.dump(None)).
    # Using the imported alias `ast3` (typed_ast.ast3) so references match file-level imports.
    ast3.dump(node)

