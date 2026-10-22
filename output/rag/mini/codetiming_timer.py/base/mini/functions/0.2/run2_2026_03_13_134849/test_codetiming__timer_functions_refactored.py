import pytest

import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Instantiate TimerError to verify it constructs without raising exceptions."""
    # Create an instance of the TimerError exception class using the module alias.
    timer_error = timer.TimerError()
    assert isinstance(timer_error, timer.TimerError)

def test_timer_enter_exit_then_start_called_on_both_references():
    """Exercise __enter__, __exit__, and start() calls on a Timer instance and its entered reference.
    
    This ensures invoking the context manager methods and start() in this sequence executes
    without altering behaviour (no assertions here; the calls must simply succeed).
    """
    # Create a Timer instance
    timer_instance = timer.Timer()
    # Call __enter__ explicitly (returns the same Timer instance)
    entered_timer = timer_instance.__enter__()
    # Call __exit__ explicitly (expected to return None)
    exit_result = timer_instance.__exit__()
    # Call start() on the entered reference (expected to return None)
    start_result_on_entered = entered_timer.start()
    # Call start() on the original instance reference as well
    timer_instance.start()

def test_timer_enter_and_exit_methods_invokable_directly():
    """Ensure a Timer can be entered and exited by calling its dunder methods directly.

    This simulates using the Timer as a context manager but invokes __enter__/__exit__
    explicitly to verify those methods are callable and return/control flow is preserved.
    """
    # Instantiate a Timer
    timer_instance = timer.Timer()

    # Invoke __enter__ as if using 'with Timer() as t:'
    entered_timer = timer_instance.__enter__()
    assert entered_timer is timer_instance

    # Invoke __exit__ as if leaving the context normally (no exception info provided)
    exit_result = timer_instance.__exit__()
    assert exit_result in (None, False, True)

def test_timer_exit_called_without_arguments():
    """Ensure calling Timer.__exit__ with no arguments executes (regression check)."""
    # Create an instance of a FloatArg (unused, kept for original setup)
    float_arg = timer.FloatArg()
    # Create a TimerError instance (unused, kept for original setup)
    timer_error = timer.TimerError()
    # Instantiate a Timer and call its __exit__ method without arguments
    t = timer.Timer()
    t.__exit__()

def test_timer_with_none_logger_and_invalid_enter_call():
    """Starting a Timer with logger=None, performing dict.__setitem__, then calling __enter__ on its result raises AttributeError."""
    # Use an explicit None for the logger (matching the original test)
    none_logger = None

    # Create and start the timer (logger is None)
    timer_instance = timer.Timer(logger=none_logger)
    timer_instance.start()

    # Prepare a dictionary and perform __setitem__ which returns None
    sample_dict = {}
    setitem_result = sample_dict.__setitem__(None, sample_dict)

    # Attempting to call __enter__ on the None result should raise AttributeError
    with pytest.raises(AttributeError):
        setitem_result.__enter__()

def test_timer_context_enter_stop_and_initial_text_repr():
    """Exercise Timer __enter__/stop, equality, repr, and start with various args."""
    # Create a base Timer instance and enter its context manually
    root_timer = timer.Timer()
    context_timer = root_timer.__enter__()  # equivalent to entering a context manager

    # Use a negative integer to test equality comparison
    negative_int = -1092

    # Create formatting-like arguments (FloatArg instances) used as text parameters
    format_arg1 = timer.FloatArg()

    # Create a Timer that uses the previously entered timer object as its initial_text
    timer_with_initial_text_context = timer.Timer(initial_text=context_timer)

    # Another FloatArg instance for later use
    format_arg2 = timer.FloatArg()

    # Test equality method of the root timer against the negative integer
    eq_result = root_timer.__eq__(negative_int)

    # Stop the context timer and capture the elapsed time
    stopped_duration = context_timer.stop()

    # Create a Timer that uses a FloatArg as text and the equality result as initial_text
    timer_with_text_and_initial_text = timer.Timer(text=format_arg1, initial_text=eq_result)

    # Capture reprs for diagnostic/inspection purposes
    repr_root = root_timer.__repr__()
    repr_timer_with_text = timer_with_text_and_initial_text.__repr__()

    # Start the third timer (expecting None return)
    start_result = timer_with_text_and_initial_text.start()

    # Assertions to validate expected behavior (be permissive about exact return types)
    assert hasattr(context_timer, "stop")
    assert (eq_result is NotImplemented) or isinstance(eq_result, bool)
    assert (stopped_duration is None) or isinstance(stopped_duration, (int, float))
    assert isinstance(repr_root, str) and repr_root
    assert isinstance(repr_timer_with_text, str) and repr_timer_with_text
    assert start_result is None

def test_timer_context_manager_repr_start_stop_and_equality_checks():
    """Exercise entering a Timer as a context manager, use of repr/equality, stop/start,
    and construction with text/initial_text.
    """
    # Create the main timer and simulate context-manager entry (starts timer)
    main_timer = timer.Timer()
    entered_timer = main_timer.__enter__()

    # Capture a representation from the entered timer to use as initial_text elsewhere
    repr_text = entered_timer.__repr__()

    # Construct timers using the captured representation and some FloatArg instances
    float_arg_a = timer.FloatArg()
    timer_with_initial_text = timer.Timer(initial_text=repr_text)

    float_arg_b = timer.FloatArg()
    timer_with_text_and_initial = timer.Timer(text=float_arg_a, initial_text=repr_text)

    # Perform an equality comparison against an integer to exercise __eq__
    negative_value = -1092
    eq_result = main_timer.__eq__(negative_value)

    # Stop the entered/context timer and capture repr outputs after operations
    elapsed = entered_timer.stop()
    repr_after = main_timer.__repr__()
    repr_timer3 = timer_with_text_and_initial.__repr__()

    # Start the timer that was created with text and initial_text
    timer_with_text_and_initial.start()

def test_timer_start_then_exit_and_none_interactions():
    """Start a Timer with logger=None, exit it, perform a dict.setitem with None,
    inspect the result's repr, and then (intentionally) call .start() on that result.
    This preserves the original call sequence and side effects.
    """
    # Use an explicit None for the logger (matches original test)
    logger_none = None

    # Create a Timer with a None logger and start it
    timer_instance = timer.Timer(logger=logger_none)
    start_result = timer_instance.start()

    # Prepare an empty dict and use None as a key (as in the original)
    sample_dict = {}
    none_key = None

    # Call __exit__() on the timer (context-exit behavior)
    exit_result = timer_instance.__exit__()

    # dict.__setitem__ returns None; keep that returned value in a variable
    setitem_result = sample_dict.__setitem__(none_key, sample_dict)

    # Call __repr__ on the result (None.__repr__() is valid and returns 'None')
    repr_result = setitem_result.__repr__()

    # Verify the repr result is as expected
    assert repr_result == "None"

    # Finally, call .start() on the setitem_result (this should raise AttributeError)
    try:
        setitem_result.start()
    except AttributeError:
        # Expected outcome: None has no .start() attribute
        pass
    else:
        raise AssertionError("Expected AttributeError when calling .start() on the result of dict.__setitem__()")

def test_timer_start_stop_enter_and_copy_behavior():
    """Exercise Timer start/stop/enter sequence and call copy().

    Creates a Timer with the literal "Timer started", starts and stops it,
    enters it via __enter__(), and calls copy() — preserving the original
    call sequence and values.
    """
    timer_label = "Timer started"
    timer_obj = timer.Timer(timer_label)  # construct Timer with the same literal

    # Start the timer (original captured the return value)
    start_result = timer_obj.start()

    # Stop the timer and capture elapsed time (as in the original test)
    stop_result = timer_obj.stop()

    # Enter the timer as a context manager (call __enter__ directly)
    enter_result = timer_obj.__enter__()

    # Invoke copy() exactly as in the original test
    timer_obj.copy()

