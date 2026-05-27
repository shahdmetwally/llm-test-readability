import pytest
import packages as packages

def test_version_part_default_instantiation():
    """Test that _VersionPart can be instantiated with no arguments without raising an error."""
    # Construct _VersionPart with default arguments; no exception should be raised
    packages._VersionPart()

