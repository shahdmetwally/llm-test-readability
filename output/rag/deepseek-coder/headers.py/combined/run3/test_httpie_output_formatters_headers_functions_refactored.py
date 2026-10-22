import headers as headers

import pytest
from codetiming import Timer, TimerError

TIME_MESSAGE = "Wasted time: {:.4f} seconds"
RE_TIME_MESSAGE = "Elapsed time: 0\\.\\d{4} seconds"

def waste_time(num: int = 1000) -> None:
    sum(n**2 for n in range(num))

def test_timer_start_stops_correctly(capsys: pytest.CaptureFixture[str]) -> None:
    t = Timer(text=TIME_MESSAGE)
    t.start()
    waste_time()
    t.stop()

    stdout, stderr = capsys.readouterr()
    assert stdout.startswith(RE_TIME_MESSAGE)
    assert stdout.count("\n") == 1
    assert stderr == ""