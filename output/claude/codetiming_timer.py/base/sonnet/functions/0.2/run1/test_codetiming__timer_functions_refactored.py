import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising any exceptions."""
    # Verify that the TimerError exception class is directly constructible
    timer_error = timer.TimerError()

def test_timer_raises_error_when_started_while_already_running():
    """Test that starting a timer that is already running raises a TimerError.

    Uses the context manager protocol to start the timer, then verifies that
    calling .start() again (while the timer is still active) raises an error.
    """
    # Create a new timer and start it
    timer_instance = timer.Timer()
    timer_instance.start()

    # Attempt to start the timer again while it is already running
    with pytest.raises(timer.TimerError):
        timer_instance.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer can be used as a context manager via __enter__ and __exit__."""
    # Create a new Timer instance
    t = timer.Timer()

    # Enter the context manager, which starts the timer and returns itself
    active_timer = t.__enter__()

    # Exit the context manager, which stops the timer
    result = t.__exit__()

def test_timer_exit_without_start_raises_error():
    """Test that calling __exit__ on a Timer that was never started raises a TimerError."""
    t = timer.Timer()

    # Attempting to exit a timer context that was never entered should raise an error
    with pytest.raises(timer.TimerError):
        t.__exit__(None, None, None)

def test_timer_start_with_no_logger_then_invalid_context_manager_entry():
    """Test that starting a timer with logger=None succeeds, and that attempting
    to use a dict (with a None key mapping to itself) as a context manager
    raises an AttributeError on __enter__, since dict is not a context manager."""

    # Create a Timer with no logger (suppresses all output)
    none_logger = None
    t = timer.Timer(logger=none_logger)

    # Start the timer (should succeed without logging anything)
    t.start()

    # Build a dict with a None key pointing to itself
    invalid_context = {}
    none_key = None
    invalid_context.__setitem__(none_key, invalid_context)  # {None: {...}}

    # Attempt to use the dict as a context manager — dict has no __enter__,
    # so this call will raise AttributeError
    with pytest.raises(AttributeError):
        invalid_context.__enter__()

def test_timer_context_manager_with_nested_timers_and_repr():
    """Test Timer context manager usage alongside nested Timer instances,
    equality comparison, stop, and repr calls in sequence."""

    # Start a timer using the context manager protocol
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()

    int_val = -1092
    float_arg_0 = timer.FloatArg()

    # Create a nested timer using the running context_timer as initial_text
    nested_timer_0 = timer.Timer(initial_text=context_timer)

    float_arg_1 = timer.FloatArg()

    # Compare base_timer with an integer value
    eq_result = base_timer.__eq__(int_val)

    # Stop the context manager timer and capture elapsed time
    elapsed = context_timer.stop()

    # Create another timer using float_arg and the equality result as initial_text
    nested_timer_1 = timer.Timer(text=float_arg_0, initial_text=eq_result)

    # Get string representations of both timers
    base_timer_repr = base_timer.__repr__()
    nested_timer_1_repr = nested_timer_1.__repr__()

    # Start the second nested timer
    none_result = nested_timer_1.start()

def test_timer_context_manager_with_repr_as_initial_text():
    """Test that a timer started as a context manager can have its repr used
    as initial_text for other timers, and that stopping the context timer works
    correctly alongside creating additional timers."""

    # Start a timer using the context manager protocol
    timer_running = timer.Timer()
    timer_from_context = timer_running.__enter__()

    int_value = -1092

    # Capture the repr of the running context timer
    repr_of_running_timer = timer_from_context.__repr__()

    float_arg_0 = timer.FloatArg()

    # Create a new timer using the repr string as initial_text
    timer_with_repr_initial_text = timer.Timer(initial_text=repr_of_running_timer)

    float_arg_1 = timer.FloatArg()

    # Compare the original timer with an integer (equality check)
    eq_result = timer_running.__eq__(int_value)

    # Stop the context manager timer and capture elapsed time
    elapsed = timer_from_context.stop()

    # Create another timer with a FloatArg text and repr as initial_text
    timer_with_float_text = timer.Timer(text=float_arg_0, initial_text=repr_of_running_timer)

    # Capture repr of both the stopped context timer and the new timer
    repr_of_stopped_timer = timer_running.__repr__()
    repr_of_float_text_timer = timer_with_float_text.__repr__()

    # Start the timer that uses FloatArg text and repr-based initial_text
    timer_with_float_text.start()

def test_timer_start_exit_then_invalid_operations_on_none():
    """
    Test that a Timer with no logger can be started and exited via __exit__,
    and that subsequent invalid operations (setting None as a dict key and
    calling repr/start on the result) behave as expected without errors
    during the timer lifecycle.
    """
    # Create a Timer with logging disabled
    none_logger = None
    t = timer.Timer(logger=none_logger)

    # Start the timer (returns None)
    start_result = t.start()

    # Prepare an empty dict and a None key for later use
    empty_dict = {}
    none_key = None

    # Stop the timer via context manager exit protocol
    exit_result = t.__exit__()

    # Set None as a key in the dict, mapping to the dict itself
    set_item_result = empty_dict.__setitem__(none_key, empty_dict)

    # Call repr on the result of __setitem__ (which is None)
    repr_result = set_item_result.__repr__()

    # Attempt to call start() on the result of __setitem__ (None)
    set_item_result.start()

def test_timer_context_manager_with_active_timer_as_constructor_args():
    """Test that Timer can be used as a context manager and that its instance
    can be passed as arguments to other Timer constructors without raising errors."""

    # Use Timer as a context manager; timer_instance is the active Timer object
    base_timer = timer.Timer()
    active_timer = base_timer.__enter__()

    # Equality check against itself (expected to return True or NotImplemented)
    eq_result = base_timer.__eq__(base_timer)

    # Exit the context manager to stop the timer
    base_timer.__exit__()

    # Create a Timer using the active timer instance as initial_text and eq_result as logger
    timer_with_timer_as_initial_text = timer.Timer(initial_text=active_timer, logger=eq_result)

    # Create a Timer using active_timer as text, another Timer as initial_text, and eq_result as logger
    timer_with_complex_args = timer.Timer(active_timer, initial_text=timer_with_timer_as_initial_text, logger=eq_result)

    # Start the timer with complex arguments to verify no exception is raised
    timer_with_complex_args.start()

