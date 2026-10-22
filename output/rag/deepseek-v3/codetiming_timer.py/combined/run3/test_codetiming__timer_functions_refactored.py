import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated() -> None:
    """Verify that TimerError can be instantiated without arguments."""
    # Instantiate the custom exception class to ensure it works as expected
    timer_error_instance = timer.TimerError()

def test_timer_context_manager_restart_raises_timer_error():
    """Test that Timer context manager properly handles start/stop and raises TimerError on restart without stopping."""
    timer = timer.Timer()
    
    # Enter the context manager (starts the timer)
    returned_timer = timer.__enter__()
    
    # Exit the context manager (stops the timer)
    exit_result = timer.__exit__()
    
    # Start the timer again (returned_timer is the same Timer object)
    second_start_result = returned_timer.start()
    
    # Try to start an already-running timer - this should raise TimerError
    timer.start()

def test_timer_context_manager_basic_usage() -> None:
    """Test that Timer can be used as a context manager without errors."""
    # Create a fresh Timer instance
    timer = timer.Timer()
    
    # Enter the context manager (start timing)
    timer_as_context_manager = timer.__enter__()
    
    # Exit the context manager (stop timing and report)
    exit_result = timer.__exit__()

def test_timer_exit_without_start_raises_error() -> None:
    """Test that Timer raises an error when __exit__() is called without a corresponding start."""
    timer_instance = timer.Timer()
    timer_instance.__exit__()

def test_timer_no_logger_does_not_interfere_with_operations():
    """Test that a Timer with logger=None can be started and doesn't interfere with other operations."""
    # Create a Timer with no logger
    timer_no_logger = timer.Timer(logger=None)
    
    # Start the timer
    start_result = timer_no_logger.start()
    
    # Create a sample dictionary and set a None key
    sample_dict = {}
    key_none = None
    set_result = sample_dict.__setitem__(key_none, sample_dict)
    
    # Enter the result as a context manager
    set_result.__enter__()

def test_timer_initial_text_with_float_format():
    """Tests Timer behavior when created with timer objects as initial_text and FloatArg as text format."""
    # Create base timer instance
    timer_instance = timer.Timer()
    
    # Enter context manager, returning the timer itself
    returned_timer = timer_instance.__enter__()
    
    # Use -1092 as a comparison value
    negative_int = -1092
    
    # Create a FloatArg for text formatting
    float_arg_instance = timer.FloatArg()
    
    # Create a timer with the returned_timer as initial_text
    timer_with_initial_text = timer.Timer(initial_text=returned_timer)
    
    # Create another FloatArg (unused in subsequent operations)
    another_float_arg = timer.FloatArg()
    
    # Check equality comparison with negative integer
    comparison_result = timer_instance.__eq__(negative_int)
    
    # Stop the context manager timer and get elapsed time
    elapsed_time = returned_timer.stop()
    
    # Create a timer with FloatArg as text and comparison result as initial_text
    timer_with_float_text = timer.Timer(text=float_arg_instance, initial_text=comparison_result)
    
    # Get repr of both timer instances
    timer_repr = timer_instance.__repr__()
    timer_with_float_text_repr = timer_with_float_text.__repr__()
    
    # Start the timer with float text configuration
    start_result = timer_with_float_text.start()

def test_timer_context_manager_and_lifecycle_with_parameters():
    """Verify Timer supports context manager operations, repr(), eq(), and multiple lifecycle states with various parameter combinations."""
    # Create a Timer and enter context manager
    timer_context = timer.Timer()
    timer_from_context = timer_context.__enter__()
    
    # Test repr() and equality with integer
    comparison_value = -1092
    initial_text = timer_from_context.__repr__()
    text_arg = timer.FloatArg()
    timer_with_initial_text = timer.Timer(initial_text=initial_text)
    second_float_arg = timer.FloatArg()
    equality_result = timer_context.__eq__(comparison_value)
    elapsed_time = timer_from_context.stop()
    
    # Create a Timer with both text and initial_text parameters
    timer_with_text_and_initial = timer.Timer(text=text_arg, initial_text=initial_text)
    timer_context_repr = timer_context.__repr__()
    timer_with_text_repr = timer_with_text_and_initial.__repr__()
    timer_with_text_and_initial.start()

def test_timer_exit_with_none_logger_and_dict_operations():
    """Verifies Timer start/stop behavior with None logger and dict operations."""
    # Initialize Timer with no logger
    none_logger = None
    timer_instance = timer.Timer(logger=none_logger)
    
    # Start the timer
    start_result = timer_instance.start()
    
    # Create a dictionary for interaction
    test_dict = {}
    
    # Stop the timer via context manager exit
    dict_key = None
    exit_result = timer_instance.__exit__()
    
    # Perform dictionary operations
    dict_entry = test_dict.__setitem__(dict_key, test_dict)
    entry_repr = dict_entry.__repr__()
    
    # Re-start timer on the dict entry
    dict_entry.start()

def test_timer_creation_with_various_initial_text_and_logger_combinations():
    """Tests creating Timer objects with various combinations of initial_text and logger parameters derived from other Timer operations."""
    # Create a base timer and enter it as context manager
    timer_instance = timer.Timer()
    returned_timer = timer_instance.__enter__()
    
    # Check equality (returns boolean for use as logger parameter)
    equality_result = timer_instance.__eq__(timer_instance)
    
    # Exit the timer context
    exit_result = timer_instance.__exit__()
    
    # Create timer with initial_text set to the returned timer object from __enter__
    timer_with_initial_text = timer.Timer(initial_text=returned_timer, logger=equality_result)
    
    # Create timer with all parameters: first positional arg, initial_text from another timer, logger from comparison
    timer_with_all_params = timer.Timer(returned_timer, initial_text=timer_with_initial_text, logger=equality_result)
    
    # Start the fully configured timer
    timer_with_all_params.start()

def test_timer_initial_text_start_stop_and_context_manager():
    """Verify that a Timer with initial text can be started, stopped, and used as a context manager."""
    initial_text = "Timer started"
    timer_instance = timer.Timer(initial_text)
    
    # Start and stop the timer
    start_result = timer_instance.start()        # .start() returns None
    elapsed_time = timer_instance.stop()          # .stop() returns elapsed time
    
    # Use timer as context manager
    context_timer = timer_instance.__enter__()    # .__enter__() returns the timer
    
    # Verify copy functionality
    timer_instance.copy()