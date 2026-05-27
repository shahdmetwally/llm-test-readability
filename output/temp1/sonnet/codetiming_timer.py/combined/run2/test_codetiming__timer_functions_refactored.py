import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising an exception."""
    # Simply constructing TimerError should succeed without any errors
    timer_error_instance = timer.TimerError()

def test_timer_start_raises_error_when_already_running():
    """Test that calling start() on a timer already entered as a context manager raises a TimerError."""

    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the timer as a context manager, which calls start() internally
    context_timer = timer_instance.__enter__()

    # Exit the context manager explicitly, which calls stop() internally
    exit_result = timer_instance.__exit__()

    # Attempt to start the context timer again after the context has exited
    start_result = context_timer.start()

    # Attempt to start the outer timer instance again (already running scenario)
    timer_instance.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer supports the context manager protocol via __enter__ and __exit__."""
    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager, which starts the timer and returns itself
    entered_timer = timer_instance.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = timer_instance.__exit__()

def test_timer_exit_without_start_raises_timer_error():
    """Test that calling __exit__ on a Timer that was never started raises a TimerError."""
    # Instantiate a FloatArg as part of the original test setup
    float_arg = timer.FloatArg()

    # Instantiate a TimerError as part of the original test setup
    timer_error = timer.TimerError()

    # Create a Timer instance that has not been started
    timer_instance = timer.Timer()

    # Attempt to exit the timer without having started it
    timer_instance.__exit__()

def test_timer_setitem_returns_none_then_enter_raises_attribute_error():
    """Test that Timer.start() with logger=None succeeds, and __enter__ on None (from dict.__setitem__) raises AttributeError."""
    # Create a timer with no logger (silent mode)
    no_logger = None
    timer_instance = timer.Timer(logger=no_logger)

    # Start the timer; start() returns None
    start_result = timer_instance.start()

    # Build a self-referential dict: {None: dict_itself}
    self_referential_dict = {}
    none_key = None
    # dict.__setitem__ always returns None
    setitem_result = self_referential_dict.__setitem__(none_key, self_referential_dict)

    # Calling __enter__ on None (the return value of __setitem__) will raise AttributeError
    with pytest.raises(AttributeError):
        setitem_result.__enter__()

def test_timer_context_manager_with_various_configurations():
    """Tests Timer context-manager entry/exit, equality, repr, and construction with varied text/initial_text args."""

    # Create a base timer and enter its context manager
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()

    # Values used as arguments in subsequent Timer constructions and comparisons
    negative_int = -1092
    float_arg_for_text = timer.FloatArg()

    # Timer constructed with a running context_timer as its initial_text argument
    timer_with_context_as_initial_text = timer.Timer(initial_text=context_timer)

    # Second FloatArg instance (unused beyond construction)
    float_arg_unused = timer.FloatArg()

    # Compare base_timer against an integer (result used as initial_text below)
    eq_result = base_timer.__eq__(negative_int)

    # Stop the context_timer, capturing elapsed time
    elapsed_time = context_timer.stop()

    # Timer constructed with a FloatArg as text and the equality result as initial_text
    timer_with_float_text = timer.Timer(text=float_arg_for_text, initial_text=eq_result)

    # Retrieve string representations of both timers
    base_timer_repr = base_timer.__repr__()
    float_text_timer_repr = timer_with_float_text.__repr__()

    # Start the float-text timer
    start_result = timer_with_float_text.start()

def test_timer_context_manager_repr_as_initial_text():
    """Test that a timer's repr can serve as initial_text, and that context manager, stop, and equality checks behave correctly."""

    # Create a base timer and enter it as a context manager
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()

    # A negative integer used for equality comparison
    negative_int = -1092

    # Capture the repr of the running context timer to reuse as initial_text
    timer_repr_str = context_timer.__repr__()

    # Build a FloatArg to use as the text formatter for a new timer
    float_arg_text = timer.FloatArg()

    # Create a timer using the repr string as its initial_text
    timer_with_repr_initial_text = timer.Timer(initial_text=timer_repr_str)

    # Construct a second FloatArg (unused further in this test)
    float_arg_unused = timer.FloatArg()

    # Check equality of base_timer against the negative integer
    eq_result = base_timer.__eq__(negative_int)

    # Stop the context timer and capture elapsed time
    elapsed_time = context_timer.stop()

    # Create a timer with both a FloatArg text formatter and repr-based initial_text
    timer_with_float_arg_and_repr = timer.Timer(text=float_arg_text, initial_text=timer_repr_str)

    # Capture repr of the base timer after it has been stopped
    base_timer_repr = base_timer.__repr__()

    # Capture repr of the combined timer before starting it
    timer3_repr = timer_with_float_arg_and_repr.__repr__()

    # Start the combined timer
    timer_with_float_arg_and_repr.start()

def test_timer_no_logger_exit_and_none_setitem_raises_attribute_error():
    """Test that a Timer with no logger can start and exit, and that subsequent dict operations on its results behave as expected."""
    # Use None as the logger to disable all logging output
    no_logger = None
    timer_no_logger = timer.Timer(logger=no_logger)

    # Start the timer; Timer.start() returns None
    start_result = timer_no_logger.start()

    # Prepare an empty dict and a None key for subsequent operations
    empty_dict = {}
    none_key = None

    # Exit the timer via the context-manager protocol (equivalent to .stop())
    exit_result = timer_no_logger.__exit__()

    # Set a None key in the dict mapping it to the dict itself; __setitem__ returns None
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)

    # Call __repr__ on the None result of __setitem__
    repr_result = setitem_result.__repr__()

    # Call .start() on the None result — preserving original behaviour (raises AttributeError at runtime)
    setitem_result.start()

def test_timer_context_manager_result_used_as_constructor_args():
    """Test that Timer context manager results and equality output can be passed as constructor arguments to new Timer instances."""
    # Create a base timer and use it as a context manager
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()

    # Capture the result of equality comparison (used later as a logger argument)
    eq_result = base_timer.__eq__(base_timer)

    # Exit the context manager
    exit_result = base_timer.__exit__()

    # Construct a new Timer using the entered timer as initial_text and eq_result as logger
    timer_with_entered_as_initial = timer.Timer(initial_text=entered_timer, logger=eq_result)

    # Construct another Timer using the entered timer as text, previous timer as initial_text, and eq_result as logger
    timer_chained = timer.Timer(entered_timer, initial_text=timer_with_entered_as_initial, logger=eq_result)

    # Start the chained timer to verify no errors are raised
    timer_chained.start()

def test_timer_start_stop_then_enter_and_copy():
    """Test that a Timer can be started, stopped, re-entered as a context manager, and copied."""
    # Define the initial text label for the timer
    initial_text = "Timer started"

    # Create a timer instance with the given initial text
    timer_instance = timer.Timer(initial_text)

    # Start the timer; returns None
    start_result = timer_instance.start()

    # Stop the timer; returns elapsed time as a float
    elapsed = timer_instance.stop()

    # Re-enter the timer as a context manager
    context_timer = timer_instance.__enter__()

    # Verify the timer instance can be copied
    timer_instance.copy()