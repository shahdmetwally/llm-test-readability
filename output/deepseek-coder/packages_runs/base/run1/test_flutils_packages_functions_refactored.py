import packages as pkg

def test_version_part_creation():
    """
    Test that the _VersionPart class can be instantiated without errors.
    """
    # Create an instance of _VersionPart
    version_part = pkg.moduleutils._VersionPart()

    # Assert that the instance was created successfully
    assert isinstance(version_part, pkg.moduleutils._VersionPart)

