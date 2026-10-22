import pytest
import journaling as journa
from codetiming import Timer
import re

def test_timer_class_accurately_measures_time_and_stops_correctly():
    """Test that Timer class accurately measures time and stops correctly."""
    timer_instance = Timer(name="accumulator", text=TIME_MESSAGE)
    accumulated_timewaste(1000)
    assert_format = lambda message, timer: f"Elapsed time: {timer.last_time:0.4f} seconds"
    assertion = assert_format(TIME_MESSAGE, timer_instance)
    assert re.match(RE_TIME_MESSAGE, str(timer_instance)), f"Unexpected timer output. Expected: {TIME_MESSAGE}, Got: {assertion}"
    
    # Testing that the timer is stopped and can't be started again.
    with pytest.raises(TimerError):
        timer_instance.start()
    timer_instance.stop()

def test_journal_entry_validation_with_None_values():
    none_type_value = None
    entry = journa.JournalEntry(none_type_value, none_type_value, none_type_value)
    validated_entry_value = entry.validate()
    assert validated_entry_value is None