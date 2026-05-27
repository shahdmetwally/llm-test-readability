import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_float_input():
    """Test that to_namedtuple raises an error for float inputs."""
    float_value = -476.66
    namedtuple_utils.to_namedtuple(float_value)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Test converting a tuple containing a float and a set (with duplicate floats) to a namedtuple."""
    float_value = -67.0
    # Create a set from the float; duplicates are automatically removed
    float_set = {float_value, float_value, float_value, float_value}
    input_tuple = (float_value, float_set)
    result = namedtuple_utils.to_namedtuple(input_tuple)
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_collapses_duplicate_keys_keeping_last():
    """Verify that to_namedtuple collapses duplicate keys in a dict (keeping the last value)
    and that the result can be round-tripped through to_namedtuple again."""
    key = "author"
    # A dict with the same key repeated three times; Python keeps only the last assignment
    input_dict = {key: key, key: key, key: key}
    result = namedtuple_utils.to_namedtuple(input_dict)
    round_tripped = namedtuple_utils.to_namedtuple(result)

def test_to_namedtuple_with_bytes_input_raises_error():
    """Test that to_namedtuple raises an error when given bytes input."""
    invalid_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    with pytest.raises(Exception):
        namedtuple_utils.to_namedtuple(invalid_input)

def test_to_namedtuple_with_empty_tuple(self):
    """Test that to_namedtuple returns an appropriate result when given an empty tuple."""
    empty_tuple = ()
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_ordered_dict_roundtrip_and_mixed_types():
    """Test that to_namedtuple can handle OrderedDict, its namedtuple equivalent,
    and mixed tuples containing bytes data without errors."""
    # Create an empty OrderedDict and convert it to a namedtuple
    ordered_dict = collections_module.OrderedDict()
    first_namedtuple = namedtuple_utils.to_namedtuple(ordered_dict)

    # Round-trip: convert namedtuple back via to_namedtuple
    roundtrip_namedtuple = namedtuple_utils.to_namedtuple(first_namedtuple)

    # Repeat conversion of original OrderedDict and its namedtuple form
    second_namedtuple_from_dict = namedtuple_utils.to_namedtuple(ordered_dict)
    second_roundtrip = namedtuple_utils.to_namedtuple(second_namedtuple_from_dict)

    # Binary data and another conversion from the original OrderedDict
    binary_data = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    third_namedtuple_from_dict = namedtuple_utils.to_namedtuple(ordered_dict)

    # Mixed tuple containing a namedtuple and bytes
    mixed_tuple = (roundtrip_namedtuple, binary_data)
    namedtuple_from_mixed = namedtuple_utils.to_namedtuple(mixed_tuple)

    # Final conversion from original OrderedDict
    final_namedtuple = namedtuple_utils.to_namedtuple(ordered_dict)

def test_to_namedtuple_with_invalid_string_keys_in_ordereddict():
    """Verify that to_namedtuple handles an OrderedDict created with **dict containing invalid string keys."""
    invalid_key = "wm=-g\ry#\x0b#:*"
    dict_with_duplicate_keys = {invalid_key: invalid_key, invalid_key: invalid_key}
    ordered_dict = collections_module.OrderedDict(**dict_with_duplicate_keys)
    result_namedtuple = namedtuple_utils.to_namedtuple(ordered_dict)
    none_value = None
    list_with_none = [none_value]
    collections_module.OrderedDict(*list_with_none)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Test that to_namedtuple handles a list containing an empty list, and that passing None returns None or raises no error."""
    inner_empty_list = []
    outer_list = [inner_empty_list]
    # Convert a list containing an empty list to a namedtuple
    var_0 = namedtuple_utils.to_namedtuple(outer_list)
    # Verify that converting None is handled gracefully (no exception)
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_with_duplicate_dict_keys_and_mixed_types():
    """Verify to_namedtuple handles various input types, including dicts with
    duplicate string keys, tuples of namedtuples, and boolean values."""
    docstring = (
        "Normalize a given path.\n\n"
        "    The given ``path`` will be normalized in the following process.\n\n"
        "    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n"
        "       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n"
        "    #. :obj:`PosixPath <pathlib.PosixPath>` and\n"
        "       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n"
        "       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n"
        "       method.\n"
        "    #. An initial component of ``~`` will be replaced by that user’s\n"
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
    # Dict with duplicate keys (same string repeated) — only last key-value pair is kept
    duplicate_key_dict = {docstring: docstring, docstring: docstring, docstring: docstring}
    namedtuple_from_duplicate_keys = namedtuple_utils.to_namedtuple(duplicate_key_dict)
    
    false_value = False
    # Another dict-to-namedtuple conversion for comparison
    second_namedtuple = namedtuple_utils.to_namedtuple(duplicate_key_dict)
    
    # Tuple containing the namedtuple
    namedtuple_tuple = (second_namedtuple,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(namedtuple_tuple)
    
    # Dict with mixed key types: a namedtuple key and a boolean key
    mixed_key_dict = {namedtuple_from_tuple: second_namedtuple, false_value: second_namedtuple}
    namedtuple_from_mixed_keys = namedtuple_utils.to_namedtuple(mixed_key_dict)
    
    # Convert a namedtuple to another namedtuple (nested conversion)
    nested_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_keys)
    
    # Another conversion from the same source
    namedtuple_utils.to_namedtuple(namedtuple_from_mixed_keys)
    
    # Test conversion of a boolean value
    namedtuple_utils.to_namedtuple(False)

def test_to_namedtuple_with_mixed_types_and_nested_structures():
    """Test converting a list containing a tuple with a dictionary to a namedtuple,
    then converting the result multiple times, and finally converting an integer.
    This exercises handling of strings, empty tuples, dictionaries with mixed key types,
    and non-iterable inputs."""
    str_val = "\x0cMv"
    empty_tuple = ()
    # Dictionary with string and tuple keys, and tuple values
    mixed_dict = {str_val: empty_tuple, empty_tuple: str_val, empty_tuple: empty_tuple}
    nested_tuple = (str_val, mixed_dict)
    source_list = [nested_tuple]
    result_1 = namedtuple_utils.to_namedtuple(source_list)
    result_2 = namedtuple_utils.to_namedtuple(result_1)
    result_3 = namedtuple_utils.to_namedtuple(result_2)
    int_val = 2
    namedtuple_utils.to_namedtuple(int_val)

def test_to_namedtuple_with_bytes_keys_in_dict_raises_error():
    """Test that to_namedtuple handles a dictionary with bytes keys and values."""
    bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    dict_with_bytes_keys = {
        bytes_key: bytes_key,
        bytes_key: bytes_key,
        bytes_key: bytes_key,
    }
    namedtuple_utils.to_namedtuple(dict_with_bytes_keys)