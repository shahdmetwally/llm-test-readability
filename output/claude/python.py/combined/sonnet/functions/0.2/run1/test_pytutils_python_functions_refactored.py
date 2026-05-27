import pytest
import python as python_module

def test_pyinfo_instantiation_succeeds():
    """Test that PyInfo can be instantiated without raising an exception."""
    # Construct a PyInfo instance; no exception should be raised
    py_info_instance = python_module.PyInfo()

