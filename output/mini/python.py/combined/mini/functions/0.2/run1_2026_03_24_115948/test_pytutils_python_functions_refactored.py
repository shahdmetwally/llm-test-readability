import pytest

import python as python_module

def test_pyinfo_can_be_instantiated_without_errors():
    """Instantiate PyInfo; the test passes if no exception is raised and an instance is returned."""
    # Instantiate PyInfo from the module under test.
    py_info = python_module.PyInfo()
    # Basic sanity check: an instance should be created.
    assert py_info is not None

