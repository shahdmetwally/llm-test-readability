import pytest
import codetiming_timer as module_0
import collections as module_1

def test_to_namedtuple_converts_float_to_namedtuple():
    """Test that to_namedtuple function correctly converts float to namedtuple."""
    # Given
    float_value = -476.66

    # When
    result = module_0.to_namedtuple(float_value)

    # Then
    assert isinstance(result, module_1.namedtuple)
    assert result.value == float_value

def test_convert_tuple_to_namedtuple():
    # Given
    float_value = -67.0
    set_value = {float_value, float_value, float_value, float_value}
    tuple_value = (float_value, set_value)

    # When
    named_tuple = module_0.to_namedtuple(tuple_value)

    # Then
    assert named_tuple._fields == ('float_value', 'set_value')
    assert named_tuple.float_value == float_value
    assert named_tuple.set_value == set_value

    # When and Then
    with pytest.raises(TypeError):
        module_0.to_namedtuple(set_value)

def test_namedtuple_conversion():
    """
    Test that a dictionary is correctly converted to a namedtuple,
    and that the namedtuple is correctly converted back to a namedtuple.
    """
    author = "author"
    author_dict = {author: author, author: author, author: author}
    author_namedtuple = module_0.to_namedtuple(author_dict)
    author_namedtuple_again = module_0.to_namedtuple(author_namedtuple)

    # Assert that the namedtuple is correctly converted back to a namedtuple
    assert author_namedtuple == author_namedtuple_again

def test_to_namedtuple_converts_bytes_to_namedtuple():
    """
    Test that the to_namedtuple function correctly converts bytes to a namedtuple.
    """
    # Given
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"

    # When
    result = module_0.to_namedtuple(bytes_input)

    # Then
    assert isinstance(result, module_1.namedtuple)
    assert result.field_1 == b"xs&,\x9b\xc2\xf1\x80\xb3y"

def test_namedtuple_conversion_from_empty_tuple():
    """
    Test that an empty tuple is correctly converted to a namedtuple.
    """
    empty_tuple = ()
    result = module_0.to_namedtuple(empty_tuple)

    # Assert that the result is a namedtuple
    assert isinstance(result, tuple)
    assert isinstance(result, collections.namedtuple)

    # Assert that the namedtuple is empty
    assert len(result) == 0

def test_namedtuple_conversion():
    """Test namedtuple conversion from various types."""
    ordered_dict_0 = module_1.OrderedDict()
    namedtuple_0 = module_0.to_namedtuple(ordered_dict_0)
    namedtuple_1 = module_0.to_namedtuple(namedtuple_0)
    namedtuple_2 = module_0.to_namedtuple(ordered_dict_0)
    namedtuple_3 = module_0.to_namedtuple(namedtuple_2)
    bytes_0 = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    namedtuple_4 = module_0.to_namedtuple(ordered_dict_0)
    tuple_0 = (namedtuple_1, bytes_0)
    namedtuple_5 = module_0.to_namedtuple(tuple_0)
    namedtuple_6 = module_0.to_namedtuple(ordered_dict_0)

def test_timers_initialization():
    """Test that Timers are initialized correctly."""
    str_0 = "wm=-g\ry#\x0b#:*"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    none_type_0 = None
    list_0 = [none_type_0]
    module_1.OrderedDict(*list_0)

def test_namedtuple_conversion_from_list():
    """Test namedtuple conversion from list"""
    empty_list = []
    list_of_lists = [empty_list]
    namedtuple_from_list = module_0.to_namedtuple(list_of_lists)
    none_type = None
    module_0.to_namedtuple(none_type)

def test_to_namedtuple():
    # Given
    str_input = "Normalize a given path."
    dict_input = {str_input: str_input, str_input: str_input, str_input: str_input}
    tuple_input = (dict_input,)
    bool_input = False

    # When
    namedtuple_from_dict = module_0.to_namedtuple(dict_input)
    namedtuple_from_tuple = module_0.to_namedtuple(tuple_input)
    dict_input_with_bool = {namedtuple_from_tuple: namedtuple_from_dict, bool_input: namedtuple_from_dict}
    namedtuple_from_dict_with_bool = module_0.to_namedtuple(dict_input_with_bool)
    namedtuple_from_namedtuple = module_0.to_namedtuple(namedtuple_from_dict_with_bool)

    # Then
    assert namedtuple_from_dict == namedtuple_from_namedtuple
    assert namedtuple_from_tuple != namedtuple_from_dict
    assert namedtuple_from_dict_with_bool != namedtuple_from_namedtuple
    assert namedtuple_from_namedtuple == namedtuple_from_namedtuple

def test_namedtuple_conversion():
    """Test the conversion of a list of tuples to a namedtuple."""

    # Given
    str_0 = "\x0cMv"
    tuple_0 = ()
    dict_0 = {str_0: tuple_0, tuple_0: str_0, tuple_0: tuple_0}
    tuple_1 = (str_0, dict_0)
    list_0 = [tuple_1]

    # When
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)

    # Then
    int_0 = 2
    with pytest.raises(TypeError):
        module_0.to_namedtuple(int_0)

def test_namedtuple_conversion_from_dict():
    """Test namedtuple conversion from dictionary"""
    # Given
    bytes_0 = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}

    # When
    result = module_0.to_namedtuple(dict_0)

    # Then
    assert isinstance(result, module_1.namedtuple)
    assert len(result) == 3
    assert all(key in result for key in dict_0.keys())

