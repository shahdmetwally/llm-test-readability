import pytest
import packages as packages_module

def test_cherry_pick_raises_import_error_without_attr_map():
    """Verify that _VersionPart() raises ImportError when __attr_map__ is not defined."""
    packages_module._VersionPart()

