import pytest
import headers as header_module

def test_timer_start_and_stop():
    """Test that Timer instance can be successfully started and stopped."""
    t = Timer(text=TIME_MESSAGE)
    t.start()
    assert t._start_time is not None

    time.sleep(0.1)     # Give timer some time to register time
    t.stop()
    assert t._stop_time is not None
    assert isinstance(t.last, float)
    assert t._stop_time >= t._start_time