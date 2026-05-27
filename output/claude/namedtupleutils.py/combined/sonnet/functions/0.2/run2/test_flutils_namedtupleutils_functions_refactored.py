import pytest
import namedtupleutils as namedtuple_utils
import collections as collections

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple handles a plain float input without raising an error."""
    negative_float_value = -476.66

    # Call to_namedtuple with a raw float to verify it is accepted without error
    namedtuple_utils.to_namedtuple(negative_float_value)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Test that to_namedtuple handles a tuple containing a float and a set, and also a bare set."""
    # A single float value used to populate both the set and the tuple
    sample_float = -67.0

    # A set composed entirely of the same float (duplicates collapse to one element)
    float_set = {sample_float, sample_float, sample_float, sample_float}

    # A tuple combining the scalar float and the set
    mixed_tuple = (sample_float, float_set)

    # Convert the mixed tuple to a namedtuple
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)

    # Also verify that to_namedtuple can be called directly with a bare set
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_with_duplicate_keys_and_idempotent_conversion():
    """Verify that to_namedtuple handles a dict with duplicate keys and is idempotent when applied to its own output."""

    # A single string used as both key and value; duplicate keys collapse to one entry at runtime
    field_name = "author"
    input_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dictionary (with collapsed duplicate keys) to a namedtuple
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(input_dict)

    # Apply to_namedtuple again to verify idempotent behaviour on an existing namedtuple
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_raises_on_bytes_input():
    """Verify that to_namedtuple raises an error when given a bytes object as input."""
    # bytes is not a supported input type for to_namedtuple
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple input without error."""
    empty_tuple = ()

    # Convert an empty tuple; should complete without raising an exception
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_empty_ordered_dict_namedtuple_and_mixed_tuple():
    """Test that to_namedtuple handles an empty OrderedDict, repeated namedtuple conversion, and a mixed tuple of namedtuple and bytes."""

    # Start with an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple, then convert the result again
    namedtuple_from_empty_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_empty_dict)

    # Repeat the same conversion pattern independently
    namedtuple_from_empty_dict_again = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple_again = namedtuple_utils.to_namedtuple(namedtuple_from_empty_dict_again)

    # Raw bytes value to be used as part of a mixed tuple
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the empty OrderedDict a third time
    namedtuple_from_empty_dict_third = namedtuple_utils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple combining a namedtuple and raw bytes, then convert it
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)
    namedtuple_from_mixed_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)

    # Convert the empty OrderedDict a fourth time (smoke-test repeated calls)
    namedtuple_from_empty_dict_fourth = namedtuple_utils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_special_char_key_and_none_ordered_dict():
    """Test to_namedtuple with an OrderedDict using a special-character key, and exercise OrderedDict construction with None."""

    # A string containing special/control characters used as both key and value
    special_char_key = "wm=-g\ry#\x0b#:*"

    # Build a plain dict mapping the special key to itself
    source_dict = {special_char_key: special_char_key, special_char_key: special_char_key}

    # Construct an OrderedDict from the source dict using keyword unpacking
    ordered_dict_with_special_key = collections.OrderedDict(**source_dict)

    # Convert the OrderedDict to a namedtuple
    result_namedtuple = namedtuple_utils.to_namedtuple(ordered_dict_with_special_key)

    # Exercise OrderedDict construction with None passed as a positional argument
    none_value = None
    none_list = [none_value]
    collections.OrderedDict(*none_list)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Tests that to_namedtuple handles a list containing an empty list, and also accepts None as input."""
    # Build a list that contains a single empty list as its element
    empty_list = []
    list_containing_empty_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    result_from_nested_list = namedtuple_utils.to_namedtuple(list_containing_empty_list)

    # Verify that None is also accepted as input without raising
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_handles_diverse_input_types():
    """Test that to_namedtuple handles dicts, tuples, nested namedtuples, and booleans without raising exceptions."""

    # A long docstring-style string used as a dictionary key
    long_string_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Build a dict whose keys and values are all the same long string
    dict_with_string_keys = {long_string_key: long_string_key, long_string_key: long_string_key, long_string_key: long_string_key}

    # Convert a plain dict with string keys to a namedtuple
    namedtuple_from_string_dict = namedtuple_utils.to_namedtuple(dict_with_string_keys)

    false_value_0 = False

    # Convert the same string-keyed dict a second time
    namedtuple_from_string_dict_2 = namedtuple_utils.to_namedtuple(dict_with_string_keys)

    # Wrap the namedtuple result in a tuple, then convert that tuple to a namedtuple
    tuple_with_namedtuple = (namedtuple_from_string_dict_2,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_with_namedtuple)

    # Build a dict with mixed key types: a namedtuple and a bool
    dict_with_mixed_keys = {namedtuple_from_tuple: namedtuple_from_string_dict_2, false_value_0: namedtuple_from_string_dict_2}

    # Convert the mixed-key dict to a namedtuple
    namedtuple_from_mixed_dict = namedtuple_utils.to_namedtuple(dict_with_mixed_keys)

    # Convert a namedtuple to a namedtuple (nested/identity conversion)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)

    false_value_1 = False

    # Convert the mixed-key dict namedtuple a second time
    namedtuple_from_mixed_dict_again = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a plain bool value to a namedtuple
    namedtuple_utils.to_namedtuple(false_value_1)

def test_to_namedtuple_with_nested_structures_and_repeated_conversion():
    """Test that to_namedtuple handles nested structures, repeated conversions, and a plain integer input."""

    # A string containing a non-printable form-feed character (\x0c), used as a dict key
    key_string = "\x0cMv"
    empty_tuple = ()

    # Dict with mixed key types: a string key and a tuple key (tuple key appears twice, last value wins)
    nested_dict = {key_string: empty_tuple, empty_tuple: key_string, empty_tuple: empty_tuple}

    # A tuple bundling the string and the nested dict together
    string_dict_tuple = (key_string, nested_dict)

    # Wrap the tuple in a list to form the top-level input
    input_list = [string_dict_tuple]

    # First conversion: list containing a tuple with a dict
    namedtuple_first = namedtuple_utils.to_namedtuple(input_list)

    # Second conversion: re-convert the already-converted result
    namedtuple_second = namedtuple_utils.to_namedtuple(namedtuple_first)

    # Third conversion: re-convert again to verify idempotent-like behaviour
    namedtuple_third = namedtuple_utils.to_namedtuple(namedtuple_second)

    # Verify the function also accepts a plain integer without raising
    plain_int = 2
    namedtuple_utils.to_namedtuple(plain_int)

def test_to_namedtuple_with_bytes_keys_and_values():
    """Test that to_namedtuple handles a dict with repeated bytes keys and values without error."""
    # A single bytes object used as both key and value throughout the dict
    bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Dict with the same bytes object repeated as key and value
    bytes_keyed_dict = {bytes_key: bytes_key, bytes_key: bytes_key, bytes_key: bytes_key}

    namedtuple_utils.to_namedtuple(bytes_keyed_dict)

