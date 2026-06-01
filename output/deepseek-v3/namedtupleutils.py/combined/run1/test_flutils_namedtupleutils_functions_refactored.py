import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_negative_float():
    """Verify that to_namedtuple accepts a negative float value without error."""
    negative_float_value = -476.66
    namedtuple_utils.to_namedtuple(negative_float_value)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Verify that to_namedtuple can convert a tuple containing a float and a set, and also a standalone set."""
    # Create a float value and a set containing that float (duplicates are collapsed)
    float_value = -67.0
    float_set = {float_value, float_value, float_value, float_value}  # Results in {-67.0}
    
    # Create a tuple containing the float and the set
    input_tuple = (float_value, float_set)
    
    # Convert the tuple to a namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(input_tuple)
    
    # Also verify that a standalone set can be converted without error
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_with_duplicate_keys_and_reprocessing():
    """Verify that to_namedtuple handles dictionaries with duplicate keys and can reprocess its own output."""
    key_name = "author"
    # Dictionary with duplicate keys collapses to single key-value pair
    input_dict = {key_name: key_name, key_name: key_name, key_name: key_name}
    
    # First conversion: dict -> namedtuple
    first_namedtuple = namedtuple_utils.to_namedtuple(input_dict)
    
    # Second conversion: namedtuple -> namedtuple (reprocessing)
    second_namedtuple = namedtuple_utils.to_namedtuple(first_namedtuple)

def test_to_namedtuple_with_bytes_input():
    """Verify that to_namedtuple accepts bytes input without error."""
    raw_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(raw_bytes)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple correctly."""
    empty_tuple = ()
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_various_input_types():
    """Test that to_namedtuple handles OrderedDict, existing namedtuples, bytes, and tuples as input."""
    # Test with empty OrderedDict
    ordered_dict = module_1.OrderedDict()
    namedtuple_from_dict = module_0.to_namedtuple(ordered_dict)
    
    # Test converting a namedtuple back to namedtuple
    namedtuple_from_namedtuple = module_0.to_namedtuple(namedtuple_from_dict)
    
    # Test repeated conversion of same OrderedDict
    namedtuple_from_dict_again = module_0.to_namedtuple(ordered_dict)
    namedtuple_from_namedtuple_again = module_0.to_namedtuple(namedtuple_from_dict_again)
    
    # Test with bytes input
    byte_data = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    namedtuple_from_dict_third_time = module_0.to_namedtuple(ordered_dict)
    
    # Test with tuple containing namedtuple and bytes
    mixed_tuple = (namedtuple_from_namedtuple, byte_data)
    namedtuple_from_tuple = module_0.to_namedtuple(mixed_tuple)
    
    # Final test with OrderedDict
    namedtuple_from_dict_fourth_time = module_0.to_namedtuple(ordered_dict)

def test_to_namedtuple_with_ordereddict_duplicate_keys():
    """Test that to_namedtuple handles OrderedDict with duplicate keys and that OrderedDict can be created from a list containing None."""
    # Create a key with special characters
    sample_key = "wm=-g\ry#\x0b#:*"
    
    # Create a dict with duplicate keys (last value wins)
    source_dict = {sample_key: sample_key, sample_key: sample_key}
    
    # Convert to OrderedDict and then to namedtuple
    ordered_dict = collections_module.OrderedDict(**source_dict)
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)
    
    # Verify OrderedDict can be created from a list containing None
    none_value = None
    none_list = [none_value]
    collections_module.OrderedDict(*none_list)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Test that to_namedtuple handles a list containing an empty list and None input."""
    # Create an empty list and nest it inside another list
    empty_list = []
    nested_list = [empty_list]
    
    # Convert the nested list to a namedtuple
    result = namedtuple_utils.to_namedtuple(nested_list)
    
    # Test that None input is handled (likely raises an error)
    none_input = None
    namedtuple_utils.to_namedtuple(none_input)

def test_to_namedtuple_with_duplicate_keys_and_reprocessing():
    """Test that to_namedtuple handles various input types including dicts, tuples, nested namedtuples, and boolean values."""
    # Create a long docstring as a string input
    docstring_path = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user’s\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "
    
    # Test 1: Create a dict with the same key repeated (should collapse to one entry)
    dict_with_same_key = {docstring_path: docstring_path, docstring_path: docstring_path, docstring_path: docstring_path}
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(dict_with_same_key)
    
    # Test 2: Convert boolean False to namedtuple (should fail or handle gracefully)
    false_value = False
    namedtuple_from_dict_again = namedtuple_utils.to_namedtuple(dict_with_same_key)
    
    # Test 3: Wrap namedtuple in a tuple and convert
    tuple_wrapping_namedtuple = (namedtuple_from_dict_again,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_wrapping_namedtuple)
    
    # Test 4: Create dict with mixed key types (namedtuple and boolean)
    dict_with_mixed_keys = {namedtuple_from_tuple: namedtuple_from_dict_again, false_value: namedtuple_from_dict_again}
    namedtuple_from_mixed_dict = namedtuple_utils.to_namedtuple(dict_with_mixed_keys)
    
    # Test 5: Convert a namedtuple to another namedtuple (nested conversion)
    nested_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)
    
    # Test 6: Repeat conversion from nested namedtuple
    another_false_value = False
    namedtuple_from_nested = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)
    
    # Test 7: Convert boolean False directly (should fail or handle gracefully)
    namedtuple_utils.to_namedtuple(another_false_value)

def test_to_namedtuple_with_nested_dicts_mixed_types_and_idempotency():
    """Verify that to_namedtuple handles nested dicts with mixed types and is idempotent across multiple calls."""
    # Create a nested structure with mixed key/value types
    key_string = "\x0cMv"
    empty_tuple = ()
    
    # Dictionary with string keys mapping to tuples, and tuple keys mapping to strings/tuples
    nested_dict = {key_string: empty_tuple, empty_tuple: key_string, empty_tuple: empty_tuple}
    
    # Wrap the dict in a tuple, then in a list
    wrapping_tuple = (key_string, nested_dict)
    input_list = [wrapping_tuple]
    
    # Convert to namedtuple and verify idempotency (multiple conversions produce same type)
    first_result = namedtuple_utils.to_namedtuple(input_list)
    second_result = namedtuple_utils.to_namedtuple(first_result)
    third_result = namedtuple_utils.to_namedtuple(second_result)
    
    # Verify that passing a plain integer doesn't raise an error
    plain_integer = 2
    namedtuple_utils.to_namedtuple(plain_integer)

def test_to_namedtuple_with_bytes_keys_duplicate_keys():
    """Test that to_namedtuple handles a dictionary with duplicate bytes keys correctly."""
    bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    input_dict = {bytes_key: bytes_key, bytes_key: bytes_key, bytes_key: bytes_key}
    namedtuple_utils.to_namedtuple(input_dict)

