import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising any exceptions."""
    # Verify that TimerError is a valid, constructible exception class
    timer_error = timer.TimerError()

def test_timer_raises_error_when_started_while_already_running():
    """Test that starting an already-running timer raises a TimerError.

    Uses the context manager protocol to start the timer, then attempts
    to call .start() again on the inner timer reference, which should
    raise an error because the timer is already running.
    """
    # Create a new timer and enter the context manager (calls .start() internally)
    outer_timer = timer.Timer()
    inner_timer = outer_timer.__enter__()

    # Attempt to start the inner timer reference again while it is already running
    with pytest.raises(timer.TimerError):
        inner_timer.start()

    # Exit the context manager (calls .stop() internally)
    outer_timer.__exit__(None, None, None)

def test_timer_context_manager_enter_and_exit():
    """Test that Timer can be used as a context manager via __enter__ and __exit__."""
    # Create a new Timer instance
    t = timer.Timer()

    # Enter the context manager, which starts the timer and returns itself
    t_inner = t.__enter__()

    # Exit the context manager, which stops the timer
    none_type_0 = t.__exit__()

def test_timer_exit_without_start_raises_error():
    """Test that calling __exit__ on a Timer that was never started raises a TimerError."""
    t = timer.Timer()

    # Attempting to exit a timer context that was never started should raise an error
    with pytest.raises(timer.TimerError):
        t.__exit__(None, None, None)

def test_timer_start_with_no_logger_does_not_raise():
    """Test that starting a timer with logger=None succeeds without raising any errors."""
    # Create a timer with no logger so it won't print any output
    none_logger = None
    t = timer.Timer(logger=none_logger)

    # Start the timer (should not raise even without a logger)
    t.start()

def test_timer_context_manager_with_nested_timers_and_repr():
    """Test Timer context manager usage alongside nested Timer instances,
    equality comparison, stop, and repr calls in a realistic sequence."""

    # Start a timer using the context manager protocol
    base_timer = timer.Timer()
    active_timer = base_timer.__enter__()

    int_val = -1092
    float_arg_0 = timer.FloatArg()

    # Create a nested timer using the active context manager timer as initial_text
    nested_timer_with_initial = timer.Timer(initial_text=active_timer)

    float_arg_1 = timer.FloatArg()

    # Compare base_timer with an integer value
    eq_result = base_timer.__eq__(int_val)

    # Stop the active (context manager) timer and capture elapsed time
    elapsed = active_timer.stop()

    # Create another timer using float_arg as text and the equality result as initial_text
    nested_timer_with_text = timer.Timer(text=float_arg_0, initial_text=eq_result)

    # Get string representations of both timers
    base_timer_repr = base_timer.__repr__()
    nested_timer_repr = nested_timer_with_text.__repr__()

    # Start the nested timer with custom text/initial_text
    none_result = nested_timer_with_text.start()

def test_timer_context_manager_with_repr_as_initial_text():
    """
    Test that a Timer used as a context manager can be stopped,
    and that its __repr__ output can be reused as initial_text for new Timer instances.
    Also verifies that __eq__ and __repr__ behave correctly on active/stopped timers.
    """
    # Start a timer using the context manager protocol
    running_timer = timer.Timer()
    entered_timer = running_timer.__enter__()

    arbitrary_int = -1092

    # Capture the repr of the running timer to use as initial_text for other timers
    repr_of_running_timer = entered_timer.__repr__()

    float_arg_0 = timer.FloatArg()

    # Create a timer using the repr string as initial_text
    timer_with_repr_initial_text = timer.Timer(initial_text=repr_of_running_timer)

    float_arg_1 = timer.FloatArg()

    # Compare the original timer against an arbitrary integer
    eq_result = running_timer.__eq__(arbitrary_int)

    # Stop the entered (running) timer and capture elapsed time
    elapsed_time = entered_timer.stop()

    # Create another timer with a FloatArg text and repr-based initial_text
    timer_with_float_text = timer.Timer(text=float_arg_0, initial_text=repr_of_running_timer)

    # Capture repr of the original (now stopped) timer
    repr_of_stopped_timer = running_timer.__repr__()

    # Capture repr of the new timer before starting it
    repr_of_float_text_timer = timer_with_float_text.__repr__()

    # Start the new timer
    timer_with_float_text.start()

