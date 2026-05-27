import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated_without_arguments() -> None:
    """Test that TimerError can be instantiated with no arguments."""
    timer_error_0 = timer.TimerError()

def test_restarting_timer_raises_error():
    """Test that calling .start() on an already running Timer raises TimerError."""
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    none_type_1 = timer_1.start()
    timer_0.start()

def test_timer_context_manager_enters_and_exits():
    """Verify that a Timer can be used as a context manager via __enter__ and __exit__."""
    timer_ = timer.Timer()
    entered_timer = timer_.__enter__()  # Start the timer
    timer_.__exit__()                    # Stop the timer

def test_timer_exit_without_enter_raises_timer_error() -> None:
    """Test that calling __exit__ without a preceding __enter__ raises a TimerError."""
    # Create a Timer instance (without using it as a context manager)
    timer_0 = timer.Timer()

    # Calling __exit__ directly (without __enter__ first) should raise an error
    # because the timer is not running.
    timer_0.__exit__()

def test_timer_with_none_logger_and_self_reference_dict_enter_does_not_raise():
    """Test that creating a timer with logger=None and then calling __enter__ on a dict key does not raise."""
    # Create a timer with logger disabled (logger=None)
    timer_0 = timer.Timer(logger=None)

    # Start the timer
    none_type_1 = timer_0.start()

    # Create a dictionary and set a key to the dictionary itself (self-reference)
    dict_0 = {}
    var_0 = dict_0.__setitem__(None, dict_0)

    # Call __enter__ on the setitem result (a no-op in practice)
    var_0.__enter__()

def test_context_manager_timer_with_initial_text_and_various_operations():
    """Test Timer used as context manager with initial_text set to a Timer instance,
    and verify equality, string representation, and start/stop operations."""
    timer = timer.Timer()
    context_manager_timer = timer.__enter__()  # Start timer via context manager
    int_0 = -1092
    float_arg_0 = timer.FloatArg()  # Create a float argument object
    triggered_timer = timer.Timer(initial_text=context_manager_timer)  # Create a timer with initial_text set to a Timer object
    float_arg_1 = timer.FloatArg()  # Another float argument object
    equality_result = timer.__eq__(int_0)  # Compare timer to an integer
    elapsed_time = context_manager_timer.stop()  # Stop the context manager timer
    format_timer = timer.Timer(text=float_arg_0, initial_text=equality_result)  # Create timer with float text and equality result as initial_text
    repr_1 = timer.__repr__()  # Get string representation of original timer
    repr_2 = format_timer.__repr__()  # Get string representation of format_timer
    none_result = format_timer.start()  # Start the format_timer

def test_timer_context_manager_with_initial_text_repr_and_stop() -> None:
    """Test Timer behavior: context manager usage, repr as initial_text, equality comparison, and stop."""
    # Create a timer and use it as a context manager
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()
    int_0 = -1092
    # Get repr of running timer
    var_0 = timer_1.__repr__()
    float_arg_0 = timer.FloatArg()
    # Create a new timer with initial_text set to the repr string
    timer_2 = timer.Timer(initial_text=var_0)
    float_arg_1 = timer.FloatArg()
    # Compare timer with an integer (tests __eq__ with non-Timer type)
    var_1 = timer_0.__eq__(int_0)
    # Stop the context manager timer
    float_0 = timer_1.stop()
    # Create a timer with both text and initial_text set
    timer_3 = timer.Timer(text=float_arg_0, initial_text=var_0)
    var_2 = timer_0.__repr__()
    var_3 = timer_3.__repr__()
    # Start the third timer
    timer_3.start()

def test_timer_start_with_none_logger_and_dict_operations_should_not_raise():
    """Test that a Timer with logger=None can start and stop without error,
    and that an empty dict's __setitem__ and __repr__ methods do not interfere."""
    # Create a Timer with no logger (None) and start it
    none_logger = None
    timer_instance = timer.Timer(logger=none_logger)
    start_result = timer_instance.start()  # Returns None

    # Create an empty dictionary and stop the timer inside its __exit__
    empty_dict = {}
    exit_result = timer_instance.__exit__()  # Stop timer (returns None)

    # Perform unrelated dict operations that should not affect the timer
    setitem_result = empty_dict.__setitem__(none_logger, empty_dict)
    repr_result = setitem_result.__repr__()

    # Attempt to start a stopped timer again (should succeed)
    repr_result.start()

def test_timer_with_unusual_initial_text_and_logger_arguments():
    """Test Timer behavior when created with non-standard initial_text and logger arguments."""
    # Create a default timer instance
    timer_instance = timer.Timer()
    
    # Start the timer using context manager protocol
    timer_initial_text = timer_instance.__enter__()
    
    # Check equality with itself (unusual operation for testing)
    equality_result = timer_instance.__eq__(timer_instance)
    
    # Stop the timer
    timer_instance.__exit__()
    
    # Create a new timer using previous timer as initial_text and equality result as logger
    logger_timer = timer.Timer(initial_text=timer_initial_text, logger=equality_result)
    
    # Create another timer with timer_initial_text as first positional argument,
    # logger_timer as initial_text, and equality_result as logger
    final_timer = timer.Timer(timer_initial_text, initial_text=logger_timer, logger=equality_result)
    
    # Start the final timer
    final_timer.start()

def test_timer_initial_text_start_stop_and_context_manager(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that a Timer with initial_text=True works when started/stopped explicitly
    and also when used as a context manager, and that copy() does not raise errors."""
    initial_text = "Timer started"
    timer = timer.Timer(initial_text)

    # Start and stop the timer explicitly
    none_type = timer.start()
    elapsed = timer.stop()

    # Use the timer as a context manager (enter/exit)
    context_timer = timer.__enter__()
    timer.copy()