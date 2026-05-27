import python as py
import re as regex
import helpers as utils

def test_py_info_creation():
    """
    Test that PyInfo object is created successfully.
    """
    # Given
    py_info = py.PyInfo()

    # Then
    assert isinstance(py_info, py.PyInfo), "PyInfo object is not created successfully."