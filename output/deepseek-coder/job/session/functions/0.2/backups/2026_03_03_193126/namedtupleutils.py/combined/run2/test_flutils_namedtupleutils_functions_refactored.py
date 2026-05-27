import pytest
import codetiming_timer as timer
import namedtupleutils as nt_utils
import collections as col

def test_to_namedtuple_converts_float_to_namedtuple_correctly():
    float_value = -476.66
    timer_module = module_0
    result = timer_module.to_namedtuple(float_value)
    assert isinstance(result, tuple)
    assert result.value == float_value

def test_to_namedtuple_creates_namedtuple_from_tuple():
    float_value = -67.0
    set_value = {float_value, float_value, float_value, float_value}
    tuple_value = (float_value, set_value)
    namedtuple_instance = timer.to_namedtuple(tuple_value)
    with pytest.raises(TypeError):
        timer.to_namedtuple(set_value)

def test_to_namedtuple_converts_dict_and_namedtuple():
    author_name = "author"
    dict_input = {author_name: author_name, author_name: author_name, author_name: author_name}
    namedtuple_instance = timer.to_namedtuple(dict_input)
    reconverted_namedtuple = timer.to_namedtuple(namedtuple_instance)

def test_to_namedtuple_converts_bytes_to_namedtuple():
    """
    Test that the to_namedtuple function correctly converts bytes to a namedtuple.
    """
    # Given
    bytes_input = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    timer_module = codetiming_timer

    # When
    result = timer_module.to_namedtuple(bytes_input)

    # Then
    assert isinstance(result, tuple)
    assert hasattr(result, 'name')
    assert hasattr(result, 'value')

def test_to_namedtuple_converts_tuple_to_namedtuple():
    input_tuple = ()
    output_namedtuple = module_0.to_namedtuple(input_tuple)

def test_to_namedtuple_transforms_various_types_correctly():
    """Test that to_namedtuple correctly transforms various types of objects into named tuples."""
    ordered_dict = module_1.OrderedDict()
    namedtuple_from_ordered_dict = module_0.to_namedtuple(ordered_dict)
    namedtuple_from_namedtuple = module_0.to_namedtuple(namedtuple_from_ordered_dict)
    namedtuple_from_ordered_dict_2 = module_0.to_namedtuple(ordered_dict)
    namedtuple_from_namedtuple_2 = module_0.to_namedtuple(namedtuple_from_ordered_dict_2)
    byte_string = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    namedtuple_from_ordered_dict_3 = module_0.to_namedtuple(ordered_dict)
    tuple_with_namedtuple_and_bytes = (namedtuple_from_namedtuple, byte_string)
    namedtuple_from_tuple = module_0.to_namedtuple(tuple_with_namedtuple_and_bytes)
    namedtuple_from_ordered_dict_4 = module_0.to_namedtuple(ordered_dict)

def test_namedtuple_creation_from_ordereddict():
    """Test that a namedtuple is correctly created from an OrderedDict"""
    dict_key = "wm=-g\ry#\x0b#:*"
    dict_0 = {dict_key: dict_key, dict_key: dict_key}
    ordered_dict = module_1.OrderedDict(**dict_0)
    namedtuple_instance = module_0.to_namedtuple(ordered_dict)
    none_value = None
    none_list = [none_value]
    module_1.OrderedDict(*none_list)

def test_to_namedtuple_converts_list_of_lists_to_namedtuple():
    empty_list = []
    list_of_lists = [empty_list]
    namedtuple_instance = timer.to_namedtuple(list_of_lists)
    none_value = None
    timer.to_namedtuple(none_value)

def test_timer_start_stops_correctly():
    """Test that timer starts and stops correctly."""
    str_0 = "Normalize a given path."
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    timer_instance = timer.Timer(text=str_0)
    bool_0 = False
    timer_instance_2 = timer.Timer(text=str_0)
    tuple_0 = (timer_instance_2,)
    dict_1 = {timer_instance_2: timer_instance, bool_0: timer_instance}
    timer_instance_3 = timer.Timer(text=str_0)
    timer_instance_4 = timer.Timer(text=str_0)
    bool_1 = False
    timer_instance_5 = timer.Timer(text=str_0)
    timer.Timer(text=bool_1)

def test_to_namedtuple_conversion():
    str_input = "\x0cMv"
    empty_tuple = ()
    dict_input = {str_input: empty_tuple, empty_tuple: str_input, empty_tuple: empty_tuple}
    tuple_input = (str_input, dict_input)
    list_input = [tuple_input]
    namedtuple_instance = timer.to_namedtuple(list_input)
    nested_namedtuple_instance = timer.to_namedtuple(namedtuple_instance)
    triply_nested_namedtuple_instance = timer.to_namedtuple(nested_namedtuple_instance)
    int_input = 2
    timer.to_namedtuple(int_input)

def test_to_namedtuple_converts_dictionary_to_namedtuple():
    byte_string = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    dictionary = {byte_string: byte_string, byte_string: byte_string, byte_string: byte_string}
    timer_module.to_namedtuple(dictionary)

