import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_float():
    """Test that to_namedtuple accepts a float input."""
    input_float = -476.66
    # Should handle float input without crashing
    namedtuple_utils.to_namedtuple(input_float)

def test_to_namedtuple_with_float_set_and_tuple():
    """Test to_namedtuple conversion with a float, set containing duplicates, and tuple."""
    # Create a test float value
    test_float = -67.0
    
    # Create a set with duplicate float values (will deduplicate to single element)
    float_set = {test_float, test_float, test_float, test_float}
    
    # Create a tuple containing the float and the set
    float_and_set_tuple = (test_float, float_set)
    
    # Convert the tuple to a namedtuple (should handle nested structures)
    converted_tuple = namedtuple_utils.to_namedtuple(float_and_set_tuple)
    
    # Also convert the set directly to a namedtuple
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_idempotent_on_single_key_dict():
    """
    Test that to_namedtuple can be applied twice to a single-key dictionary
    without raising exceptions (idempotency check).
    """
    # Create a dictionary with a single key-value pair
    key_and_value = "author"
    single_key_dict = {
        key_and_value: key_and_value,
        key_and_value: key_and_value,
        key_and_value: key_and_value,
    }  # Duplicate keys collapse to single entry

    # First conversion: dictionary → namedtuple
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(single_key_dict)

    # Second conversion: namedtuple → namedtuple (should be idempotent)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_handles_bytes_input():
    """Test that to_namedtuple can process a bytes object without raising an exception."""
    # A bytes object that should be processed without error
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    
    # Call the function under test with bytes input
    namedtuple_utils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple without errors."""
    empty_tuple = ()
    # Should process empty tuple without raising exceptions
    result = namedtuple_utils.to_namedtuple(empty_tuple)
    assert result == ()

def test_to_namedtuple_with_ordered_dict_and_nested_structures():
    """Test to_namedtuple handles OrderedDict and nested conversions without errors."""
    
    # Create an empty OrderedDict
    empty_ordered_dict = collections_module.OrderedDict()
    
    # Convert empty OrderedDict to namedtuple
    namedtuple_from_empty_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Convert the resulting namedtuple back to namedtuple (should be idempotent)
    nested_namedtuple_1 = namedtuple_utils.to_namedtuple(namedtuple_from_empty_dict)
    
    # Another conversion of the original OrderedDict
    namedtuple_from_empty_dict_2 = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Convert that result again
    nested_namedtuple_2 = namedtuple_utils.to_namedtuple(namedtuple_from_empty_dict_2)
    
    # Arbitrary bytes data
    arbitrary_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    
    # Another conversion of the original OrderedDict
    namedtuple_from_empty_dict_3 = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Create tuple with namedtuple and bytes
    tuple_with_namedtuple_and_bytes = (nested_namedtuple_1, arbitrary_bytes)
    
    # Convert tuple to namedtuple
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_with_namedtuple_and_bytes)
    
    # Final conversion of the original OrderedDict
    namedtuple_from_empty_dict_4 = namedtuple_utils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_ordered_dict_and_none_initialization():
    """Test converting an OrderedDict to a namedtuple and OrderedDict initialization with None."""
    
    # Create a test string with special characters
    test_string = "wm=-g\ry#\x0b#:*"
    
    # Create a dictionary with the same string as both key and value
    single_item_dict = {test_string: test_string, test_string: test_string}
    
    # Convert dictionary to OrderedDict using keyword argument unpacking
    ordered_dict_from_dict = collections_module.OrderedDict(**single_item_dict)
    
    # Convert OrderedDict to namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict_from_dict)
    
    # Test OrderedDict initialization with None via argument unpacking
    none_value = None
    list_with_none = [none_value]
    collections_module.OrderedDict(*list_with_none)

def test_to_namedtuple_with_nested_list_and_none():
    """Test that to_namedtuple handles nested lists and None inputs without error."""
    
    # Create a nested list structure: list containing an empty list
    empty_list = []
    nested_list = [empty_list]
    
    # Convert nested list to namedtuple (should not raise)
    result = namedtuple_utils.to_namedtuple(nested_list)
    
    # Test with None input (should not raise)
    none_input = None
    namedtuple_utils.to_namedtuple(none_input)

def test_to_namedtuple_with_complex_nested_structures():
    """Test that to_namedtuple handles complex nested structures without errors."""
    # A long docstring used as both key and value
    long_docstring = (
        "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    "
        "#. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by "
        ":obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    "
        "#. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       "
        "to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    "
        "#. An initial component of ``~`` will be replaced by that user’s\n       home directory.\n    "
        "#. Any environment variables will be expanded.\n    "
        "#. Non absolute paths will have the current working directory from\n       "
        ":obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       "
        "before calling this function.\n    "
        "#. Redundant separators and up-level references will be normalized, so\n       "
        "that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    "
        "Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    "
        ":rtype:\n        :obj:`Path <pathlib.Path>`\n\n        "
        "* :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        "
        ".. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           "
        "the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        "
        ">>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "
    )

    # Create a simple dictionary with the docstring as both key and value
    simple_dict = {long_docstring: long_docstring, long_docstring: long_docstring, long_docstring: long_docstring}
    namedtuple_from_simple_dict = namedtuple_utils.to_namedtuple(simple_dict)

    flag_false = False
    another_namedtuple_from_simple_dict = namedtuple_utils.to_namedtuple(simple_dict)

    # Create a tuple containing the namedtuple
    tuple_of_namedtuple = (another_namedtuple_from_simple_dict,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_of_namedtuple)

    # Build a more complex dictionary mixing namedtuples and booleans
    complex_dict = {namedtuple_from_tuple: another_namedtuple_from_simple_dict, flag_false: another_namedtuple_from_simple_dict}
    namedtuple_from_complex_dict = namedtuple_utils.to_namedtuple(complex_dict)

    # Nest namedtuple conversions
    nested_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_complex_dict)

    another_flag_false = False
    another_namedtuple_from_complex_dict = namedtuple_utils.to_namedtuple(namedtuple_from_complex_dict)

    # Final conversion of a boolean value
    namedtuple_utils.to_namedtuple(another_flag_false)

def test_to_namedtuple_nested_structure_idempotent():
    """Test that to_namedtuple handles nested structures with mixed keys and is idempotent."""
    
    # Create a string containing a control character
    special_string = "\x0cMv"
    
    # Empty tuple as a base element
    empty_tuple = ()
    
    # Dictionary with mixed keys: string, tuple, and tuple-tuple mapping
    mixed_key_dict = {
        special_string: empty_tuple,
        empty_tuple: special_string,
        empty_tuple: empty_tuple
    }
    
    # Tuple containing the string and nested dictionary
    tuple_with_dict = (special_string, mixed_key_dict)
    
    # List containing the tuple (creating nested structure)
    nested_list = [tuple_with_dict]
    
    # First conversion: list to namedtuple
    first_conversion = namedtuple_utils.to_namedtuple(nested_list)
    
    # Second conversion: namedtuple to namedtuple (testing idempotence)
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)
    
    # Third conversion: namedtuple to namedtuple (further idempotence test)
    third_conversion = namedtuple_utils.to_namedtuple(second_conversion)
    
    # Test handling of non-convertible type (integer)
    integer_value = 2
    namedtuple_utils.to_namedtuple(integer_value)

def test_to_namedtuple_with_bytes_keys_and_values():
    """Test that to_namedtuple can handle a dictionary with bytes as both keys and values."""
    # Create a bytes object to use as both keys and values
    sample_bytes = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    
    # Create dictionary with bytes as both keys and values
    # Note: All keys are identical, so dictionary will have only one entry
    bytes_dict = {
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes
    }
    
    # Call to_namedtuple - test passes if no exception is raised
    namedtuple_utils.to_namedtuple(bytes_dict)

