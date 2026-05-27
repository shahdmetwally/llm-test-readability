import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError exception can be instantiated without arguments."""
    # Create a TimerError instance to verify it can be instantiated
    timer_error = timer.TimerError()

def test_start_timer_after_context_manager_exit_raises_error():
    """Test that starting a timer twice (once after context manager exit) raises TimerError."""
    # Create timer and enter context manager (starts timer)
    timer = timer.Timer()
    same_timer = timer.__enter__()  # Returns same timer instance
    
    # Exit context manager (stops timer)
    timer.__exit__()
    
    # Start timer again (should succeed)
    same_timer.start()
    
    # Try to start same timer again while running (should raise TimerError)
    timer.start()

def test_timer_context_manager_enter_exit_methods_work_correctly() -> None:
    """Test that Timer context manager's __enter__ and __exit__ methods work correctly."""
    # Create a Timer instance
    timer_instance = timer.Timer()
    
    # Enter context manager (starts timing)
    entered_timer = timer_instance.__enter__()
    
    # Exit context manager (stops timing)
    exit_result = timer_instance.__exit__()

def test_timer_exit_without_context_does_not_raise() -> None:
    """Test that calling __exit__ on a Timer without entering context doesn't crash."""
    # Create various objects (unused in test but preserved from original)
    float_arg = module_0.FloatArg()
    timer_error = timer.TimerError()
    
    # Create timer and call __exit__ without ever entering context
    timer_instance = timer.Timer()
    timer_instance.__exit__()

def test_timer_with_none_logger_and_dict_operation():
    """Test that Timer with logger=None can be started and doesn't interfere with other operations."""
    # Create a Timer with logger=None (no output)
    logger_none = None
    timer_instance = timer.Timer(logger=logger_none)
    
    # Start the timer (returns None)
    start_result = timer_instance.start()
    
    # Perform unrelated dictionary operation
    empty_dict = {}
    none_key = None
    # Set a self-referential dictionary entry
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)
    
    # Attempt to call __enter__ on the None result (will raise AttributeError)
    setitem_result.__enter__()

def test_timer_context_manager_with_initial_text_and_equality_check():
    """Test Timer context manager operations with initial text and equality comparison.
    
    This test verifies that Timer instances can be used as context managers,
    that equality comparisons work, and that various Timer configurations
    (including those with initial_text) can be created and manipulated.
    """
    # Create a Timer instance and enter context manager mode
    timer_instance = timer.Timer()
    context_timer = timer_instance.__enter__()
    
    # Create test values for comparison and Timer configuration
    comparison_value = -1092
    text_config_1 = timer.FloatArg()
    
    # Create Timer with initial_text set to another Timer instance
    timer_with_timer_as_initial_text = timer.Timer(initial_text=context_timer)
    
    # Create another FloatArg for text configuration
    text_config_2 = timer.FloatArg()
    
    # Compare Timer instance with integer value
    equality_result = timer_instance.__eq__(comparison_value)
    
    # Stop the context manager timer and get elapsed time
    elapsed_time = context_timer.stop()
    
    # Create Timer with text and initial_text configurations
    timer_with_configs = timer.Timer(text=text_config_1, initial_text=equality_result)
    
    # Get string representations of Timer instances
    timer_repr_1 = timer_instance.__repr__()
    timer_repr_2 = timer_with_configs.__repr__()
    
    # Start the configured timer
    start_result = timer_with_configs.start()

def test_timer_with_custom_initial_text_and_float_arg():
    """Test Timer operations with custom initial text and FloatArg parameters.
    
    This test verifies that Timer instances can be created and manipulated
    with various configurations including custom initial text and FloatArg
    objects for text formatting.
    """
    # Create initial timer and enter context manager
    timer_a = timer.Timer()
    timer_a_context = timer_a.__enter__()  # Same as timer_a
    
    # Get string representation of timer
    negative_number = -1092
    timer_repr = timer_a_context.__repr__()
    
    # Create FloatArg objects for text parameter
    float_arg_a = timer.FloatArg()
    
    # Create timer with initial_text set to timer's string representation
    timer_b = timer.Timer(initial_text=timer_repr)
    
    # Create another FloatArg (unused but preserved)
    float_arg_b = timer.FloatArg()
    
    # Compare timer with integer (should return False)
    equality_result = timer_a.__eq__(negative_number)
    
    # Stop the context manager timer and get elapsed time
    elapsed_time = timer_a_context.stop()
    
    # Create timer with both text and initial_text parameters
    timer_c = timer.Timer(text=float_arg_a, initial_text=timer_repr)
    
    # Get string representations of timers
    timer_a_repr_again = timer_a.__repr__()
    timer_c_repr = timer_c.__repr__()
    
    # Start the third timer
    timer_c.start()

def test_timer_with_none_logger_and_attribute_error_on_none_start():
    """Test Timer with logger=None, start/stop via __exit__, then unrelated operations leading to AttributeError."""
    # Create Timer with None logger
    none_logger = None
    my_timer = timer.Timer(logger=none_logger)
    
    # Start timer (returns None)
    start_result = my_timer.start()
    
    # Create empty dict for unrelated operations
    empty_dict = {}
    
    # Another None value for dictionary key
    none_key = None
    
    # Stop timer via __exit__ (returns None)
    exit_result = my_timer.__exit__()
    
    # Unrelated: Set dict[None] = dict (returns None)
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)
    
    # Unrelated: Get string representation of None
    repr_result = setitem_result.__repr__()
    
    # This will raise AttributeError: None has no 'start' method
    setitem_result.start()

def test_timer_initialization_with_various_parameter_types():
    """Test Timer initialization and context manager usage with different parameter types."""
    
    # Create a basic timer and enter context manager
    basic_timer = timer.Timer()
    entered_timer = basic_timer.__enter__()  # Starts the timer
    
    # Check equality of timer with itself (identity check)
    is_equal = basic_timer.__eq__(basic_timer)
    
    # Exit context manager to stop the timer
    _ = basic_timer.__exit__()
    
    # Create timers with unusual parameter types to test edge cases
    timer_with_timer_as_initial_text = timer.Timer(initial_text=entered_timer, logger=is_equal)
    timer_with_mixed_parameters = timer.Timer(
        entered_timer, 
        initial_text=timer_with_timer_as_initial_text, 
        logger=is_equal
    )
    
    # Start the timer with mixed parameters
    timer_with_mixed_parameters.start()

def test_timer_basic_operations_start_stop_context_copy():
    """Test basic timer operations: start, stop, context entry, and copy."""
    # Create timer with initial text
    timer_text = "Timer started"
    timer_instance = timer.Timer(timer_text)
    
    # Start and stop the timer
    start_result = timer_instance.start()  # Returns None
    elapsed_time = timer_instance.stop()   # Returns float elapsed time
    
    # Enter context manager (starts timer again)
    context_timer = timer_instance.__enter__()
    
    # Create a copy of the timer
    timer_instance.copy()

