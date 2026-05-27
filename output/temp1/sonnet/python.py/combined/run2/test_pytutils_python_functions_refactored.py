import pytest
import python as python_module

def test_pyinfo_instantiates_successfully():
    """Test that PyInfo can be instantiated without errors."""
    # Construct a PyInfo instance; no exception should be raised
    py_info_instance = python_module.PyInfo()

