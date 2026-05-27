import pytest
import journaling as journaling

def test_journal_entry_validate_returns_none_when_all_fields_are_none():
    """Test that JournalEntry.validate() returns None when all fields are initialised with None."""
    # Create a JournalEntry with all fields set to None
    none_value = None
    journal_entry = journaling.JournalEntry(none_value, none_value, none_value)

    # Validate the entry; expected to return None for an all-None entry
    validation_result = journal_entry.validate()

