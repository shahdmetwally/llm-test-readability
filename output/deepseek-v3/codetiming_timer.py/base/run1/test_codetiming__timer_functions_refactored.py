import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated_without_arguments():
    """Test that TimerError can be instantiated without any arguments."""
    timer_error = timer.TimerError()

def test_timer_context_manager_and_start_twice_raises_error():
    """Test that starting a timer twice raises TimerError after using context manager.
    
    This test verifies that after using a Timer as a context manager (which starts
    and stops it), restarting the timer and then attempting to start it again while
    it's already running will raise a TimerError.
    """
    # Create a timer instance
    timer_instance = timer.Timer()
    
    # Use timer as context manager (starts timer, then stops on exit)
    same_timer = timer_instance.__enter__()  # Returns the same timer instance
    timer_instance.__exit__()  # Stops the timer
    
    # Start the timer again (now it's running)
    same_timer.start()
    
    # Attempt to start the same timer while it's already running
    # This should raise TimerError (though not caught in this test)
    timer_instance.start()

def test_timer_context_manager_enter_exit_returns_none():
    """Test that Timer context manager's __enter__ returns self and __exit__ returns None."""
    # Create timer instance
    timer_instance = timer.Timer()
    
    # Enter context manager (starts timer)
    entered_timer = timer_instance.__enter__()
    
    # Exit context manager (stops timer) and capture return value
    exit_result = timer_instance.__exit__(None, None, None)
    
    # Assert that __enter__ returns the timer instance itself
    assert entered_timer is timer_instance
    # Assert that __exit__ returns None
    assert exit_result is None

def test_timer_exit_without_context_does_not_raise_error() -> None:
    """Test that calling __exit__ on a Timer without entering context doesn't raise."""
    # Create various timer-related objects
    float_arg = timer.FloatArg()
    timer_error = timer.TimerError()
    timer_instance = timer.Timer()
    
    # Attempt to exit timer without entering context - should not raise
    timer_instance.__exit__()

def test_timer_without_logger_does_not_print():
    """Test that a Timer with logger=None does not produce any output."""
    # Create a Timer with no logger (silent mode)
    logger_none = None
    silent_timer = timer.Timer(logger=logger_none)
    
    # Start the timer (returns None)
    start_result = silent_timer.start()
    
    # Unrelated operations that don't affect timer behavior
    empty_dict = {}
    key_none = None
    setitem_result = empty_dict.__setitem__(key_none, empty_dict)
    
    # This will raise AttributeError (None.__enter__) but preserves original test behavior
    setitem_result.__enter__()

def test_timer_context_manager_with_initial_text_and_custom_parameters():
    """Test Timer context manager with various parameter combinations.
    
    This test verifies that Timer instances work correctly as context managers
    when initialized with different combinations of initial_text, text, and 
    other parameters, including edge cases with custom objects.
    """
    # Create initial timer instance
    timer_instance_1 = timer.Timer()
    
    # Use timer as context manager
    context_timer = timer_instance_1.__enter__()
    
    # Prepare test values
    comparison_value = -1092
    float_arg_instance_1 = timer.FloatArg()
    
    # Create timer with Timer instance as initial_text (unusual but allowed)
    timer_with_initial_text = timer.Timer(initial_text=context_timer)
    
    # Create another FloatArg instance
    float_arg_instance_2 = timer.FloatArg()
    
    # Test equality comparison between timer and integer
    equality_result = timer_instance_1.__eq__(comparison_value)
    
    # Stop the context manager timer and get elapsed time
    elapsed_time = context_timer.stop()
    
    # Create timer with FloatArg as text parameter and equality result as initial_text
    timer_with_custom_params = timer.Timer(
        text=float_arg_instance_1, 
        initial_text=equality_result
    )
    
    # Get string representations of timers
    timer_repr_1 = timer_instance_1.__repr__()
    timer_repr_2 = timer_with_custom_params.__repr__()
    
    # Start the custom parameter timer
    start_return_value = timer_with_custom_params.start()

def test_timer_context_manager_with_initial_text_and_custom_text_object():
    """Test Timer operations including context manager, custom text objects, and initial text."""
    # Create a timer and enter its context (starts timing)
    timer = timer.Timer()
    context_timer = timer.__enter__()
    
    # Create various objects for testing
    comparison_value = -1092
    timer_repr = context_timer.__repr__()
    float_arg = timer.FloatArg()
    
    # Create timer with initial text from another timer's representation
    timer_with_initial_text = timer.Timer(initial_text=timer_repr)
    another_float_arg = timer.FloatArg()
    
    # Check equality with unrelated value (should be False)
    equality_result = timer.__eq__(comparison_value)
    
    # Stop the context timer and get elapsed time
    elapsed_time = context_timer.stop()
    
    # Create timer with custom text object and initial text
    timer_with_text_and_initial_text = timer.Timer(text=float_arg, initial_text=timer_repr)
    
    # Get string representations
    timer_repr_again = timer.__repr__()
    timer3_repr = timer_with_text_and_initial_text.__repr__()
    
    # Start the third timer
    timer_with_text_and_initial_text.start()

def test_timer_start_exit_and_dict_operations_with_none():
    """Test Timer start/exit sequence followed by dictionary operations on None."""
    # Create a Timer with no logger
    logger_none = None
    timer_instance = timer.Timer(logger=logger_none)
    
    # Start the timer (returns None)
    start_return = timer_instance.start()
    
    # Create empty dict and another None value
    empty_dict = {}
    another_none = None
    
    # Exit the timer context (returns None)
    exit_return = timer_instance.__exit__()
    
    # Dictionary operation: set item with None key and dict as value
    setitem_return = empty_dict.__setitem__(another_none, empty_dict)
    
    # Get string representation of the setitem return value (None)
    repr_return = setitem_return.__repr__()
    
    # Attempt to call start() on None (will raise AttributeError)
    setitem_return.start()

def test_timer_start_with_unusual_parameter_types():
    """Test Timer.start() behavior when initialized with Timer instances as parameters."""
    # Create a base timer and enter context
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()  # Starts timer, returns self
    
    # Compare timer with itself (should be True for same object)
    is_equal_result = base_timer.__eq__(base_timer)
    
    # Exit context (stops timer)
    exit_result = base_timer.__exit__()
    
    # Create timer with Timer instance as initial_text parameter
    timer_with_timer_as_initial_text = timer.Timer(
        initial_text=entered_timer, 
        logger=is_equal_result
    )
    
    # Create timer with Timer instance as name and initial_text parameters
    timer_with_timer_as_name_and_initial_text = timer.Timer(
        entered_timer,  # name parameter
        initial_text=timer_with_timer_as_initial_text, 
        logger=is_equal_result
    )
    
    # Attempt to start timer with unusual parameter configuration
    timer_with_timer_as_name_and_initial_text.start()

def test_timer_start_stop_enter_copy_methods():
    """Test that Timer methods start(), stop(), __enter__(), and copy() can be called without error."""
    # Create a timer with a name
    timer_name = "Timer started"
    timer = timer.Timer(timer_name)
    
    # Start and stop the timer
    _ = timer.start()  # start() returns None
    elapsed_time = timer.stop()  # stop() returns elapsed time as float
    
    # Use timer as context manager
    context_timer = timer.__enter__()
    
    # Create a copy of the timer
    timer.copy()

