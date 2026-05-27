import codetiming_timer as timer

def test_timer_error_creation():
    # Given
    expected_error = timer.TimerError()

    # When
    actual_error = timer.TimerError()

    # Then
    assert isinstance(actual_error, Exception)
    assert type(actual_error) == type(expected_error)
    assert str(actual_error) == str(expected_error)

def test_timer_start_and_stop():
    """
    Test that a Timer can be started and stopped.
    """
    # Create a Timer instance
    t = timer.Timer()

    # Enter the context manager
    t_context = t.__enter__()

    # Exit the context manager
    t.__exit__()

    # Start the timer within the context manager
    t_context.start()

    # Start the timer outside the context manager
    t.start()

def test_timer_enter_and_exit():
    """
    Test that Timer can be used as a context manager.
    """
    # Given a Timer instance
    timer = Timer()

    # When the Timer is used as a context manager
    with timer:
        # Then the Timer should start
        assert timer._start_time is not None

    # And the Timer should stop
    assert timer._start_time is None

def test_timer_exit_method():
    """
    Test that Timer.__exit__ method does not raise an exception.
    """
    # Given
    float_arg = timer.FloatArg()
    timer_error = timer.TimerError()
    t = timer.Timer()

    # When
    try:
        t.__exit__()
    except Exception:
        assert False, "Timer.__exit__ method raised an exception."
    else:
        assert True

def test_timer_without_text_logging():
    """
    Test that timer with logger=None does not print anything.
    """
    # Create a timer with logger=None
    timer_without_text = timer.Timer(logger=None)

    # Start the timer
    timer_without_text.start()

    # Waste some time
    waste_time()

    # Stop the timer
    timer_without_text.stop()

    # Capture the output
    stdout, stderr = capsys.readouterr()

    # Assert that no output was produced
    assert stdout == ""
    assert stderr == ""

def test_timer_enter_and_exit():
    # Given
    timer_0 = timer.Timer()

    # When
    timer_1 = timer_0.__enter__()
    timer_2 = timer.Timer(initial_text=timer_1)
    timer_3 = timer.Timer(text=float_arg_0, initial_text=var_0)

    # Then
    assert timer_0.__eq__(int_0)
    assert timer_1.stop()
    assert timer_0.__repr__()
    assert timer_3.__repr__()
    assert timer_3.start() is None

def test_timer_enter_and_exit_1():
    """Test that the timer can be used as a context manager."""
    # Given
    timer_0 = timer.Timer()

    # When
    with timer_0 as timer_1:
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

def test_timer_start_and_exit_1():
    """
    Test that the Timer class can start and exit without errors.
    """
    # Create a Timer instance with a None logger
    timer = timer.Timer(logger=None)

    # Start the timer and store the result
    start_result = timer.start()

    # Create an empty dictionary
    dict_0 = {}

    # Exit the timer and store the result
    exit_result = timer.__exit__()

    # Set an item in the dictionary and store the result
    setitem_result = dict_0.__setitem__(None, dict_0)

    # Get a string representation of the setitem_result and store it
    repr_result = setitem_result.__repr__()

    # Attempt to start the timer again
    timer.start()

def test_timer_enter_exit_and_equality_check():
    """Test the Timer's __enter__, __exit__ and __eq__ methods."""
    # Given
    timer_0 = module_0.Timer()

    # When
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__eq__(timer_0)
    none_type_0 = timer_0.__exit__()

    # Then
    assert var_0 is True
    assert none_type_0 is None

    # Given
    timer_2 = timer_0.Timer(initial_text=timer_1, logger=var_0)
    timer_3 = timer_0.Timer(timer_1, initial_text=timer_2, logger=var_0)

    # When
    timer_3.start()

    # Then
    assert timer_3.last >= 0.0

def test_timer_start_and_stop():
    """Test that Timer starts and stops correctly."""
    # Given
    timer_name = "Timer started"
    timer = timer.Timer(timer_name)  # Timer instance

    # When
    none_type = timer.start()  # Start the timer
    float_value = timer.stop()  # Stop the timer

    # Then
    assert none_type is None  # Check that start() returns None
    assert isinstance(float_value, float)  # Check that stop() returns a float

def test_timer_context_manager():
    """Test that Timer works as a context manager."""
    # Given
    timer_name = "Timer started"
    timer = timer.Timer(timer_name)  # Timer instance

    # When
    with timer as timer_context:  # Use timer as a context manager
        timer_copy = timer_context.copy()  # Copy the timer

    # Then
    assert isinstance(timer_context, timer.Timer)  # Check that the context manager returns a Timer instance
    assert isinstance(timer_copy, timer.Timer)  # Check that copy() returns a Timer instance

