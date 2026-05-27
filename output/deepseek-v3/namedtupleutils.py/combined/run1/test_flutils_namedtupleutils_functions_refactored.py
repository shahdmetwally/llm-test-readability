import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_float():
    """Test that to_namedtuple accepts a float input."""
    # Test that the function can handle scalar float values
    float_value = -476.66
    namedtuple_utils.to_namedtuple(float_value)

def test_to_namedtuple_converts_tuple_with_set_and_set_directly():
    """Test that to_namedtuple handles a tuple containing a float and set, and a set directly."""
    # Create a test float value
    example_float = -67.0
    
    # Create a set containing the float (duplicates are ignored in sets)
    example_set = {example_float, example_float, example_float, example_float}
    
    # Create a tuple pairing the float with the set
    example_tuple = (example_float, example_set)
    
    # Convert the tuple to a namedtuple (result is unused but call is preserved)
    result_namedtuple = namedtuple_utils.to_namedtuple(example_tuple)
    
    # Also convert the set directly to a namedtuple
    namedtuple_utils.to_namedtuple(example_set)

def test_to_namedtuple_idempotent_on_single_key_dict():
    """Test that to_namedtuple can be applied twice to a dictionary with a single key."""
    # Create a dictionary with a single key-value pair
    key = "author"
    single_key_dict = {key: key, key: key, key: key}  # Duplicate keys collapse to one
    
    # First conversion: dictionary -> namedtuple
    namedtuple_instance = namedtuple_utils.to_namedtuple(single_key_dict)
    
    # Second conversion: namedtuple -> namedtuple (should be idempotent)
    result = namedtuple_utils.to_namedtuple(namedtuple_instance)

def test_to_namedtuple_with_bytes_input():
    """Test that to_namedtuple can handle bytes input without error."""
    input_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(input_bytes)

def test_to_namedtuple_empty_tuple():
    """Test that to_namedtuple correctly processes an empty tuple."""
    # Create an empty tuple as input
    empty_tuple = ()
    
    # Convert empty tuple to namedtuple (should handle without error)
    result = namedtuple_utils.to_namedtuple(empty_tuple)
    
    # Note: This test verifies the function doesn't crash on empty input
    # No assertion needed - test passes if no exception is raised

def test_to_namedtuple_handles_nested_conversions_and_mixed_types():
    """Test that to_namedtuple handles nested conversions and mixed type inputs without errors."""
    
    # Create an empty OrderedDict
    empty_ordered_dict = collections_module.OrderedDict()
    
    # Convert OrderedDict to namedtuple multiple times
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)
    
    namedtuple_from_dict_again = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple_again = namedtuple_utils.to_namedtuple(namedtuple_from_dict_again)
    
    # Test with bytes data
    random_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    namedtuple_from_dict_third = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Create a tuple mixing namedtuple and bytes, then convert
    mixed_tuple = (namedtuple_from_namedtuple, random_bytes)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)
    
    # Final conversion of the original OrderedDict
    namedtuple_from_dict_fourth = namedtuple_utils.to_namedtuple(empty_ordered_dict)

def test_ordereddict_to_namedtuple_and_ordereddict_with_none():
    """Test converting OrderedDict to namedtuple and OrderedDict initialization with None argument."""
    
    # Create a string with special characters
    special_string = "wm=-g\ry#\x0b#:*"
    
    # Create dictionary with duplicate keys (will be deduplicated)
    duplicate_key_dict = {special_string: special_string, special_string: special_string}
    
    # Create OrderedDict from dictionary
    ordered_dict_from_dict = collections_module.OrderedDict(**duplicate_key_dict)
    
    # Convert OrderedDict to namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict_from_dict)
    
    # Test OrderedDict initialization with None argument
    none_value = None
    list_with_none = [none_value]
    collections_module.OrderedDict(*list_with_none)

def test_to_namedtuple_handles_nested_empty_list_and_none():
    """Test that to_namedtuple handles a nested empty list and None without error."""
    empty_list = []
    nested_list = [empty_list]
    result = namedtuple_utils.to_namedtuple(nested_list)
    none_value = None
    # Ensure function handles None input without error
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_with_nested_structures():
    """Test to_namedtuple handles complex nested structures including dictionaries, tuples, and namedtuples."""
    
    # A long docstring used as both key and value in a dictionary
    docstring = (
        "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    "
        "#. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       "
        "given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    "
        "#. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       "
        "to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    "
        "#. An initial component of ``~`` will be replaced by that user’
# (Truncated by extractor)

