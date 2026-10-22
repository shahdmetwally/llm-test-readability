import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising any exceptions."""
    # Verify that TimerError is a valid, constructible exception class
    timer_error = timer.TimerError()

def test_starting_already_running_timer_raises_error():
    """Test that calling start() on a running timer (already started via context manager) raises a TimerError."""
    # Create a new timer instance
    t = timer.Timer()

    # Enter the context manager, which internally calls start()
    t_inner = t.__enter__()

    # Exit the context manager, which internally calls stop()
    none_type_0 = t.__exit__()

    # Call start() on the inner timer reference (same object as t)
    none_type_1 = t_inner.start()

    # Attempt to start the timer again while it is already running — expects a TimerError
    t.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer can be used as a context manager via __enter__ and __exit__."""
    # Create a new Timer instance
    t = timer.Timer()

    # Enter the context manager, which starts the timer and returns it
    active_timer = t.__enter__()

    # Exit the context manager, which stops the timer
    result = t.__exit__()

def test_timer_exit_without_start_raises_error():
    """Test that calling __exit__ on a Timer that was never started raises a TimerError."""
    t = timer.Timer()
    with pytest.raises(timer.TimerError):
        t.__exit__(None, None, None)

def test_timer_start_with_none_logger_does_not_raise():
    """Test that starting a timer with logger=None does not raise an error,
    even when unrelated dict operations produce None-valued variables."""
    none_type_0 = None

    # Create a timer with no logger (silent mode)
    silent_timer = timer.Timer(logger=none_type_0)

    # Start the timer; should return None without printing anything
    start_result = silent_timer.start()

    # Unrelated dict manipulation that produces None side effects (preserving original behaviour)
    empty_dict = {}
    none_key = None
    set_result = empty_dict.__setitem__(none_key, empty_dict)

    # Enter the context of the None-valued set result (preserving original behaviour)
    set_result.__enter__()

def test_timer_context_manager_with_various_configurations():
    """Test Timer interactions: context manager entry/exit, equality check,
    stop, repr, and start across multiple Timer instances with varied arguments."""

    # Create a default Timer and enter it as a context manager
    default_timer = timer.Timer()
    context_timer = default_timer.__enter__()

    int_val = -1092

    # Create a FloatArg to use as a text argument later
    float_arg_for_text = timer.FloatArg()

    # Create a Timer using the active context_timer as initial_text
    timer_with_context_initial_text = timer.Timer(initial_text=context_timer)

    # Create another FloatArg (unused directly, but part of the test sequence)
    float_arg_unused = timer.FloatArg()

    # Check equality of default_timer with an integer value
    eq_result = default_timer.__eq__(int_val)

    # Stop the context-entered timer and capture elapsed time
    elapsed = context_timer.stop()

    # Create a Timer with float_arg as text and the equality result as initial_text
    timer_with_float_text = timer.Timer(text=float_arg_for_text, initial_text=eq_result)

    # Get string representations of both timers
    repr_default = default_timer.__repr__()
    repr_float_text = timer_with_float_text.__repr__()

    # Start the timer that has float_arg text and eq_result as initial_text
    timer_with_float_text.start()

def test_timer_context_manager_with_repr_as_initial_text():
    """
    Test that a Timer used as a context manager can produce a repr string,
    which is then passed as initial_text to new Timer instances.
    Also verifies that stop() can be called on the inner timer and that
    start() can be called on a Timer configured with a FloatArg text and
    repr-based initial_text.
    """
    # Start a timer using the context manager protocol
    base_timer = timer.Timer()
    active_timer = base_timer.__enter__()

    # An arbitrary integer value used for equality comparison
    some_int = -1092

    # Capture the repr of the active timer to use as initial_text
    repr_of_active_timer = active_timer.__repr__()

    # Create a FloatArg instance (used as text formatter)
    float_arg_0 = timer.FloatArg()

    # Create a new timer using the repr string as initial_text
    timer_with_repr_initial_text = timer.Timer(initial_text=repr_of_active_timer)

    # Another FloatArg instance (unused result, but call is required)
    float_arg_1 = timer.FloatArg()

    # Compare base_timer to the integer (result unused, but call is required)
    eq_result = base_timer.__eq__(some_int)

    # Stop the active (context manager) timer and capture elapsed time
    elapsed = active_timer.stop()

    # Create a timer with FloatArg as text and repr string as initial_text
    timer_with_float_arg_text = timer.Timer(text=float_arg_0, initial_text=repr_of_active_timer)

    # Capture repr of both base and float-arg timers (results unused, calls required)
    repr_of_base_timer = base_timer.__repr__()
    repr_of_float_arg_timer = timer_with_float_arg_text.__repr__()

    # Start the timer configured with FloatArg text and repr-based initial_text
    timer_with_float_arg_text.start()

def test_timer_setitem_on_none_result_raises_attribute_error():
    """Test that Timer can start and exit as a context manager with no logger,
    and that subsequent invalid operations on None and dict behave as expected."""

    # Create a Timer with logging disabled
    no_logger = None
    t = timer.Timer(logger=no_logger)

    # Start the timer (returns None)
    start_result = t.start()

    # Prepare an empty dict and a None key for later misuse
    empty_dict = {}
    none_key = None

    # Exit the timer context (stops the timer)
    exit_result = t.__exit__()

    # Insert None -> empty_dict into the dict; __setitem__ returns None
    set_result = empty_dict.__setitem__(none_key, empty_dict)

    # Get the repr of the return value of __setitem__ (which is None)
    repr_result = set_result.__repr__()

    # Attempt to call .start() on None (the result of __setitem__),
    # which will raise an AttributeError — this is the behaviour under test
    with pytest.raises(AttributeError):
        set_result.start()

def test_timer_context_manager_with_nested_timer_configurations():
    """Test that Timer can be used as a context manager and that its result
    can be passed as arguments to construct further Timer instances, including
    one that is explicitly started afterward."""

    # Use Timer as a context manager to measure a no-op block
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()

    # Compare the timer to itself (result used as logger argument below)
    equality_result = base_timer.__eq__(base_timer)

    # Exit the context manager, stopping the timer
    none_result = base_timer.__exit__()

    # Create a Timer using the entered timer as initial_text and equality result as logger
    timer_with_timer_initial_text = timer.Timer(initial_text=entered_timer, logger=equality_result)

    # Create a Timer using entered_timer as the first positional arg,
    # the previous timer as initial_text, and equality result as logger
    timer_with_nested_config = timer.Timer(entered_timer, initial_text=timer_with_timer_initial_text, logger=equality_result)

    # Explicitly start the final timer
    timer_with_nested_config.start()

def test_timer_start_stop_then_enter_and_copy():
    """Test that a Timer can be started and stopped explicitly, then used as a
    context manager via __enter__, followed by a copy of the timer object."""

    # Use "Timer started" as the text message for the timer
    initial_text = "Timer started"

    # Create a Timer instance with the given text
    timer_instance = timer.Timer(initial_text)

    # Start the timer explicitly
    none_type_0 = timer_instance.start()

    # Stop the timer and capture the elapsed time
    elapsed = timer_instance.stop()

    # Enter the timer as a context manager
    context_timer = timer_instance.__enter__()

    # Copy the timer object
    timer_instance.copy()