import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Ensure the TimerError exception class can be instantiated."""
    # Instantiate TimerError from the aliased codetiming_timer module.
    err = timer.TimerError()
    assert isinstance(err, timer.TimerError)

def test_timer_context_enter_exit_and_start_sequence():
    """Exercise Timer.__enter__, __exit__, and start in sequence to exercise state transitions.

    This preserves the original call order without making assertions.
    """
    # Instantiate a Timer (using the imported alias 'timer')
    timer_obj = timer.Timer()

    # Directly call the context manager methods to exercise state changes
    entered_timer = timer_obj.__enter__()
    exit_result = timer_obj.__exit__()  # no exception info provided

    # Call start() on the object returned by __enter__(), then on the original
    start_result_after_enter = entered_timer.start()
    timer_obj.start()

def test_timer_context_manager_enter_exit_behavior():
    """Manually exercise Timer's context-manager methods.

    Calling __enter__ should return the Timer instance; calling __exit__ with no
    arguments should return None.
    """
    timer_instance = timer.Timer()
    entered_timer = timer_instance.__enter__()  # simulate entering the context manager
    assert entered_timer is timer_instance
    exit_result = timer_instance.__exit__()  # simulate exiting the context manager (no exception)
    assert exit_result is None

def test_timer_exit_can_be_invoked_without_arguments():
    """Sanity check: calling Timer.__exit__() without any arguments should not raise."""
    # Create a FloatArg instance (kept to preserve original call sequence)
    float_arg = timer.FloatArg()
    # Instantiate TimerError (preserved from original, not used here)
    timer_error = timer.TimerError()
    # Create a Timer and invoke its __exit__ method without passing any arguments
    t = timer.Timer()
    t.__exit__()

def test_start_timer_with_no_logger_then_call_enter_on_setitem_result():
    """Start a Timer with logger=None, perform a dict.__setitem__ (which returns None),
    and then call __enter__() on that None result to exercise error behavior.
    """
    # Use explicit None for clarity when creating the Timer with no logger.
    no_logger = None
    t = timer.Timer(logger=no_logger)

    # Start the timer (side-effect only; return value is not used).
    start_result = t.start()

    # Prepare a mapping and perform __setitem__; dict.__setitem__ returns None.
    mapping = {}
    key = None
    setitem_result = mapping.__setitem__(key, mapping)

    # Calling __enter__ on the None returned by __setitem__ (preserves original behavior).
    setitem_result.__enter__()

def test_timer_context_and_method_sequence():
    """Exercise a sequence of Timer context, comparison, logging/text args, and lifecycle methods.

    This reproduces the original execution order: create timers, enter context, create
    FloatArg instances, compare a timer to an int, stop the context timer, create more
    timers using previous results as constructor args, call __repr__ on timers, and
    finally start a timer.
    """
    # Create a primary Timer instance
    primary_timer = timer.Timer()

    # Enter the context manager (calls __enter__)
    context_timer = primary_timer.__enter__()

    # An arbitrary negative integer used for equality comparison
    negative_int = -1092

    # Create a FloatArg instance (used as a text argument later)
    float_arg_first = timer.FloatArg()

    # Construct another Timer, passing the context_timer object as initial_text
    timer_with_context_initial = timer.Timer(initial_text=context_timer)

    # Create a second FloatArg instance (not otherwise inspected here)
    float_arg_second = timer.FloatArg()

    # Compare primary_timer to an integer using __eq__
    comparison_result = primary_timer.__eq__(negative_int)

    # Stop the context timer (calls stop)
    stopped_value = context_timer.stop()

    # Construct a Timer using a FloatArg for text and the previous comparison result as initial_text
    timer_with_float_and_comparison = timer.Timer(
        text=float_arg_first, initial_text=comparison_result
    )

    # Obtain string representations via __repr__ on timers
    primary_repr = primary_timer.__repr__()
    other_timer_repr = timer_with_float_and_comparison.__repr__()

    # Start the other timer (calls start); result intentionally unused (expected None)
    start_result = timer_with_float_and_comparison.start()

def test_timer_context_and_initial_text_interactions():
    """Exercise"""
    pass

def test_timer_with_none_logger_calls_and_none_method_usage():
    """Exercise Timer with logger=None, start/exit, dict.__setitem__, and calling methods on the resulting None.

    This test intentionally:
    - constructs a Timer with an explicit None logger
    - starts the timer and then exits it
    - performs dict.__setitem__ which returns None
    - calls methods on that None to reproduce the original execution sequence and side effects
    """
    # Construct Timer with an explicit None logger
    logger_none = None
    t = timer.Timer(logger=logger_none)

    # Start the timer (capture result though Timer.start typically returns None)
    start_result = t.start()

    # Prepare a dictionary and a None key to pass to __setitem__
    sample_dict = {}
    none_key = None

    # Call __exit__ on the timer without arguments to mirror the original sequence
    exit_result = t.__exit__()

    # dict.__setitem__ returns None; preserve that exact return value
    setitem_result = sample_dict.__setitem__(none_key, sample_dict)

    # Call __repr__ on the None result (valid; returns 'None')
    repr_of_setitem_result = setitem_result.__repr__()

    # Finally, attempt to call .start() on the None result to preserve original behavior
    setitem_result.start()

def test_timer_start_with_values_from_another_timer():
    """Exercise Timer.start using values obtained from another Timer instance and its equality check."""
    # Create a primary Timer and enter it via the context-manager entry method
    primary_timer = timer.Timer()
    entered_timer = primary_timer.__enter__()  # starts the primary timer

    # Use the result of an equality check as a (non-callable) logger argument
    equality_result = primary_timer.__eq__(primary_timer)

    # Exit the primary timer context (stop it) using the dunder exit method
    exit_result = primary_timer.__exit__()  # stops the primary timer

    # Create new Timer instances using the previously obtained objects/values as arguments
    timer_with_initial_text = timer.Timer(initial_text=entered_timer, logger=equality_result)
    timer_with_positional_name = timer.Timer(entered_timer, initial_text=timer_with_initial_text, logger=equality_result)

    # Start the final timer
    timer_with_positional_name.start()

