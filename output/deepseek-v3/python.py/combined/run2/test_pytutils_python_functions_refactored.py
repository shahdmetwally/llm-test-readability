import pytest

import python as module_under_test

def test_pyinfo_instantiation():
    """Test that a PyInfo instance can be created without errors."""
    py_info_instance = module_under_test.PyInfo()

