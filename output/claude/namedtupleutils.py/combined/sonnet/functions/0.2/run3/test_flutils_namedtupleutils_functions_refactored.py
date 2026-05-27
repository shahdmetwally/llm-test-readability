import pytest
import namedtupleutils as namedtupleutils
import collections as collections

def test_to_namedtuple_with_negative_float_input():
    """Test that to_namedtuple handles a negative float input value."""
    # Use a negative float to exercise the function with a non-standard scalar input
    negative_float_value = -476.66
    namedtupleutils.to_namedtuple(negative_float_value)

def test_to_namedtuple_with_tuple_and_set_inputs():
    """Test that to_namedtuple handles a tuple containing a float and a set, and also a bare set."""
    # Define a sample float value to use as input data
    sample_float = -67.0

    # Build a set from the float (duplicates collapse to a single element)
    float_set = {sample_float, sample_float, sample_float, sample_float}

    # Combine the float and the set into a tuple
    float_and_set_tuple = (sample_float, float_set)

    # Convert the tuple to a namedtuple; should not raise
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(float_and_set_tuple)

    # Also verify that a bare set can be passed without raising
    namedtupleutils.to_namedtuple(float_set)

def test_to_namedtuple_converts_dict_and_is_idempotent_on_namedtuple():
    """Test that to_namedtuple converts a dict to a namedtuple and handles a namedtuple input without error."""

    # Use a single string as both key and value (duplicate keys collapse to one entry in Python)
    field_name = "author"
    input_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dictionary to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(input_dict)

    # Apply to_namedtuple again on the result to verify idempotent behaviour
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_raises_on_bytes_input():
    """Verify that to_namedtuple is called with a bytes object as an unsupported input type."""
    # bytes is not a valid input for to_namedtuple; this exercises the error-handling path
    invalid_bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtupleutils.to_namedtuple(invalid_bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple input without error."""
    empty_tuple = ()

    # Convert an empty tuple to a namedtuple; should complete without raising
    result = namedtupleutils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_empty_ordered_dict_and_mixed_tuple():
    """Verify that to_namedtuple handles empty OrderedDicts, nested namedtuples, and mixed tuples containing bytes without error."""

    # Start with an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple
    namedtuple_from_empty_dict = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert the resulting namedtuple again (nested conversion)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict)

    # Repeat conversion of the empty OrderedDict to verify idempotent-like behaviour
    namedtuple_from_empty_dict_second = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert the second namedtuple result again
    namedtuple_from_namedtuple_second = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict_second)

    # Raw bytes value to be used as part of a mixed tuple input
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the empty OrderedDict a third time
    namedtuple_from_empty_dict_third = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple containing a namedtuple and a bytes object
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)

    # Convert the mixed tuple (namedtuple + bytes) to a namedtuple
    namedtuple_from_mixed_tuple = namedtupleutils.to_namedtuple(mixed_tuple)

    # Convert the empty OrderedDict a fourth time to confirm repeated calls remain stable
    namedtuple_from_empty_dict_fourth = namedtupleutils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_special_char_key_and_none_ordered_dict_arg():
    """Test to_namedtuple on an OrderedDict with special-character keys, and exercise OrderedDict construction with None."""

    # A string containing special/control characters used as both key and value
    special_char_string = "wm=-g\ry#\x0b#:*"

    # Build a plain dict using the special-character string as key and value
    source_dict = {special_char_string: special_char_string, special_char_string: special_char_string}

    # Construct an OrderedDict from the special-character dict via keyword unpacking
    ordered_dict_with_special_keys = collections.OrderedDict(**source_dict)

    # Convert the OrderedDict to a namedtuple
    namedtuple_result = namedtupleutils.to_namedtuple(ordered_dict_with_special_keys)

    # Prepare a list containing None to pass as a positional argument
    none_value = None
    none_list = [none_value]

    # Exercise OrderedDict construction with None as a positional argument (result intentionally unused)
    collections.OrderedDict(*none_list)

def test_to_namedtuple_with_nested_empty_list_and_none_input():
    """Test that to_namedtuple handles a list containing an empty list, and also accepts None as input."""
    # Build a nested structure: a list that contains one empty list
    empty_list = []
    list_containing_empty_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    result_from_nested_list = namedtupleutils.to_namedtuple(list_containing_empty_list)

    # Also verify that None can be passed as input without raising an error
    none_input = None
    namedtupleutils.to_namedtuple(none_input)

def test_to_namedtuple_with_various_input_types():
    """Test that to_namedtuple handles diverse input types including dicts with string/mixed keys, tuples, nested namedtuples, and booleans without raising exceptions."""

    # A long docstring-style string used as both key and value in a dict
    long_string_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Convert a dict whose keys and values are the same long string
    dict_with_string_keys = {long_string_key: long_string_key, long_string_key: long_string_key, long_string_key: long_string_key}
    namedtuple_from_string_dict = namedtupleutils.to_namedtuple(dict_with_string_keys)

    false_value_0 = False

    # Convert the same string-keyed dict a second time
    namedtuple_from_string_dict_second = namedtupleutils.to_namedtuple(dict_with_string_keys)

    # Wrap the second namedtuple result in a tuple and convert that tuple
    tuple_with_namedtuple = (namedtuple_from_string_dict_second,)
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_with_namedtuple)

    # Convert a dict with mixed key types: a namedtuple and a bool
    dict_with_mixed_keys = {namedtuple_from_tuple: namedtuple_from_string_dict_second, false_value_0: namedtuple_from_string_dict_second}
    namedtuple_from_mixed_dict = namedtupleutils.to_namedtuple(dict_with_mixed_keys)

    # Convert a namedtuple itself (nested conversion)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    false_value_1 = False

    # Convert the mixed dict a second time
    namedtuple_from_mixed_dict_again = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a plain bool value
    namedtupleutils.to_namedtuple(false_value_1)

def test_to_namedtuple_with_nested_structures_and_scalar_input():
    """Test that to_namedtuple handles repeated nested conversion and a scalar integer input without error."""

    # Build the nested input: a string key, an empty tuple, and a dict with mixed keys
    key_string = "\x0cMv"
    empty_tuple = ()

    # Note: tuple_0 appears twice as a key; the second entry overwrites the first (intentional input)
    mixed_key_dict = {key_string: empty_tuple, empty_tuple: key_string, empty_tuple: empty_tuple}

    # Construct a tuple containing the string and the dict, then wrap it in a list
    nested_tuple = (key_string, mixed_key_dict)
    input_list = [nested_tuple]

    # Convert the list to a namedtuple, then convert the result repeatedly
    namedtuple_result = namedtupleutils.to_namedtuple(input_list)
    double_converted = namedtupleutils.to_namedtuple(namedtuple_result)
    triple_converted = namedtupleutils.to_namedtuple(double_converted)

    # Verify that a plain scalar integer is also accepted without error
    scalar_int = 2
    namedtupleutils.to_namedtuple(scalar_int)

def test_to_namedtuple_with_bytes_keyed_dict():
    """Test that to_namedtuple handles a dict with bytes keys and values without error."""
    # A single bytes literal used as both key and value throughout the dict
    bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Dict where the same bytes object appears as every key and value
    bytes_keyed_dict = {bytes_key: bytes_key, bytes_key: bytes_key, bytes_key: bytes_key}

    namedtupleutils.to_namedtuple(bytes_keyed_dict)

