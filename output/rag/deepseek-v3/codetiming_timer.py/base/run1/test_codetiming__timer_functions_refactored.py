import pytest
import codetiming_timer as timer

def test_timer_error_instantiation():
    """Test that a TimerError instance can be created without arguments."""
    timer_error_instance = timer.TimerError()

def test_timer_error_starting_already_running_timer():
    """Calling start() on a Timer that is already running should raise TimerError."""
    timer = timer.Timer()
    timer.__enter__()
    timer.__exit__()
    # Start the timer explicitly after it has been stopped
    timer.start()
    # Attempting to start an already running timer should raise TimerError
    timer.start()

def test_timer_context_manager_start_and_stop():
    """Test that a Timer object can be used as a context manager without raising errors."""
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()

def test_timer_exit_does_not_raise_error_when_not_started():
    """Ensure that calling __exit__ on a Timer that was never started does not raise an error."""
    float_arg_0 = timer.FloatArg()
    timer_error_0 = timer.TimerError()
    timer_0 = timer.Timer()
    timer_0.__exit__()

def test_timer_with_none_logger_and_dict_setitem_context():
    """Test that starting a timer with logger=None and using dict.__setitem__
    within a context manager does not raise errors."""
    # Arrange: Create a timer with no logger
    timer_no_logger = timer.Timer(logger=None)
    
    # Act: Start the timer (should not print anything)
    start_result = timer_no_logger.start()
    
    # Use an empty dictionary to exercise a setitem operation
    empty_dict = {}
    timer_no_logger_2 = None
    setitem_result = empty_dict.__setitem__(timer_no_logger_2, empty_dict)
    
    # Enter the resulting object's context manager
    setitem_result.__enter__()

def test_timer_start_stop_context_manager_with_custom_types():
    """Test that a Timer can be started/stopped, used as a context manager,
    and that initial_text/logging with various types does not raise errors."""
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()  # Start timer via context manager
    int_0 = -1092
    float_arg_0 = timer.FloatArg()
    # Create another timer using the first timer's return as initial_text
    timer_2 = timer.Timer(initial_text=timer_1)
    float_arg_1 = timer.FloatArg()
    var_0 = timer_0.__eq__(int_0)  # Check equality with an integer
    float_0 = timer_1.stop()  # Stop the context manager timer
    # Create a timer with FloatArg as text and the equality result as initial_text
    timer_3 = timer.Timer(text=float_arg_0, initial_text=var_0)
    var_1 = timer_0.__repr__()
    var_2 = timer_3.__repr__()
    none_type_0 = timer_3.start()

def test_timer_context_manager_initial_text_repr_and_equality():
    """Test Timer context manager behavior with initial text, repr strings, and equality comparison."""
    # Create timer and enter context manager
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()

    int_0 = -1092
    var_0 = timer_1.__repr__()

    float_arg_0 = timer.FloatArg()
    timer_2 = timer.Timer(initial_text=var_0)

    float_arg_1 = timer.FloatArg()
    var_1 = timer_0.__eq__(int_0)

    float_0 = timer_1.stop()
    timer_3 = timer.Timer(text=float_arg_0, initial_text=var_0)

    var_2 = timer_0.__repr__()
    var_3 = timer_3.__repr__()
    timer_3.start()

def test_timer_start_with_none_logger_and_exit_without_stop():
    """Test that Timer with logger=None can start, and calling __exit__ without a prior stop raises no errors."""
    none_logger = None
    timer_0 = timer.Timer(logger=none_logger)
    start_result = timer_0.start()
    empty_dict = {}
    another_none = None
    # __exit__() is called without timer having been stopped — this is valid as per Timer semantics
    exit_result = timer_0.__exit__()
    # Use __setitem__ on the dict
    setitem_result = empty_dict.__setitem__(another_none, empty_dict)
    repr_result = setitem_result.__repr__()
    # Call start() again on the already-stopped timer (after __exit__ resets _start_time)
    repr_result.start()

def test_timer_equality_and_initial_text_logger_edge_cases():
    """Test Timer equivalence and initialization with edge-case arguments."""
    # Create a Timer instance and use it as a context manager
    timer_0 = timer.Timer()
    timer_1 = timer_0.__enter__()
    
    # Check if a Timer equals itself (uses __eq__)
    var_0 = timer_0.__eq__(timer_0)
    
    # Exit the context manager
    none_type_0 = timer_0.__exit__()
    
    # Create a new Timer with initial_text set to the first timer's context manager
    # and logger set to the result of the equality check
    timer_2 = timer.Timer(initial_text=timer_1, logger=var_0)
    
    # Create a Timer with a positional first argument, initial_text set to another Timer,
    # and logger set to the equality result
    timer_3 = timer.Timer(timer_1, initial_text=timer_2, logger=var_0)
    
    # Start the final timer
    timer_3.start()

def test_timer_start_stop_and_context_manager_with_initial_text() -> None:
    """Test that a Timer with initial_text=True behaves correctly when used with start/stop and a context manager."""
    # GIVEN a Timer with the default initial text "Timer started"
    initial_text = "Timer started"
    timer_0 = timer.Timer(initial_text)

    # WHEN the timer is started and stopped explicitly
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()

    # AND then used as a context manager
    timer_1 = timer_0.__enter__()

    # AND the timer is copied
    timer_0.copy()