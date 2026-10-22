import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising an exception."""
    # Simply constructing TimerError should not raise any exception
    timer_error = timer.TimerError()

def test_timer_start_raises_when_called_twice_after_context_manager():
    """Test the call sequence: context manager enter/exit followed by two manual start() calls."""
    # Create a new Timer instance
    t = timer.Timer()

    # Enter the context manager, which starts the timer and returns self
    ctx_timer = t.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = t.__exit__()

    # Start the timer again manually via the reference returned by __enter__ (same object as t)
    start_result = ctx_timer.start()

    # Attempt to start the already-running timer again; raises TimerError
    t.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer supports the context manager protocol via __enter__ and __exit__."""
    # Create a new Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager, which starts the timer
    entered_timer = timer_instance.__enter__()

    # Exit the context manager, which stops the timer
    exit_result = timer_instance.__exit__()

def test_timer_exit_raises_error_when_not_started():
    """Test that calling __exit__ on a Timer that was never started raises a TimerError."""
    # Instantiate supporting objects (part of the original test setup)
    float_arg = timer.FloatArg()
    timer_error = timer.TimerError()

    # Create a Timer instance without starting it
    timer_instance = timer.Timer()

    # Attempt to exit the timer context without having started it
    timer_instance.__exit__()

def test_timer_with_no_logger_start_and_dict_enter():
    """Test that Timer with logger=None starts without error and __enter__ is called on the result of dict.__setitem__."""
    # Create a Timer that suppresses all output by using no logger
    logger_none = None
    silent_timer = timer.Timer(logger=logger_none)

    # Start the silent timer (result is None, as start() returns nothing)
    start_result = silent_timer.start()

    # Construct a dict and insert a None-keyed entry pointing to itself
    container_dict = {}
    dict_key = None
    setitem_result = container_dict.__setitem__(dict_key, container_dict)

    # Call __enter__ on the result of __setitem__ (which is None) raises AttributeError
    with pytest.raises(AttributeError):
        setitem_result.__enter__()

def test_timer_context_manager_operations_and_repr():
    """Test Timer context manager, equality, stop, repr, and start across multiple Timer instances."""

    # Create a base timer and enter it as a context manager
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()

    # Values used for comparisons and Timer construction
    comparison_int = -1092
    float_arg_for_text = timer.FloatArg()

    # Create a timer using the active context_timer as its initial_text argument
    timer_with_initial_text = timer.Timer(initial_text=context_timer)

    # A second FloatArg instance (constructed but not further used)
    unused_float_arg = timer.FloatArg()

    # Compare the base timer against an integer
    eq_result = base_timer.__eq__(comparison_int)

    # Stop the context timer and capture elapsed time
    elapsed_time = context_timer.stop()

    # Create a timer with a FloatArg as text and the equality result as initial_text
    timer_with_text_and_initial = timer.Timer(text=float_arg_for_text, initial_text=eq_result)

    # Retrieve string representations of both timers
    base_timer_repr = base_timer.__repr__()
    timer_with_text_repr = timer_with_text_and_initial.__repr__()

    # Start the timer that has custom text and initial_text configured
    start_result = timer_with_text_and_initial.start()

def test_timer_context_manager_with_repr_as_initial_text():
    """Test that a Timer's __repr__ can serve as initial_text for new timers,
    and that context manager entry, __eq__, stop, and start all work together."""

    # Start a timer via context manager protocol
    context_timer = timer.Timer()
    entered_timer = context_timer.__enter__()

    arbitrary_int = -1092

    # Capture the repr of the running timer to use as initial_text elsewhere
    timer_repr = entered_timer.__repr__()

    # Create a FloatArg and a timer that uses the repr string as initial_text
    float_arg_for_text = timer.FloatArg()
    timer_with_repr_initial_text = timer.Timer(initial_text=timer_repr)

    # Create a second FloatArg (unused beyond construction)
    unused_float_arg = timer.FloatArg()

    # Compare the context timer against an arbitrary integer
    eq_result = context_timer.__eq__(arbitrary_int)

    # Stop the entered timer and record elapsed time
    elapsed_time = entered_timer.stop()

    # Create a timer that uses a FloatArg as text and the repr string as initial_text
    timer_with_float_arg_text = timer.Timer(text=float_arg_for_text, initial_text=timer_repr)

    # Capture repr values for both timers after the context timer has stopped
    context_timer_repr = context_timer.__repr__()
    float_arg_timer_repr = timer_with_float_arg_text.__repr__()

    # Start the newly created timer to verify it runs without error
    timer_with_float_arg_text.start()

def test_timer_with_no_logger_start_and_exit():
    """Test that a Timer with no logger can be started and exited via __exit__, alongside unrelated dict operations."""

    # Create a Timer instance with logging disabled
    no_logger = None
    timer_no_logger = timer.Timer(logger=no_logger)

    # Start the timer (returns None)
    start_result = timer_no_logger.start()

    # Prepare an empty dict and a None key for subsequent operations
    empty_dict = {}
    none_key = None

    # Stop the timer using the context-manager exit protocol
    exit_result = timer_no_logger.__exit__()

    # Set a None key in the dict pointing to the dict itself; __setitem__ returns None
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)

    # Call __repr__ on the setitem result (None)
    repr_result = setitem_result.__repr__()

def test_timer_context_manager_results_used_as_constructor_args():
    """Test that Timer context manager results and equality output can be passed as constructor arguments to new Timer instances."""
    # Create a base timer and use it as a context manager
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()

    # Capture the result of equality comparison (used later as logger arg)
    equality_result = base_timer.__eq__(base_timer)

    # Exit the context manager
    exit_result = base_timer.__exit__()

    # Construct a new Timer passing the entered timer as initial_text and equality result as logger
    timer_with_entered_as_initial_text = timer.Timer(
        initial_text=entered_timer,
        logger=equality_result,
    )

    # Construct another Timer passing entered timer as positional text arg and as initial_text
    timer_with_entered_as_text_and_initial = timer.Timer(
        entered_timer,
        initial_text=timer_with_entered_as_initial_text,
        logger=equality_result,
    )

    # Start the final timer to verify no error is raised during start
    timer_with_entered_as_text_and_initial.start()

def test_timer_start_stop_and_context_manager_entry():
    """Test that a Timer can be started, stopped, entered as a context manager, and copied."""

    # Use a simple text label as the timer's display format
    text_format = "Timer started"

    # Create a Timer instance with the given text format
    timer_instance = timer.Timer(text_format)

    # Start the timer; start() returns None
    start_result = timer_instance.start()

    # Stop the timer; stop() returns the elapsed time as a float
    elapsed_time = timer_instance.stop()

    # Explicitly invoke __enter__ to simulate context manager entry,
    # which returns the Timer instance itself
    context_timer = timer_instance.__enter__()

    # Copy the original timer instance
    timer_instance.copy()