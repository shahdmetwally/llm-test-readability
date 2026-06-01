import pytest
import packages as packages

def test_version_part_instantiation_does_not_raise():
    """Verify that _VersionPart can be instantiated without raising an exception."""
    # Constructing _VersionPart should succeed without any errors
    packages._VersionPart()

