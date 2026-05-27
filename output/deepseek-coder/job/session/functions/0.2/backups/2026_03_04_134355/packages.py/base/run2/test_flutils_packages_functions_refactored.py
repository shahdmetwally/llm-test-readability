import pytest
import codetiming_timer as timer

def test_version_part_instantiation():
    """
    This test verifies that the `_VersionPart` class can be instantiated without throwing an exception.
    """
    # Create an instance of the _VersionPart class
    version_part = timer._VersionPart()

    # Assert that the instance is of the _VersionPart class
    assert isinstance(version_part, timer._VersionPart)

