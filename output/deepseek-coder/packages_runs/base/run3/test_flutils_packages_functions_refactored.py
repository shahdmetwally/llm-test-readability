import packages as pkg

def test_version_part_creation():
    """
    Test that the _VersionPart class can be instantiated.
    """
    # Given
    version_part = pkg.moduleutils._VersionPart()

    # Then
    assert isinstance(version_part, pkg.moduleutils._VersionPart)

