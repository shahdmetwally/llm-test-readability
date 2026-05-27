import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated() -> None:
    """Test that TimerError can be instantiated without error."""
    timer_error = timer.TimerError()

def test_timer_start_after_context_manager_and_start_again() -> None:
    """Test starting a timer after exiting a context manager, then starting again without stopping."""
    # Create a timer instance
    timer_instance = timer.Timer()
    
    # Use the timer as a context manager (starts and stops automatically)
    same_timer = timer_instance.__enter__()
    exit_result = timer_instance.__exit__()
    
    # Start the timer explicitly after context manager has stopped it
    start_result = same_timer.start()
    
    # Attempt to start the timer again while it's already running
    timer_instance.start()

def test_timer_context_manager_enters_and_exits():
    """Test that Timer can be used as a context manager without errors."""
    # Create a Timer instance
    timer_instance = timer.Timer()
    # Enter the context manager (starts timing)
    entered_timer = timer_instance.__enter__()
    # Exit the context manager (stops timing)
    exit_result = timer_instance.__exit__()

def test_timer_exit_without_start() -> None:
    """Test that Timer.__exit__ can be called without starting the timer."""
    float_arg = timer.FloatArg()
    timer_error_instance = timer.TimerError()
    timer_instance = timer.Timer()
    timer_instance.__exit__()

def test_timer_with_none_logger_and_dict_operations() -> None:
    """Test Timer with logger=None and unrelated dictionary operations."""
    # Create a Timer with logger set to None
    logger_none = None
    timer_instance = timer.Timer(logger=logger_none)

    # Start the timer (returns None)
    start_return_value = timer_instance.start()

    # Create an empty dictionary
    empty_dict = {}

    # Use None as a key to set the dictionary to itself (self-referential)
    none_key = None
    setitem_return_value = empty_dict.__setitem__(none_key, empty_dict)

    # Attempt to call __enter__ on the return value of __setitem__ (which is None)
    # This will raise an AttributeError because None has no __enter__ method.
    setitem_return_value.__enter__()

def test_timer_operations_with_mixed_argument_types() -> None:
    """Test Timer operations with various argument types to ensure no crashes."""
    # Create a base timer and enter context
    base_timer = timer.Timer()
    context_timer = base_timer.__enter__()  # Returns self
    
    # Various test values
    negative_int = -1092
    float_arg_instance_1 = timer.FloatArg()
    
    # Create timer with unusual initial_text (a Timer instance)
    timer_with_timer_initial_text = timer.Timer(initial_text=context_timer)
    
    float_arg_instance_2 = timer.FloatArg()
    
    # Test equality comparison with integer
    equality_result = base_timer.__eq__(negative_int)
    
    # Stop the context timer and get elapsed time
    elapsed_time = context_timer.stop()
    
    # Create timer with non-string text and initial_text arguments
    timer_with_non_string_args = timer.Timer(
        text=float_arg_instance_1, 
        initial_text=equality_result
    )
    
    # Get string representations
    base_timer_repr = base_timer.__repr__()
    non_string_timer_repr = timer_with_non_string_args.__repr__()
    
    # Start the timer (returns None)
    start_result = timer_with_non_string_args.start()
    
    # Note: This is a smoke test - no assertions, just ensuring no exceptions

def test_timer_context_manager_and_initial_text_with_string_representation() -> None:
    """Test Timer operations within context manager using string representation as initial_text parameter."""
    # Create a default timer and enter its context
    default_timer = timer.Timer()
    context_timer = default_timer.__enter__()

    # Integer value for comparison (unused in assertions)
    comparison_value = -1092

    # Get string representation of the timer in context
    timer_repr = context_timer.__repr__()

    # Create FloatArg instances for text arguments
    text_argument = timer.FloatArg()
    unused_text_argument = timer.FloatArg()

    # Create a timer with initial_text set to the string representation
    timer_with_repr_initial_text = timer.Timer(initial_text=timer_repr)

    # Compare timer with integer (expected to return False or NotImplemented)
    equality_result = default_timer.__eq__(comparison_value)

    # Stop the context timer and capture elapsed time
    elapsed_time = context_timer.stop()

    # Create a timer with custom text and initial_text from string representation
    timer_with_text_and_initial_text = timer.Timer(text=text_argument, initial_text=timer_repr)

    # Get string representations again
    default_timer_repr_again = default_timer.__repr__()
    timer_with_text_repr = timer_with_text_and_initial_text.__repr__()

    # Start the timer with custom parameters
    timer_with_text_and_initial_text.start()

def test_timer_none_logger_dict_operations_and_attribute_error():
    """Test Timer with None logger: start, __exit__, and dictionary operations."""
    # Create Timer with None logger
    none_logger = None
    timer_instance = timer.Timer(logger=none_logger)
    
    # Start the timer (returns None)
    start_result = timer_instance.start()
    
    # Create empty dict and None key for subsequent operations
    empty_dict = {}
    none_key = None
    
    # Stop timer via __exit__ (returns None)
    exit_result = timer_instance.__exit__()
    
    # Dictionary operation: set None key to empty dict (returns None)
    setitem_result = empty_dict.__setitem__(none_key, empty_dict)
    
    # Call __repr__ on the None result (returns string representation)
    repr_result = setitem_result.__repr__()
    
    # Attempt to call start() on None (will raise AttributeError)
    setitem_result.start()

def test_timer_context_manager_and_initialization_with_unusual_parameters() -> None:
    """Test Timer context manager and initialization using Timer instances as parameters."""
    # Create a Timer and use it as a context manager
    first_timer = timer.Timer()
    context_manager_timer = first_timer.__enter__()
    is_equal = first_timer.__eq__(first_timer)
    exit_result = first_timer.__exit__()

    # Create Timer instances with unusual parameters: using Timer instances as initial_text and logger
    timer_with_initial_text_and_logger = timer.Timer(initial_text=context_manager_timer, logger=is_equal)
    timer_with_name_initial_text_and_logger = timer.Timer(
        context_manager_timer, initial_text=timer_with_initial_text_and_logger, logger=is_equal
    )

    # Start the last timer
    timer_with_name_initial_text_and_logger.start()

def test_timer_start_stop_context_copy() -> None:
    """Test Timer operations: start, stop, context manager entry, and copy."""
    timer_name = "Timer started"
    
    # Create and start timer
    timer = timer.Timer(timer_name)
    _ = timer.start()  # start() returns None
    
    # Stop timer and get elapsed time
    elapsed_time = timer.stop()
    
    # Use timer as context manager
    context_timer = timer.__enter__()
    
    # Create a copy of the timer
    timer.copy()

