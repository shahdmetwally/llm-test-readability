import pytest
import packages as packages_module

def test_version_part_can_be_instantiated():
    """Test that a _VersionPart object can be created without errors."""
    packages_module._VersionPart()

