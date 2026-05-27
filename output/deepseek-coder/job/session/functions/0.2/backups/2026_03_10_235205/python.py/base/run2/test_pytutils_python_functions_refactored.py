import python as py

def test_pyinfo_creation():
    """
    This test case verifies that PyInfo object is correctly created.
    """
    # Create an instance of PyInfo
    py_info = py.PyInfo()

    # Assert that the created object is of type PyInfo
    assert isinstance(py_info, py.PyInfo)