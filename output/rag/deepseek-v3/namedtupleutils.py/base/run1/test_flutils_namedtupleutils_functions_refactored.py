import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_float_returns_empty_namedtuple():
    """Verify that calling to_namedtuple with a float value returns an empty namedtuple."""
    float_value = -476.66
    namedtuple_utils.to_namedtuple(float_value)

def test_to_namedtuple_with_tuple_containing_float_and_set():
    """Test converting a tuple containing a float and a set to a namedtuple."""
    float_value = -67.0
    # Create a set with the float value repeated (set deduplicates to single element)
    value_set = {float_value, float_value, float_value, float_value}
    # Input tuple containing the float and the set
    input_tuple = (float_value, value_set)
    # Convert tuple to namedtuple
    var_0 = namedtuple_utils.to_namedtuple(input_tuple)
    # Convert the set to namedtuple as well
    namedtuple_utils.to_namedtuple(value_set)

def test_single_repeated_key_dict_roundtrip_to_namedtuple_and_back():
    """Verify that a dict with a single repeated key converts to a namedtuple,
    and that converting that namedtuple back also works."""
    key_field = "author"
    dict_with_single_key = {key_field: key_field, key_field: key_field, key_field: key_field}
    namedtuple_result = namedtuple_utils.to_namedtuple(dict_with_single_key)
    roundtrip_result = namedtuple_utils.to_namedtuple(namedtuple_result)

def test_to_namedtuple_with_bytes_input_raises_error():
    """Verify that to_namedtuple raises an error when given a bytes object."""
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    with pytest.raises(TypeError):
        namedtuple_utils.to_namedtuple(bytes_input)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple handles an empty tuple correctly."""
    empty_tuple = ()
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_with_nested_conversion_and_bytes_tuple():
    """Test that to_namedtuple handles nested conversion (ordered_dict -> namedtuple -> ordered_dict -> namedtuple)
    and can convert a tuple containing a namedtuple and bytes to a namedtuple."""
    ordered_dict = collections_module.OrderedDict()
    namedtuple_from_ordered_dict = namedtuple_utils.to_namedtuple(ordered_dict)
    nested_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_ordered_dict)
    namedtuple_from_ordered_dict_again = namedtuple_utils.to_namedtuple(ordered_dict)
    nested_namedtuple_again = namedtuple_utils.to_namedtuple(namedtuple_from_ordered_dict_again)
    bytes_data = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    namedtuple_from_ordered_dict_third = namedtuple_utils.to_namedtuple(ordered_dict)
    tuple_with_namedtuple_and_bytes = (nested_namedtuple, bytes_data)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_with_namedtuple_and_bytes)
    namedtuple_from_ordered_dict_fourth = namedtuple_utils.to_namedtuple(ordered_dict)

def test_namedtuple_from_ordered_dict_with_invalid_keys_raises_error():
    """Verify that to_namedtuple raises an error when an OrderedDict is created with invalid keyword arguments."""
    invalid_key = "wm=-g\ry#\x0b#:*"
    # Creating a dict with the same key repeated (second overwrites first)
    dict_with_invalid_key = {invalid_key: invalid_key, invalid_key: invalid_key}
    # This pass will raise a TypeError because invalid_key is not a valid Python identifier
    ordered_dict_0 = collections_module.OrderedDict(**dict_with_invalid_key)
    var_0 = namedtuple_utils.to_namedtuple(ordered_dict_0)
    none_type_0 = None
    list_0 = [none_type_0]
    collections_module.OrderedDict(*list_0)

def test_to_namedtuple_with_nested_empty_list_and_none():
    """Test that to_namedtuple handles a list containing an empty list,
    and that calling it with None does not raise an error."""
    inner_list = []
    outer_list = [inner_list]
    result = namedtuple_utils.to_namedtuple(outer_list)
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_with_long_docstring_key_and_duplicate_keys():
    """Test converting nested dicts, tuples, and primitive types with to_namedtuple."""
    # A long docstring used as both key and value in a dict
    docstring_key = "Normalize a given path.\n\n    The given ``path`` will be normalized in the following process.\n\n    #. :obj:`bytes` will be converted to a :obj:`str` using the encoding\n       given by :obj:`getfilesystemencoding() <sys.getfilesystemencoding>`.\n    #. :obj:`PosixPath <pathlib.PosixPath>` and\n       :obj:`WindowsPath <pathlib.WindowsPath>` will be converted\n       to a :obj:`str` using the :obj:`as_posix() <pathlib.PurePath.as_posix>`\n       method.\n    #. An initial component of ``~`` will be replaced by that user's\n       home directory.\n    #. Any environment variables will be expanded.\n    #. Non absolute paths will have the current working directory from\n       :obj:`os.getcwd() <os.cwd>`prepended.  If needed, use\n       :obj:`os.chdir() <os.chdir>` to change the current working directory\n       before calling this function.\n    #. Redundant separators and up-level references will be normalized, so\n       that ``A//B``, ``A/B/``, ``A/./B`` and ``A/foo/../B`` all become\n       ``A/B``.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path to be normalized.\n\n    :rtype:\n        :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n\n        >>> from flutils.pathutils import normalize_path\n        >>> normalize_path('~/tmp/foo/../bar')\n        PosixPath('/home/test_user/tmp/bar')\n\n    "

    # Create a dict with duplicate keys (only last value is kept) and convert to namedtuple
    dict_with_duplicate_keys = {docstring_key: docstring_key, docstring_key: docstring_key, docstring_key: docstring_key}
    first_namedtuple = namedtuple_utils.to_namedtuple(dict_with_duplicate_keys)

    # Convert the same dict again — creates another namedtuple from the same data
    false_value = False
    second_namedtuple = namedtuple_utils.to_namedtuple(dict_with_duplicate_keys)

    # Pack the second namedtuple into a tuple and convert that tuple to a namedtuple
    tuple_wrapping_namedtuple = (second_namedtuple,)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_wrapping_namedtuple)

    # Build a mixed-key dict (namedtuple key + bool key) and convert to namedtuple
    mixed_key_dict = {namedtuple_from_tuple: second_namedtuple, false_value: second_namedtuple}
    nested_namedtuple = namedtuple_utils.to_namedtuple(mixed_key_dict)

    # Convert the nested namedtuple again — produces a new namedtuple from its fields
    converted_from_nested = namedtuple_utils.to_namedtuple(nested_namedtuple)

    # Another conversion of the same nested namedtuple
    false_value_2 = False
    another_conversion_of_nested = namedtuple_utils.to_namedtuple(nested_namedtuple)

    # Converting a bare bool (False) to a namedtuple — edge case with primitive
    namedtuple_utils.to_namedtuple(false_value_2)

def test_to_namedtuple_with_nested_lists_and_dicts_multiple_conversions():
    """Test converting a nested structure containing a list with a tuple and dict
    to a namedtuple and back multiple times. Also test with an integer input."""
    key = "\x0cMv"
    empty_tuple = ()
    dict_with_mixed_types = {key: empty_tuple, empty_tuple: key, empty_tuple: empty_tuple}
    tuple_with_key_and_dict = (key, dict_with_mixed_types)
    list_with_tuple = [tuple_with_key_and_dict]
    
    # Convert list to namedtuple, then convert result again twice
    first_named_tuple = namedtuple_utils.to_namedtuple(list_with_tuple)
    second_named_tuple = namedtuple_utils.to_namedtuple(first_named_tuple)
    third_named_tuple = namedtuple_utils.to_namedtuple(second_named_tuple)
    
    # Test conversion of integer (edge case)
    integer_input = 2
    namedtuple_utils.to_namedtuple(integer_input)

def test_to_namedtuple_rejects_dict_with_bytes_keys():
    """Test that to_namedtuple raises an error when passed a dict with bytes keys."""
    bytes_key = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    dict_with_bytes_keys = {bytes_key: bytes_key, bytes_key: bytes_key, bytes_key: bytes_key}
    with pytest.raises(TypeError):
        namedtuple_utils.to_namedtuple(dict_with_bytes_keys)