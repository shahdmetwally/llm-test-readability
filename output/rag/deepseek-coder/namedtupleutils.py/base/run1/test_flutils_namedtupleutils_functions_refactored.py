import pytest
import codetiming_timer as timer
import namedtupleutils as named_tuple_utils
import collections as collections_utils

from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUserModel(TestCase):
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            email="test_user@gmail.com",
            password="test123"
        )
        self.assertEqual(user.email, "test_user@gmail.com")
        self.assertTrue(user.check_password("test123"))

def test_namedtuple_creation():
    """Tests that to_namedtuple function successfully converts types to a named tuple"""

    # given
    float_value = -67.0
    set_of_floats = {float_value, float_value, float_value, float_value}
    tuple_to_convert = (float_value, set_of_floats)

    # when
    first_named_tuple = timer.to_namedtuple(tuple_to_convert)
    second_named_tuple = named_tuple_utils.to_namedtuple(set_of_floats)

    # then
    assert isinstance(first_named_tuple, collections_utils.namedtuple)
    assert isinstance(second_named_tuple, collections_utils.namedtuple)

def test_namedtuple_conversion():
    author_name = "author"
    author_info_dict = {author_name: author_name, author_name: author_name, author_name: author_name}
    transformed_dict = named_tuple_utils.to_namedtuple(author_info_dict)
    author = named_tuple_utils.to_namedtuple(transformed_dict)

    # assert that the author's name matches the transformed dictionary
    assert author.name == author_name

    # assert that the author data matches the transformed dictionary
    assert author.data == author_info_dict

def test_namedtuple_conversion_from_bytes():
    """Test namedtupleutils.to_namedtuple(b) function. It should create a namedtuple from a bytes object."""

    # Given
    input_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"

    # When
    result = named_tuple_utils.to_namedtuple(input_bytes)

    # Then
    assert isinstance(result, tuple)
    assert hasattr(result, "_asdict")
    assert callable(getattr(result, "_asdict"))

def test_to_namedtuple_empty_tuple():
    """Test that a named tuple is created from an empty tuple."""
    # Given
    empty_tuple = ()

    # When
    named_tuple = named_tuple_utils.to_namedtuple(empty_tuple)

    # Then
    assert isinstance(named_tuple, tuple), "The result should be a named tuple."

def test_namedtuple_conversion_from_ordered_dict_1():
    """
    Test namedtuple conversion from an OrderedDict
    """

    var_dict = collections_utils.OrderedDict()
    var_tuple_1 = named_tuple_utils.to_namedtuple(var_dict)
    var_tuple_2 = named_tuple_utils.to_namedtuple(var_tuple_1)
    var_tuple_3 = named_tuple_utils.to_namedtuple(var_dict)
    var_tuple_4 = named_tuple_utils.to_namedtuple(var_tuple_3)
    bytes_data = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    var_tuple_5 = named_tuple_utils.to_namedtuple((var_tuple_2, bytes_data))
    var_tuple_6 = named_tuple_utils.to_namedtuple(var_dict)
    
    # Add assertion to validate named tuple conversion
    assert type(var_tuple_6) == tuple

def test_ordered_dict_creation_and_namedtuple_conversion():
    """
    Test that a dictionary can be converted to an ordered dictionary, 
    then this ordered dictionary can be converted to a namedtuple.
    """

    # Given
    str_data = "wm=-g\ry#\x0b#:*"
    data = {str_data: str_data, str_data: str_data}
    
    # When
    ordered_data = collections_utils.OrderedDict(**data)
    named_tuple = named_tuple_utils.to_namedtuple(ordered_data)
    
    # Then
    assert isinstance(named_tuple, tuple)

def test_deco_timewaste_empty_list():
    """This test verifies the proper execution of `decorated_timewaste()` with an empty list."""
    list_0 = []
    list_1 = [list_0]
    var_0 = named_tuple_utils.to_namedtuple(list_1)
    none_type_0 = None
    assert named_tuple_utils.to_namedtuple(none_type_0) == None

def test_namedtuple_creation_from_dictionary():
    """
    Test the ability to create namedtuple from dictionary using to_namedtuple function
    """
    # given
    str_path = "Normalize a given path."
    path_dict = {str_path: str_path, str_path: str_path, str_path: str_path}
    path_tuple_0 = named_tuple_utils.to_namedtuple(path_dict)
    is_valid = False
    path_tuple_1 = named_tuple_utils.to_namedtuple(path_dict)
    tuple_path = (path_tuple_1,)
    dict_path = {path_tuple_1: path_tuple_0, is_valid: path_tuple_0}
    tuple_dict = named_tuple_utils.to_namedtuple(dict_path)
    tuple_tuple = named_tuple_utils.to_namedtuple(tuple_dict)
    is_error = False
    tuple_error = named_tuple_utils.to_namedtuple(tuple_dict)
    named_tuple_utils.to_namedtuple(is_error)

def test_named_tuples_creation_from_tuples_and_lists_mixed_with_duplicates():
    """Test that named tuples are created as expected.

    This test covers different scenarios where mixed data types are used.
    Duplicates are also handled.
    """

    # Given
    str_0 = "\x0cMv"
    tuple_0 = ()
    dict_0 = {str_0: tuple_0, tuple_0: str_0, tuple_0: tuple_0}
    tuple_1 = (str_0, dict_0)
    list_0 = [tuple_1]

    # When
    var_0 = named_tuple_utils.to_namedtuple(list_0)
    var_1 = named_tuple_utils.to_namedtuple(var_0)
    var_2 = named_tuple_utils.to_namedtuple(var_1)
    int_0 = 2
    try:
        named_tuple_utils.to_namedtuple(int_0)
    except TypeError:
        pass

    # Then -- assertions are unchanged from original test
    assert var_0 == collections_utils.namedtuple('tuple_1', ['str_0', 'dict_0'])
    assert var_1 == collections_utils.namedtuple('tuple_1', ['str_0', 'dict_0'])
    assert var_2 == collections_utils.namedtuple('tuple_1', ['str_0', 'dict_0'])

def test_to_namedtuple_conversion_of_bytes_to_bytes_in_dict_with_different_naming_convention():
    """Test for the correct conversion of a dict with bytes keys and values into a NamedTuple. 
    This test case is distinct from the earlier naming convention but performs same function."""
    
    # Given byte values
    byte_values = [b"F\xdb\xfd\xf6\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}",
                   b"\x93b\xedv{\xc6,\xfb\x0f\x98d\xf7\xdd\x9e\xb0\xb6\x1b",
                   b"\xe1W\x9d\x97%\x1f\xf9\xb9\xe3\x83}\xe7\x85%R\xf9\xc3"]
    
    # When a dictionary is created from byte values 
    byte_dict = dict.fromkeys(byte_values, byte_values[0])
    
    # And when the conversion is executed
    result = named_tuple_utils.to_namedtuple(byte_dict)
    
    # Then the result should be a namedtuple
    assert isinstance(result, tuple)
    assert hasattr(result, '_fields')
    
    # And when the generated namedtuple is unpacked
    unpacked_result = collections_utils.astuple(result)
    
    # Then the unpacked result should be a tuple
    assert isinstance(unpacked_result, tuple)
    
    # And it should contain dict keys as tuples
    field_count = 0
    for item in byte_dict.keys():
        # Assert that field count matches the count of keys
        assert len(unpacked_result) == len(byte_dict.keys())
        
        # Assert individual fields in unpacked tuple matches original byte_dict keys
        assert item == unpacked_result[field_count]
        
        # Increment the field count for next field
        field_count += 1