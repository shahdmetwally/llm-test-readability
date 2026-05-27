import pytest
import packages as packages_module

def test_version_part_instantiation():
    """Test that _VersionPart can be instantiated without error."""
    packages_module._VersionPart()  # This should not raise an exception

