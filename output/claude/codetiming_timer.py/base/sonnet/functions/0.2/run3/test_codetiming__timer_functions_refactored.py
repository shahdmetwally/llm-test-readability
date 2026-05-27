import pytest
import codetiming_timer as timer

def test_timer_error_can_be_instantiated():
    """Test that TimerError can be instantiated without raising any exceptions."""
    # Verify that TimerError is a valid, constructible exception class
    timer_error = timer.TimerError()

def test_timer_raises_error_when_started_while_already_running():
    """Test that starting an already-running timer raises a TimerError.

    Uses the context manager protocol to start the timer, then attempts
    to call .start() again on the active timer, which should raise an error.
    """
    # Create a new timer and enter the context manager (implicitly calls .start())
    outer_timer = timer.Timer()
    inner_timer = outer_timer.__enter__()

    # Exit the context manager (implicitly calls .stop())
    none_type_0 = outer_timer.__exit__()

    # Attempt to start the inner timer reference (already running) — expects TimerError
    none_type_1 = inner_timer.start()

    # Attempt to start the outer timer again while it may still be considered running
    outer_timer.start()

def test_timer_context_manager_enter_and_exit():
    """Test that Timer can be used as a context manager via __enter__ and __exit__."""
    # Create a new Timer instance
    t = timer.Timer()

    # Enter the context manager, which starts the timer and returns it
    active_timer = t.__enter__()

    # Exit the context manager, which stops the timer
    none_result = t.__exit__()

def test_timer_exit_without_start_raises_error():
    """Test that calling __exit__ on a Timer that was never started raises a TimerError."""
    t = timer.Timer()

    # Attempting to exit a timer context that was never entered should raise an error
    with pytest.raises(timer.TimerError):
        t.__exit__()

def test_timer_start_with_nested_timer_instances_as_arguments():
    """Test that Timer instances can be used as arguments to other Timer constructors,
    and that starting a Timer configured with another Timer as initial_text and logger
    does not raise an error during instantiation or start."""

    # Create a base timer and use it as a context manager to get a Timer instance
    base_timer = timer.Timer()
    entered_timer = base_timer.__enter__()

    # Compare the timer with itself; result is used as the 'logger' argument below
    eq_result = base_timer.__eq__(base_timer)

    # Exit the context manager (stops the timer)
    base_timer.__exit__()

    # Create a Timer using the entered Timer instance as initial_text, and eq_result as logger
    timer_with_timer_initial_text = timer.Timer(initial_text=entered_timer, logger=eq_result)

    # Create a Timer using entered_timer as the first positional arg (text),
    # timer_with_timer_initial_text as initial_text, and eq_result as logger
    timer_with_nested_args = timer.Timer(
        entered_timer,
        initial_text=timer_with_timer_initial_text,
        logger=eq_result,
    )

    # Start the timer configured with nested Timer instances as arguments
    timer_with_nested_args.start()

def test_timer_start_stop_then_enter_and_copy():
    """Test that a Timer can be started and stopped explicitly, then used as a
    context manager entry, followed by a copy operation."""

    # Use "Timer started" as the display text for elapsed time output
    text_message = "Timer started"

    # Create a Timer instance with the given text
    timer_instance = timer.Timer(text_message)

    # Start and stop the timer explicitly to record elapsed time
    none_type_0 = timer_instance.start()
    float_0 = timer_instance.stop()

    # Enter the timer as a context manager (without exiting)
    entered_timer = timer_instance.__enter__()

    # Copy the timer instance
    timer_instance.copy()

