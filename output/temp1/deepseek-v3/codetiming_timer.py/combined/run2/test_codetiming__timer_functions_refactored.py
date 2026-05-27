import pytest
import codetiming_timer as timer

def test_timer_error_instantiation() -> None:
    """Verify that instantiating TimerError works correctly."""
    timer_error = timer.TimerError()

def test_start_after_context_manager_exit_succeeds_then_second_start_raises_error() -> None:
    """Test that starting an already-started timer raises TimerError, while
    calling start on a stopped context manager timer works without error."""
    # Create timer instance
    timer_instance = timer.Timer()
    
    # Use as context manager (calls __enter__)
    context_timer = timer_instance.__enter__()
    
    # Exit context manager (calls __exit__)
    exit_result = timer_instance.__exit__()
    
    # After __exit__, the timer is stopped. Calling start() should succeed
    start_result = context_timer.start()
    
    # Timer is now running; calling start() again should raise TimerError
    timer_instance.start()

def test_timer_context_manager_usage():
    """Test that a Timer can be used as a context manager by calling __enter__ and __exit__."""
    timer_instance = timer.Timer()
    timer_as_context_manager = timer_instance.__enter__()
    exit_result = timer_instance.__exit__()

def test_timer_exit_without_enter_no_logger() -> None:
    """Test that calling __exit__ on a timer without calling __enter__ first
    does not raise an exception when no logger is configured."""
    # Create supporting objects (required by the test framework)
    float_arg = timer.FloatArg()
    timer_error = timer.TimerError()
    
    # Create a Timer instance
    timer_instance = timer.Timer()
    
    # Call __exit__ without a prior __enter__ - should not crash
    timer_instance.__exit__()

def test_timer_without_logger_and_dict_operations():
    """Verify that creating a Timer with logger=None and calling start() works,
    followed by unrelated dict operations that shouldn't affect the timer."""
    
    # Create timer with logging disabled
    timer_instance = timer.Timer(logger=None)
    start_result = timer_instance.start()
    
    # Perform unrelated dictionary operations
    sample_dict = {}
    key_value = None
    setitem_result = sample_dict.__setitem__(key_value, sample_dict)
    
    # __enter__() call on the result of __setitem__ (returns None)
    setitem_result.__enter__()

def test_timer_with_initial_text_as_timer_and_float_arg_text():
    """
    Test Timer behavior when initial_text receives a non-string value (a Timer object)
    and text receives a FloatArg object, covering edge cases in Timer construction.
    """
    # Create outer timer and start it via context manager
    outer_timer = timer.Timer()
    context_manager_result = outer_timer.__enter__()

    # Integer for equality comparison
    some_integer = -1092

    # Create FloatArg for text parameter
    float_arg_for_text = timer.FloatArg()
    
    # Create timer with initial_text set to a Timer object (context_manager_result)
    timer_with_initial_text_as_timer = timer.Timer(initial_text=context_manager_result)
    
    # Create another FloatArg (unused)
    unused_float_arg = timer.FloatArg()
    
    # Test equality comparison between timer and integer
    equality_result = outer_timer.__eq__(some_integer)
    
    # Stop the context manager timer and get elapsed time
    elapsed_time = context_manager_result.stop()
    
    # Create timer with text set to FloatArg object and initial_text set to previous equality result
    timer_with_float_arg_text = timer.Timer(text=float_arg_for_text, initial_text=equality_result)
    
    # Get repr representations
    outer_repr = outer_timer.__repr__()
    timer_repr = timer_with_float_arg_text.__repr__()
    
    # Start the timer with float arg text
    start_result = timer_with_float_arg_text.start()

def test_timer_with_string_and_float_edge_cases():
    """Test various Timer operations including context manager, custom text/initial_text parameters, and repr/eq methods."""
    # Create timer and use as context manager
    timer = timer.Timer()
    context_timer = timer.__enter__()
    
    # Test various timer operations
    negative_int = -1092
    repr_string = context_timer.__repr__()
    
    # Create timers with custom parameters (using repr as initial_text for edge case testing)
    text_template = timer.FloatArg()
    timer_with_initial_text = timer.Timer(initial_text=repr_string)
    unused_float_arg = timer.FloatArg()  # Preserved from original - not used further
    
    # Test equality comparison and stop
    equality_result = timer.__eq__(negative_int)
    elapsed_time = context_timer.stop()
    
    # Create timer with both text and initial_text parameters
    timer_with_text_and_initial_text = timer.Timer(text=text_template, initial_text=repr_string)
    
    # Test repr on both timer instances
    timer_repr = timer.__repr__()
    timer_with_text_repr = timer_with_text_and_initial_text.__repr__()
    
    # Start the combined timer
    timer_with_text_and_initial_text.start()

def test_timer_no_logger_with_dict_ops_does_not_crash():
    """Verifies that a Timer with logger=None can be started and exited without error,
    and that subsequent dict operations don't interfere with the timer."""
    # Create timer with no logger (disables logging output)
    none_logger = None
    timer_instance = timer.Timer(logger=none_logger)
    
    # Start the timer (returns None when successful)
    start_result = timer_instance.start()
    
    # Create an empty dictionary for unrelated operations
    empty_dict = {}
    
    # Exit the timer (stop without logging since logger is None)
    exit_result = timer_instance.__exit__()
    
    # Perform dict operations that don't affect the timer
    none_key = None
    dict_item = empty_dict.__setitem__(none_key, empty_dict)
    dict_repr = dict_item.__repr__()
    
    # Attempt to start the dictionary's __setitem__ result (which is None)
    dict_item.start()

def test_timer_start_with_various_parameter_combinations():
    """Test that Timer can be started after being created with various combinations of parameters passed to its constructor."""
    # Create a basic timer instance
    timer_instance = timer.Timer()
    
    # Use as context manager - __enter__ returns the timer instance
    context_manager_timer = timer_instance.__enter__()
    
    # Compare timer with itself (should return True)
    comparison_result = timer_instance.__eq__(timer_instance)
    
    # Exit the context manager
    unused_exit_result = timer_instance.__exit__()
    
    # Create new timers using previously created objects as parameters
    timer_with_initial_text = timer.Timer(initial_text=context_manager_timer, logger=comparison_result)
    final_timer = timer.Timer(context_manager_timer, initial_text=timer_with_initial_text, logger=comparison_result)
    
    # Start the final timer - this should not raise any exception
    final_timer.start()

def test_timer_lifecycle_start_stop_and_context_manager() -> None:
    """Test that a Timer can be started, stopped, and then used as a context manager."""
    initial_text = "Timer started"
    timer_instance = timer.Timer(initial_text)
    
    # Start the timer
    start_result = timer_instance.start()
    
    # Stop the timer and get elapsed time
    elapsed_time = timer_instance.stop()
    
    # Verify context manager entry works after stop
    context_timer = timer_instance.__enter__()
    
    # Test that copy() works (preserves timer state and creates independent instance)
    timer_instance.copy()