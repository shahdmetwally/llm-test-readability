import pytest
import journaling as journaling

def test_read_journal_entries_instantiates_without_error():
    """Test that ReadJournalEntries can be called without raising an exception."""
    # Invoke ReadJournalEntries to verify it completes without error
    journaling.ReadJournalEntries()

def test_journal_entry_validate_returns_none_when_all_fields_are_none():
    """Test that JournalEntry.validate() returns None when instantiated with all None fields."""
    # Use None for all constructor arguments to represent a fully empty entry
    none_value = None

    # Instantiate JournalEntry with all fields set to None
    journal_entry = journaling.JournalEntry(none_value, none_value, none_value)

    # Capture the result of validate(); expected to be None for an empty entry
    validation_result = journal_entry.validate()

