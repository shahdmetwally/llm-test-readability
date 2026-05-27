import pytest
import codetiming as timer

def test_version_part_initialization():
    """
    Tests if the version part object is initialized correctly.
    """
    version_part = timer._VersionPart()