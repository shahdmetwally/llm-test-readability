import journaling as journal

def test_read_journal_entries():
    journal.ReadJournalEntries()

def test_journal_entry_validate_returns_none_when_all_fields_are_none():
    none_value = None
    journal_entry = journal.JournalEntry(none_value, none_value, none_value)
    validation_result = journal_entry.validate()
    assert validation_result is None