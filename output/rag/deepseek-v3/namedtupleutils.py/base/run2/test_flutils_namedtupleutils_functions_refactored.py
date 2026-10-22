import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_rejects_float(self):
    """Calling to_namedtuple with a float should raise an error."""
    input_value = -476.66
    with self.assertRaises(TypeError):
        namedtuple_utils.to_namedtuple(input_value)

def test_to_namedtuple_with_tuple_containing_set():
    """Test that to_namedtuple handles a tuple containing a set of floats."""
    float_value = -67.0
    float_set = {float_value, float_value, float_value, float_value}
    input_tuple = (float_value, float_set)
    result = namedtuple_utils.to_namedtuple(input_tuple)
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_with_duplicate_keys_in_dict():
    """Verify that to_namedtuple converts a dict with duplicate keys to a namedtuple,
    and that the result can be recursively converted again."""
    key = "author"
    # Dict with duplicate keys (only last key-value pair is kept in Python)
    input_dict = {key: key, key: key, key: key}
    result = namedtuple_utils.to_namedtuple(input_dict)
    # Recursively convert the namedtuple back to a namedtuple
    result_again = namedtuple_utils.to_namedtuple(result)

def test_to_namedtuple_with_bytes_input():
    """Test that to_namedtuple can handle bytes input without error."""
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple returns a namedtuple when given an empty tuple."""
    empty_tuple = ()
    var_0 = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_idempotency_with_various_inputs():
    """Test that to_namedtuple handles OrderedDict, its own output (idempotency),
    and tuple inputs correctly."""
    # Create an empty OrderedDict
    ordered_dict_0 = collections_module.OrderedDict()

    # First conversion from OrderedDict to namedtuple
    var_0 = namedtuple_utils.to_namedtuple(ordered_dict_0)

    # Second conversion should be idempotent (namedtuple -> namedtuple)
    var_1 = namedtuple_utils.to_namedtuple(var_0)

    # Convert original OrderedDict again to namedtuple
    var_2 = namedtuple_utils.to_namedtuple(ordered_dict_0)

    # Convert the second namedtuple result (should also be idempotent)
    var_3 = namedtuple_utils.to_namedtuple(var_2)

    # Some arbitrary bytes data
    bytes_0 = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the original OrderedDict once more
    var_4 = namedtuple_utils.to_namedtuple(ordered_dict_0)

    # Form a tuple containing a namedtuple and bytes
    tuple_0 = (var_1, bytes_0)

    # Convert that mixed tuple to namedtuple
    var_5 = namedtuple_utils.to_namedtuple(tuple_0)

    # Final conversion of the original OrderedDict
    var_6 = namedtuple_utils.to_namedtuple(ordered_dict_0)

def test_to_namedtuple_with_ordered_dict_containing_identical_control_characters():
    """Test that to_namedtuple correctly processes an OrderedDict with control character keys."""
    # Setup
    control_char_key = "wm=-g\ry#\x0b#:*"
    dict_with_same_key = {control_char_key: control_char_key, control_char_key: control_char_key}
    ordered_dict = collections_module.OrderedDict(**dict_with_same_key)

    # Act
    result_namedtuple = namedtuple_utils.to_namedtuple(ordered_dict)

    # Additional setup for a subsequent call (preserving original behavior)
    none_value = None
    list_with_none = [none_value]
    collections_module.OrderedDict(*list_with_none)

def test_to_namedtuple_handles_none_and_nested_lists():
    """Test that to_namedtuple correctly handles a list containing an empty list
    and a None value without raising exceptions."""
    empty_list = []
    list_containing_empty_list = [empty_list]
    result = namedtuple_utils.to_namedtuple(list_containing_empty_list)
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_with_string_keys_and_nested_conversion():
    """Test that to_namedtuple handles dicts with string docstring keys,
    converts tuples, and handles nested namedtuple conversions correctly,
    including edge cases with boolean keys."""
    docstring_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user’s\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "
    # Create a dict with the same string as both key and value (repeated)
    dict_with_string_keys = {docstring_key: docstring_key, docstring_key: docstring_key, docstring_key: docstring_key}
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(dict_with_string_keys)

    false_bool = False
    # Convert the same dict again
    second_namedtuple = namedtuple_utils.to_namedtuple(dict_with_string_keys)

    # Wrap the second namedtuple in a tuple and convert that tuple
    tuple_wrapping_namedtuple = (second_namedtuple,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_wrapping_namedtuple)

    # Create a mixed dict with namedtuple key, boolean key, both pointing to same namedtuple value
    mixed_dict = {namedtuple_from_tuple: second_namedtuple, false_bool: second_namedtuple}
    namedtuple_from_mixed = namedtuple_utils.to_namedtuple(mixed_dict)

    # Convert the namedtuple itself (nested conversion)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_mixed)

    another_false_bool = False
    # Convert the namedtuple again
    namedtuple_from_namedtuple_again = namedtuple_utils.to_namedtuple(namedtuple_from_mixed)

    # Edge case: convert a plain boolean value (False)
    namedtuple_utils.to_namedtuple(another_false_bool)

def test_to_namedtuple_with_nested_dict_and_list_conversion_stability():
    """Test that to_namedtuple correctly converts a list containing a tuple
    with a nested dictionary that has mixed key/value types, and subsequent
    conversions of the result remain stable."""
    # Create a string key for the dictionary
    str_key = "\x0cMv"
    # Empty tuple to serve as both a key and value in the dictionary
    empty_tuple = ()
    # Dictionary with mixed types: string key -> tuple, tuple key -> string, tuple key -> tuple
    nested_dict = {str_key: empty_tuple, empty_tuple: str_key, empty_tuple: empty_tuple}
    # Wrap in a tuple along with the original string
    inner_tuple = (str_key, nested_dict)
    # Create list containing the tuple
    input_list = [inner_tuple]
    
    # Convert list to namedtuple
    result_1 = namedtuple_utils.to_namedtuple(input_list)
    # Convert the result again to verify stability
    result_2 = namedtuple_utils.to_namedtuple(result_1)
    # Convert a third time to ensure idempotent behavior
    result_3 = namedtuple_utils.to_namedtuple(result_2)
    
    # Test that conversion of a plain integer raises appropriate error
    int_value = 2
    namedtuple_utils.to_namedtuple(int_value)

def test_to_namedtuple_converts_dict_with_bytes_keys_and_values():
    """Verify that `to_namedtuple` can handle a dictionary with bytes as both keys and values."""
    bytes_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    dict_with_bytes = {bytes_value: bytes_value, bytes_value: bytes_value, bytes_value: bytes_value}
    namedtuple_utils.to_namedtuple(dict_with_bytes)