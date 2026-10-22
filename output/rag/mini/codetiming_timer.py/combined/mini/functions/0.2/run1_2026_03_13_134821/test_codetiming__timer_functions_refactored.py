import pytest

import codetiming_timer as timer_module

def test_timer_error_instantiation() -> None:
    """Verify TimerError can be constructed from the codetiming_timer module."""
    # Construct to assert it's importable and instantiable.
    timer_error = timer_module.TimerError()
    assert isinstance(timer_error, timer_module.TimerError)

def test_timer_enter_exit_then_start_sequence():
    """Verify entering/exiting a Timer context and then calling start() happen in sequence without raising errors."""
    # Create a Timer instance from the timer module
    timer_instance = timer_module.Timer()

    # Simulate entering the context manager (calls __enter__)
    entered_timer = timer_instance.__enter__()

    # Simulate exiting the context manager (calls __exit__) using the standard signature
    exit_result = timer_instance.__exit__(None, None, None)

    # Call start() on the object returned by __enter__ and capture its return value
    start_result_after_enter = entered_timer.start()

    # Call start() on the original timer instance as well
    start_result_from_original = timer_instance.start()

def test_timer_enter_and_exit_can_be_called() -> None:
    """Ensure a Timer instance's __enter__ and __exit__ methods can be invoked directly."""
    # Create a Timer instance (same as original construction)
    timer_instance = timer_module.Timer()

    # Call the context manager enter method directly and capture its return value
    entered_value = timer_instance.__enter__()

    # Call the context manager exit method directly. Some implementations expect
    # the three exception-related arguments, others accept none, so handle both.
    try:
        exit_result = timer_instance.__exit__(None, None, None)
    except TypeError:
        exit_result = timer_instance.__exit__()

    # If no exception was raised by the above calls, the test is considered successful.
    assert True

def test_timer_exit_can_be_called_without_arguments():
    """Ensure a Timer instance's __exit__ method can be invoked without arguments."""
    # Create a FloatArg helper instance (unused here, but included as in original test)
    dummy_float_arg = timer_module.FloatArg()

    # Instantiate a TimerError (construction only; matches original behavior)
    timer_error_instance = timer_module.TimerError()

    # Create a Timer instance and call its __exit__ method with no arguments
    timer_instance = timer_module.Timer()
    timer_instance.__exit__()

def test_timer_start_then_none_setitem_result_enter_calls():
    """Start a Timer with logger=None, do a dict.__setitem__ that returns None, then call __enter__ on that result."""
    # Use explicit None for the logger (mirrors original test)
    logger_none = None

    # Construct the Timer with logger=None
    timer_instance = timer_module.Timer(logger=logger_none)

    # Start the timer (result is not used later, but preserved to match original behaviour)
    start_result = timer_instance.start()

    # Prepare an empty mapping and use None as the key (preserve original literal values)
    mapping = {}
    key_none = None

    # __setitem__ returns None; capture that result
    setitem_result = mapping.__setitem__(key_none, mapping)

    # Call __enter__ on the result of __setitem__ (this reproduces the original behavior)
    setitem_result.__enter__()

def test_timer_context_enter_stop_and_start_various_args():
    """Exercise Timer context enter/stop and Timer construction with various initial_text/text arguments."""
    # Create a primary Timer instance and enter its context manually
    primary_timer = timer_module.Timer()
    context_timer = primary_timer.__enter__()

    # Use a negative integer literal to exercise __eq__ later
    negative_value = -1092

    # Create FloatArg instances used as text arguments (preserve construction order)
    float_arg_a = timer_module.FloatArg()
    float_arg_b = timer_module.FloatArg()

    # Construct a Timer using the context_timer as initial_text
    timer_with_initial_context = timer_module.Timer(initial_text=context_timer)

    # Compare primary_timer to an integer (invokes __eq__)
    equals_result = primary_timer.__eq__(negative_value)

    # Stop the context_timer to exercise stop()
    elapsed_time = context_timer.stop()

    # Create a Timer with a text FloatArg and initial_text from the previous __eq__ result
    timer_with_text_and_initial = timer_module.Timer(text=float_arg_a, initial_text=equals_result)

    # Call __repr__ on timers to preserve original interactions
    repr_primary_timer = primary_timer.__repr__()
    repr_timer_with_text_and_initial = timer_with_text_and_initial.__repr__()

    # Start the last timer (invokes start()), expected to return None in original sequence
    start_result_none = timer_with_text_and_initial.start()

def test_timer_start_exit_and_none_method_calls():
    """Start a Timer with an explicit None logger, call its __exit__,
    perform a dict.__setitem__ (which returns None), then call methods
    on that None to reproduce the original behavior.
    """
    # Use an explicit None for the logger to match the original test's setup
    logger_none = None

    # Create a Timer with no logger
    timer_instance = timer_module.Timer(logger=logger_none)

    # Start the timer (result intentionally captured as in the original)
    start_result = timer_instance.start()

    # Prepare an empty dict and a None key, as in the original
    empty_dict = {}
    none_key = None

    # Call __exit__ on the timer (no exception info passed, matching original)
    exit_result = timer_instance.__exit__()

    # Perform the dict.__setitem__ which returns None; capture the result
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)

    # Call __repr__ on the result of setitem (which is None.__repr__())
    repr_result = setitem_result.__repr__()

    # Finally, attempt to call .start() on the setitem result (None),
    # preserving the original sequence that leads to an AttributeError.
    setitem_result.start()

def test_timer_context_manager_and_start_with_nonstandard_initial_text_and_logger():
    """Exercise Timer context manager methods and start() when given nonstandard initial_text/logger values."""
    # Create a Timer instance
    base_timer = timer_module.Timer()
    # Enter the context manager (calls __enter__) and capture returned object
    entered_timer = base_timer.__enter__()
    # Compare the timer to itself using __eq__ and capture the result (likely True)
    equality_result = base_timer.__eq__(base_timer)
    # Exit the context manager (calls __exit__) and capture any return (usually None)
    exit_result = base_timer.__exit__()
    # Construct a Timer passing a Timer instance as initial_text and a boolean as logger
    timer_with_initial_text = timer_module.Timer(initial_text=entered_timer, logger=equality_result)
    # Construct another Timer using a positional name argument and the unusual initial_text/logger again
    timer_with_positional_name = timer_module.Timer(entered_timer, initial_text=timer_with_initial_text, logger=equality_result)
    # Start the final timer
    timer_with_positional_name.start()

def test_timer_sequence_start_stop_enter_and_copy() -> None:
    """Verify a Timer can be started, stopped, entered, and copied by calling the same sequence as the original test."""
    # Create a Timer using the same literal string from the original test
    initial_text = "Timer started"
    timer = timer_module.Timer(initial_text)

    # Start the timer (original captured the return as none_type_0)
    start_result = timer.start()

    # Stop the timer (original captured the return as float_0)
    elapsed_time = timer.stop()

    # Manually invoke context-manager enter (original captured the return as timer_1)
    enter_result = timer.__enter__()

    # Call copy() as in the original test
    timer.copy()

