import pytest

import packages as packages_pkg

def test_version_part_instantiation_does_not_raise():
    """Ensure that constructing _VersionPart does not raise an exception."""
    # Constructing the object is the behavior under test; no further assertions needed.
    packages_pkg.module_0._VersionPart()

