import pytest
import timer

def test_create_timer_error_without_args():
    error = timer.TimerError()
    assert isinstance(error, timer.TimerError)

def test_create_timer_object():
    my_timer = timer.Timer()
    assert isinstance(my_timer, timer.Timer)

def test_timer_start_and_exit():
    my_timer = timer.Timer()
    result = my_timer.__enter__()
    assert result is None
    result = my_timer.__exit__()
    assert result is None
    
def test_timer_enter_exit_execution():
    base_timer = timer.Timer()
    timer_enter = base_timer.__enter__()
    timer_exit = base_timer.__exit__(exc_type=None, exc_value=None, traceback=None)
    assert base_timer == timer_exit
    assert timer_exit == timer_enter
    
def test_timer_exits_properly():
    float_arg_0 = timer.FloatArg()
    timer_error_0 = timer.TimerError()
    timer_0 = timer.Timer()
    assert isinstance(timer_0, timer.Timer)
    assert isinstance(float_arg_0, timer.FloatArg)
    timer_0.__exit__()
    with pytest.raises(timer_error_0):
        assert not timer_0._running

def test_timer_without_logging_does_not_output_anything():
    timer_no_logging = timer.Timer(logger=None)
    timer_no_logging.start()
    waste_time()
    timer_no_logging.stop()
    stdout, stderr = capsys.readouterr()
    assert stdout == ""
    assert stderr == ""
    
def test_timer_start_stop():
    timer_1 = timer.Timer()
    timer_1_entered = timer_1.__enter__()
    timer_2 = timer.Timer(initial_text=timer_1_entered)
    var_0 = timer_1.__eq__(timer_2)
    var_1 = timer_1.stop()
    timer_3 = timer.Timer(text=var_1)
    timer_3.start()
    repr_timer_1 = timer_1.__repr__()
    repr_timer_2 = timer_2.__repr__()
    repr_timer_3 = timer_3.__repr__()
    assert timer_1.__eq__(timer_2)
    assert timer_2.__eq__(timer_3)
    assert timer_1.__repr__() == timer_2.__repr__()
    assert timer_2.__repr__() == timer_3.__repr__()
    timer_3.start()

def test_timer_enter_start_stop_repr_eq():
    default_timer = timer.Timer()
    with default_timer as timer_1:
        str_float_0 = str(-1092.0)
        timer_repr_0 = timer_1.__repr__()
        float_arg_0 = timer.FloatArg()
        timer_2 = timer.Timer(initial_text=timer_repr_0)
        timer_2.start()
        float_arg_1 = timer.FloatArg()
        are_timer_eq_int_0 = default_timer.__eq__(int_0)
        float_0 = timer_1.stop()
        timer_3 = timer.Timer(text=float_arg_0, initial_text=timer_repr_0)
        timer_3.start()
        timer_0_repr = default_timer.__repr__()
        timer_3_repr = timer_3.__repr__()

    assert str(float_0) == "0.0"
    assert timer_0_repr == "Timer(text={0:.4f} seconds, logger=None, name=None)"
    assert timer_3_repr == "Timer(text=FloatArg(1), initial_text=-1092.0, logger=None, name=None)"
    assert are_timer_eq_int_0 == False

def test_timer_start_stop():
    timer = timer.Timer()
    timer.start()
    waste_time()
    elapsed_time = timer.stop()
    assert timer._start_time is None
    time_taken_perf_counter = time.perf_counter() - timer._start_timer
    assert abs(elapsed_time - time_taken_perf_counter) < 0.001 
    assert timer.name in timer.timers

def test_timer_context_management_and_initial_text_and_logger():
    t1 = timer.Timer()
    t2 = t1.__enter__()
    assert t1.__eq__(t1)
    none_type = t1.__exit__()
    assert none_type is None
    t3 = timer.Timer(initial_text=t2, logger=t1.__eq__(t1))
    t4 = timer.Timer(t2, initial_text=t3, logger=t1.__eq__(t1))
    t4.start()
    assert t4.__exit__() is None

def test_timer_start_and_stop():
    initial_text = "Timer started"
    timer_instance = timer.Timer(initial_text)
    timer_start = timer_instance.start()
    time_seconds = timer_instance.stop()
    assert timer_instance.__enter__() is timer_instance
    assert timer_instance.copy() is not timer_instance
    assert initial_text in capsys.readouterr().out.split('\n')
    assert f'Timer {time_seconds} seconds' in capsys.readouterr().out.split('\n')
    assert len(capsys.readouterr().out.split('\n')) == 2