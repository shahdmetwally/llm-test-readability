import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising an exception."""
    # Simply constructing TimerError should not raise any errors
    timer_error_instance = timer.TimerError()

def test_timer_raises_error_when_started_while_already_running():
    """Test that calling start() on an already-running timer raises a TimerError."""
    # Create a new timer instance
    t = timer.Timer()

    # Enter context manager, which starts the timer; same_timer is the same object as t
    same_timer = t.__enter__()

    # Exit context manager, which stops the timer
    _exit_result = t.__exit__()

    # Restart the timer explicitly via the reference returned by __enter__
    _start_result = same_timer.start()

    # Calling start() again while the timer is already running should raise TimerError
    with pytest.raises(timer.TimerError):
        t.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer supports the context manager protocol via __enter__ and __exit__."""
    # Instantiate a new Timer object
    timer_instance = timer.Timer()

    # Enter the context manager, which should start the timer
    entered_timer = timer_instance.__enter__()

    # Exit the context manager, which should stop the timer
    exit_result = timer_instance.__exit__()

def test_timer_exit_without_start():
    """Test that Timer, FloatArg, and TimerError can be instantiated, and __exit__ can be called on an unstarted Timer."""
    # Instantiate FloatArg (unused, but part of the original test setup)
    float_arg = timer.FloatArg()

    # Instantiate TimerError (unused, but part of the original test setup)
    timer_error = timer.TimerError()

    # Create a new Timer instance without starting it
    timer_instance = timer.Timer()

    # Call __exit__ directly on the unstarted timer
    timer_instance.__exit__()

def test_timer_start_returns_none_when_logger_is_none():
    """Test that Timer.start() returns None when logger is disabled."""
    # Create a timer with logging disabled (logger=None)
    no_logger = None
    silent_timer = timer.Timer(logger=no_logger)

    # Start the timer and capture the return value (expected to be None)
    start_result = silent_timer.start()

    # Verify that start() returns None when logger is disabled
    assert start_result is None

def test_timer_context_manager_with_varied_constructor_args():
    """Test Timer context manager and construction with timer, FloatArg, and eq-result as arguments."""
    # Start a base timer using the context manager protocol
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()

    # Create supporting values to pass as constructor arguments
    negative_int = -1092
    float_arg_text = timer.FloatArg()

    # Timer constructed with another timer instance as initial_text
    timer_with_timer_as_initial_text = timer.Timer(initial_text=context_timer)

    # FloatArg created (unused, mirrors original structure)
    float_arg_unused = timer.FloatArg()

    # Compare base_timer to a negative int; result used as initial_text below
    eq_result = base_timer.__eq__(negative_int)

    # Stop the context timer and capture elapsed time
    elapsed = context_timer.stop()

    # Timer constructed with FloatArg as text and the eq result as initial_text
    timer_with_float_text_and_eq_initial = timer.Timer(
        text=float_arg_text, initial_text=eq_result
    )

    # Retrieve string representations of timers
    base_timer_repr = base_timer.__repr__()
    timer_with_float_text_repr = timer_with_float_text_and_eq_initial.__repr__()

    # Start the timer that was constructed with float text and eq initial_text
    start_result = timer_with_float_text_and_eq_initial.start()

def test_timer_context_manager_with_repr_as_initial_text_and_start():
    """Test that Timer repr output can serve as initial_text, context manager entry/exit works, and a new timer can be started after these operations."""

    # Start a timer using the context manager protocol
    context_timer = timer.Timer()
    entered_timer = context_timer.__enter__()

    # Arbitrary negative integer used to test __eq__ against the timer
    negative_int = -1092

    # Capture the repr of the active (entered) timer to use as initial_text
    repr_text = entered_timer.__repr__()

    # Construct a FloatArg to be used as a text formatter
    float_arg_text = timer.FloatArg()

    # Create a timer using the repr string as its initial_text
    timer_with_repr_initial_text = timer.Timer(initial_text=repr_text)

    # Create another FloatArg (result unused but call is exercised)
    unused_float_arg = timer.FloatArg()

    # Test __eq__ between context_timer and a negative integer
    eq_result = context_timer.__eq__(negative_int)

    # Stop the entered timer and capture elapsed time
    elapsed_time = entered_timer.stop()

    # Create a timer with FloatArg as text and repr string as initial_text
    timer_with_float_text = timer.Timer(text=float_arg_text, initial_text=repr_text)

    # Capture repr of context_timer after it has been stopped
    context_timer_repr = context_timer.__repr__()

    # Capture repr of the new timer before it has been started
    timer_with_float_text_repr = timer_with_float_text.__repr__()

    # Start the new timer (exercising start() after all prior operations)
    timer_with_float_text.start()

def test_timer_with_no_logger_starts_and_exits_cleanly():
    """Test that a Timer with no logger starts and exits cleanly."""

    # Use None as the logger to disable any output during timing
    no_logger = None
    timer_instance = timer.Timer(logger=no_logger)

    # Start the timer; start() returns None
    start_result = timer_instance.start()

    # Verify start returns None when logger is None
    assert start_result is None

    # Stop the timer via the context manager exit protocol
    exit_result = timer_instance.__exit__()

    # Verify exit returns None
    assert exit_result is None

def test_timer_context_manager_result_used_as_nested_timer_args():
    """Test that context-manager entry and equality results can be passed as Timer constructor args, and the timer can be started."""
    # Create a base timer and enter its context manager protocol
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()  # Returns the timer itself when used as a context manager

    # Capture the result of equality comparison (used as a logger argument below)
    equality_result = base_timer.__eq__(base_timer)

    # Exit the context manager (no exception info supplied)
    exit_result = base_timer.__exit__()

    # Construct a new Timer passing the context-manager result as initial_text
    # and the equality result as the logger
    timer_with_context_as_initial_text = timer.Timer(
        initial_text=context_timer,
        logger=equality_result,
    )

    # Construct a further Timer using the context timer as the first positional arg,
    # the previous timer as initial_text, and the equality result as the logger
    timer_with_nested_args = timer.Timer(
        context_timer,
        initial_text=timer_with_context_as_initial_text,
        logger=equality_result,
    )

    # Start the nested timer to verify no error is raised
    timer_with_nested_args.start()

def test_timer_start_stop_copy_and_context_manager_entry():
    """Test that a Timer can be started, stopped, entered as a context manager, and copied."""
    # Use a named timer to identify it during logging
    timer_name = "Timer started"
    timer_instance = timer.Timer(timer_name)

    # Start and stop the timer to record elapsed time
    start_result = timer_instance.start()
    elapsed = timer_instance.stop()

    # Enter the timer as a context manager and verify it returns a Timer
    context_timer = timer_instance.__enter__()

    # Verify that the timer supports copying
    timer_instance.copy()