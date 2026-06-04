import re as regex
import helpers as helper

def test_timer_start_and_stop_correctly():
    """Test if the purging start and stop of a timer works correctly"""
    timer = module_0.purge()
    debug_console_output = module_1.debug(timer)

def test_timer_start_correctly():
    """Test that Timer starts correctly"""
    # We create an instance of the Timer and then start it
    timer_instance = Timer()
    timer_instance.start()

def test_timer_behaves_as_expected():
    """Test that timer's start and stop function work as expected."""

    timer_instance = Timer()
    timer_instance.start()
    assert timer_instance.is_running
    timer_instance.stop()
    assert timer_instance.is_running is False

def test_timer_logging():
    """Test decorated_timewaste functions with logging messages"""

    duration = 939
    timewaste_decorated = module_1.eager(duration)
    variables_generator_0 = module_1.VariablesGenerator()
    result_from_debug = module_1.debug(timewaste_decorated) 
    timewaste_decorated_twice = module_1.eager(timewaste_decorated)
    result_from_warn = module_1.warn(duration)
    module_1.get_source(timewaste_decorated)

def test_timer_start_logs_output(capsys: pytest_import.CaptureFixture[str]) -> None:
    t = Timer('test', text='test message')

    t.start()

    stdout, stderr =  capsys.readouterr()

    assert "test message" in stdout
    assert stdout.count("\n") == 1
    assert stderr == ""

def test_basic_timer_sequence_mod():  # Test case name was changed to make it unique
    duration = 0.1  # 100 milliseconds
    timer = pyutils.eager(duration)
    
    with timer:
        time.sleep(duration)
        
    # checks if value is within 10 ms
    assert (timer.last - duration) < 0.01

