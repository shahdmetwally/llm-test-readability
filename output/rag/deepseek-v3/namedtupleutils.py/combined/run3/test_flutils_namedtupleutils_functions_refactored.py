import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_negative_float():
    """Verify that to_namedtuple can convert a negative float value."""
    negative_float_value = -476.66
    namedtuple_utils.to_namedtuple(negative_float_value)

def test_to_namedtuple_with_float_and_set():
    """Test that to_namedtuple processes tuples containing float and set values, 
    and standalone sets, without errors."""
    test_float = -67.0
    duplicate_set = {test_float, test_float, test_float, test_float}
    nested_tuple = (test_float, duplicate_set)
    
    result_namedtuple = namedtuple_utils.to_namedtuple(nested_tuple)
    namedtuple_utils.to_namedtuple(duplicate_set)

def test_to_namedtuple_with_duplicate_keys_roundtrip():
    """Verify to_namedtuple handles duplicates and round-trips work."""
    field_name = "author"
    # Dictionary with duplicate keys - later values overwrite earlier ones
    dict_with_duplicate_keys = {
        field_name: field_name,
        field_name: field_name,
        field_name: field_name,
    }
    # First conversion: dict -> namedtuple
    first_namedtuple = namedtuple_utils.to_namedtuple(dict_with_duplicate_keys)
    # Second conversion: namedtuple -> namedtuple (round-trip)
    second_namedtuple = namedtuple_utils.to_namedtuple(first_namedtuple)

def test_to_namedtuple_with_bytes_input():
    """Verify that to_namedtuple accepts bytes input without error."""
    raw_bytes_data = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(raw_bytes_data)

def test_to_namedtuple_with_empty_tuple():
    """Verify to_namedtuple handles an empty tuple correctly."""
    empty_tuple = ()
    result_namedtuple = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_multiple_input_types():
    """Verify that to_namedtuple handles multiple calls with OrderedDict, namedtuple, and tuple inputs without raising errors."""
    # Create an OrderedDict and convert it to a namedtuple
    ordered_dict_0 = collections_module.OrderedDict()
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(ordered_dict_0)
    
    # Convert the resulting namedtuple back to a namedtuple (test idempotency)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)
    
    # Repeat the process from the original dict
    second_namedtuple_from_dict = namedtuple_utils.to_namedtuple(ordered_dict_0)
    namedtuple_from_second = namedtuple_utils.to_namedtuple(second_namedtuple_from_dict)
    
    # Test with arbitrary bytes data mixed into the process
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    third_namedtuple_from_dict = namedtuple_utils.to_namedtuple(ordered_dict_0)
    
    # Create a tuple mixing a namedtuple and bytes, then convert it
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)
    
    # Final conversion from the original dict
    fourth_namedtuple_from_dict = namedtuple_utils.to_namedtuple(ordered_dict_0)

def test_to_namedtuple_with_ordereddict_and_unique_key():
    """Verify to_namedtuple handles an OrderedDict and create a separate list-based OrderedDict."""
    # Setup: create a dictionary with a single key-value pair
    sample_key_value = "wm=-g\ry#\x0b#:*"
    simple_dict = {sample_key_value: sample_key_value, sample_key_value: sample_key_value}
    
    # Create an OrderedDict from the dictionary
    ordered_dict = collections_module.OrderedDict(**simple_dict)
    
    # Convert the OrderedDict to a namedtuple
    result_namedtuple = namedtuple_utils.to_namedtuple(ordered_dict)
    
    # Additional test: create an OrderedDict from a list containing only None
    none_value = None
    none_list = [none_value]
    collections_module.OrderedDict(*none_list)

def test_to_namedtuple_with_nested_lists_and_none():
    """Verify to_namedtuple handles nested lists and None input without raising unexpected errors."""
    # Create a nested list structure: outer list containing an inner empty list
    inner_empty_list = []
    outer_list_with_inner = [inner_empty_list]
    
    # Convert the nested list to a namedtuple
    result = namedtuple_utils.to_namedtuple(outer_list_with_inner)
    
    # Verify behavior with None input
    none_input = None
    namedtuple_utils.to_namedtuple(none_input)

def test_to_namedtuple_with_repeated_conversions_nested_structures_and_boolean_edge_cases():
    """Verify that to_namedtuple correctly handles repeated conversions,
    nested structures, tuples, mixed-type dictionaries, and boolean edge cases."""
    
    # Create a long docstring as dictionary key/value
    normalize_path_docstring = (
        "Normalize a given path.\n\n"
        "    The given ``path`` will be normalized in the following process.\n\n"
        "    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n"
        "       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n"
        "    #. :obj:`PosixPath <pathlib.PosixPath>` and\n"
        "       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n"
        "       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n"
        "       method.\n"
        "    #. An initial component of ``~`` will be replaced by that user's\n"
        "       home directory.\n"
        "    #. Any environment variables will be expanded.\n"
        "    #. Non absolute paths will have the current working directory from\n"
        "       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n"
        "       :obj:`os.chdir() <os.chdir>` to change the current working directory\n"
        "       before calling this function.\n"
        "    #. Redundant separators and up-level references will be normalized, so\n"
        "       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n"
        "       ``A/B``.\n\n"
        "    Args:\n"
        "        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n"
        "            The path to be normalized.\n\n"
        "    :rtype:\n"
        "        :obj:`Path <pathlib.Path>`\n\n"
        "        * :obj:`PosixPath <pathlib.PosixPath>` or\n"
        "          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n"
        "        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n"
        "           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n"
        "           the same object returned.\n\n"
        "    Example:\n\n"
        "        >>> from flutils.pathutils import normalize_path\n"
        "        >>> normalize_path('~/tmp/foo/../bar')\n"
        "        PosixPath('/home/test_user/tmp/bar')\n\n"
    )
    
    # Test 1: Convert a dict with identical key-value pairs
    single_key_dict = {
        normalize_path_docstring: normalize_path_docstring,
        normalize_path_docstring: normalize_path_docstring,
        normalize_path_docstring: normalize_path_docstring
    }
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(single_key_dict)
    
    # Test 2: Convert the same dict again (idempotency)
    false_value = False
    namedtuple_from_dict_again = namedtuple_utils.to_namedtuple(single_key_dict)
    
    # Test 3: Convert a tuple containing the namedtuple from step 2
    single_element_tuple = (namedtuple_from_dict_again,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(single_element_tuple)
    
    # Test 4: Convert a mixed-type dict (namedtuple key and boolean key)
    mixed_type_dict = {
        namedtuple_from_tuple: namedtuple_from_dict_again,
        false_value: namedtuple_from_dict_again
    }
    namedtuple_from_mixed_dict = namedtuple_utils.to_namedtuple(mixed_type_dict)
    
    # Test 5: Convert the result of test 4 (a namedtuple) back to namedtuple
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)
    
    # Test 6: Convert the same namedtuple again
    false_value_two = False
    namedtuple_from_namedtuple_again = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)
    
    # Test 7: Edge case - convert a boolean value directly
    namedtuple_utils.to_namedtuple(false_value_two)

def test_to_namedtuple_handles_nested_structures_and_invalid_input():
    """Tests that to_namedtuple handles nested structures (including conversion results)
    and properly handles non-iterable inputs."""
    control_char_string = "\x0cMv"
    empty_tuple = ()
    
    # Create a dict with mixed key/value types including nested empty tuple
    mixed_dict = {
        control_char_string: empty_tuple,
        empty_tuple: control_char_string,
        empty_tuple: empty_tuple,  # last duplicate key wins in Python
    }
    
    # Wrap the dict in a tuple, then in a list
    nested_tuple = (control_char_string, mixed_dict)
    input_list = [nested_tuple]
    
    # Test converting a list containing nested structures to namedtuple
    first_conversion = namedtuple_utils.to_namedtuple(input_list)
    
    # Test re-converting an already converted namedtuple
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)
    
    # Test triple conversion (already converted nested namedtuples)
    third_conversion = namedtuple_utils.to_namedtuple(second_conversion)
    
    # Test that converting a plain integer does not raise (edge case)
    invalid_input = 2
    namedtuple_utils.to_namedtuple(invalid_input)

def test_to_namedtuple_with_bytes_keys_and_values():
    """Test that to_namedtuple handles a dictionary with bytes objects as both keys and values."""
    bytes_key_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    input_dict = {
        bytes_key_value: bytes_key_value,
        bytes_key_value: bytes_key_value,
        bytes_key_value: bytes_key_value,
    }
    namedtuple_utils.to_namedtuple(input_dict)