import pytest
import codetiming_timer as timer

def test_timer_error_instantiation():
    """Test that TimerError can be instantiated without arguments."""
    timer_error_0 = timer.TimerError()

def test_restarting_an_active_timer_raises_error():
    """Test that calling start() on an already running timer raises a TimerError."""
    # Create a Timer instance and start it using the context manager
    timer = timer.Timer()
    timer.__enter__()
    
    # Attempt to start the timer again while it's still running
    # This should raise a TimerError, but since the exception isn't caught
    # in this test, it tests that __exit__ was called first.
    timer.__exit__()
    timer.start()
    timer.start()

def test_timer_context_manager_enters_and_exits():
    """Test that a Timer can be used as a context manager with __enter__ and __exit__."""
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()

def test_exit_without_starting_timer_should_not_raise():
    """Test that calling __exit__ on a Timer that was never started does not raise an error."""
    float_arg_0 = timer.FloatArg()
    timer_error_0 = timer.TimerError()
    timer_0 = timer.Timer()
    timer_0.__exit__()

def test_timer_with_logger_none_and_context_manager_on_setitem_result():
    """Test that starting a Timer with logger=None and then calling __enter__ on a variable works."""
    # Arrange: Create a Timer with no logger
    timer_0 = timer.Timer(logger=None)
    
    # Act: Start the timer (returns None)
    none_type_1 = timer_0.start()
    
    # Create an empty dict and set a key-value pair (key=None, value=the dict itself)
    dict_0 = {}
    none_type_2 = None
    var_0 = dict_0.__setitem__(none_type_2, dict_0)
    
    # Call __enter__ on the result of __setitem__ (which returns None)
    var_0.__enter__()

def test_timer_context_manager_with_initial_text_and_various_operations():
    """Test using a Timer as a context manager, then creating another Timer
    with the context manager's return value as initial_text, performing
    equality comparison, stop, and repr operations."""
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()  # Start the timer via context manager
    int_0 = -1092
    float_arg_0 = timer.FloatArg()
    timer_2 = timer.Timer(initial_text=timer_1)
    float_arg_1 = timer.FloatArg()
    var_0 = timer_0.__eq__(int_0)  # Compare timer with integer
    float_0 = timer_1.stop()  # Stop the context-managed timer
    timer_3 = timer.Timer(text=float_arg_0, initial_text=var_0)
    var_1 = timer_0.__repr__()
    var_2 = timer_3.__repr__()
    none_type_0 = timer_3.start()

def test_timer_context_manager_with_repr_and_eq_and_mixed_timers():
    """Test Timer context manager usage combined with __repr__ as initial_text and __eq__ comparison."""
    # Create a Timer and use it as a context manager
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()

    # Create a negative integer for equality comparison
    int_0 = -1092

    # Get the string representation of the context manager timer
    var_0 = timer_1.__repr__()

    # Create a FloatArg instance for use as the text parameter
    float_arg_0 = timer.FloatArg()

    # Create a new Timer with the repr string as initial_text
    timer_2 = timer.Timer(initial_text=var_0)

    # Create another FloatArg instance
    float_arg_1 = timer.FloatArg()

    # Compare the first timer with the negative integer
    var_1 = timer_0.__eq__(int_0)

    # Stop the context manager timer and get elapsed time
    float_0 = timer_1.stop()

    # Create a Timer with both text and initial_text parameters
    timer_3 = timer.Timer(text=float_arg_0, initial_text=var_0)

    # Get string representations of the timers
    var_2 = timer_0.__repr__()
    var_3 = timer_3.__repr__()

    # Start the Timer with custom text and initial_text
    timer_3.start()

def test_timer_exit_without_stop_and_setitem_on_none():
    """Test that calling start() with logger=None, then __exit__() (without stop) works."""
    none_logger = None
    timer_0 = timer.Timer(logger=none_logger)
    none_return = timer_0.start()  # start() returns None
    dict_0 = {}
    none_type_2 = None
    none_type_3 = timer_0.__exit__()  # __exit__() returns None
    var_0 = dict_0.__setitem__(none_type_2, dict_0)  # dict.__setitem__() returns None
    var_1 = var_0.__repr__()  # repr(None) returns "None"
    var_0.start()  # This will fail if not on a Timer-like object

def test_explicit_timer_with_initial_text_set_to_timer_and_logger_from_eq_result() -> None:
    """Test that creating a Timer with initial_text set to a Timer object and logger set to the result of __eq__ still starts correctly."""
    # Create a base timer and use it as a context manager
    base_timer = timer.Timer()
    base_timer.__enter__()
    
    # Use equality comparison result as logger, and the first timer as initial_text
    logger_value = base_timer.__eq__(base_timer)
    base_timer.__exit__()
    
    # Create a new timer with unusual parameter types (Timer object as initial_text, bool as logger)
    initial_text_timer = timer.Timer(initial_text=base_timer, logger=logger_value)
    another_timer = timer.Timer(base_timer, initial_text=initial_text_timer, logger=logger_value)
    another_timer.start()

def test_timer_with_initial_text_and_explicit_start_stop_and_context_manager() -> None:
    """Test that a Timer with initial_text=True works for start/stop and as a context manager."""
    # Set up a timer with the default initial text
    initial_text = "Timer started"
    timer_0 = timer.Timer(initial_text)
    
    # Start the timer explicitly
    none_type_0 = timer_0.start()
    # Stop the timer
    float_0 = timer_0.stop()
    
    # Enter the timer as a context manager
    timer_1 = timer_0.__enter__()
    
    # Create a copy of the timer
    timer_0.copy()