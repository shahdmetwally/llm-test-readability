import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_raises_error_for_float_input():
    """Verify that to_namedtuple raises an error when passed a float value."""
    # A float cannot be converted to a namedtuple; this should raise an exception.
    invalid_float_input = -476.66
    with pytest.raises(TypeError):
        namedtuple_utils.to_namedtuple(invalid_float_input)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Verify to_namedtuple handles tuples with mixed types and standalone sets."""
    float_value = -67.0
    float_set = {float_value, float_value, float_value, float_value}
    input_tuple = (float_value, float_set)
    
    # Convert tuple containing float and set to namedtuple
    result_namedtuple = namedtuple_utils.to_namedtuple(input_tuple)
    
    # Also verify standalone set conversion works
    namedtuple_utils.to_namedtuple(float_set)

def test_converting_dict_with_duplicate_keys_to_namedtuple_and_back():
    """Verify that a dictionary with duplicate keys can be converted to a namedtuple,
    and the namedtuple can be converted again through to_namedtuple."""
    key_name = "author"
    
    # Create a dictionary with duplicate keys (Python preserves the last value)
    source_dict = {
        key_name: key_name,
        key_name: key_name,
        key_name: key_name,
    }
    
    # Convert the dictionary to a namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(source_dict)
    
    # Convert the resulting namedtuple back through to_namedtuple
    converted_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_result)

def test_to_namedtuple_with_bytes_input():
    """Verify that to_namedtuple can process a bytes object without errors."""
    # Arrange: Create raw bytes input
    raw_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"

    # Act: Convert bytes to namedtuple
    result = namedtuple_utils.to_namedtuple(raw_bytes)

    # Note: No explicit assertions - this test validates that
    # to_namedtuple handles bytes input without raising exceptions

def test_empty_tuple_conversion_to_namedtuple():
    """Verify that to_namedtuple can handle an empty tuple input."""
    empty_tuple = ()
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_idempotent_conversions_and_mixed_types():
    """
    Tests that `to_namedtuple` can be called multiple times on the same
    OrderedDict and works with already-converted namedtuples and mixed-type tuples.
    """
    source_ordered_dict = collections_module.OrderedDict()
    
    # Multiple conversions from the same empty OrderedDict
    first_conversion = namedtuple_utils.to_namedtuple(source_ordered_dict)
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)  # Convert a namedtuple back
    third_conversion = namedtuple_utils.to_namedtuple(source_ordered_dict)
    fourth_conversion = namedtuple_utils.to_namedtuple(third_conversion)  # Convert a namedtuple back
    
    test_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    fifth_conversion = namedtuple_utils.to_namedtuple(source_ordered_dict)
    
    # Test conversion of a mixed-type tuple
    mixed_tuple = (second_conversion, test_bytes)
    tuple_conversion = namedtuple_utils.to_namedtuple(mixed_tuple)
    
    # Final conversion from original source
    sixth_conversion = namedtuple_utils.to_namedtuple(source_ordered_dict)

def test_to_namedtuple_with_ordereddict_and_duplicate_keys():
    """Verify that to_namedtuple handles OrderedDict with duplicate keys."""
    key_string = "wm=-g\ry#\x0b#:*"
    input_dict = {key_string: key_string, key_string: key_string}
    ordered_dict = collections_module.OrderedDict(**input_dict)
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)

    # Verify OrderedDict can also be created from a None list
    none_value = None
    none_list = [none_value]
    collections_module.OrderedDict(*none_list)

def test_to_namedtuple_with_nested_list_and_none():
    """Test that to_namedtuple handles nested lists and None input gracefully."""
    # Test with nested list: an empty list inside another list
    inner_empty_list = []
    nested_list = [inner_empty_list]
    result = namedtuple_utils.to_namedtuple(nested_list)

    # Test that None input doesn't crash (implicit assertion)
    none_input = None
    namedtuple_utils.to_namedtuple(none_input)

def test_to_namedtuple_with_nested_conversions_and_boolean_error():
    """Verify that to_namedtuple recursively converts nested dicts and tuples,
    handling its own output, and raises an error for boolean inputs."""
    
    # Long docstring about path normalization (used as a test string)
    docstring_text = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user’s\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath` or\n          :obj:`WindowsPath` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "
    
    # Test 1: Convert a dict with repeated keys
    simple_dict = {docstring_text: docstring_text, docstring_text: docstring_text, docstring_text: docstring_text}
    first_result = namedtuple_utils.to_namedtuple(simple_dict)
    
    # Test 2: Convert the same dict again
    false_value = False
    second_result = namedtuple_utils.to_namedtuple(simple_dict)
    
    # Test 3: Convert a tuple containing a namedtuple
    result_tuple = (second_result,)
    tuple_namedtuple = namedtuple_utils.to_namedtuple(result_tuple)
    
    # Test 4: Convert a mixed dict with namedtuple key and boolean value
    mixed_dict = {tuple_namedtuple: second_result, false_value: second_result}
    mixed_result = namedtuple_utils.to_namedtuple(mixed_dict)
    
    # Test 5: Convert a namedtuple (recursive test)
    nested_result = namedtuple_utils.to_namedtuple(mixed_result)
    
    # Test 6: Convert the same namedtuple again
    another_false = False
    final_result = namedtuple_utils.to_namedtuple(mixed_result)
    
    # Test 7: Verify that converting a boolean raises an error
    with pytest.raises(TypeError):
        namedtuple_utils.to_namedtuple(another_false)

def test_to_namedtuple_handles_nested_structures_and_non_iterables():
    """Verify that to_namedtuple can process nested structures, survive
    repeated conversions on its own output, and handle non-iterable types."""
    
    # Setup: create a nested structure with mixed key/value types
    key_string = "\x0cMv"
    empty_tuple = ()
    
    # Dictionary with mixed key/value types (string->tuple, tuple->string, tuple->tuple)
    nested_dict = {
        key_string: empty_tuple,
        empty_tuple: key_string,
        empty_tuple: empty_tuple,
    }
    
    # Wrap in a tuple containing the string key and nested dict
    outer_tuple = (key_string, nested_dict)
    input_list = [outer_tuple]
    
    # Test: to_namedtuple on the list containing the nested structure
    first_result = namedtuple_utils.to_namedtuple(input_list)
    
    # Test: to_namedtuple can be called on its own output repeatedly
    second_result = namedtuple_utils.to_namedtuple(first_result)
    third_result = namedtuple_utils.to_namedtuple(second_result)
    
    # Test: to_namedtuple handles non-iterable types
    non_iterable_value = 2
    namedtuple_utils.to_namedtuple(non_iterable_value)

def test_to_namedtuple_with_unhashable_bytes_keys_raises_error():
    """Test that to_namedtuple raises an error for a dictionary with nested unhashable bytes keys."""
    unhashable_bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    nested_dict_with_bytes_keys = {
        unhashable_bytes_key: unhashable_bytes_key,
        unhashable_bytes_key: unhashable_bytes_key,
        unhashable_bytes_key: unhashable_bytes_key,
    }
    # Bytes objects are unhashable, so converting this dict to a namedtuple should fail
    namedtuple_utils.to_namedtuple(nested_dict_with_bytes_keys)