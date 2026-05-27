import pytest
import codetiming_timer as timer

def test_timer_error_instantiation_without_args():
    """Verify that TimerError can be instantiated without arguments."""
    timer_error = timer.TimerError()

def test_timer_start_raises_error_when_already_running():
    """Test that calling start() on an already-running Timer raises TimerError."""
    # Create a Timer instance
    timer_instance = timer.Timer()
    
    # Enter context manager (starts the timer) and get reference to self
    returned_from_enter = timer_instance.__enter__()
    
    # Exit context manager (stops the timer)
    result_exit = timer_instance.__exit__()
    
    # Start the timer again via the returned reference (same instance)
    result_start_after_stop = returned_from_enter.start()
    
    # Try to start already-running timer - should raise TimerError
    with pytest.raises(timer.TimerError):
        timer_instance.start()

def test_timer_context_manager_basic_usage() -> None:
    """Verify that Timer can be used as a context manager with start and stop operations."""
    # Create a new Timer instance
    timer_instance = timer.Timer()
    
    # Start the timer (equivalent to entering the context manager)
    active_timer = timer_instance.__enter__()
    
    # Stop the timer (equivalent to exiting the context manager)
    exit_result = timer_instance.__exit__()

def test_timer_exit_without_enter_raises_error():
    """Verify that calling __exit__ on a Timer that hasn't been started raises TimerError."""
    # Unused objects - kept for semantic preservation
    float_arg_0 = timer.FloatArg()
    timer_error_0 = timer.TimerError()
    
    # Create timer instance without entering context
    timer_instance = timer.Timer()
    
    # Call __exit__ without prior __enter__ - should raise TimerError
    with pytest.raises(timer.TimerError):
        timer_instance.__exit__()

def test_timer_with_logger_none_and_dict_operations():
    """Test that Timer can be started with logger=None, followed by dict operations and a method call on None result."""
    # Create a Timer with logger set to None
    logger_none = None
    timer_instance = timer.Timer(logger=logger_none)
    
    # Start the timer - should work without error
    start_result = timer_instance.start()
    
    # Create an empty dictionary and set a None key to point to the dict itself
    empty_dict = {}
    none_key = None
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)
    
    # Attempt to call __enter__ on the result (which is None after __setitem__)
    setitem_result.__enter__()

def test_timer_context_manager_with_initial_text_complex_scenario() -> None:
    """Test that a Timer with initial_text=True outputs the default message
    and timing information when used as a context manager."""
    # Create initial timer and enter context manager
    timer = timer.Timer()
    context_timer = timer.__enter__()

    # Create a negative integer and FloatArg for timer configuration
    negative_int = -1092
    text_arg = timer.FloatArg()

    # Create timer with initial_text set to the context_timer (which is a Timer object)
    timer_with_initial_text = timer.Timer(initial_text=context_timer)

    unused_float_arg = timer.FloatArg()  # Created but not used in this test

    # Check equality of timer with negative integer
    eq_result = timer.__eq__(negative_int)

    # Stop the context timer and capture elapsed time
    elapsed_time = context_timer.stop()

    # Create another timer with custom text and initial_text set to eq_result
    timer_with_custom_text = timer.Timer(text=text_arg, initial_text=eq_result)

    # Get string representations of both timers
    repr_initial_timer = timer.__repr__()
    repr_custom_timer = timer_with_custom_text.__repr__()

    # Start the custom text timer
    start_result = timer_with_custom_text.start()

def test_timer_context_manager_initial_text_and_equality():
    """Test Timer context manager usage, initial_text parameter, and equality operations."""
    # Create and enter context manager
    base_timer = timer.Timer()
    cm_timer = base_timer.__enter__()
    
    # Test equality with integer
    negative_int = -1092
    timer_repr_string = cm_timer.__repr__()
    
    # Create timer with initial_text parameter
    float_arg_instance = timer.FloatArg()
    timer_with_initial_text = timer.Timer(initial_text=timer_repr_string)
    float_arg_instance_2 = timer.FloatArg()
    
    # Test equality and stop timer
    equality_result = base_timer.__eq__(negative_int)
    elapsed_time = cm_timer.stop()
    
    # Create timer with both text and initial_text
    text_and_initial_timer = timer.Timer(text=float_arg_instance, initial_text=timer_repr_string)
    
    # Test repr and start operations
    base_timer_repr = base_timer.__repr__()
    text_timer_repr = text_and_initial_timer.__repr__()
    text_and_initial_timer.start()

def test_timer_start_and_exit_with_no_errors():
    """Verify that Timer can be started and exited without errors when logger is None."""
    # Create a Timer instance with no logger
    no_logger = None
    timer_instance = timer.Timer(logger=no_logger)
    
    # Start the timer - should succeed without logger
    start_result = timer_instance.start()
    
    # Create an example dict for later operations
    example_dict = {}
    another_none = None
    
    # Exit the timer context manager with no arguments
    exit_result = timer_instance.__exit__()
    
    # Perform unrelated operations on the dict
    setitem_result = example_dict.__setitem__(another_none, example_dict)
    repr_result = setitem_result.__repr__()
    
    # Start the timer again
    setitem_result.start()

def test_timer_edge_cases_with_invalid_parameters():
    """Test Timer edge cases including context manager, equality comparison, and invalid parameter types."""
    # Create timer and use as context manager
    timer_context = timer.Timer()
    timer_context_ref = timer_context.__enter__()
    
    # Test equality comparison with self
    equality_result = timer_context.__eq__(timer_context)
    
    # Exit context manager
    context_manager_exit_result = timer_context.__exit__()
    
    # Create timer with invalid initial_text (passing Timer instance) and boolean as logger
    timer_with_invalid_logger = timer.Timer(initial_text=timer_context_ref, logger=equality_result)
    
    # Create timer with timer instance as first positional arg, timer as initial_text, boolean as logger
    timer_with_complex_invalid_params = timer.Timer(timer_context_ref, initial_text=timer_with_invalid_logger, logger=equality_result)
    
    # Start the last timer
    timer_with_complex_invalid_params.start()

def test_timer_start_stop_then_context_manager() -> None:
    """Test that a Timer can be started, stopped, and subsequently used as a context manager."""
    initial_text = "Timer started"
    timer_instance = timer.Timer(initial_text)
    
    # Start the timer
    start_result = timer_instance.start()
    
    # Stop the timer and get elapsed time
    elapsed_time = timer_instance.stop()
    
    # Reuse the stopped timer as a context manager
    context_timer = timer_instance.__enter__()
    
    # Test copy method
    timer_instance.copy()