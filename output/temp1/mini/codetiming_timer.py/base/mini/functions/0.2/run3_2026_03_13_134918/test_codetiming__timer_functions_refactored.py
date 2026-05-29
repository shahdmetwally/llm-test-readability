import pytest

import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Ensure TimerError can be constructed without raising an exception."""
    # Instantiate TimerError from the codetiming_timer alias to verify construction.
    timer_error = timer.TimerError()
    assert isinstance(timer_error, timer.TimerError)

def test_timer_context_and_redundant_start_sequence():
    """Exercise entering/exiting a Timer and then starting it twice (preserves original call sequence)."""
    # Create a Timer instance from the imported module alias `timer`
    timer_instance = timer.Timer()

    # Enter the timer context (this calls start()) and capture the returned object
    entered_timer = timer_instance.__enter__()

    # Exit the timer context (this calls stop())
    exit_result = timer_instance.__exit__()

    # Start the timer again via the object returned by __enter__()
    start_result_via_entered = entered_timer.start()

    # Start the timer once more using the original instance (preserves original behavior/order)
    second_start_result = timer_instance.start()

def test_timer_context_manager_enter_and_exit_methods():
    """Call the context-manager methods directly to ensure they execute without error."""
    # Create a Timer instance
    timer_instance = timer.Timer()
    # Simulate entering the context manager (starts the timer)
    entered = timer_instance.__enter__()
    # Simulate exiting the context manager (stops the timer); no exception info passed
    exit_result = timer_instance.__exit__()

def test_timer_exit_called_directly():
    """Smoke test: instantiate related objects and call Timer.__exit__ directly."""
    # Create a FloatArg instance (unused in this test, preserved from original)
    dummy_float_arg = timer.FloatArg()
    # Create a TimerError instance (unused, preserved from original)
    timer_error_instance = timer.TimerError()
    # Create a Timer instance and call its __exit__ method without arguments
    timer_instance = timer.Timer()
    timer_instance.__exit__()

def test_timer_start_with_no_logger_then_call_enter_on_setitem_result():
    """Start a Timer with logger=None, create a self-referential dict via __setitem__,
    and call __enter__ on the result (preserving the original behavior)."""
    # Create a Timer with logger explicitly set to None and start it
    timer_instance = timer.Timer(logger=None)
    start_result = timer_instance.start()

    # Create an empty dict and set its None key to reference itself.
    # dict.__setitem__ returns None (the original test captured that return value).
    self_ref_dict = {}
    setitem_result = self_ref_dict.__setitem__(None, self_ref_dict)

    # Invoke __enter__ on the result of __setitem__ (which is None) to preserve original execution.
    # This mirrors the original test's call sequence exactly.
    setitem_result.__enter__()

def test_timer_context_and_methods_combination():
    """
    Verify interactions between Timer context enter/stop, equality, repr, and start
    while using FloatArg instances for the text argument.
    """
    # Create a base Timer and enter its context (calls __enter__())
    main_timer = timer.Timer()
    cm_timer = main_timer.__enter__()  # context-manager Timer (returned by __enter__)

    # Use a negative integer to exercise __eq__ with a non-Timer value
    negative_value = -1092

    # Create FloatArg instances used as callable/text arguments
    float_arg_a = timer.FloatArg()
    float_arg_b = timer.FloatArg()

    # Create another Timer using the context-manager Timer as initial_text
    timer_with_initial_from_cm = timer.Timer(initial_text=cm_timer)

    # Call __eq__ on the original timer with the negative integer
    equality_result = main_timer.__eq__(negative_value)

    # Stop the context-manager timer and capture the elapsed time
    elapsed_from_cm = cm_timer.stop()

    # Create a Timer that uses a FloatArg for text and the equality result as initial_text
    timer_with_callable_text = timer.Timer(text=float_arg_a, initial_text=equality_result)

    # Capture string representations via __repr__()
    repr_main = main_timer.__repr__()
    repr_third = timer_with_callable_text.__repr__()

    # Start the third timer (calls start())
    start_result = timer_with_callable_text.start()

def test_timer_context_manager_repr_and_start_stop_and_equality():
    """Exercise Timer context enter/exit, repr, equality, and construction with initial text."""
    # Create a base Timer and explicitly enter it as a context manager (starts the timer)
    root_timer = timer.Timer()
    ctx_timer = root_timer.__enter__()  # equivalent to using 'with', starts timer

    # Use a negative integer to test equality against the Timer object
    negative_value = -1092

    # Capture the representation of the timer while it's running
    repr_running = ctx_timer.__repr__()

    # Create FloatArg instances used as text arguments when constructing timers
    float_arg_a = timer.FloatArg()
    float_arg_b = timer.FloatArg()

    # Construct a Timer using the captured repr_running as initial_text
    timer_with_initial_repr = timer.Timer(initial_text=repr_running)

    # Test equality comparison of the root timer with an integer
    eq_result = root_timer.__eq__(negative_value)

    # Stop the context-managed timer and capture the elapsed time
    elapsed = ctx_timer.stop()

    # Construct another Timer with a text FloatArg and the same initial_text repr
    timer_with_text_and_initial = timer.Timer(text=float_arg_a, initial_text=repr_running)

    # Capture representations after stop and for the new timer
    repr_after_stop = root_timer.__repr__()
    repr_timer3 = timer_with_text_and_initial.__repr__()

    # Start the newly constructed timer
    timer_with_text_and_initial.start()

def test_timer_start_exit_then_dict_setitem_with_none_and_call_start():
    """Exercise Timer.start/exit with a None logger and then call .start() on the None result
    returned by dict.__setitem__ to reproduce the original AttributeError flow.
    """
    # Construct Timer with an explicit None logger
    logger_none = None
    timer_inst = timer.Timer(logger=logger_none)

    # Start the timer (start() returns None)
    start_result = timer_inst.start()

    # Prepare a mapping and a None key
    mapping = {}
    none_key = None

    # Call __exit__ on the timer (no arguments)
    exit_result = timer_inst.__exit__()

    # dict.__setitem__ returns None; capture that None
    setitem_result = mapping.__setitem__(none_key, mapping)

    # Calling __repr__ on None is valid (yields 'None')
    repr_result = setitem_result.__repr__()

    # Reproduce the original final call: attempt to call .start() on None
    setitem_result.start()

def test_timer_enter_exit_and_construction_with_unusual_arguments():
    """Exercise Timer's context methods and construction using non-string arguments.

    This test intentionally calls dunder methods and constructs timers with objects
    (the Timer instance and booleans) passed to parameters like initial_text and
    logger to ensure those call paths execute without raising.
    """
    # Create a Timer instance
    first_timer = timer.Timer()

    # Explicitly enter the timer (returns self)
    entered_timer = first_timer.__enter__()

    # Use the equality dunder to produce a logger-like boolean value
    equality_result = first_timer.__eq__(first_timer)

    # Explicitly exit the timer (no args)
    exit_result = first_timer.__exit__()

    # Create a Timer using the entered_timer object as initial_text and the equality_result as logger
    second_timer = timer.Timer(initial_text=entered_timer, logger=equality_result)

    # Create another Timer using entered_timer as the positional name argument,
    # second_timer as the initial_text, and the same logger flag
    third_timer = timer.Timer(entered_timer, initial_text=second_timer, logger=equality_result)

    # Start the third timer to exercise start() behavior
    third_timer.start()

def test_timer_start_stop_enter_and_copy():
    """Exercise Timer.start(), Timer.stop(), __enter__(), and copy() in sequence."""
    initial_text = "Timer started"
    timer_instance = timer.Timer(initial_text)

    # Start and stop the timer
    start_result = timer_instance.start()
    stop_result = timer_instance.stop()

    # Enter the context manager and copy the timer
    entered_timer = timer_instance.__enter__()
    timer_instance.copy()

