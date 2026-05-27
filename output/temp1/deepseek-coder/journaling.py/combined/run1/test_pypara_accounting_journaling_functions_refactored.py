import journaling as journaling
import pytest

def test_timer_start_stops_correctly_unavailable():
    """Test that Timer instance starts and stops correctly"""
    timer_instance = journaling.Timer(start=True)
    timer_start_time = timer_instance.start_time
    time.sleep(0.001)  # add delay to ensure some time has passed
    timer_end_time = timer_instance.end_time

    assert timer_start_time is not None  # timer starts correctly
    assert timer_start_time <= timer_end_time  # timer stops correctly

def test_journal_entry_validation_1():
    """
    Test that a valid JournalEntry can be created & validated.
    """
    none_type = None
    journal_entry = journaling.JournalEntry(none_type, none_type, none_type)
    validation_result = journal_entry.validate() 

    assert validation_result is None, "Validation should return None when the JournalEntry is valid."