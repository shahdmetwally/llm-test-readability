import pytest
import packages as packages

def test_version_part_default_instantiation():
    """Test that _VersionPart can be instantiated with no arguments without raising an error."""
    # Verify default construction of _VersionPart succeeds
    packages._VersionPart()

