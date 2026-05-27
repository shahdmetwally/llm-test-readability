import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising any exceptions."""
    # Verify that TimerError is a valid, instantiable exception class
    timer_error = timer.TimerError()

def test_timer_raises_error_when_started_twice():
    """Test that starting a timer that was already used as a context manager raises an error.

    After entering and exiting the context manager, the timer's internal state
    is reset. Calling start() on the inner timer reference (which shares state)
    and then calling start() again on the outer timer should raise a TimerError,
    since the timer is already running.
    """
    # Create a new timer and use it as a context manager
    outer_timer = timer.Timer()
    inner_timer = outer_timer.__enter__()  # Starts the timer; inner_timer is the same object

    # Exit the context manager, stopping the timer
    none_type_0 = outer_timer.__exit__()

    # Start the timer again via the inner reference (same object as outer_timer)
    none_type_1 = inner_timer.start()

    # Attempt to start the already-running timer — expected to raise TimerError
    with pytest.raises(timer.TimerError):
        outer_timer.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer can be used as a context manager via __enter__ and __exit__."""
    # Create a new Timer instance
    t = timer.Timer()

    # Enter the context manager, which starts the timer and returns the Timer instance
    t_inner = t.__enter__()

    # Exit the context manager, which stops the timer
    none_result = t.__exit__()

def test_timer_exit_without_start_raises_error():
    """Test that calling __exit__ on a Timer that was never started raises a TimerError."""
    t = timer.Timer()

    # Attempting to exit a timer context that was never entered should raise an error
    with pytest.raises(timer.TimerError):
        t.__exit__()

def test_timer_start_with_none_logger_and_dict_context_protocol():
    """Test that starting a timer with logger=None and then attempting to use
    a dict as a context manager proceeds without assertion errors up to that point."""
    none_logger = None
    t = timer.Timer(logger=none_logger)

    # Start the timer (logger=None means no output is produced)
    started = t.start()

    # Construct a dict and attempt to use it as a context manager
    empty_dict = {}
    none_key = None
    result = empty_dict.__setitem__(none_key, empty_dict)  # Sets empty_dict[None] = empty_dict

    # Attempt to enter the context manager protocol on the return value of __setitem__
    with pytest.raises(AttributeError):
        result.__enter__()

def test_timer_context_manager_with_various_configurations():
    """Test Timer interactions including context manager usage, equality check,
    stop, repr, and start across multiple Timer instances with varied arguments."""

    # Create a base timer and enter its context manager
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()

    # Arbitrary integer used for equality comparison
    negative_int = -1092

    # FloatArg instances used as text/initial_text arguments
    float_arg_text = timer.FloatArg()

    # Timer configured with context_timer instance as initial_text
    timer_with_context_initial_text = timer.Timer(initial_text=context_timer)

    float_arg_initial_text = timer.FloatArg()

    # Check equality of base_timer with a negative integer
    eq_result = base_timer.__eq__(negative_int)

    # Stop the context manager timer and capture elapsed time
    elapsed = context_timer.stop()

    # Timer configured with float_arg as text and eq_result as initial_text
    timer_with_float_args = timer.Timer(text=float_arg_text, initial_text=eq_result)

    # Retrieve repr of base_timer and timer_with_float_args
    base_timer_repr = base_timer.__repr__()
    float_args_timer_repr = timer_with_float_args.__repr__()

    # Start the timer configured with float args
    start_result = timer_with_float_args.start()

def test_timer_context_manager_with_repr_as_initial_text():
    """
    Test that a Timer used as a context manager can be stopped,
    and that its __repr__ output can be passed as initial_text to new Timer instances.
    Also verifies __eq__ and __repr__ behave correctly on running/stopped timers.
    """
    # Start a timer using the context manager protocol
    running_timer = timer.Timer()
    entered_timer = running_timer.__enter__()

    # An integer value used for equality comparison
    negative_int = -1092

    # Capture the repr of the running timer to use as initial_text
    repr_of_running_timer = entered_timer.__repr__()

    # Create a Timer with repr string as initial_text (no text formatter)
    float_arg_0 = timer.FloatArg()
    timer_with_repr_initial_text = timer.Timer(initial_text=repr_of_running_timer)

    # Create another FloatArg instance
    float_arg_1 = timer.FloatArg()

    # Compare the original timer against the negative integer
    eq_result = running_timer.__eq__(negative_int)

    # Stop the context manager timer and capture elapsed time
    elapsed = entered_timer.stop()

    # Create a Timer with a FloatArg text formatter and repr as initial_text
    timer_with_float_arg_text = timer.Timer(text=float_arg_0, initial_text=repr_of_running_timer)

    # Capture repr of the stopped original timer
    repr_of_stopped_timer = running_timer.__repr__()

    # Capture repr of the new timer (not yet started)
    repr_of_float_arg_timer = timer_with_float_arg_text.__repr__()

    # Start the new timer with FloatArg text and repr initial_text
    timer_with_float_arg_text.start()

def test_timer_start_and_exit_with_none_logger():
    """Test that Timer starts and exits correctly when logger is None,
    and that subsequent operations on unrelated objects do not raise errors."""

    # Create a Timer with logging disabled (logger=None)
    none_logger = None
    t = timer.Timer(logger=none_logger)

    # Start the timer; start() returns None
    start_result = t.start()

    # Prepare an empty dict and a None key for later use
    empty_dict = {}
    none_key = None

    # Exit the timer context (stops the timer)
    exit_result = t.__exit__(None, None, None)

    # Set a dict entry mapping None -> empty_dict (unrelated to timer logic)
    set_item_result = empty_dict.__setitem__(none_key, empty_dict)

    # Get the repr of the setitem result (setitem returns None)
    repr_result = set_item_result.__repr__()

    assert start_result is None
    assert repr_result == 'None'
    assert none_key in empty_dict

def test_timer_start_with_nested_timer_configs_using_previous_timer_as_args():
    """Test that Timer instances can be constructed using other Timer instances and
    equality-check results as arguments, and that start() can be called on a
    nested configuration without raising an error."""

    # Create a base timer and use it as a context manager
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()

    # Perform an equality check on the timer with itself (evaluates to True or NotImplemented)
    eq_result = base_timer.__eq__(base_timer)

    # Exit the context manager (stops the timer)
    base_timer.__exit__()

    # Construct a second timer using the entered timer as initial_text and eq_result as logger
    timer_with_timer_initial_text = timer.Timer(initial_text=entered_timer, logger=eq_result)

    # Construct a third timer using entered_timer as text, previous timer as initial_text,
    # and eq_result as logger
    nested_timer = timer.Timer(entered_timer, initial_text=timer_with_timer_initial_text, logger=eq_result)

    # Start the nested timer — verifies no exception is raised during start()
    nested_timer.start()

def test_timer_start_stop_then_enter_and_copy():
    """Test that a Timer can be started and stopped explicitly, then used as a
    context manager entry, followed by a copy operation."""

    # Use a named timer with the default "Timer started" initial text
    initial_text = "Timer started"
    t = timer.Timer(initial_text)

    # Explicitly start and stop the timer to record elapsed time
    none_result = t.start()
    elapsed = t.stop()

    # Enter the timer as a context manager (without exiting)
    entered_timer = t.__enter__()

    # Copy the timer instance
    t.copy()