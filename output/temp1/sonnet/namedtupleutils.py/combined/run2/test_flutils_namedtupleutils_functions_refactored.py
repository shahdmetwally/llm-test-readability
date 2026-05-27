import pytest
import namedtupleutils as namedtupleutils
import collections as collections

def test_to_namedtuple_with_float_scalar_input():
    """Test that to_namedtuple handles a negative float scalar (non-iterable) input."""
    # A bare float is a non-collection scalar — an edge case for to_namedtuple
    float_scalar = -476.66
    namedtupleutils.to_namedtuple(float_scalar)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Test that to_namedtuple handles a tuple containing a float and a set, and a bare set."""

    # A single float value used to construct both a set and a tuple
    sample_float = -67.0

    # A set built entirely from the same float value
    float_set = {sample_float, sample_float, sample_float, sample_float}

    # A tuple pairing the float with the set
    tuple_with_set = (sample_float, float_set)

    # Convert the tuple (containing a float and a set) to a namedtuple
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_with_set)

    # Also verify that to_namedtuple can handle a plain set input
    namedtupleutils.to_namedtuple(float_set)

def test_to_namedtuple_converts_dict_and_is_idempotent_on_namedtuple():
    """Test that to_namedtuple converts a dict to a namedtuple and can be safely re-applied to an existing namedtuple."""
    # Use "author" as both key and value in the input dictionary
    field_name = "author"
    input_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dictionary to a namedtuple
    namedtuple_result = namedtupleutils.to_namedtuple(input_dict)

    # Re-apply to_namedtuple on the already-converted namedtuple (idempotency check)
    idempotent_result = namedtupleutils.to_namedtuple(namedtuple_result)

def test_to_namedtuple_raises_or_handles_bytes_input():
    """Test that to_namedtuple handles a raw bytes object as input."""
    # Provide a raw bytes value, which is not a supported namedtuple-convertible type
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"

    namedtupleutils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple input without error."""
    empty_tuple = ()

    # Convert the empty tuple to a namedtuple and capture the result
    result = namedtupleutils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_empty_ordered_dict_and_nested_types():
    """Test that to_namedtuple handles an empty OrderedDict, idempotent namedtuple input, and a mixed tuple of namedtuple and bytes."""

    # Start with an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple
    namedtuple_from_empty_dict = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert an already-converted namedtuple (idempotency check)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict)

    # Convert the empty OrderedDict again (statelessness check — no side effects)
    namedtuple_from_empty_dict_again = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert the result of the second conversion (chained idempotency)
    namedtuple_from_namedtuple_again = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict_again)

    # Raw bytes value used as part of a mixed tuple input
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the empty OrderedDict a third time (repeated statelessness check)
    namedtuple_from_empty_dict_third = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple containing a namedtuple and raw bytes
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)

    # Convert the mixed tuple to a namedtuple (heterogeneous input check)
    namedtuple_from_mixed_tuple = namedtupleutils.to_namedtuple(mixed_tuple)

    # Convert the empty OrderedDict a fourth time (final statelessness verification)
    namedtuple_from_empty_dict_fourth = namedtupleutils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_special_char_key_and_ordered_dict_with_none_arg():
    """Test to_namedtuple on an OrderedDict with a special-character key, and that OrderedDict accepts None as a positional arg."""

    # A key containing special/control characters
    special_char_key = "wm=-g\ry#\x0b#:*"

    # Build a plain dict using the special-character key
    dict_with_special_key = {special_char_key: special_char_key, special_char_key: special_char_key}

    # Construct an OrderedDict from the special-character dict
    ordered_dict_with_special_key = collections.OrderedDict(**dict_with_special_key)

    # Convert the OrderedDict to a namedtuple
    namedtuple_result = namedtupleutils.to_namedtuple(ordered_dict_with_special_key)

    # Verify that OrderedDict can be constructed with None as a positional argument
    none_value = None
    none_arg_list = [none_value]
    collections.OrderedDict(*none_arg_list)

def test_to_namedtuple_with_nested_empty_list_and_none_input():
    """Tests that to_namedtuple handles a list containing an empty list and a None input without error."""

    # Build a list that contains a single empty list as its element
    empty_list = []
    list_containing_empty_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    result_namedtuple = namedtupleutils.to_namedtuple(list_containing_empty_list)

    # Also verify that passing None does not raise an unexpected error
    none_value = None
    namedtupleutils.to_namedtuple(none_value)

def test_to_namedtuple_with_nested_and_mixed_input_types():
    """Test that to_namedtuple handles nested structures, mixed-key dicts, tuples, namedtuples, and booleans without error."""

    # A long string used as both key and value in the initial dict
    long_string_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Dict whose keys and values are all the same long string
    string_keyed_dict = {long_string_key: long_string_key, long_string_key: long_string_key, long_string_key: long_string_key}

    # Convert a plain string-keyed dict to a namedtuple
    namedtuple_from_string_dict = namedtupleutils.to_namedtuple(string_keyed_dict)

    false_value = False

    # Convert the same string-keyed dict a second time
    namedtuple_from_string_dict_second = namedtupleutils.to_namedtuple(string_keyed_dict)

    # Wrap the namedtuple result in a tuple, then convert that tuple to a namedtuple
    tuple_with_namedtuple = (namedtuple_from_string_dict_second,)
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_with_namedtuple)

    # Build a dict with mixed key types: a namedtuple and a bool
    mixed_key_dict = {namedtuple_from_tuple: namedtuple_from_string_dict_second, false_value: namedtuple_from_string_dict_second}

    # Convert the mixed-key dict to a namedtuple
    namedtuple_from_mixed_dict = namedtupleutils.to_namedtuple(mixed_key_dict)

    # Convert a namedtuple to a namedtuple (nested namedtuple input)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    another_false_value = False

    # Convert the mixed-key namedtuple a second time
    namedtuple_from_mixed_dict_second = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a plain boolean to a namedtuple
    namedtupleutils.to_namedtuple(another_false_value)

def test_to_namedtuple_with_nested_structures_and_primitive_input():
    """Test that to_namedtuple handles repeated conversion of nested structures and a plain integer input without error."""

    # Build the nested input: a string key, an empty tuple, and a dict with mixed-type keys
    key_str = "\x0cMv"
    empty_tuple = ()

    # Note: dict has duplicate key `empty_tuple`; last value wins, but input must remain as-is
    nested_dict = {key_str: empty_tuple, empty_tuple: key_str, empty_tuple: empty_tuple}

    nested_tuple = (key_str, nested_dict)
    input_list = [nested_tuple]

    # Convert nested list structure to namedtuple representation
    first_conversion = namedtupleutils.to_namedtuple(input_list)

    # Apply conversion again to verify idempotent/re-conversion behaviour
    second_conversion = namedtupleutils.to_namedtuple(first_conversion)

    # Apply a third time to further confirm stability under repeated conversion
    third_conversion = namedtupleutils.to_namedtuple(second_conversion)

    # Verify that a plain integer input is also handled without error
    plain_integer = 2
    namedtupleutils.to_namedtuple(plain_integer)

def test_to_namedtuple_with_bytes_keys_and_values():
    """Test that to_namedtuple handles a dict with identical bytes keys and values."""
    # A single bytes object used as both the key and value throughout the dict
    bytes_key_and_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Construct a dict where the same bytes object appears as every key and value
    bytes_keyed_dict = {
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
    }

    # Convert the bytes-keyed dict to a namedtuple; should not raise
    namedtupleutils.to_namedtuple(bytes_keyed_dict)