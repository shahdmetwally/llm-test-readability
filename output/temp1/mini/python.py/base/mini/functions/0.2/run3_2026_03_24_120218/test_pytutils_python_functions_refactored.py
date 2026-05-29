import pytest

import python as python_module

def test_pyinfo_instantiation():
    """Verify a PyInfo object can be instantiated without error and has the correct type."""
    py_info = python_module.PyInfo()
    assert isinstance(py_info, python_module.PyInfo)

