import pytest
import collections as collections_module
import namedtupleutils as namedtuple_utils

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple can be called with a float argument."""
    # This tests the function's handling of a non-dict/namespace input
    float_value = -476.66
    namedtuple_utils.to_namedtuple(float_value)

def test_to_namedtuple_handles_nested_set_and_tuple():
    """Test that to_namedtuple can process nested structures containing sets and tuples."""
    # Create a float value and a set containing that value (duplicates removed)
    negative_float = -67.0
    float_set = {negative_float, negative_float, negative_float, negative_float}
    
    # Create a tuple containing the float and the set
    nested_tuple = (negative_float, float_set)
    
    # Convert the tuple to a namedtuple (tests nested structure handling)
    result = namedtuple_utils.to_namedtuple(nested_tuple)
    
    # Convert the set directly to a namedtuple (tests flat set handling)
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_can_be_called_on_dict_and_then_on_resulting_namedtuple():
    """Test that to_namedtuple can be applied twice: first to a dict, then to the resulting namedtuple."""
    # Create a simple dictionary with repeated key-value pairs
    key_and_value = "author"
    input_dict = {key_and_value: key_and_value, key_and_value: key_and_value, key_and_value: key_and_value}
    
    # First conversion: dictionary to namedtuple
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(input_dict)
    
    # Second conversion: namedtuple to namedtuple (should handle gracefully)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_with_bytes_object():
    """Test that to_namedtuple can process a bytes object without raising exceptions."""
    input_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(input_bytes)

def test_to_namedtuple_with_empty_tuple():
    """Test converting an empty tuple to a namedtuple."""
    empty_tuple = ()
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_nested_conversions_and_mixed_types():
    """Verify to_namedtuple correctly processes nested conversions and mixed type inputs."""
    # Create an empty OrderedDict as base test input
    empty_ordered_dict = collections_module.OrderedDict()
    
    # Convert empty OrderedDict to namedtuple
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Convert the resulting namedtuple back to namedtuple (should be idempotent)
    nested_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)
    
    # Repeat conversion chain starting from same base OrderedDict
    second_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    second_nested_namedtuple = namedtuple_utils.to_namedtuple(second_namedtuple_from_dict)
    
    # Test with bytes data
    random_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    
    # Another conversion from same base OrderedDict
    third_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Create tuple mixing namedtuple and bytes, then convert to namedtuple
    mixed_tuple = (nested_namedtuple, random_bytes)
    namedtuple_from_mixed_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)
    
    # Final conversion from same base OrderedDict
    fourth_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Assertions
    # Test idempotency: applying to_namedtuple twice should yield same result
    assert nested_namedtuple == namedtuple_from_dict
    assert second_nested_namedtuple == second_namedtuple_from_dict
    
    # Test consistency: same input should produce same output
    assert namedtuple_from_dict == second_namedtuple_from_dict == third_namedtuple_from_dict == fourth_namedtuple_from_dict
    
    # Test mixed type conversion
    assert isinstance(namedtuple_from_mixed_tuple, tuple)
    assert len(namedtuple_from_mixed_tuple) == 2
    assert namedtuple_from_mixed_tuple[0] == nested_namedtuple
    assert namedtuple_from_mixed_tuple[1] == random_bytes

def test_to_namedtuple_with_ordereddict_containing_special_characters():
    """Test converting an OrderedDict with special character keys/values to a namedtuple."""
    # Create a string containing special characters (newline, carriage return, vertical tab)
    special_string = "wm=-g\ry#\x0b#:*"
    
    # Build a dictionary where the same string is both key and value
    data_dict = {special_string: special_string, special_string: special_string}
    
    # Create an OrderedDict from the dictionary using keyword arguments
    ordered_dict = collections_module.OrderedDict(**data_dict)
    
    # Convert the OrderedDict to a namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)
    
    # Test edge case: Attempt to create OrderedDict with None unpacked from list
    none_value = None
    none_list = [none_value]
    collections_module.OrderedDict(*none_list)

def test_to_namedtuple_handles_nested_list_and_none():
    """Test that to_namedtuple correctly processes nested list and None inputs."""
    empty_list = []
    nested_list = [empty_list]
    # Convert nested list structure to namedtuple
    result = namedtuple_utils.to_namedtuple(nested_list)
    
    none_value = None
    # Ensure function handles None input without error
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_with_nested_structures_and_duplicate_keys():
    """Test to_namedtuple handles nested structures, duplicate keys, and non-dict inputs."""
    # A long docstring used as both key and value in a dictionary
    path_docstring = (
        "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n"
        "#. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n"
        "#. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n"
        "       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n"
        "#. An initial component of ``~`` will be replaced by that user’s\n       home directory.\n"
        "#. Any environment variables will be expanded.\n"
        "#. Non absolute paths will have the current working directory from\n"
        "       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n"
        "       before calling this function.\n"
        "#. Redundant separators and up-level references will be normalized, so\n"
        "       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n"
        "    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n"
        "            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n"
        "        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n"
        "        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n"
        "           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n"
        "    Example:\n\n        >>> from flutils.pathutils import normalize_path\n"
        "        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "
    )
    
    # Dictionary with duplicate keys (same string used as key and value multiple times)
    simple_dict = {path_docstring: path_docstring, path_docstring: path_docstring, path_docstring: path_docstring}
    namedtuple_from_simple_dict = namedtuple_utils.to_namedtuple(simple_dict)
    
    false_flag = False
    another_namedtuple_from_simple_dict = namedtuple_utils.to_namedtuple(simple_dict)
    
    # Create a tuple containing a namedtuple
    tuple_of_namedtuple = (another_namedtuple_from_simple_dict,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_of_namedtuple)
    
    # Dictionary with namedtuple keys and boolean keys
    complex_dict = {namedtuple_from_tuple: another_namedtuple_from_simple_dict, false_flag: another_namedtuple_from_simple_dict}
    namedtuple_from_complex_dict = namedtuple_utils.to_namedtuple(complex_dict)
    
    # Nest namedtuple conversion
    nested_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_complex_dict)
    
    another_false_flag = False
    another_namedtuple_from_complex_dict = namedtuple_utils.to_namedtuple(namedtuple_from_complex_dict)
    
    # Test conversion of a boolean value (non-dict/tuple input)
    namedtuple_utils.to_namedtuple(another_false_flag)

def test_to_namedtuple_handles_deeply_nested_structures_and_non_dict_types():
    """Test that to_namedtuple correctly processes deeply nested structures and non-dict/list/tuple inputs."""
    # Create a complex nested structure with duplicate dictionary keys
    key_string = "\x0cMv"
    empty_tuple = ()
    nested_dict = {key_string: empty_tuple, empty_tuple: key_string, empty_tuple: empty_tuple}
    mixed_tuple = (key_string, nested_dict)
    nested_list = [mixed_tuple]

    # Convert nested structure multiple times (testing idempotence)
    converted_once = namedtuple_utils.to_namedtuple(nested_list)
    converted_twice = namedtuple_utils.to_namedtuple(converted_once)
    converted_thrice = namedtuple_utils.to_namedtuple(converted_twice)

    # Test with non-dict/list/tuple input (should handle gracefully)
    integer_input = 2
    namedtuple_utils.to_namedtuple(integer_input)

def test_to_namedtuple_handles_dictionary_with_duplicate_bytes_keys():
    """Test that to_namedtuple can process a dictionary where both keys and values are bytes objects."""
    
    # Create a bytes object to use as both key and value
    sample_bytes = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    
    # Create dictionary with bytes as both keys and values
    # Note: Duplicate keys will be collapsed in the dictionary
    input_dict = {
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
    }
    
    # Call the function under test - should process without errors
    namedtuple_utils.to_namedtuple(input_dict)

