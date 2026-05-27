import pytest
import namedtupleutils as namedtuple_utils
import collections as collections_module

def test_to_namedtuple_with_float():
    """Test that to_namedtuple can handle float input."""
    # Create a float value to test conversion
    float_value = -476.66
    
    # Attempt to convert float to namedtuple
    namedtuple_utils.to_namedtuple(float_value)

def test_to_namedtuple_converts_float_and_set_containing_float():
    """Test that to_namedtuple correctly handles a tuple containing a float and a set of floats."""
    # Create test data: a negative float value
    negative_float = -67.0
    
    # Create a set with duplicate float values (will deduplicate to single element)
    float_set = {negative_float, negative_float, negative_float, negative_float}
    
    # Create a tuple containing the float and the set
    float_and_set_tuple = (negative_float, float_set)
    
    # Convert the tuple to a namedtuple
    result = namedtuple_utils.to_namedtuple(float_and_set_tuple)
    
    # Also test converting the set directly to a namedtuple
    namedtuple_utils.to_namedtuple(float_set)

def test_to_namedtuple_single_key_dict_idempotent():
    """Test that to_namedtuple works on a dict with a single repeated key and is idempotent."""
    # Create a dictionary with a single key-value pair (key repeated, last value wins)
    key_and_value = "author"
    single_key_dict = {key_and_value: key_and_value}
    
    # First conversion: dict -> namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(single_key_dict)
    
    # Second conversion: namedtuple -> namedtuple (should be idempotent)
    double_conversion_result = namedtuple_utils.to_namedtuple(namedtuple_result)

def test_to_namedtuple_accepts_bytes_input():
    """Verify that to_namedtuple can process bytes objects without raising exceptions."""
    # Create a bytes object with mixed content to test conversion
    test_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    
    # This should process bytes without raising TypeError or other exceptions
    namedtuple_utils.to_namedtuple(test_bytes)

def test_to_namedtuple_converts_empty_tuple():
    """Test that an empty tuple is correctly converted to a namedtuple."""
    empty_tuple = ()
    result = namedtuple_utils.to_namedtuple(empty_tuple)

def test_to_namedtuple_handles_nested_conversions_and_mixed_types():
    """Test that to_namedtuple correctly handles repeated conversions and mixed type inputs."""
    # Create an empty OrderedDict as base test input
    empty_ordered_dict = collections_module.OrderedDict()
    
    # Convert empty OrderedDict to namedtuple
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    # Convert the resulting namedtuple back to namedtuple (should be idempotent)
    namedtuple_from_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_dict)
    
    # Another conversion from the same empty OrderedDict
    another_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    # Convert that result again
    namedtuple_from_another_namedtuple = namedtuple_utils.to_namedtuple(another_namedtuple_from_dict)
    
    # Test with binary data
    random_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    
    # Yet another conversion from empty OrderedDict
    yet_another_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)
    
    # Create tuple containing namedtuple and bytes
    mixed_tuple = (namedtuple_from_namedtuple, random_bytes)
    # Convert tuple to namedtuple
    namedtuple_from_mixed_tuple = namedtuple_utils.to_namedtuple(mixed_tuple)
    
    # Final conversion from empty OrderedDict
    final_namedtuple_from_dict = namedtuple_utils.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_handles_ordereddict_with_duplicate_keys_and_ordereddict_constructor_with_none():
    """Test that to_namedtuple can process OrderedDict with duplicate keys,
    and OrderedDict constructor can be called with None (though this may raise TypeError)."""
    
    # Create a string with special characters to use as both key and value
    special_string = "wm=-g\ry#\x0b#:*"
    
    # Create a dictionary with duplicate keys (last value wins)
    duplicate_key_dict = {special_string: special_string, special_string: special_string}
    
    # Convert dictionary to OrderedDict
    ordered_dict = collections_module.OrderedDict(**duplicate_key_dict)
    
    # Convert OrderedDict to namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)
    
    # Test OrderedDict constructor with None argument (may raise TypeError)
    none_value = None
    list_with_none = [none_value]
    collections_module.OrderedDict(*list_with_none)

def test_to_namedtuple_handles_nested_empty_list_and_none():
    """Test that to_namedtuple correctly processes nested list with empty list and None input."""
    # Create a nested list containing an empty list
    empty_list = []
    nested_list = [empty_list]
    
    # Convert nested list to namedtuple (should succeed without error)
    result = namedtuple_utils.to_namedtuple(nested_list)
    
    # Test with None input (should handle gracefully)
    none_value = None
    namedtuple_utils.to_namedtuple(none_value)

def test_to_namedtuple_handles_complex_nested_structures():
    """Test that to_namedtuple correctly processes deeply nested structures
    including dictionaries, tuples, and boolean values."""
    # A long docstring that serves as test data
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
        "        PosixPath('/home/test_user/tmp/bar')\n\n    "
    )

    # Create a dictionary with the docstring as both keys and values
    docstring_dict = {
        path_docstring: path_docstring,
        path_docstring: path_docstring,
        path_docstring: path_docstring,
    }

    # Convert dictionary to namedtuple
    namedtuple_from_dict = namedtuple_utils.to_namedtuple(docstring_dict)

    false_flag = False

    # Convert same dictionary again (should produce same structure)
    namedtuple_from_dict_again = namedtuple_utils.to_namedtuple(docstring_dict)

    # Create a tuple containing the namedtuple and convert it
    singleton_tuple = (namedtuple_from_dict_again,)
    namedtuple_from_singleton = namedtuple_utils.to_namedtuple(singleton_tuple)

    # Create a mixed dictionary with namedtuple and boolean as keys
    mixed_dict = {
        namedtuple_from_singleton: namedtuple_from_dict_again,
        false_flag: namedtuple_from_dict_again,
    }

    # Convert mixed dictionary to namedtuple
    namedtuple_from_mixed_dict = namedtuple_utils.to_namedtuple(mixed_dict)

    # Convert the resulting namedtuple again (testing nested conversion)
    nested_namedtuple = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)

    another_false_flag = False

    # Convert the mixed dict namedtuple again
    nested_namedtuple_again = namedtuple_utils.to_namedtuple(namedtuple_from_mixed_dict)

    # Test conversion of boolean value
    namedtuple_utils.to_namedtuple(another_false_flag)

def test_to_namedtuple_handles_nested_structures_with_cycles_and_primitives():
    """Test that to_namedtuple correctly handles complex nested structures with cyclic references and primitive types."""
    # Create a string with a non-printable character
    key_string = "\x0cMv"
    
    # Create an empty tuple to use as both key and value
    empty_tuple = ()
    
    # Create a dictionary with cyclic references (string->tuple, tuple->string, tuple->tuple)
    cyclic_dict = {key_string: empty_tuple, empty_tuple: key_string, empty_tuple: empty_tuple}
    
    # Create a tuple containing the string and the cyclic dictionary
    nested_tuple = (key_string, cyclic_dict)
    
    # Wrap the tuple in a list
    list_with_nested_tuple = [nested_tuple]
    
    # Convert the list to a namedtuple (should handle nested structures)
    namedtuple_1 = namedtuple_utils.to_namedtuple(list_with_nested_tuple)
    
    # Convert the result again (should be idempotent for already-converted structures)
    namedtuple_2 = namedtuple_utils.to_namedtuple(namedtuple_1)
    
    # Convert once more (should remain unchanged)
    namedtuple_3 = namedtuple_utils.to_namedtuple(namedtuple_2)
    
    # Test that primitive integer type doesn't cause errors (should return unchanged)
    integer_value = 2
    namedtuple_utils.to_namedtuple(integer_value)

def test_to_namedtuple_with_bytes_keys_and_values():
    """Test that to_namedtuple can handle dictionaries with bytes as both keys and values."""
    # Create a bytes object to use as both keys and values
    sample_bytes = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    
    # Create a dictionary where bytes serve as both keys and values
    # Note: Duplicate keys will be collapsed in the dictionary
    bytes_dict = {
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes
    }
    
    # Verify the function can process this dictionary without errors
    namedtuple_utils.to_namedtuple(bytes_dict)

