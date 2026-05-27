import journaling as journal

def test_read_journal_entries():
    # Given
    expected_entries = ['Entry 1', 'Entry 2', 'Entry 3']

    # When
    actual_entries = journal.ReadJournalEntries()

    # Then
    assert actual_entries == expected_entries, "The entries read from the journal do not match the expected entries."

def test_journal_entry_initialized_with_none_values():
    # Given
    none_value = None
    journal_entry = journal.JournalEntry(none_value, none_value, none_value)

    # When
    validation_result = journal_entry.validate()

    # Then
    assert validation_result is None