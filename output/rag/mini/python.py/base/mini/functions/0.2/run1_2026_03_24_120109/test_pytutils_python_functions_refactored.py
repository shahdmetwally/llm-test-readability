import pytest

import python as python_module

def test_pyinfo_can_be_instantiated():
    """Ensure PyInfo can be instantiated and returns an instance of the expected type."""
    py_info = python_module.PyInfo()
    assert isinstance(py_info, python_module.PyInfo)

