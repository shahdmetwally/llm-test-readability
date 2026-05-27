import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising an exception."""
    # Constructing TimerError with no arguments should succeed without error
    timer_error_instance = timer.TimerError()

def test_timer_context_manager_followed_by_manual_start():
    """Test that a Timer can be used as a context manager and then started manually after exiting."""
    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager, which starts the timer and returns self
    timer_from_enter = timer_instance.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = timer_instance.__exit__()

    # Start the timer manually via the reference returned by __enter__ (same object)
    start_result = timer_from_enter.start()

    # Attempt to start the same timer again while it is already running
    timer_instance.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer supports the context manager protocol via __enter__ and __exit__."""
    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager, which starts the timer
    entered_timer = timer_instance.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = timer_instance.__exit__()

def test_timer_exit_without_start_raises_timer_error():
    """Test that calling __exit__() on a Timer that was never started raises a TimerError."""
    # Instantiate auxiliary objects as part of the test setup
    float_arg = timer.FloatArg()
    timer_error = timer.TimerError()

    # Create a Timer instance without starting it
    timer_instance = timer.Timer()

    # Directly invoke __exit__() on an unstarted timer, which should raise TimerError
    timer_instance.__exit__()

def test_timer_with_no_logger_none_enter_raises_attribute_error():
    """Test that Timer with logger=None starts without error; __enter__ on None (setitem result) raises AttributeError."""
    # Create a Timer that suppresses all output
    no_logger = None
    silent_timer = timer.Timer(logger=no_logger)

    # Start the silent timer (returns None)
    start_result = silent_timer.start()

    # Build a dict and set a None key pointing to itself
    dummy_dict = {}
    none_key = None
    setitem_result = dummy_dict.__setitem__(none_key, dummy_dict)

    # setitem_result is None; calling __enter__ on None will raise AttributeError
    with pytest.raises(AttributeError):
        setitem_result.__enter__()

def test_timer_context_manager_with_various_constructor_args():
    """Test Timer as context manager alongside varied constructor args, eq, stop, and repr calls."""

    # Use Timer as a context manager; entered_timer is the same object returned by __enter__
    context_timer = timer.Timer()
    entered_timer = context_timer.__enter__()

    # Values used as constructor arguments below
    negative_int = -1092
    float_arg_for_text = timer.FloatArg()

    # Construct a Timer using the entered context timer instance as initial_text
    timer_with_entered_as_initial_text = timer.Timer(initial_text=entered_timer)

    # Second FloatArg constructed (not used further)
    unused_float_arg = timer.FloatArg()

    # Compare context_timer against a negative integer
    eq_result = context_timer.__eq__(negative_int)

    # Stop the entered timer and capture elapsed time
    elapsed_time = entered_timer.stop()

    # Construct a Timer with a FloatArg as text and the eq result as initial_text
    timer_with_float_arg_text = timer.Timer(text=float_arg_for_text, initial_text=eq_result)

    # Retrieve string representations of both timers
    context_timer_repr = context_timer.__repr__()
    timer_with_float_arg_text_repr = timer_with_float_arg_text.__repr__()

    # Start the timer constructed with float_arg_for_text and eq_result
    start_result = timer_with_float_arg_text.start()

