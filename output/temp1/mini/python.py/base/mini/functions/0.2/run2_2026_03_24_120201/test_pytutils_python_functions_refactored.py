import pytest

import python as python_module

def test_instantiates_pyinfo():
    """Verify that PyInfo can be constructed without raising an exception."""
    # Instantiate the PyInfo object from the python_module alias.
    py_info = python_module.PyInfo()
    assert py_info is not None

