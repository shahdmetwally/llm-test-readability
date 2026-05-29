import pytest

import codetiming_timer as timer

def test_timer_error_instantiation_succeeds() -> None:
    """Ensure TimerError can be instantiated and is an instance of TimerError."""
    timer_error = timer.TimerError()
    assert isinstance(timer_error, timer.TimerError)

def test_timer_enter_exit_and_start_sequence():
    """Smoke test: call Timer.__enter__, Timer.__exit__, then start twice in the same sequence as the original test."""
    # Create a Timer instance
    timer_instance = timer.Timer()

    # Enter the context manager (calls __enter__ and returns the timer)
    context_timer = timer_instance.__enter__()

    # Exit the context manager (calls __exit__)
    exit_result = timer_instance.__exit__()

    # Start the timer using the object returned by __enter__()
    start_result_1 = context_timer.start()

    # Start the original timer instance again (preserves original call order)
    start_result_2 = timer_instance.start()

def test_timer_context_manager_enter_and_exit_sequence():
    """Verify a Timer can be entered and exited using the context manager protocol."""
    # Create a Timer instance and invoke the context manager protocol methods directly.
    timer_obj = timer.Timer()
    # Simulate entering the context manager (calls __enter__).
    entered = timer_obj.__enter__()
    # Simulate exiting the context manager (calls __exit__); no exception info provided.
    exited = timer_obj.__exit__()
    # Test succeeds if no exceptions are raised during enter/exit.

def test_timer_exit_can_be_called_directly():
    """Call Timer.__exit__ directly on a fresh Timer instance (no context manager)."""
    # Create a FloatArg instance (mirrors original setup; not otherwise used)
    float_arg = timer.FloatArg()

    # Instantiate a TimerError (mirrors original setup; not otherwise used)
    timer_error = timer.TimerError()

    # Create a Timer instance and invoke its __exit__ method directly
    timer_instance = timer.Timer()
    timer_instance.__exit__()

def test_timer_start_with_none_logger_and_invalid_enter_call():
    """Create a Timer with logger=None, start it, then call __enter__() on the return
    value of dict.__setitem__ (which is None) to reproduce the original behavior."""
    # Explicitly use None as the logger
    logger_none = None

    # Construct the Timer with logger=None
    timer_instance = timer.Timer(logger=logger_none)

    # Start the timer (return value intentionally ignored in original test)
    start_result = timer_instance.start()

    # Create a dictionary and set it to contain itself at key None.
    # dict.__setitem__ returns None.
    container = {}
    key_none = None
    setitem_result = container.__setitem__(key_none, container)

    # Attempt to call __enter__ on the result of __setitem__ (None).
    # This reproduces the original behavior (will raise AttributeError at runtime).
    setitem_result.__enter__()

def test_timer_context_manager_and_methods_with_various_args():
    """Exercise Timer context-management and instance methods with varied arguments."""
    # Create a base Timer instance and enter it as a context manager
    root_timer = timer.Timer()
    ctx_timer = root_timer.__enter__()

    # Prepare a negative integer used for an equality check
    negative_value = -1092

    # Create FloatArg instances used as 'text' arguments for Timer
    float_arg_a = timer.FloatArg()
    float_arg_b = timer.FloatArg()

    # Create another Timer using the context manager object as initial_text
    timer_with_initial_from_ctx = timer.Timer(initial_text=ctx_timer)

    # Perform an equality comparison using __eq__
    equality_result = root_timer.__eq__(negative_value)

    # Stop the context timer and capture the elapsed time
    elapsed_time = ctx_timer.stop()

    # Create a Timer using a FloatArg for text and the equality result as initial_text
    timer_with_text_and_initial = timer.Timer(text=float_arg_a, initial_text=equality_result)

    # Capture __repr__ outputs
    repr_root = root_timer.__repr__()
    repr_other = timer_with_text_and_initial.__repr__()

    # Start the newly created timer (expected to return None)
    start_result = timer_with_text_and_initial.start()

def test_timer_context_manager_repr_eq_and_start_stop():
    """Exercise Timer context-manager enter/stop, repr, equality, and start with FloatArg/text/initial_text."""
    # Create a root Timer and enter it like a context manager
    root_timer = timer.Timer()
    ctx_timer = root_timer.__enter__()

    # Preserve an integer literal (should remain unchanged)
    negative_value = -1092

    # Capture string representation of the context timer
    ctx_repr = ctx_timer.__repr__()

    # Create FloatArg placeholders for use as text arguments
    float_arg_a = timer.FloatArg()
    float_arg_b = timer.FloatArg()  # kept for parity with original flow

    # Create another Timer using the captured repr as initial_text
    timer_with_initial_text = timer.Timer(initial_text=ctx_repr)

    # Call equality comparator on the root timer with an integer
    eq_result = root_timer.__eq__(negative_value)

    # Stop the context timer and record the elapsed time returned
    stopped_elapsed = ctx_timer.stop()

    # Create a Timer with text set to a FloatArg and the same initial_text
    timer_with_text_and_initial = timer.Timer(text=float_arg_a, initial_text=ctx_repr)

    # Capture represenations after operations
    root_repr_after = root_timer.__repr__()
    t3_repr = timer_with_text_and_initial.__repr__()

    # Start the last timer instance
    timer_with_text_and_initial.start()

def test_timer_logger_none_sequence_of_calls():
    """Exercise Timer with logger=None and repeat the original sequence of calls exactly."""
    # Use a None logger to emulate the original test input
    logger_none = None

    # Create a Timer instance with logger=None
    timer_instance = timer.Timer(logger=logger_none)

    # Start the timer (original test stored the return value)
    start_result = timer_instance.start()

    # Prepare an empty dictionary as in the original test
    some_dict = {}

    # Use None as the key just like the original test
    key_none = None

    # Call __exit__() on the timer instance (no args), preserving original call
    exit_result = timer_instance.__exit__()

    # Call dict.__setitem__(None, dict) and store its (None) return value
    setitem_result = some_dict.__setitem__(key_none, some_dict)

    # Call __repr__ on the result of __setitem__ (preserves original behavior)
    repr_result = setitem_result.__repr__()

    # Finally attempt to call start() on the result of __setitem__ (preserves original behavior/order)
    setitem_result.start()

def test_timer_enter_exit_and_start_with_initial_text_and_logger_interaction() -> None:
    """Exercise enter/exit, equality, and start with various initial_text/logger combinations."""
    # Create a base Timer and manually enter the context (calls __enter__())
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()  # returned value from __enter__ (typically the Timer itself)

    # Perform an equality check against itself to obtain a boolean value
    is_equal_to_self = base_timer.__eq__(base_timer)

    # Call __exit__() to simulate exiting the context manager
    exit_result = base_timer.__exit__()

    # Use previous results as constructor arguments to exercise parameter handling
    timer_with_initial_and_logger = timer.Timer(initial_text=entered_timer, logger=is_equal_to_self)
    timer_with_name_initial_and_logger = timer.Timer(
        entered_timer, initial_text=timer_with_initial_and_logger, logger=is_equal_to_self
    )

    # Start the final timer to exercise start() behavior
    timer_with_name_initial_and_logger.start()

def test_timer_start_stop_enter_and_copy_calls():
    """Exercise Timer start, stop, context enter, and copy methods in sequence."""
    # Initial text passed to the Timer constructor (kept exactly as in the original)
    initial_text = "Timer started"

    # Construct the Timer instance
    timer_instance = timer.Timer(initial_text)

    # Start the timer (original code assigned the result; keep the assignment)
    start_result = timer_instance.start()

    # Stop the timer and capture the elapsed time (original assignment preserved)
    elapsed_time = timer_instance.stop()

    # Enter the timer context (calls __enter__); preserve original call and assignment
    entered_timer = timer_instance.__enter__()

    # Call the copy method as in the original test (no assertion, just ensure the call exists)
    timer_instance.copy()

