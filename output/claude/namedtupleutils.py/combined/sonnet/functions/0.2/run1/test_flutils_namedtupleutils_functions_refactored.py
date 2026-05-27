import pytest
import namedtupleutils as namedtuple_utils
import collections as collections

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple handles a plain float input without raising an error."""
    # Use a negative float to exercise the function with a primitive numeric type
    negative_float_value = -476.66

    namedtuple_utils.to_namedtuple(negative_float_value)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Test that to_namedtuple handles a tuple containing a float and a set, and also a bare set."""

    sample_float = -67.0

    # Duplicate values collapse into a single-element set
    float_set = {sample_float, sample_float, sample_float, sample_float}

    # A tuple combining the float and the set
    mixed_tuple = (sample_float, float_set)

    # Convert the mixed tuple to a namedtuple
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)

    # Also verify to_namedtuple handles a bare set without raising
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_converts_dict_and_is_idempotent_on_namedtuple():
    """Test that to_namedtuple converts a dict to a namedtuple and is idempotent when applied to an existing namedtuple."""
    field_name = "author"

    # Duplicate keys collapse to a single entry {"author": "author"} in Python
    input_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dictionary to a namedtuple
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(input_dict)

    # Apply to_namedtuple again to verify idempotency on an already-converted namedtuple
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_raises_on_bytes_input():
    """Verify that to_namedtuple raises when given a bytes object as input."""
    # bytes is not a supported input type for to_namedtuple
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtuple_utils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple input without error."""
    # An empty tuple is a valid edge-case input for to_namedtuple
    empty_tuple = ()

    # Convert the empty tuple; expect no exception to be raised
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_empty_ordered_dict_namedtuple_and_mixed_tuple():
    """Test that to_namedtuple handles empty OrderedDicts, previously converted namedtuples, and mixed tuples containing bytes."""

    # Create an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple
    namedtuple_from_empty_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)

    # Test idempotency: convert an already-converted namedtuple
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_empty_dict)

    # Repeat conversion of the empty dict to verify consistent behaviour
    namedtuple_from_empty_dict_second = namedtuple_utils.to_namedtuple(empty_ordered_dict)

    # Test idempotency again on the second conversion result
    namedtuple_from_namedtuple_second = namedtuple_utils.to_namedtuple(namedtuple_from_empty_dict_second)

    # Raw bytes value used as part of a mixed tuple input
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the empty dict a third time (repeated-call consistency check)
    namedtuple_from_empty_dict_third = namedtuple_utils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple combining a namedtuple and a bytes object
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)

    # Convert the mixed tuple containing a namedtuple and bytes
    namedtuple_from_mixed_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)

    # Convert the empty dict a fourth time (repeated-call consistency check)
    namedtuple_from_empty_dict_fourth = namedtuple_utils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_ordered_dict_special_key():
    """Test that to_namedtuple converts an OrderedDict with special-character keys,
    and that OrderedDict can be constructed with None as a positional argument."""

    # A string containing special/escape characters used as both key and value
    special_char_key = "wm=-g\ry#\x0b#:*"

    # Build a plain dict using the special-character string as key and value
    source_dict = {special_char_key: special_char_key, special_char_key: special_char_key}

    # Construct an OrderedDict from the source dict using keyword unpacking
    ordered_dict = collections.OrderedDict(**source_dict)

    # Convert the OrderedDict to a namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)

    # Prepare a None value to be passed as a positional argument
    none_value = None
    none_args = [none_value]

    # Exercise OrderedDict construction with None as a positional argument
    collections.OrderedDict(*none_args)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Tests that to_namedtuple handles a list containing an empty list, and also accepts None as input."""

    # Build a list that contains a single empty list as its element
    empty_list = []
    list_containing_empty_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    result_from_nested_list = namedtuple_utils.to_namedtuple(list_containing_empty_list)

    # Verify that to_namedtuple also accepts None without raising an error
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_with_mixed_input_types():
    """Test that to_namedtuple handles dicts with complex string keys, nested namedtuples, tuples, and boolean inputs."""

    # A long docstring string used as both key and value in a dict
    docstring_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Build a dict using the docstring string as both key and value, then convert to namedtuple
    dict_with_docstring_keys = {docstring_key: docstring_key, docstring_key: docstring_key, docstring_key: docstring_key}
    namedtuple_from_docstring_dict = namedtuple_utils.to_namedtuple(dict_with_docstring_keys)

    false_value = False

    # Convert the same dict a second time to get another namedtuple instance
    namedtuple_from_docstring_dict_second = namedtuple_utils.to_namedtuple(dict_with_docstring_keys)

    # Wrap the namedtuple in a tuple, then convert that tuple to a namedtuple
    tuple_with_namedtuple = (namedtuple_from_docstring_dict_second,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_with_namedtuple)

    # Build a dict with namedtuple and bool keys, then convert to namedtuple
    dict_with_namedtuple_keys = {namedtuple_from_tuple: namedtuple_from_docstring_dict_second, false_value: namedtuple_from_docstring_dict_second}
    namedtuple_from_mixed_dict = namedtuple_utils.to_namedtuple(dict_with_namedtuple_keys)

    # Convert an already-converted namedtuple back through to_namedtuple (recursive/idempotent check)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)

    false_value_second = False

    # Convert the mixed-dict namedtuple a second time
    namedtuple_from_namedtuple_second = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)

    # Verify that to_namedtuple handles a plain boolean input without error
    namedtuple_utils.to_namedtuple(false_value_second)

def test_to_namedtuple_with_nested_structures_and_repeated_conversion():
    """Smoke test: verifies to_namedtuple handles nested list/tuple/dict structures, repeated conversions, and a plain integer without raising."""

    # A string containing a form-feed character used as a dict key
    form_feed_string = "\x0cMv"
    empty_tuple = ()

    # Dict with both a string key and a tuple key (duplicate tuple key: last value wins)
    mixed_key_dict = {form_feed_string: empty_tuple, empty_tuple: form_feed_string, empty_tuple: empty_tuple}

    # Nested tuple containing the string and the dict, wrapped in a list
    nested_tuple = (form_feed_string, mixed_key_dict)
    input_list = [nested_tuple]

    # First conversion: list containing a nested tuple/dict structure
    namedtuple_from_list = namedtuple_utils.to_namedtuple(input_list)

    # Second conversion: convert the already-converted result again
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_list)

    # Third conversion: convert the doubly-converted result once more
    namedtuple_from_double_converted = namedtuple_utils.to_namedtuple(namedtuple_from_namedtuple)

    # Verify the function also accepts a plain integer without raising
    plain_integer = 2
    namedtuple_utils.to_namedtuple(plain_integer)

def test_to_namedtuple_with_bytes_key_and_value_dict():
    """Test that to_namedtuple handles a dict with identical bytes keys and values without error."""
    # A bytes object used as both key and value throughout the dict
    bytes_key_and_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Duplicate keys collapse to a single entry at runtime; the result is a one-entry dict
    bytes_keyed_dict = {
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
    }

    namedtuple_utils.to_namedtuple(bytes_keyed_dict)

