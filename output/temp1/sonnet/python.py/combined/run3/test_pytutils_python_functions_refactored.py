import pytest
import python as python_module

def test_pyinfo_instantiation_succeeds():
    """Test that PyInfo can be instantiated without raising any errors."""
    # Construct a PyInfo instance; success means no exception is raised
    py_info_instance = python_module.PyInfo()

