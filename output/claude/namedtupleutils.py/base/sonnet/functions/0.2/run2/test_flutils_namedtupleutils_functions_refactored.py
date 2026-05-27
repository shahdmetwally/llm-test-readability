import pytest
import namedtupleutils as namedtupleutils
import collections as collections

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple raises an error when given a plain float value."""
    invalid_input = -476.66

    # Floats are not convertible to namedtuples; expect an error to be raised
    namedtupleutils.to_namedtuple(invalid_input)

def test_to_namedtuple_with_nested_tuple_containing_set():
    """Test that to_namedtuple handles a tuple containing a set,
    and also handles a plain set as input, without raising errors."""

    # A single float value used to construct both the set and the outer tuple
    sample_float = -67.0

    # A set with a single unique float (duplicates collapse in a set)
    sample_set = {sample_float, sample_float, sample_float, sample_float}

    # A tuple nesting the float and the set together
    nested_tuple = (sample_float, sample_set)

    # Convert the nested tuple to a namedtuple
    result = namedtupleutils.to_namedtuple(nested_tuple)

    # Also exercise to_namedtuple directly with a plain set
    namedtupleutils.to_namedtuple(sample_set)

def test_to_namedtuple_with_duplicate_keys_and_namedtuple_input():
    """Test that to_namedtuple handles a dict with duplicate keys and that
    passing an already-converted namedtuple through to_namedtuple is idempotent."""

    # A dict with duplicate keys collapses to a single entry in Python
    field_name = "author"
    author_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dict to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(author_dict)

    # Pass the resulting namedtuple back through to_namedtuple (idempotency check)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_raises_on_bytes_input():
    """Test that to_namedtuple raises an error when given a bytes object instead of a supported type."""
    # bytes is not a valid input type for to_namedtuple conversion
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtupleutils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that converting an empty tuple to a namedtuple succeeds without error."""
    empty_tuple = ()
    result = namedtupleutils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_repeated_empty_dict_and_mixed_tuple():
    """Test that to_namedtuple handles repeated conversions of an empty OrderedDict,
    and correctly processes a mixed tuple containing a namedtuple and a bytes object."""

    # Create an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert the resulting namedtuple again (idempotency check)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

    # Repeat conversion of the empty OrderedDict
    namedtuple_from_dict_again = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert the repeated result once more
    namedtuple_from_namedtuple_again = namedtupleutils.to_namedtuple(namedtuple_from_dict_again)

    # Define a raw bytes object to be used as part of a mixed tuple
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the empty OrderedDict once more (additional repeated conversion)
    namedtuple_from_dict_third = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple containing a namedtuple and a bytes object
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)

    # Convert the mixed tuple to a namedtuple
    namedtuple_from_mixed_tuple = namedtupleutils.to_namedtuple(mixed_tuple)

    # Convert the empty OrderedDict one final time
    namedtuple_from_dict_final = namedtupleutils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_ordered_dict_containing_special_key():
    """Test that to_namedtuple handles an OrderedDict with a special-character key,
    and that constructing an OrderedDict with None as a positional argument is valid."""

    # A string key containing special/control characters
    special_key = "wm=-g\ry#\x0b#:*"

    # Build a regular dict using the special key (duplicate keys collapse to one entry)
    raw_dict = {special_key: special_key, special_key: special_key}

    # Create an OrderedDict from the special-key dict via keyword unpacking
    ordered_dict = collections.OrderedDict(**raw_dict)

    # Convert the OrderedDict to a namedtuple; verifies to_namedtuple accepts OrderedDicts
    var_0 = namedtupleutils.to_namedtuple(ordered_dict)

    # Construct a second OrderedDict by passing None as a positional argument
    none_value = None
    positional_args = [none_value]
    collections.OrderedDict(*positional_args)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Test that to_namedtuple handles a list containing an empty list,
    and also accepts None as input without raising an error."""
    # Create a nested structure: a list containing one empty list
    empty_list = []
    nested_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    namedtupleutils.to_namedtuple(nested_list)

    # Also verify that None is accepted as input
    none_value = None
    namedtupleutils.to_namedtuple(none_value)

def test_to_namedtuple_with_various_input_types():
    """Test that to_namedtuple handles dicts, tuples, namedtuples, and primitives
    without raising errors, including nested and repeated conversions."""

    # A long descriptive string used as a dict key/value (simulates real-world data)
    path_docstring = (
        "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n"
        "    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n"
        "       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n"
        "    #. :obj:`PosixPath <pathlib.PosixPath>` and\n"
        "       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n"
        "       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n"
        "       method.\n"
        "    #. An initial component of ``~`` will be replaced by that user's\n"
        "       home directory.\n"
        "    #. Any environment variables will be expanded.\n"
        "    #. Non absolute paths will have the current working directory from\n"
        "       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n"
        "       :obj:`os.chdir() <os.chdir>` to change the current working directory\n"
        "       before calling this function.\n"
        "    #. Redundant separators and up-level references will be normalized, so\n"
        "       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n"
        "       ``A/B``.\n\n"
        "    Args:\n"
        "        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n"
        "            The path to be normalized.\n\n"
        "    :rtype:\n"
        "        :obj:`Path <pathlib.Path>`\n\n"
        "        * :obj:`PosixPath <pathlib.PosixPath>` or\n"
        "          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n"
        "        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n"
        "           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n"
        "           the same object returned.\n\n"
        "    Example:\n\n"
        "        >>> from flutils.pathutils import normalize_path\n"
        "        >>> normalize_path('~/tmp/foo/../bar')\n"
        "        PosixPath('/home/test_user/tmp/bar')\n\n"
        "    "
    )

    # Convert a dict with repeated string keys/values to a namedtuple
    str_keyed_dict = {path_docstring: path_docstring, path_docstring: path_docstring, path_docstring: path_docstring}
    namedtuple_from_str_dict = namedtupleutils.to_namedtuple(str_keyed_dict)

    false_value = False

    # Convert the same dict again to produce a second namedtuple
    second_namedtuple_from_str_dict = namedtupleutils.to_namedtuple(str_keyed_dict)

    # Wrap the namedtuple in a tuple and convert that tuple to a namedtuple
    tuple_wrapping_namedtuple = (second_namedtuple_from_str_dict,)
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_wrapping_namedtuple)

    # Build a dict keyed by a namedtuple and a bool, then convert to namedtuple
    mixed_key_dict = {namedtuple_from_tuple: second_namedtuple_from_str_dict, false_value: second_namedtuple_from_str_dict}
    namedtuple_from_mixed_dict = namedtupleutils.to_namedtuple(mixed_key_dict)

    # Convert an already-converted namedtuple again (idempotency check)
    namedtuple_reconverted = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    false_value_2 = False

    # Convert the mixed-key namedtuple once more
    namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a plain bool value — should handle primitives gracefully
    namedtupleutils.to_namedtuple(false_value_2)

def test_to_namedtuple_with_nested_structures_and_repeated_conversion():
    """Test that to_namedtuple handles nested structures (list containing a tuple with a dict),
    repeated conversion of already-converted results, and a plain integer input."""

    # Build a dict with mixed key types (string and tuple) and a nested tuple value
    key_str = "\x0cMv"
    empty_tuple = ()
    nested_dict = {key_str: empty_tuple, empty_tuple: key_str, empty_tuple: empty_tuple}

    # Wrap the string and dict together in a tuple, then place it in a list
    str_dict_pair = (key_str, nested_dict)
    input_list = [str_dict_pair]

    # First conversion: list containing a tuple with a nested dict
    result_first = namedtupleutils.to_namedtuple(input_list)

    # Second conversion: re-convert the already-converted result
    result_second = namedtupleutils.to_namedtuple(result_first)

    # Third conversion: re-convert again to verify idempotent-like behaviour
    result_third = namedtupleutils.to_namedtuple(result_second)

    # Conversion of a plain integer (non-collection type)
    plain_int = 2
    namedtupleutils.to_namedtuple(plain_int)

def test_to_namedtuple_with_duplicate_bytes_keys():
    """Test that to_namedtuple handles a dict with duplicate bytes keys without error."""
    # A bytes object used as the sole (repeated) key and value in the dict
    bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Python dicts deduplicate keys, so this effectively has one entry: {bytes_key: bytes_key}
    dict_with_bytes_keys = {bytes_key: bytes_key, bytes_key: bytes_key, bytes_key: bytes_key}

    namedtupleutils.to_namedtuple(dict_with_bytes_keys)

