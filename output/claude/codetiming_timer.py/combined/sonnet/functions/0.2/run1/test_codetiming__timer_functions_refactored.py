import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising an exception."""
    # Instantiate TimerError to confirm it is a valid, constructible exception class
    timer_error = timer.TimerError()

def test_timer_context_manager_then_manual_start_sequence():
    """Test Timer used as context manager followed by manual start calls on the same instance."""
    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager, which starts the timer and returns self
    timer_from_enter = timer_instance.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = timer_instance.__exit__()

    # Manually start the timer via the reference returned by __enter__ (same object)
    start_result = timer_from_enter.start()

    # Start the original timer reference again (already running at this point)
    timer_instance.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer supports the context manager protocol via __enter__ and __exit__."""
    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager, which starts the timer and returns itself
    entered_timer = timer_instance.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = timer_instance.__exit__()

def test_exit_on_unstarted_timer_raises_timer_error():
    """Test that calling __exit__() on a Timer that was never started raises TimerError."""
    # These instances are constructed as part of the original test setup (unused directly)
    unused_float_arg = timer.FloatArg()
    unused_timer_error = timer.TimerError()

    # Create a timer without starting it
    unstarted_timer = timer.Timer()

    # Calling __exit__() on an unstarted timer triggers stop(), which raises TimerError
    unstarted_timer.__exit__()

def test_timer_with_no_logger_start_returns_none_and_setitem_result_has_no_enter():
    """Test Timer started with logger=None, then __enter__ called on None (result of __setitem__)."""
    # Create a Timer that suppresses all output by passing logger=None
    no_logger = None
    timer_instance = timer.Timer(logger=no_logger)

    # Start the timer; .start() returns None
    start_result = timer_instance.start()

    # Build a dict and set a None key pointing to itself
    container = {}
    none_key = None
    setitem_result = container.__setitem__(none_key, container)  # returns None

    # Attempt to use the None return value of __setitem__ as a context manager
    with pytest.raises(AttributeError):
        setitem_result.__enter__()

def test_timer_context_manager_with_varied_constructor_args():
    """Test Timer as context manager and composition of __eq__, stop, and __repr__ with varied constructor args."""

    # Use Timer as a context manager and capture the entered instance
    context_timer = timer.Timer()
    entered_timer = context_timer.__enter__()

    # Values used as constructor arguments
    negative_int = -1092
    float_arg_for_text = timer.FloatArg()

    # Construct a Timer using the entered timer instance as initial_text
    timer_initial_text_from_entered = timer.Timer(initial_text=entered_timer)

    # Construct a second FloatArg (unused beyond construction)
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

    # Start the timer constructed with float_arg text
    start_result = timer_with_float_arg_text.start()

def test_timer_context_manager_with_repr_as_initial_text():
    """Test Timer as context manager, using its repr as initial_text, and verifying start/stop behaviour."""

    # Start a timer using the context manager protocol
    base_timer = timer.Timer()
    ctx_timer = base_timer.__enter__()

    # A negative integer used for equality comparison
    negative_int = -1092

    # Capture the repr of the running context-managed timer
    repr_of_ctx_timer = ctx_timer.__repr__()

    # Create a FloatArg to use as a text formatter
    float_arg_text = timer.FloatArg()

    # Create a timer using the repr string as its initial_text
    timer_with_repr_initial_text = timer.Timer(initial_text=repr_of_ctx_timer)

    # Create a second FloatArg (constructed but not further used)
    float_arg_unused = timer.FloatArg()

    # Compare the base timer against a negative integer
    eq_result = base_timer.__eq__(negative_int)

    # Stop the context-managed timer and capture elapsed time
    elapsed_time = ctx_timer.stop()

    # Create a timer combining a FloatArg text formatter with the repr as initial_text
    timer_with_float_arg_and_initial_text = timer.Timer(
        text=float_arg_text, initial_text=repr_of_ctx_timer
    )

    # Capture repr of the base timer (now stopped) and the new combined timer
    repr_of_base_timer = base_timer.__repr__()
    repr_of_timer_with_float_arg = timer_with_float_arg_and_initial_text.__repr__()

    # Start the combined timer to verify it starts without error
    timer_with_float_arg_and_initial_text.start()

