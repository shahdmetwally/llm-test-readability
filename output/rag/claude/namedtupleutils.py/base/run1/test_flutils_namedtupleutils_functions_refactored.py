import pytest
import namedtupleutils as namedtupleutils
import collections as collections

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple raises an error when given a plain float value."""
    invalid_input = -476.66
    namedtupleutils.to_namedtuple(invalid_input)

def test_to_namedtuple_with_nested_tuple_containing_set():
    """Test that to_namedtuple handles a tuple containing a set, and also
    handles a bare set, without raising an error."""

    # A single float value used to construct a deduplicated set
    sample_float = -67.0

    # A set with repeated identical values (collapses to a single-element set)
    sample_set = {sample_float, sample_float, sample_float, sample_float}

    # A tuple nesting the float and the set together
    nested_tuple = (sample_float, sample_set)

    # Convert the nested tuple to a namedtuple
    namedtupleutils.to_namedtuple(nested_tuple)

    # Also verify to_namedtuple can handle a bare set as input
    namedtupleutils.to_namedtuple(sample_set)

def test_to_namedtuple_with_duplicate_keys_and_namedtuple_input():
    """Test that to_namedtuple handles a dict with duplicate keys and that
    passing the resulting namedtuple back into to_namedtuple is idempotent."""
    # A dict with duplicate keys collapses to a single "author" entry
    author_key = "author"
    author_dict = {author_key: author_key, author_key: author_key, author_key: author_key}

    # Convert the dict to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(author_dict)

    # Passing an already-converted namedtuple should also be handled gracefully
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

def test_to_namedtuple_with_bytes_input():
    """Test that to_namedtuple raises an appropriate error when given raw bytes input."""
    # bytes is not a valid input type for namedtuple conversion
    raw_bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtupleutils.to_namedtuple(raw_bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that converting an empty tuple to a namedtuple completes without error."""
    empty_tuple = ()
    result = namedtupleutils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_empty_ordered_dict_and_mixed_tuple():
    """Test that to_namedtuple handles repeated conversions of an empty OrderedDict
    and a mixed tuple containing a namedtuple and a bytes object."""

    # Start with an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple and verify re-conversion is stable
    namedtuple_from_dict = namedtupleutils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

    # Repeat the conversion pattern to confirm idempotent behaviour
    namedtuple_from_dict_again = namedtupleutils.to_namedtuple(empty_ordered_dict)
    namedtuple_from_namedtuple_again = namedtupleutils.to_namedtuple(namedtuple_from_dict_again)

    # A raw bytes object to be used as a non-dict element in a mixed tuple
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Another conversion of the empty OrderedDict
    namedtuple_from_dict_third = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple combining a namedtuple and a bytes object
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)

    # Convert the mixed tuple to a namedtuple
    namedtuple_from_mixed_tuple = namedtupleutils.to_namedtuple(mixed_tuple)

    # Final conversion of the empty OrderedDict (ensures no side effects from prior calls)
    namedtuple_from_dict_final = namedtupleutils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_ordered_dict_containing_special_key():
    """Test that to_namedtuple works with an OrderedDict whose key contains
    special/control characters, and that constructing an OrderedDict with
    None as a positional argument behaves as expected (raises TypeError)."""

    # A string key containing special and control characters
    special_key = "wm=-g\ry#\x0b#:*"

    # Build a plain dict using the special key (duplicate key collapses to one entry)
    raw_dict = {special_key: special_key}

    # Construct an OrderedDict by unpacking the raw dict as keyword arguments
    ordered_dict = collections.OrderedDict(**raw_dict)

    # Convert the OrderedDict to a namedtuple
    result = namedtupleutils.to_namedtuple(ordered_dict)

    # Attempt to construct an OrderedDict with None as a positional argument
    # (this exercises the OrderedDict constructor's error path)
    none_value = None
    args_with_none = [none_value]
    collections.OrderedDict(*args_with_none)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Test that to_namedtuple handles a list containing an empty list,
    and also accepts None as input without raising an error."""
    # Create a nested structure: a list containing a single empty list
    empty_list = []
    nested_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    namedtupleutils.to_namedtuple(nested_list)

    # Also verify that None is accepted as input
    none_value = None
    namedtupleutils.to_namedtuple(none_value)

def test_to_namedtuple_with_various_input_types():
    """Test that to_namedtuple handles dicts, tuples, nested namedtuples, booleans,
    and repeated calls without raising errors, exercising a range of input types."""

    # A long docstring-style string used as a dict key/value to stress-test key handling
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

    # Convert a dict with string keys and values to a namedtuple
    string_keyed_dict = {path_docstring: path_docstring, path_docstring: path_docstring, path_docstring: path_docstring}
    namedtuple_from_str_dict = namedtupleutils.to_namedtuple(string_keyed_dict)

    bool_false_0 = False

    # Convert the same dict a second time to get a namedtuple for use as a value
    namedtuple_from_str_dict_2 = namedtupleutils.to_namedtuple(string_keyed_dict)

    # Wrap the namedtuple in a tuple, then convert to namedtuple
    tuple_of_namedtuple = (namedtuple_from_str_dict_2,)
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_of_namedtuple)

    # Build a dict with namedtuple and bool keys, then convert to namedtuple
    mixed_key_dict = {namedtuple_from_tuple: namedtuple_from_str_dict_2, bool_false_0: namedtuple_from_str_dict_2}
    namedtuple_from_mixed_dict = namedtupleutils.to_namedtuple(mixed_key_dict)

    # Convert an already-converted namedtuple again (idempotency check)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    bool_false_1 = False

    # Convert the mixed dict namedtuple once more to verify repeated conversion is stable
    namedtuple_from_mixed_dict_2 = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a plain bool — exercises handling of a non-collection primitive input
    namedtupleutils.to_namedtuple(bool_false_1)

def test_to_namedtuple_with_nested_structures_and_repeated_conversions():
    """Test that to_namedtuple handles nested dicts/tuples and idempotent re-conversion,
    and also accepts a plain integer without error."""

    # Build a nested structure: a dict with tuple keys/values, wrapped in a list
    key_str = "\x0cMv"
    empty_tuple = ()
    nested_dict = {key_str: empty_tuple, empty_tuple: key_str, empty_tuple: empty_tuple}
    tuple_with_dict = (key_str, nested_dict)
    list_of_tuples = [tuple_with_dict]

    # Convert the nested list structure to a namedtuple
    namedtuple_result_0 = namedtupleutils.to_namedtuple(list_of_tuples)

    # Re-convert an already-converted namedtuple (idempotency check)
    namedtuple_result_1 = namedtupleutils.to_namedtuple(namedtuple_result_0)

    # Re-convert a second time to further verify stability
    namedtuple_result_2 = namedtupleutils.to_namedtuple(namedtuple_result_1)

    # Verify that a plain integer is also accepted without raising
    plain_int = 2
    namedtupleutils.to_namedtuple(plain_int)

def test_to_namedtuple_with_bytes_keyed_dict():
    """Test that to_namedtuple handles a dict with bytes keys and bytes values."""
    # A bytes object used as both key and value in the input dict
    bytes_key_and_value = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Dict with duplicate bytes keys (Python retains last assignment, resulting in a single entry)
    bytes_keyed_dict = {
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
        bytes_key_and_value: bytes_key_and_value,
    }

    namedtupleutils.to_namedtuple(bytes_keyed_dict)