import pytest

import python as python_module

def test_pyinfo_instantiation_creates_object():
    """Ensure PyInfo can be instantiated without raising an exception."""
    # Construct a PyInfo instance; the test passes if no exception is raised.
    py_info = python_module.PyInfo()

