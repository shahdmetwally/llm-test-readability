import pytest
import packages as packages_module

def test_version_part_can_be_instantiated():
    """Test that the _VersionPart class can be instantiated without errors."""
    packages_module._VersionPart()

