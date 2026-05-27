import pytest
import packages as packages_module

def test__version_part_can_be_instantiated():
    """Verify that _VersionPart can be instantiated without raising an exception."""
    # Instantiate the _VersionPart class from the packages module
    version_part_instance = packages_module._VersionPart()

