import pytest

import python as python_module

def test_pyinfo_instantiation_creates_object():
    """Smoke test: constructing PyInfo should produce a PyInfo instance."""
    py_info = python_module.PyInfo()
    assert isinstance(py_info, python_module.PyInfo)

