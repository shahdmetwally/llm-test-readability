import pytest
import typed_ast.ast3 as ast3

def test_dump_with_none_input():
    """Test that ast3.dump handles None as input without error."""
    # Pass None explicitly to verify dump accepts it without raising
    none_input = None
    ast3.dump(none_input)

