import codetiming.timer as timer

def test_timer_instance_created_correctly():
    timer_instance = timer.Timer()
    assert isinstance(timer_instance, timer.Timer)