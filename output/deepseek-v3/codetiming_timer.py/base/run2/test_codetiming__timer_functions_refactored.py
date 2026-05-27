import pytest
import codetiming_timer as timer

def test_timer_error_instantiation():
    """Test that TimerError can be instantiated without arguments."""
    timer_error = timer.TimerError()  # Instantiate TimerError to ensure no errors occur

def test_timer_context_manager_can_be_restarted_after_exit():
    """Test that a Timer used as a context manager can be manually started again after context exit."""
    # Create timer and use it as context manager (starts on enter, stops on exit)
    timer_instance = timer.Timer()
    same_timer_instance = timer_instance.__enter__()  # Returns self
    exit_result = timer_instance.__exit__()  # Stops timer
    
    # Timer should now be stopped and can be started again
    start_result = same_timer_instance.start()  # Start the timer again
    timer_instance.start()  # This should raise TimerError since timer is already running

def test_context_manager_can_be_entered_and_exited_without_error() -> None:
    """Test that Timer can be used as a context manager without raising errors."""
    # Create a timer instance
    timer_instance = timer.Timer()
    
    # Enter the context manager (starts timing)
    entered_timer = timer_instance.__enter__()
    
    # Exit the context manager (stops timing)
    exit_result = timer_instance.__exit__()

def test_timer_exit_called_without_context_manager():
    """Test that Timer.__exit__ can be called without entering context manager.
    
    This tests the behavior when __exit__ is called directly on a Timer instance
    that wasn't used as a context manager.
    """
    # Create unused objects (may be from test generation artifacts)
    float_arg = module_0.FloatArg()  # Unused in this test
    timer_error = timer.TimerError()  # Unused in this test
    
    # Create timer instance and call __exit__ without entering context
    timer_instance = timer.Timer()
    timer_instance.__exit__()

def test_timer_with_none_logger_and_unrelated_dict_operation():
    """Test Timer with logger=None alongside unrelated dictionary operations.
    
    This test creates a Timer with no logger, starts it, then performs
    an unrelated dictionary operation that returns None, and finally
    attempts to call __enter__ on that None value (which will raise
    AttributeError). The test's primary focus appears to be on Timer
    initialization with logger=None, though the subsequent operations
    are unrelated to Timer functionality.
    """
    # Create Timer with no logger (logger=None)
    logger_none = None
    timer_instance = timer.Timer(logger=logger_none)
    
    # Start the timer (returns None)
    start_return = timer_instance.start()
    
    # Perform unrelated dictionary operation
    empty_dict = {}
    key_none = None
    setitem_return = empty_dict.__setitem__(key_none, empty_dict)
    
    # This will raise AttributeError since setitem_return is None
    setitem_return.__enter__()

def test_timer_context_manager_with_custom_arguments_and_equality_check():
    """Test Timer operations including context manager usage, equality comparison, 
    and instantiation with various argument types."""
    
    # Create a base timer instance
    base_timer = timer.Timer()
    
    # Use timer as context manager (starts timing)
    context_timer = base_timer.__enter__()
    
    # Various test values
    negative_number = -1092
    float_arg_instance_a = timer.FloatArg()
    
    # Create timer with Timer instance as initial_text (unusual but valid)
    timer_with_timer_initial = timer.Timer(initial_text=context_timer)
    
    float_arg_instance_b = timer.FloatArg()
    
    # Check equality between timer and integer (returns False)
    equality_check_result = base_timer.__eq__(negative_number)
    
    # Stop the context manager timer
    elapsed_time = context_timer.stop()
    
    # Create timer with FloatArg as text and equality result as initial_text
    custom_timer = timer.Timer(text=float_arg_instance_a, initial_text=equality_check_result)
    
    # Get string representations
    base_timer_repr = base_timer.__repr__()
    custom_timer_repr = custom_timer.__repr__()
    
    # Start the custom timer (returns None)
    start_return_value = custom_timer.start()

def test_timer_context_manager_with_repr_and_initial_text():
    """Test Timer context manager functionality with repr() and initial_text parameters."""
    # Create a timer and enter context manager
    timer_context = timer.Timer()
    entered_timer = timer_context.__enter__()
    
    # Prepare test values
    comparison_value = -1092
    timer_repr_str = entered_timer.__repr__()
    
    # Create FloatArg instances (test utilities)
    float_arg_1 = timer.FloatArg()
    
    # Create timer with initial_text from repr string
    timer_with_initial_text = timer.Timer(initial_text=timer_repr_str)
    
    # Create another FloatArg instance
    float_arg_2 = timer.FloatArg()
    
    # Compare timer with integer (should return NotImplemented or False)
    eq_result = timer_context.__eq__(comparison_value)
    
    # Stop the context manager timer
    elapsed_time = entered_timer.stop()
    
    # Create timer with both text and initial_text parameters
    timer_with_text_and_initial = timer.Timer(text=float_arg_1, initial_text=timer_repr_str)
    
    # Get repr strings for both timers
    timer_context_repr = timer_context.__repr__()
    timer_with_text_repr = timer_with_text_and_initial.__repr__()
    
    # Start the timer with text and initial_text
    timer_with_text_and_initial.start()

def test_timer_with_none_logger_and_self_referential_dict():
    """Test Timer with logger=None and operations on a self-referential dictionary.

    This test creates a Timer with a None logger, starts it, and then performs
    operations on a dictionary that becomes self-referential. The test then
    attempts to call methods on the result of a dictionary operation (which is None),
    leading to an AttributeError.
    """
    logger_none = None
    my_timer = timer.Timer(logger=logger_none)
    start_result = my_timer.start()  # Returns None

    empty_dict = {}
    none_key = None

    # This stops the timer (if it was running) and returns None.
    exit_result = my_timer.__exit__()

    # Set a self-referential entry in the dictionary: empty_dict[None] = empty_dict.
    # The __setitem__ method returns None.
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)

    # Get the string representation of None: 'None'.
    repr_result = setitem_result.__repr__()

    # This will raise an AttributeError because setitem_result is None.
    setitem_result.start()

def test_timer_start_with_complex_initialization():
    """Test Timer behavior with nested context managers and unusual parameter combinations."""
    
    # Create initial timer and enter context manager
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()  # Starts timing
    
    # Check equality of timer with itself
    equality_result = base_timer.__eq__(base_timer)
    
    # Exit the context manager (stops timing)
    exit_result = base_timer.__exit__()
    
    # Create timers with unusual parameter combinations:
    # - initial_text set to a Timer instance (unusual usage)
    # - logger set to boolean equality result
    timer_with_initial_as_timer = timer.Timer(initial_text=entered_timer, logger=equality_result)
    
    # Create timer with Timer instance as name parameter (unusual)
    timer_with_complex_params = timer.Timer(
        entered_timer,  # name parameter (unusual: Timer instance as name)
        initial_text=timer_with_initial_as_timer,  # initial_text as Timer instance
        logger=equality_result  # logger as boolean
    )
    
    # Attempt to start the complex timer
    timer_with_complex_params.start()

def test_timer_operations_with_string_parameter():
    """Test Timer operations when initialized with a string parameter."""
    # Create timer with string parameter (likely name or text)
    timer_name_or_text = "Timer started"
    timer = timer.Timer(timer_name_or_text)
    
    # Start and stop timer (basic operation)
    start_result = timer.start()  # Returns None
    elapsed_time = timer.stop()   # Returns float
    
    # Use timer as context manager
    context_timer = timer.__enter__()
    
    # Attempt to copy timer (method may exist in some implementations)
    timer.copy()

