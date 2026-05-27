import pytest

import packages as packages_module

def test_version_part_initializes_successfully():
    """Ensure packages_module._VersionPart() constructs successfully without raising an exception."""
    version_part_instance = packages_module._VersionPart()
    assert version_part_instance is not None

