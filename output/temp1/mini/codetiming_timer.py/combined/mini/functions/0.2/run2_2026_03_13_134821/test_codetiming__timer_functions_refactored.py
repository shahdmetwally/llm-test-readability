import pytest

import codetiming_timer as timer

def test_timererror_can_be_instantiated():
    """Ensure TimerError can be instantiated without raising."""
    # Instantiate the TimerError class from the codetiming module to verify it exists.
    timer_error_instance = timer.TimerError()

def test_timer_enter_exit_and_start_sequence():
    """Exercise Timer.__enter__, __exit__, and start() in the original call order.

    This test calls the context enter/exit dunder methods and start() on the
    object returned by __enter__ and on the original instance to ensure the
    sequence of calls is preserved (the dunder methods are invoked
    intentionally).
    """
    # Create a Timer instance
    timer_instance = timer.Timer()

    # Simulate entering the context manager (calls __enter__)
    context_timer = timer_instance.__enter__()

    # Simulate exiting the context manager (calls __exit__); result is intentionally ignored
    _ = timer_instance.__exit__()

    # Start the timer returned by __enter__()
    _ = context_timer.start()

    # Start the original timer instance as well
    timer_instance.start()

def test_timer_context_manager_enter_and_exit_calls():
    """Ensure Timer.__enter__ and __exit__ can be called in sequence without errors."""
    # Create a Timer instance
    timer_instance = timer.Timer()
    # Call __enter__ explicitly (simulating the context manager enter)
    entered_timer = timer_instance.__enter__()
    # __enter__ should return something (commonly the timer instance)
    assert entered_timer is not None
    # Call __exit__ explicitly (simulating the context manager exit)
    exit_result = timer_instance.__exit__()
    # __exit__ typically returns None or a boolean; ensure calling it does not raise and returns an expected type
    assert exit_result is None or isinstance(exit_result, bool)

def test_call_timer_exit_directly() -> None:
    """Ensure FloatArg and TimerError can be instantiated and Timer.__exit__ can be invoked directly."""
    # Construct the same helper objects used by the original test
    float_arg = timer.FloatArg()
    timer_error = timer.TimerError()

    # Create a Timer instance and call its __exit__ method directly,
    # preserving the original invocation order.
    t = timer.Timer()
    t.__exit__()

def test_timer_logger_none_start_and_none_enter_call() -> None:
    """Create a Timer with logger=None, start it, then call __enter__ on a None value (preserve original behaviour)."""
    # Use explicit None logger as in the original test
    logger_none = None
    timer_instance = timer.Timer(logger=logger_none)

    # Start the timer (return value intentionally not used in assertions)
    _ = timer_instance.start()

    # dict.__setitem__ returns None. Create a dict that references itself to mirror original test.
    self_ref_dict = {}
    setitem_result = self_ref_dict.__setitem__(None, self_ref_dict)

    # Call __enter__() on the result of dict.__setitem__ (which is None).
    # This preserves the original behaviour (will raise AttributeError at runtime).
    setitem_result.__enter__()

def test_timer_enter_stop_eq_and_repr_sequence():
    """Smoke-test a sequence of Timer operations: enter, equality check, stop, repr, and start."""
    # Create a root Timer instance
    root_timer = timer.Timer()

    # Simulate entering the timer context (start) and get the returned object
    entered_timer = root_timer.__enter__()

    # Use a negative integer literal as in the original test
    negative_value = -1092

    # Create FloatArg instances (kept as in original)
    float_arg_a = timer.FloatArg()

    # Construct another Timer using the entered_timer as the initial_text argument
    timer_with_initial_from_enter = timer.Timer(initial_text=entered_timer)

    # Create a second FloatArg instance as originally done
    float_arg_b = timer.FloatArg()

    # Perform an equality check on the original timer with the negative integer
    eq_result = root_timer.__eq__(negative_value)

    # Stop the entered timer (record elapsed time)
    elapsed_time = entered_timer.stop()

    # Construct a Timer with text and initial_text based on earlier values
    timer_with_text_and_initial = timer.Timer(text=float_arg_a, initial_text=eq_result)

    # Call __repr__ on both Timer objects as in the original sequence
    repr_root = root_timer.__repr__()
    repr_timer_with_text = timer_with_text_and_initial.__repr__()

    # Start the last timer (as in the original test)
    start_result = timer_with_text_and_initial.start()

def test_timer_start_then_exit_and_followup_dict_operations():
    """
    Start a Timer with a None logger, call __exit__, perform dict setitem with None as key,
    then call .start() on the result of dict.__setitem__ to reproduce the original AttributeError.
    """
    # Use None as the logger (matches original test's none_type_0)
    logger = None

    # Construct a Timer with the None logger
    timer_instance = timer.Timer(logger=logger)

    # Start the timer (original: none_type_1 = timer_0.start())
    start_result = timer_instance.start()

    # Create an empty dictionary (original: dict_0 = {})
    sample_dict = {}

    # Use None as the key (original: none_type_2 = None)
    none_key = None

    # Call __exit__() on the timer (original: none_type_3 = timer_0.__exit__())
    exit_result = timer_instance.__exit__()

    # Set the dictionary to contain itself under the None key
    # (original: var_0 = dict_0.__setitem__(none_type_2, dict_0))
    setitem_result = sample_dict.__setitem__(none_key, sample_dict)

    # Call __repr__ on the result of __setitem__ (setitem_result is None, so repr_result == 'None')
    repr_result = setitem_result.__repr__()

    # Finally, attempt to call .start() on the result of __setitem__ to preserve original behavior
    # (this will raise AttributeError because setitem_result is None)
    setitem_result.start()

def test_timer_enter_exit_eq_and_start_with_object_initial_text_and_logger_flag():
    """Exercise Timer's __enter__, __exit__, and __eq__, then build timers using
    an object as initial_text and a boolean logger, and call start() on the final timer.
    """
    # Create a Timer instance
    primary_timer = timer.Timer()

    # Explicitly enter the context manager; __enter__ should return the Timer instance
    entered_timer = primary_timer.__enter__()

    # Call __eq__ comparing the timer to itself (expected to be True)
    is_self_equal = primary_timer.__eq__(primary_timer)

    # Explicitly exit the context manager; __exit__ typically returns None
    exit_result = primary_timer.__exit__()

    # Construct a Timer using the previously-entered Timer object as initial_text,
    # and using the boolean result from __eq__ as logger
    timer_with_initial_text = timer.Timer(initial_text=entered_timer, logger=is_self_equal)

    # Construct another Timer, passing entered_timer positionally (as name),
    # using the previous Timer instance as initial_text, and the same logger value
    timer_with_name_and_logger = timer.Timer(entered_timer, initial_text=timer_with_initial_text, logger=is_self_equal)

    # Start the final timer (preserves the original execution)
    timer_with_name_and_logger.start()

def test_timer_lifecycle_start_stop_enter_and_copy() -> None:
    """Verify that Timer can be started, stopped, entered, and that copy() is callable using the literal initial text."""
    # Use the exact literal as in the original test
    initial_text = "Timer started"

    # Create a Timer instance using the provided module alias `timer`
    timer_instance = timer.Timer(initial_text)

    # Start the timer (original code captured this return as none_type_0)
    start_result = timer_instance.start()

    # Stop the timer and capture the elapsed time (original code captured this as float_0)
    elapsed_seconds = timer_instance.stop()

    # Enter the timer as a context manager (original code called __enter__ and stored it)
    entered_timer = timer_instance.__enter__()

    # Call the copy method exactly as the original test did (preserve call)
    timer_instance.copy()

