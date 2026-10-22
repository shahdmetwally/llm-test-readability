from codetiming_timer import PyInfo

def test_pyinfo_initialization():
    """
    Test the correct initialization of PyInfo object. 
    Expected result: a new PyInfo instance is created without errors.
    """
    py_info = PyInfo()

    # check that the object was successfully initialized
    assert isinstance(py_info, PyInfo)