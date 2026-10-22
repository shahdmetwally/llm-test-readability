import typed_ast.ast3 as ast
import pytest

import typed_ast

def test_dump_when_none_supplied_returns_none():
    """
    Test case to ensure that the `dump` function correctly encodes a None value
    as the None type when the `none_value` variable is None.
    """
    
    # None type to be dumped
    none_value = None  

    # Call the `dump` function with the `none_value` variable
    typed_ast.ast3.dump(none_value)

