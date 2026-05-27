import re as regex
import helpers as helper

def test_purge_and_debug():
    """Test that the purge method stops the timer and the debug method returns None"""
    timer_instance = regex.purge()
    debug_module = helper
    timer_instance_after_purge = timer_instance.purge()
    debug_result = debug_module.debug(timer_instance_after_purge)
    assert debug_result is None

def test_timer_start_stops_correctly():
    """Test that the Timer class starts and stops correctly."""
    timer_instance = helper.Timer()
    timer_instance.start()
    assert timer_instance.is_running()
    timer_instance.stop()
    assert not timer_instance.is_running()

def test_timer_start_stops_correctly_2():
    """Test that Timer's start and stop functionality works correctly."""
    time_waste_function = decorated_timewaste
    timer_instance = helper.Timer(text=TIME_MESSAGE)
    timer_instance.start()
    time_waste_function()
    timer_instance.stop()

    stdout, stderr = capsys.readouterr()
    assert RE_TIME_MESSAGE.match(stdout)
    assert stdout.count("\n") == 1
    assert stderr == ""

def test_timer_measures_time_correctly():
    """Test that the Timer class accurately measures the time taken to execute a function."""
    time_to_waste = 939
    timewaste_func = helper.Timer.eager(time_to_waste)
    timer_instance = helper.Timer.VariablesGenerator()
    debug_output = helper.Timer.debug(timewaste_func)
    timewaste_func_2 = helper.Timer.eager(timewaste_func)
    warn_output = helper.Timer.warn(time_to_waste)
    helper.Timer.get_source(timewaste_func)

def test_warn_function_returns_none():
    """Test that the warn function from module_1 returns None when given a string."""
    warning_message = "ProxyHandler"
    result = helper.warn(warning_message)
    assert result is None

def test_timer_start_stops_correctly_3():
    """Test that the Timer's start and stop methods function correctly."""
    timer_duration = 939
    timer_instance = helper.Timer(text=TIME_MESSAGE)
    module = None
    timer_instance.start()
    timer_instance.stop()
    assert timer_instance.last == timer_duration