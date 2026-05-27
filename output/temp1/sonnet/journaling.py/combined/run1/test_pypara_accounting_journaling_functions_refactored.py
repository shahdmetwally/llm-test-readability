import pytest
import journaling as journaling

def test_read_journal_entries_instantiates_without_error():
    """Tests that ReadJournalEntries can be called without raising an exception."""
    # Invoke ReadJournalEntries to verify it runs successfully with no errors
    journaling.ReadJournalEntries()

def test_journal_entry_validate_returns_none_when_all_fields_are_none():
    """Test that JournalEntry.validate() returns None when instantiated with all None fields."""
    # Use None for all constructor arguments to represent an empty/uninitialized entry
    none_value = None

    # Create a JournalEntry with all fields set to None
    journal_entry = journaling.JournalEntry(none_value, none_value, none_value)

    # Validate the entry and capture the result (expected to be None)
    validation_result = journal_entry.validate()