import pytest

import re as regex
import helpers as test_helpers

def test_purge_result_passed_to_debug():
    """Call purge(), then pass its result to debug(); ensure the call sequence runs as expected."""
    # Call purge() to get the value that should be forwarded to debug()
    purge_result = test_helpers.purge()

    # Forward the purge result to debug(); keep the returned value for potential inspection
    debug_result = test_helpers.debug(purge_result)

def test_variables_generator_instantiation():
    """Verify that VariablesGenerator can be instantiated without raising an exception."""
    # Instantiate VariablesGenerator to ensure construction succeeds.
    variables_generator = test_helpers.module_1.VariablesGenerator()
    assert variables_generator is not None

def test_eager_accepts_variables_generator():
    """Ensure module_1.eager can be invoked with a VariablesGenerator instance."""
    # Create a VariablesGenerator instance to use as input to eager
    variables_generator = module_1.VariablesGenerator()
    # Call the eager wrapper with the generator (preserves original call sequence)
    eager_result = module_1.eager(variables_generator)

def test_eager_debug_warn_and_get_source_sequence():
    """Call eager, VariablesGenerator, debug, eager again, warn, and get_source in sequence."""
    # Keep the same literal input as the original test
    sample_number = 939

    # First eager() call with the numeric input
    first_result = test_helpers.eager(sample_number)

    # Instantiate VariablesGenerator (side-effect / setup)
    vars_generator = test_helpers.VariablesGenerator()

    # Call debug() with the result of the first eager() call
    debug_result = test_helpers.debug(first_result)

    # Call eager() again using the first_result as input
    second_result = test_helpers.eager(first_result)

    # Call warn() with the original numeric input
    warn_result = test_helpers.warn(sample_number)

    # Finally, call get_source() with the first_result
    test_helpers.get_source(first_result)

def test_warn_accepts_proxyhandler_message():
    """Call module_1.warn with the 'ProxyHandler' message to exercise the warn code path (no exceptions expected)."""
    # Prepare the message literal used by the original test
    message = "ProxyHandler"

    # Call the warn function from the module (preserve original call; store return value)
    result = test_helpers.module_1.warn(message)

def test_eager_callable_invocation_with_module_none_and_start():
    """Ensure the object returned by module_1.eager can be invoked via __call__
    with module=None and the callable itself used for positional and start parameters.
    """
    # Use the original integer literal to construct the eager callable
    value = 939

    # Create the eager callable using the original factory call
    eager_callable = module_1.eager(value)

    # Preserve the original None literal for the module parameter
    module_none = None

    # Invoke __call__ exactly as in the original test:
    # - two positional args that are the callable itself
    # - keyword args: module=None and start=<the callable>
    eager_callable.__call__(eager_callable, eager_callable, module=module_none, start=eager_callable)

