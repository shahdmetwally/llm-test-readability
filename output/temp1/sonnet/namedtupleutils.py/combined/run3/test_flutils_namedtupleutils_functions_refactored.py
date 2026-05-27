import pytest
import namedtupleutils as namedtupleutils
import collections as collections

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple is called with a float scalar value."""
    float_input = -476.66

    # Invoke to_namedtuple with a plain float to exercise scalar input handling
    namedtupleutils.to_namedtuple(float_input)

def test_to_namedtuple_with_tuple_and_set_inputs():
    """Test that to_namedtuple handles a tuple-of-(float, set) and a bare set without error."""

    # A single float value used to construct both inputs
    sample_float = -67.0

    # A set composed entirely of the same float (deduplicates to one element)
    float_set = {sample_float, sample_float, sample_float, sample_float}

    # A tuple combining the float and the set
    float_and_set_tuple = (sample_float, float_set)

    # Convert the tuple (containing a float and a set) to a namedtuple
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(float_and_set_tuple)

    # Also verify that a bare set can be passed to to_namedtuple without error
    namedtupleutils.to_namedtuple(float_set)

def test_to_namedtuple_with_duplicate_keys_and_idempotent_conversion():
    """Test that to_namedtuple handles a dict with duplicate keys and is idempotent on an already-converted namedtuple."""
    # A single field name used as both key and value
    field_name = "author"

    # Python collapses duplicate keys in a dict literal to a single entry: {"author": "author"}
    input_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dict (with effectively one key) to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(input_dict)

    # Apply to_namedtuple again to verify idempotency on an already-converted namedtuple
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_raises_or_handles_bytes_input():
    """Test that to_namedtuple handles a raw bytes object as input."""
    # Bytes is not a typical structured input for to_namedtuple;
    # this exercises behaviour with an unsupported/unexpected input type.
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtupleutils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple as input."""
    # Provide an empty tuple as the input to convert
    empty_tuple = ()

    result = namedtupleutils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_empty_ordered_dict_and_mixed_tuple():
    """Test that to_namedtuple handles empty OrderedDicts, nested namedtuples, and mixed tuples containing bytes without error."""

    # Start with an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple, then convert the result again
    namedtuple_from_empty_dict = namedtupleutils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict)

    # Repeat the same conversion pattern to verify consistent behaviour across multiple calls
    namedtuple_from_empty_dict_2 = namedtupleutils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple_2 = namedtupleutils.to_namedtuple(namedtuple_from_empty_dict_2)

    # Raw bytes value used as a non-dict element in a mixed tuple
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the empty dict once more before building the mixed tuple
    namedtuple_from_empty_dict_3 = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple combining a namedtuple and raw bytes, then convert it
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)
    namedtuple_from_mixed_tuple = namedtupleutils.to_namedtuple(mixed_tuple)

    # Final conversion of the empty OrderedDict to confirm repeated calls remain stable
    namedtuple_from_empty_dict_4 = namedtupleutils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_ordered_dict_and_none_positional_arg():
    """Test that to_namedtuple handles an OrderedDict with special-character keys, and that OrderedDict accepts None as a positional argument."""

    # A string containing special/control characters used as both key and value
    special_char_key = "wm=-g\ry#\x0b#:*"

    # Build a plain dict mapping the special key to itself
    source_dict = {special_char_key: special_char_key, special_char_key: special_char_key}

    # Construct an OrderedDict from the source dict using keyword unpacking
    ordered_dict_input = collections.OrderedDict(**source_dict)

    # Convert the OrderedDict to a namedtuple
    namedtuple_result = namedtupleutils.to_namedtuple(ordered_dict_input)

    # Ensure None can be used as a positional argument when constructing an OrderedDict
    none_value = None
    none_list = [none_value]
    collections.OrderedDict(*none_list)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Test that to_namedtuple handles a list containing an empty list and also accepts None as input."""

    # Build input: a list that contains one element — an empty list
    empty_list = []
    nested_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    result_from_nested_list = namedtupleutils.to_namedtuple(nested_list)

    # Verify that None is also accepted as input without error
    none_value = None
    namedtupleutils.to_namedtuple(none_value)

def test_to_namedtuple_handles_diverse_input_types():
    """Test that to_namedtuple handles diverse input types including string-keyed dicts, tuples, nested namedtuples, and booleans."""

    # A long docstring string used as a dictionary key
    long_docstring_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Dict whose keys and values are all the same long string
    dict_with_long_string_keys = {long_docstring_key: long_docstring_key, long_docstring_key: long_docstring_key, long_docstring_key: long_docstring_key}

    # Convert a plain string-keyed dict to a namedtuple
    namedtuple_from_string_dict = namedtupleutils.to_namedtuple(dict_with_long_string_keys)

    # Boolean value used later as a dict key
    false_dict_key = False

    # Convert the same string-keyed dict again to get a second namedtuple instance
    namedtuple_from_string_dict_2 = namedtupleutils.to_namedtuple(dict_with_long_string_keys)

    # Wrap that namedtuple in a tuple, then convert the tuple to a namedtuple
    tuple_with_namedtuple = (namedtuple_from_string_dict_2,)
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_with_namedtuple)

    # Build a dict with mixed key types: a namedtuple key and a bool key
    dict_with_mixed_keys = {namedtuple_from_tuple: namedtuple_from_string_dict_2, false_dict_key: namedtuple_from_string_dict_2}

    # Convert the mixed-key dict to a namedtuple
    namedtuple_from_mixed_dict = namedtupleutils.to_namedtuple(dict_with_mixed_keys)

    # Convert an already-converted namedtuple to a namedtuple (idempotency check)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # A second boolean input used for a direct conversion call
    false_input = False

    # Convert the namedtuple once more (repeated conversion)
    namedtuple_from_namedtuple_again = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a bare boolean value to a namedtuple
    namedtupleutils.to_namedtuple(false_input)

def test_to_namedtuple_repeated_conversion_and_scalar_input():
    """Tests that to_namedtuple handles repeated conversion of its own output and a plain integer scalar."""

    # Build a nested structure: a dict with mixed key/value types, wrapped in a list
    key_string = "\x0cMv"
    empty_tuple = ()
    nested_dict = {key_string: empty_tuple, empty_tuple: key_string, empty_tuple: empty_tuple}
    mixed_tuple = (key_string, nested_dict)
    input_list = [mixed_tuple]

    # Convert the list to a namedtuple, then convert the result repeatedly
    namedtuple_first = namedtupleutils.to_namedtuple(input_list)
    namedtuple_second = namedtupleutils.to_namedtuple(namedtuple_first)
    namedtuple_third = namedtupleutils.to_namedtuple(namedtuple_second)

    # Verify that a plain integer scalar can also be passed without error
    scalar_int = 2
    namedtupleutils.to_namedtuple(scalar_int)

def test_to_namedtuple_with_bytes_key_and_value_dict():
    """Test that to_namedtuple handles a dict with repeated bytes keys and values without error."""
    # A bytes object used as both the key and the value in the dictionary
    bytes_key_and_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Python deduplicates identical keys, so this effectively produces a single-entry dict
    bytes_keyed_dict = {
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
    }

    namedtupleutils.to_namedtuple(bytes_keyed_dict)