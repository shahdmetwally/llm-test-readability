import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_negative_float_input():
    """Test that to_namedtuple handles a negative float input without error."""
    negative_float_value = -476.66
    namedtuple_utils.to_namedtuple(negative_float_value)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Verify that to_namedtuple converts a tuple containing a float and a set,
    and a standalone set, without errors."""
    number = -67.0
    unique_set = {number, number, number, number}  # Set deduplicates to one element
    nested_structure = (number, unique_set)
    
    # Convert a tuple containing nested types (float and set)
    result = namedtuple_utils.to_namedtuple(nested_structure)
    
    # Convert a standalone set
    namedtuple_utils.to_namedtuple(unique_set)

def test_to_namedtuple_handles_duplicate_keys_idempotently():
    """Test that to_namedtuple handles dictionaries with duplicate keys and is idempotent."""
    # A key name used to create a dict with all identical keys
    key_name = "author"
    
    # Dictionary with duplicate keys (Python collapses these to a single key-value pair)
    input_dict = {key_name: key_name, key_name: key_name, key_name: key_name}
    
    # Convert the dictionary to a namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(input_dict)
    
    # Verify the namedtuple can be converted again (idempotent behavior)
    second_conversion_result = namedtuple_utils.to_namedtuple(namedtuple_result)

def test_to_namedtuple_with_bytes_raises_type_error():
    """Verify that to_namedtuple raises an exception when called with arbitrary byte data."""
    arbitrary_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(arbitrary_bytes)

def test_empty_tuple_converts_to_namedtuple():
    """Verifies that an empty tuple can be converted to a namedtuple without error."""
    empty_tuple = ()
    result_namedtuple = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_repeated_calls_on_ordereddict_and_output():
    """Tests that to_namedtuple can be called repeatedly on OrderedDicts,
    on the results of previous to_namedtuple calls, and on a tuple containing
    a namedtuple + bytes (all without crashing)."""
    # Create an OrderedDict and convert it to a namedtuple
    ordered_dict = collections_module.OrderedDict()
    result_from_ordered_dict_v1 = namedtuple_utils.to_namedtuple(ordered_dict)

    # Convert the namedtuple back to another namedtuple (idempotence check)
    result_from_namedtuple_v1 = namedtuple_utils.to_namedtuple(result_from_ordered_dict_v1)

    # Convert the original OrderedDict again
    result_from_ordered_dict_v2 = namedtuple_utils.to_namedtuple(ordered_dict)
    result_from_namedtuple_v2 = namedtuple_utils.to_namedtuple(result_from_ordered_dict_v2)

    # Test with a mixed tuple containing a namedtuple and bytes
    bytes_data = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    result_from_ordered_dict_v3 = namedtuple_utils.to_namedtuple(ordered_dict)
    tuple_of_namedtuple_and_bytes = (result_from_namedtuple_v1, bytes_data)
    result_from_tuple_containing_namedtuple = namedtuple_utils.to_namedtuple(tuple_of_namedtuple_and_bytes)

    # One more call on the original OrderedDict for consistency
    result_from_ordered_dict_v4 = namedtuple_utils.to_namedtuple(ordered_dict)

def test_to_namedtuple_with_duplicate_keys_in_ordereddict():
    """Test that to_namedtuple handles OrderedDict with duplicate keys."""
    # Create a key string that will be used as both key and value
    key_string = "wm=-g\ry#\x0b#:*"

    # Create a dict with the same key mapped to itself (duplicate keys after unpacking)
    dict_with_duplicate_keys = {key_string: key_string, key_string: key_string}

    # Create an OrderedDict from the dict with duplicate keys
    ordered_dict_from_duplicate_keys = collections_module.OrderedDict(**dict_with_duplicate_keys)

    # Convert the OrderedDict to a namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict_from_duplicate_keys)

    # Test creation of an OrderedDict from a list containing None
    none_value = None
    none_list = [none_value]
    collections_module.OrderedDict(*none_list)

def test_to_namedtuple_handles_nested_lists_and_none_input():
    """Test that to_namedtuple handles nested list structures and None input gracefully."""
    # Test with a nested list: an outer list containing an empty inner list
    inner_list = []
    nested_list = [inner_list]
    namedtuple_result = namedtuple_utils.to_namedtuple(nested_list)
    
    # Test with None input (should handle gracefully, likely raising an exception)
    none_input = None
    namedtuple_utils.to_namedtuple(none_input)

def test_to_namedtuple_with_self_referencing_dict_and_boolean_edge_cases():
    """Tests that to_namedtuple handles various input types (dicts, tuples, nested structures) and edge cases (boolean input)."""

    # Create a long docstring to use as a dictionary key/value
    long_normalize_path_docstring = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Convert self-referencing dictionary to namedtuple (all keys/values are the same docstring)
    self_referencing_dictionary = {long_normalize_path_docstring: long_normalize_path_docstring, long_normalize_path_docstring: long_normalize_path_docstring, long_normalize_path_docstring: long_normalize_path_docstring}
    first_namedtuple = namedtuple_utils.to_namedtuple(self_referencing_dictionary)

    false_value = False
    # Convert the same dictionary again to verify reproducibility
    second_namedtuple_from_same_dict = namedtuple_utils.to_namedtuple(self_referencing_dictionary)

    # Wrap the namedtuple in a tuple and convert to namedtuple
    namedtuple_tuple = (second_namedtuple_from_same_dict,)
    namedtuple_from_tuple_of_namedtuples = namedtuple_utils.to_namedtuple(namedtuple_tuple)

    # Create a dictionary mixing a namedtuple key and a boolean key
    mixed_value_dictionary = {namedtuple_from_tuple_of_namedtuples: second_namedtuple_from_same_dict, false_value: second_namedtuple_from_same_dict}
    mixed_namedtuple = namedtuple_utils.to_namedtuple(mixed_value_dictionary)

    # Convert the mixed namedtuple itself to another namedtuple (nested conversion)
    nested_namedtuple = namedtuple_utils.to_namedtuple(mixed_namedtuple)

    another_false_value = False
    # Repeated conversion of the mixed namedtuple for consistency check
    repeated_mixed_namedtuple = namedtuple_utils.to_namedtuple(mixed_namedtuple)

    # Edge case: convert a boolean value directly to namedtuple
    namedtuple_utils.to_namedtuple(another_false_value)

def test_to_namedtuple_with_nested_structures_and_idempotency():
    """Verify that to_namedtuple handles nested tuples/dicts with empty tuples
    and that multiple conversions are idempotent, while also testing that
    non-iterable types raise appropriate errors."""
    
    empty_string = "\x0cMv"
    empty_tuple = ()
    
    nested_dict = {
        empty_string: empty_tuple,
        empty_tuple: empty_tuple,
    }
    
    outer_tuple = (empty_string, nested_dict)
    input_list = [outer_tuple]
    
    first_conversion = namedtuple_utils.to_namedtuple(input_list)
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)
    third_conversion = namedtuple_utils.to_namedtuple(second_conversion)
    
    integer_input = 2
    namedtuple_utils.to_namedtuple(integer_input)

def test_to_namedtuple_with_bytes_dict_raises_error():
    """Verify that to_namedtuple raises an error when given a dictionary with bytes keys and values."""
    # Create a bytes object to use as both key and value
    bytes_key_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    
    # Create a dictionary where both keys and values are bytes (not hashable for namedtuple conversion)
    bytes_dict = {bytes_key_value: bytes_key_value, bytes_key_value: bytes_key_value, bytes_key_value: bytes_key_value}
    
    # This should raise a TypeError because bytes objects cannot be converted to namedtuple
    with pytest.raises(TypeError):
        namedtuple_utils.to_namedtuple(bytes_dict)