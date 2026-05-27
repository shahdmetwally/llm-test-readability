import re
import journaling as log_generator
import helpers as utils

def test_read_journal_entries_function():
    """
    Test if the read journal entries function is behaving as expected
    """
    # given
    journal_entries = log_generator.ReadJournalEntries()

    # when
    result = log_generator.ReadJournalEntries()

    # then
    assert journal_entries == result

def test_journal_entry_validation():
    default_value = None

    journal_entry = log_generator.JournalEntry(default_value, default_value, default_value)

    is_valid = journal_entry.validate()

    assert is_valid == None, "Validation of JournalEntry object should be successful."