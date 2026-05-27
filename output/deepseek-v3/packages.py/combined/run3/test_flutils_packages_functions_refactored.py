import pytest
import packages as packages_module

def test_version_part_can_be_instantiated():
    """Test that _VersionPart class can be instantiated successfully."""
    # Instantiate _VersionPart to verify it doesn't raise any errors
    packages_module._VersionPart()

