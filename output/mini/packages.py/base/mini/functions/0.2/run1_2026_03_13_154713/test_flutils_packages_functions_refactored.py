import pytest

import packages as packages_module

def test_instantiation_of_internal_VersionPart_does_not_raise():
    """Ensure the internal _VersionPart can be instantiated without raising an exception."""
    v = packages_module.module_0._VersionPart()
    assert v is not None

