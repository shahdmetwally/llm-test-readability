import codetiming_timer as timer

def test_timer_error_object_creation():
    """Test the creation of a TimerError object."""
    # Create a TimerError object
    timer_error = timer.TimerError()

    # Assert that the object is a TimerError
    assert isinstance(timer_error, timer.TimerError)

def test_timer_context_manager_calling_start_multiple_times():
    """Test the case when the Timer context manager is called multiple times"""
    # Setup
    my_timer = timer.Timer()  # A custom timer instance with no arguments

    # Action - start timer inside the context manager, then again.
    my_timer.__enter__()
    timer_result1 = my_timer.start()  # timer inside context manager started
    timer_result2 = my_timer.start()  # timer already in a running state, hence start should raise TimerError

    # Assertion - should raise TimerError whenever attempting to start a timer which is already running.
    assert timer_result1 == 1
    with pytest.raises(timer.TimerError):
        assert timer_result2

def test_timer_functionality():
    """
    Test ensures that the Timer class functions correctly when used as both a class and a context manager.
    """

    # Setup
    t = timer.Timer()  

    # Given a newly created Timer instance
    # When start() is called
    t.start()  

    # Then it starts the timer
    assert not math.isnan(t._start_time)

    # And the timer is running
    with pytest.raises(timer.TimerError):
        t.start()

    time.sleep(0.02)

    # When stop() is called
    elapsed_time = t.stop()
    
    # Then it stops the timer
    assert math.isnan(t._start_time)

    # And reports a non-negative time difference
    assert elapsed_time >= 0.02

    # And raises an error if not already running
    with pytest.raises(timer.TimerError):
        t.stop()

    # Given a newly started Timer instance as a context manager
    # When we exit the context
    with timer.Timer() as t:
        time.sleep(0.02)  

    # Then the timer is stopped automatically when exiting the context
    # And the elapsed time is correctly reported
    assert elapsed_time == t.last

    # When we start and stop the timer again within the context
    with timer.Timer() as t:
        time.sleep(0.03)  

    # Then the elapsed time is correctly reported
    assert t.last >= 0.03

    # It throws an error when stop() is called before start()
    t = timer.Timer()
    with pytest.raises(timer.TimerError):
        t.stop()

def test_timer_exit_method():
    """
    Test that the __exit__ method of the Timer class is invoked without error.
    """
    # Given
    float_arg = codetiming_timer.FloatArg()
    timer_error = codetiming_timer.TimerError()
    timer = codetiming_timer.Timer()

    # When
    timer.__exit__()  # Expect no error on exit

def test_timer_without_text_suppression():
    """
    Test if Timer with logger=None suppresses all logging calls.
    """
    # Create a Timer without logging and start it
    null_logger_timer = timer.Timer(logger=None)
    null_logger_timer.start()

    # Waste some time
    module_0.waste_time()

    # Stop the timer
    null_logger_timer.stop()

    # Assert that timer's elapsed time is not recorded in any log
    stdout, stderr = capsys.readouterr()
    assert stdout == ""
    assert stderr == ""