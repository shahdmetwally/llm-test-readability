import pytest

import typed_ast.ast3 as ast3

def test_dump_with_none_value():
    """Call dump on a None value to ensure it accepts None without error."""
    # Prepare the input value (originally: none_type_0 = None)
    none_value = None

    # Invoke the module's dump function with None. The symbol `module_0`
    # is preserved exactly as in the original test (provided by the test harness).
    module_0.dump(none_value)

