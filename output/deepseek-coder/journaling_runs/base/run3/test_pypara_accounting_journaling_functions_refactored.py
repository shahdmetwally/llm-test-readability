import journaling as journal

def test_read_journal_entries():
    # Given a journal file with entries
    journal_file = "test_journal.txt"
    with open(journal_file, "w") as f:
        f.write("Entry 1\nEntry 2\nEntry 3")

    # When the ReadJournalEntries function is called
    entries = journal.ReadJournalEntries(journal_file)

    # Then it should return the entries from the file
    assert entries == ["Entry 1", "Entry 2", "Entry 3"]

    # Clean up
    os.remove(journal_file)

def test_journal_entry_validate_returns_none_when_created_with_none_values():
    # Given
    none_value = None
    journal_entry = journal.JournalEntry(none_value, none_value, none_value)

    # When
    result = journal_entry.validate()

    # Then
    assert result is None