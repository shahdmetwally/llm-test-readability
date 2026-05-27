import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising an exception."""
    # Instantiate TimerError to confirm it is a valid, constructible exception class
    timer_error_instance = timer.TimerError()

def test_timer_raises_on_double_start_after_context_manager_cycle():
    """Test that starting an already-running timer raises TimerError after a context manager cycle."""
    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager, which starts the timer and returns self
    timer_from_enter = timer_instance.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = timer_instance.__exit__()

    # Start the timer again via the reference returned by __enter__ (same object)
    start_result = timer_from_enter.start()

    # Attempt to start the already-running timer again — raises TimerError
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
    # Construct supporting objects as part of the test setup
    float_arg = timer.FloatArg()
    timer_error = timer.TimerError()

    # Create a Timer instance without starting it
    timer_instance = timer.Timer()

    # Attempt to exit the timer context without a prior start
    timer_instance.__exit__()

def test_timer_with_no_logger_start_does_not_raise():
    """Test that a Timer with logger=None starts without error and that the result of a dict setitem can be entered as a context manager."""
    # Use None as the logger to suppress all output
    no_logger = None
    silent_timer = timer.Timer(logger=no_logger)

    # Start the silent timer; should not raise any errors
    start_result = silent_timer.start()

    # Construct a dict and insert a None key mapping to the dict itself
    context_dict = {}
    none_key = None
    setitem_result = context_dict.__setitem__(none_key, context_dict)

    # Attempt to enter the result of __setitem__ as a context manager (preserved from original)
    setitem_result.__enter__()

def test_timer_context_manager_with_varied_constructor_args():
    """Test Timer as context manager alongside Timers built with varied argument types including another Timer, FloatArg, and an equality result."""

    # Start a base timer using the context manager protocol
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()

    # Values used as constructor arguments for subsequent timers
    negative_int = -1092
    float_arg_text = timer.FloatArg()

    # Create a timer using the running context_timer as its initial_text argument
    timer_with_context_initial_text = timer.Timer(initial_text=context_timer)

    # FloatArg instance created (preserved from original test structure)
    float_arg_unused = timer.FloatArg()

    # Compare base_timer against an integer; result used as initial_text below
    eq_result = base_timer.__eq__(negative_int)

    # Stop the context timer and capture elapsed time
    elapsed = context_timer.stop()

    # Create a timer with a FloatArg as text and the equality result as initial_text
    timer_with_float_text = timer.Timer(text=float_arg_text, initial_text=eq_result)

    # Retrieve string representations of both timers
    base_timer_repr = base_timer.__repr__()
    float_text_timer_repr = timer_with_float_text.__repr__()

    # Start the timer that was constructed with float text and eq_result initial_text
    start_result = timer_with_float_text.start()

def test_timer_context_manager_repr_as_initial_text_and_start():
    """Test Timer as context manager, using repr output as initial_text, and starting a new timer with FloatArg text."""

    # Start a timer using the context manager protocol
    base_timer = timer.Timer()
    ctx_timer = base_timer.__enter__()

    # A negative integer used for equality comparison
    negative_int = -1092

    # Capture the repr of the active context-manager timer
    timer_repr = ctx_timer.__repr__()

    # Create a FloatArg to be used as the text parameter
    float_arg_text = timer.FloatArg()

    # Create a timer using the repr string as its initial_text
    timer_with_repr_initial_text = timer.Timer(initial_text=timer_repr)

    # Create a second FloatArg (constructed but not further used)
    float_arg_unused = timer.FloatArg()

    # Compare the base timer against a negative integer
    eq_result = base_timer.__eq__(negative_int)

    # Stop the context-manager timer and capture elapsed time
    elapsed = ctx_timer.stop()

    # Create a timer with FloatArg as text and repr string as initial_text
    timer_with_float_arg_and_initial_text = timer.Timer(text=float_arg_text, initial_text=timer_repr)

    # Capture repr of the base timer (now stopped)
    base_timer_repr = base_timer.__repr__()

    # Capture repr of the new combined timer
    timer3_repr = timer_with_float_arg_and_initial_text.__repr__()

    # Start the combined timer
    timer_with_float_arg_and_initial_text.start()

