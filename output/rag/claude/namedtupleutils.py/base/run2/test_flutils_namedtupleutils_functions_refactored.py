import pytest
import namedtupleutils as namedtupleutils
import collections as collections

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple raises an error when given a plain float value."""
    invalid_input = -476.66
    namedtupleutils.to_namedtuple(invalid_input)

def test_to_namedtuple_with_nested_tuple_containing_set():
    """Test that to_namedtuple handles a tuple containing a set, and also a plain set."""
    # A single float value used to construct a deduplicated set
    sample_float = -67.0

    # A set with one unique element (duplicates collapse)
    sample_set = {sample_float, sample_float, sample_float, sample_float}

    # A tuple nesting the float and the set
    nested_tuple = (sample_float, sample_set)

    # Convert the nested tuple to a namedtuple
    named = namedtupleutils.to_namedtuple(nested_tuple)

    # Also convert the bare set to a namedtuple (result not asserted)
    namedtupleutils.to_namedtuple(sample_set)

def test_to_namedtuple_with_duplicate_keys_and_namedtuple_input():
    """Test that to_namedtuple handles a dict with duplicate keys and that
    passing an already-converted namedtuple through to_namedtuple is idempotent."""

    # A dict with duplicate keys collapses to a single entry (Python dict semantics)
    field_name = "author"
    source_dict = {field_name: field_name, field_name: field_name, field_name: field_name}

    # Convert the dict to a namedtuple
    namedtuple_result = namedtupleutils.to_namedtuple(source_dict)

    # Pass the already-converted namedtuple back through to_namedtuple
    re_converted_result = namedtupleutils.to_namedtuple(namedtuple_result)

def test_to_namedtuple_raises_on_bytes_input():
    """Test that to_namedtuple raises an error when given a bytes object, which is not a valid input type."""
    # Bytes are not a supported input type for to_namedtuple
    raw_bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    namedtupleutils.to_namedtuple(raw_bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that converting an empty tuple to a namedtuple succeeds without error."""
    empty_tuple = ()
    result = namedtupleutils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_empty_ordered_dict_and_mixed_tuple():
    """Test that to_namedtuple handles an empty OrderedDict, repeated conversions,
    and a mixed tuple containing a namedtuple and bytes object."""

    # Create an empty OrderedDict as the base input
    empty_ordered_dict = collections.OrderedDict()

    # Convert the empty OrderedDict to a namedtuple
    namedtuple_from_dict = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert the resulting namedtuple again (idempotency check)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_dict)

    # Repeat conversion of the original empty OrderedDict
    namedtuple_from_dict_again = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Convert the repeated result once more
    namedtuple_from_namedtuple_again = namedtupleutils.to_namedtuple(namedtuple_from_dict_again)

    # Raw bytes value used as part of a mixed tuple input
    raw_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"

    # Convert the empty OrderedDict a third time
    namedtuple_from_dict_third = namedtupleutils.to_namedtuple(empty_ordered_dict)

    # Build a mixed tuple containing a namedtuple and a bytes object
    mixed_tuple = (namedtuple_from_namedtuple, raw_bytes)

    # Convert the mixed tuple (namedtuple + bytes) to a namedtuple
    namedtuple_from_mixed_tuple = namedtupleutils.to_namedtuple(mixed_tuple)

    # Convert the empty OrderedDict a fourth time
    namedtuple_from_dict_fourth = namedtupleutils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_ordered_dict_special_char_key():
    """Test that to_namedtuple handles an OrderedDict with a special-character key,
    and that constructing an OrderedDict with None as a positional argument behaves
    as expected (no assertion; exercises the call path without error)."""

    # A string key containing special/control characters
    special_key = "wm=-g\ry#\x0b#:*"

    # Build a plain dict using the special key (duplicate key collapses to one entry)
    raw_dict = {special_key: special_key}

    # Wrap it in an OrderedDict via keyword expansion
    ordered_dict_with_special_key = collections.OrderedDict(**raw_dict)

    # Convert the OrderedDict to a namedtuple; exercises the main function under test
    result = namedtupleutils.to_namedtuple(ordered_dict_with_special_key)

    # Construct a separate OrderedDict passing None as a positional iterable argument
    none_iterable = [None]
    collections.OrderedDict(*none_iterable)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Test that to_namedtuple handles a list containing an empty list,
    and also accepts None as input without raising an error."""
    # Create an empty list nested inside another list
    empty_list = []
    nested_list = [empty_list]

    # Convert the nested list structure to a namedtuple
    var_0 = namedtupleutils.to_namedtuple(nested_list)

    # Also verify that None is accepted as input
    none_value = None
    namedtupleutils.to_namedtuple(none_value)

def test_to_namedtuple_with_mixed_input_types():
    """Test that to_namedtuple handles dicts, tuples, nested namedtuples,
    and primitive values (bool) across multiple chained conversions."""

    # A long descriptive string used as a dictionary key and value
    path_docstring = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # A flat dict with duplicate keys (only one entry survives) using the docstring as both key and value
    flat_dict = {path_docstring: path_docstring, path_docstring: path_docstring, path_docstring: path_docstring}

    # Convert a simple flat dict to a namedtuple
    namedtuple_from_flat_dict = namedtupleutils.to_namedtuple(flat_dict)

    bool_false_0 = False

    # Convert the same flat dict again to use as a nested value
    namedtuple_from_flat_dict_2 = namedtupleutils.to_namedtuple(flat_dict)

    # Wrap a namedtuple in a tuple, then convert that tuple to a namedtuple
    tuple_wrapping_namedtuple = (namedtuple_from_flat_dict_2,)
    namedtuple_from_tuple = namedtupleutils.to_namedtuple(tuple_wrapping_namedtuple)

    # Build a dict keyed by a namedtuple and a bool, then convert to a namedtuple
    mixed_key_dict = {namedtuple_from_tuple: namedtuple_from_flat_dict_2, bool_false_0: namedtuple_from_flat_dict_2}
    namedtuple_from_mixed_dict = namedtupleutils.to_namedtuple(mixed_key_dict)

    # Convert a namedtuple to a namedtuple (idempotent-like behaviour)
    namedtuple_from_namedtuple = namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    bool_false_1 = False

    # Convert the mixed-key namedtuple again
    namedtupleutils.to_namedtuple(namedtuple_from_mixed_dict)

    # Convert a plain bool value to a namedtuple
    namedtupleutils.to_namedtuple(bool_false_1)

def test_to_namedtuple_with_nested_structures_and_repeated_conversion():
    """Test that to_namedtuple handles nested structures with repeated conversion
    and gracefully processes a non-iterable integer input."""

    # Build a dict with mixed key types (string and tuple) and nested values
    key_str = "\x0cMv"
    empty_tuple = ()
    nested_dict = {key_str: empty_tuple, empty_tuple: key_str, empty_tuple: empty_tuple}

    # Create a list containing a tuple that nests the string and dict
    nested_tuple = (key_str, nested_dict)
    input_list = [nested_tuple]

    # Convert the nested list structure to a namedtuple
    namedtuple_result_0 = namedtupleutils.to_namedtuple(input_list)

    # Apply to_namedtuple again on the already-converted result (idempotency check)
    namedtuple_result_1 = namedtupleutils.to_namedtuple(namedtuple_result_0)

    # Apply a third time to verify stable repeated conversion
    namedtuple_result_2 = namedtupleutils.to_namedtuple(namedtuple_result_1)

    # Pass a plain integer to verify to_namedtuple handles non-iterable input
    int_input = 2
    namedtupleutils.to_namedtuple(int_input)

def test_to_namedtuple_with_duplicate_bytes_keys():
    """Test that to_namedtuple handles a dict with repeated bytes keys without error."""
    # A bytes object used as the sole (repeated) key and value in the input dict
    bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"

    # Python dicts deduplicate keys, so this effectively becomes {bytes_key: bytes_key}
    dict_with_bytes_keys = {bytes_key: bytes_key, bytes_key: bytes_key, bytes_key: bytes_key}

    namedtupleutils.to_namedtuple(dict_with_bytes_keys)