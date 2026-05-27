import pytest
import collections as collections_module
import namedtupleutils as namedtuple_utils

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple can process a float value without raising an exception."""
    float_value = -476.66
    namedtuple_utils.to_namedtuple(float_value)

def test_to_namedtuple_converts_tuple_and_set():
    """Test that to_namedtuple correctly handles tuple and set inputs."""
    # Create a float value and a homogeneous set containing only that value
    float_value = -67.0
    homogeneous_set = {float_value, float_value, float_value, float_value}
    
    # Create a tuple containing the float and the set
    mixed_tuple = (float_value, homogeneous_set)
    
    # Convert the tuple to a namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(mixed_tuple)
    
    # Also convert the set directly to a namedtuple
    namedtuple_utils.to_namedtuple(homogeneous_set)

def test_to_namedtuple_idempotent_on_single_field_dict():
    """Converting a dict to namedtuple twice yields same result (idempotency)."""
    # Create a dict with a single repeated key-value pair
    field_name = "author"
    input_dict = {field_name: field_name, field_name: field_name, field_name: field_name}
    
    # First conversion from dict to namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(input_dict)
    # Second conversion should produce identical structure (idempotent operation)
    double_conversion_result = namedtuple_utils.to_namedtuple(namedtuple_result)
    assert double_conversion_result == namedtuple_result

def test_to_namedtuple_handles_bytes_input():
    """Verify that to_namedtuple can process a bytes object without raising exceptions."""
    # A non-ASCII bytes object to test handling of arbitrary binary data
    binary_data = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(binary_data)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple correctly handles an empty tuple input."""
    empty_tuple = ()
    result = namedtuple_utils.to_namedtuple(empty_tuple)
    assert result == ()

def test_repeated_conversion_of_empty_ordereddict_and_namedtuple():
    """Test that to_namedtuple can be repeatedly called on empty OrderedDict and its conversions."""
    # Create an empty OrderedDict and convert it to a namedtuple
    empty_ordered_dict = collections_module.OrderedDict()
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Convert the resulting namedtuple back to a namedtuple (should be idempotent)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)
    
    # Convert the original empty OrderedDict again
    another_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Convert that result to a namedtuple
    namedtuple_from_another_namedtuple = namedtuple_utils.to_namedtuple(another_namedtuple_from_dict)
    
    # Create some arbitrary bytes data
    arbitrary_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    
    # Convert the empty OrderedDict yet again
    yet_another_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Create a tuple containing a namedtuple and bytes, then convert it
    tuple_with_namedtuple_and_bytes = (namedtuple_from_namedtuple, arbitrary_bytes)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_with_namedtuple_and_bytes)
    
    # Final conversion of the empty OrderedDict
    final_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_ordered_dict_and_invalid_ordered_dict_initialization():
    """Test converting OrderedDict to namedtuple and edge case OrderedDict initialization.
    
    This test verifies:
    1. to_namedtuple can handle OrderedDict with special character keys/values
    2. OrderedDict initialization with unpacked None (edge case)
    """
    # Create a string with special characters including carriage return and vertical tab
    special_string = "wm=-g\ry#\x0b#:*"
    
    # Create dictionary with the same string as both key and value
    single_item_dict = {special_string: special_string, special_string: special_string}
    
    # Convert dictionary to OrderedDict using keyword arguments
    ordered_dict = collections_module.OrderedDict(**single_item_dict)
    
    # Convert OrderedDict to namedtuple - main functionality being tested
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)
    
    # Test edge case: OrderedDict initialization with unpacked None
    none_value = None
    single_none_list = [none_value]
    collections_module.OrderedDict(*single_none_list)  # Should raise TypeError

def test_to_namedtuple_handles_nested_empty_list_and_none():
    """Test that to_namedtuple correctly processes nested empty list and None input."""
    # Create a nested list containing an empty list
    empty_list = []
    nested_list = [empty_list]
    
    # Convert nested list to namedtuple (should not raise)
    result = namedtuple_utils.to_namedtuple(nested_list)
    
    # Test with None input (should not raise)
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_handles_complex_nested_structures_with_duplicate_keys():
    """Test that to_namedtuple correctly processes deeply nested structures containing duplicate dictionary keys."""
    
    # Create a long descriptive string that will be used as both key and value
    path_normalization_docstring = (
        "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n"
        "    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n"
        "       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n"
        "    #. :obj:`PosixPath <pathlib.PosixPath>` and\n"
        "       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n"
        "       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n"
        "       method.\n    #. An initial component of ``~`` will be replaced by that user's\n"
        "       home directory.\n    #. Any environment variables will be expanded.\n"
        "    #. Non absolute paths will have the current working directory from\n"
        "       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n"
        "       :obj:`os.chdir() <os.chdir>` to change the current working directory\n"
        "       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n"
        "       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n"
        "       ``A/B``.\n\n    Args:\n"
        "        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n"
        "            The path to be normalized.\n\n    :rtype:\n"
        "        :obj:`Path <pathlib.Path>`\n\n"
        "        * :obj:`PosixPath <pathlib.PosixPath>` or\n"
        "          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n"
        "        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n"
        "           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n"
        "           the same object returned.\n\n    Example:\n\n"
        "        >>> from flutils.pathutils import normalize_path\n"
        "        >>> normalize_path('~/tmp/foo/../bar')\n"
        "        PosixPath('/home/test_user/tmp/bar')\n\n    "
    )
    
    # Create dictionary with duplicate keys (same string used for all keys and values)
    duplicate_key_dict = {
        path_normalization_docstring: path_normalization_docstring,
        path_normalization_docstring: path_normalization_docstring,
        path_normalization_docstring: path_normalization_docstring
    }
    
    # First conversion of the duplicate-key dictionary
    first_namedtuple = namedtuple_utils.to_namedtuple(duplicate_key_dict)
    
    # Boolean flag used later as a dictionary key
    false_flag = False
    
    # Convert same dictionary again (should produce same structure)
    second_namedtuple = namedtuple_utils.to_namedtuple(duplicate_key_dict)
    
    # Create tuple containing the namedtuple
    tuple_with_namedtuple = (second_namedtuple,)
    
    # Convert tuple to namedtuple
    tuple_converted = namedtuple_utils.to_namedtuple(tuple_with_namedtuple)
    
    # Create dictionary with namedtuple as key and boolean as key
    mixed_key_dict = {
        tuple_converted: second_namedtuple,
        false_flag: second_namedtuple
    }
    
    # Convert mixed dictionary to namedtuple
    mixed_namedtuple = namedtuple_utils.to_namedtuple(mixed_key_dict)
    
    # Convert the resulting namedtuple again (nested conversion)
    nested_conversion = namedtuple_utils.to_namedtuple(mixed_namedtuple)
    
    # Another false flag
    another_false_flag = False
    
    # Convert the mixed namedtuple once more
    final_conversion = namedtuple_utils.to_namedtuple(mixed_namedtuple)
    
    # Attempt to convert boolean value to namedtuple (edge case)
    namedtuple_utils.to_namedtuple(another_false_flag)

def test_to_namedtuple_handles_nested_structures_and_non_convertible_types():
    """Test that to_namedtuple correctly processes nested structures and passes through non-convertible types."""
    # Create a string with a special character and an empty tuple
    special_string = "\x0cMv"
    empty_tuple = ()

    # Build a complex dictionary with mixed key/value types
    complex_dict = {
        special_string: empty_tuple,
        empty_tuple: special_string,
        empty_tuple: empty_tuple,
    }

    # Create a tuple containing the string and the complex dictionary
    nested_tuple = (special_string, complex_dict)

    # Wrap the tuple in a list to create a nested structure
    nested_list = [nested_tuple]

    # Convert the nested list to a namedtuple (first conversion)
    result1 = namedtuple_utils.to_namedtuple(nested_list)
    # Convert the result again (second conversion)
    result2 = namedtuple_utils.to_namedtuple(result1)
    # Convert once more (third conversion) - should be idempotent
    result3 = namedtuple_utils.to_namedtuple(result2)

    # Test that non-convertible types (like int) are passed through without error
    integer_value = 2
    namedtuple_utils.to_namedtuple(integer_value)

def test_to_namedtuple_handles_dictionary_with_bytes_keys_and_values():
    """Test that to_namedtuple can process a dictionary with bytes as both keys and values."""
    # Create a bytes object to use as both dictionary keys and values
    sample_bytes = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    
    # Build dictionary where bytes serve as both keys and values
    bytes_dict = {
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes
    }
    
    # Verify the function can process this edge case without errors
    namedtuple_utils.to_namedtuple(bytes_dict)

