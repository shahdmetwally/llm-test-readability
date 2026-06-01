import maybe as maybe
import typing as typing

def test_maybe_instance_creation():
    """Test if Maybe instance is created correctly."""
    bytes_0 = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    maybe_instance = maybe.Maybe(bytes_0, bytes_0)

def test_maybe_start_stops_correctly():
    """Test that the Maybe class starts and stops correctly."""
    none_type_0 = None
    maybe_0 = maybe_lib.Maybe(none_type_0, none_type_0)

def test_maybe_equality_and_mapping():
    """Test Maybe class equality, mapping and filtering methods."""
    str_0 = "p4xa>bl^oP"
    maybe_0 = maybe.Maybe(str_0, str_0)
    bool_0 = maybe_0.__eq__(str_0)
    var_0 = maybe_0.ap(str_0)
    var_1 = maybe_0.get_or_else(str_0)
    var_2 = maybe_0.map(var_0)
    var_3 = maybe_0.filter(var_0)
    var_4 = maybe_0.map(var_0)
    var_5 = maybe_0.ap(str_0)
    bool_1 = var_0.__eq__(var_5)
    var_6 = var_0.filter(var_1)
    var_7 = var_5.get_or_else(str_0)
    maybe_1 = maybe.Maybe(str_0, str_0)
    var_8 = maybe_1.to_validation()
    var_9 = maybe_1.bind(var_8)
    var_10 = var_9.to_either()

def test_maybe_object_equality_with_set():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    none_type_0 = None
    maybe_0 = maybe.Maybe(none_type_0, none_type_0)
    bool_1 = maybe_0.__eq__(set_0)
    assert bool_1 == False

def test_maybe_bind_and_map():
    """Test the Maybe class bind and map methods"""
    bool_0 = True
    maybe_0 = maybe.Maybe(bool_0, bool_0)
    var_0 = maybe_0.bind(bool_0)
    var_1 = var_0.map(bool_0)
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    maybe_1 = maybe.Maybe(tuple_0, bool_0)
    set_0 = set()
    set_0.to_box()

def test_maybe_map_function():
    """Test that the Maybe class's map function works as expected."""
    none_type_0 = None
    bool_0 = False
    maybe_0 = maybe_lib.Maybe(none_type_0, bool_0)
    maybe_0.map(bool_0)

def test_maybe_instance_start_stops_correctly():
    """Test that a Maybe instance starts and stops correctly."""
    bool_0 = True
    maybe_0 = maybe_lib.Maybe(bool_0, bool_0)
    dict_0 = {}
    none_type_0 = None
    bool_1 = False
    maybe_1 = maybe_lib.Maybe(none_type_0, bool_1)
    maybe_1.bind(dict_0)

def test_maybe_class_behavior():
    """Test the behavior of the Maybe class."""
    bytes_0 = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_type_0 = None
    maybe_0 = maybe.Maybe(bytes_0, none_type_0)
    box_0 = maybe_0.to_box()
    int_0 = 0
    bool_0 = True
    maybe_1 = maybe.Maybe(int_0, bool_0)
    filtered_maybe_1 = maybe_1.filter(maybe_1)
    lazy_1 = maybe_1.to_lazy()
    applied_maybe = maybe_1.ap(maybe_0)
    filtered_applied_maybe = maybe_1.filter(applied_maybe)
    maybe_2 = maybe.Maybe(lazy_1, box_0)
    is_bool_0 = lazy_1 == bool_0

def test_maybe_object_creation_and_ap_method():
    int_0 = 2862
    none_type_0 = None
    bool_0 = False
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
    maybe_0.ap(int_0)

def test_maybe_filter_and_map_operations():
    """Testing the filter and map operations of the Maybe class."""
    int_0 = 0
    bool_0 = True
    maybe_0 = maybe.Maybe(int_0, bool_0)
    var_0 = maybe_0.filter(maybe_0)
    var_1 = maybe_0.to_lazy()
    var_2 = var_0.to_lazy()
    var_3 = var_0.filter(var_2)
    var_4 = var_3.to_try()
    var_5 = maybe_0.to_lazy()
    var_6 = var_0.map(var_0)

def test_maybe_filter_and_to_lazy():
    int_0 = -283
    tuple_0 = (int_0, int_0, int_0)
    none_type_0 = None
    bool_0 = True
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
    var_0 = maybe_0.filter(tuple_0)
    var_1 = var_0.to_lazy()
    none_type_1 = None
    maybe_1 = maybe.Maybe(none_type_1, none_type_1)
    maybe_1.filter(var_1)

def test_maybe_filter_works_correctly():
    """Test that the Maybe filter method works correctly."""
    int_0 = 2281
    str_0 = "gZ(\\mOcN"
    dict_0 = {str_0: str_0}
    tuple_0 = (str_0, str_0, dict_0, dict_0)
    bool_0 = True
    maybe_0 = maybe.Maybe(tuple_0, bool_0)
    timer_instance = maybe_0.get_or_else(int_0)
    generic_0 = typing.Generic()
    bool_1 = False
    box_0 = maybe_0.to_box()
    maybe_1 = maybe.Maybe(generic_0, bool_1)
    maybe_1.filter(timer_instance)

def test_maybe_conversions():
    bool_0 = True
    none_type_0 = None
    maybe_0 = maybe.Maybe(bool_0, none_type_0)
    validation_0 = maybe_0.to_validation()

    int_0 = -1784
    tuple_0 = ()
    maybe_1 = maybe.Maybe(int_0, tuple_0)
    validation_1 = maybe_1.to_validation()
    value_1 = maybe_1.get_or_else(int_0)
    try_1 = maybe_1.to_try()

    float_0 = -286.64
    maybe_2 = maybe.Maybe(float_0, float_0)
    maybe_1.bind(try_1)

def test_maybe_and_either_behavior():
    """Test the behavior of Maybe and Either types."""
    none_type_0 = None
    bool_0 = True
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
    set_0 = {bool_0}
    timer_instance = maybe_0.map(set_0)
    int_0 = -1095
    bool_1 = True
    maybe_1 = maybe.Maybe(int_0, bool_1)
    either_instance = maybe_1.to_either()

def test_maybe_to_lazy_and_to_either():
    """Test the Maybe class's to_lazy and to_either methods."""
    none_type_0 = None
    maybe_0 = maybe.Maybe(none_type_0, none_type_0)
    tuple_0 = (maybe_0,)
    lazy_0 = maybe_0.to_lazy()
    bool_0 = False
    maybe_1 = maybe.Maybe(tuple_0, bool_0)
    either_0 = maybe_0.to_either()
    try_1 = maybe_1.to_try()
    either_1 = maybe_0.to_either()
    either_2 = maybe_1.to_either()
    lazy_1 = try_1.to_lazy()

def test_maybe_to_try_to_box():
    bool_0 = True
    bool_1 = False
    maybe_0 = maybe.Maybe(bool_0, bool_1)
    try_0 = maybe_0.to_try()
    try_0.to_box()

def test_maybe_filter_and_get_or_else():
    bytes_0 = b"C\xcf\xe7/"
    none_type_0 = None
    bool_0 = True
    maybe_0 = maybe_lib.Maybe(none_type_0, bool_0)
    var_0 = maybe_0.ap(none_type_0)
    var_1 = var_0.to_lazy()
    var_2 = var_1.to_validation()
    var_3 = maybe_0.filter(var_2)
    var_4 = var_3.get_or_else(var_3)
    var_5 = var_3.to_either()
    var_6 = var_2.to_try()
    bool_1 = var_3.__eq__(var_0)
    var_7 = var_4.to_box()
    var_6.ap(bytes_0)

def test_maybe_instance_behavior():
    """Test the behavior of Maybe instances."""
    bytes_0 = b"\xdbC\xcf\xe7/"
    none_type_0 = None
    bool_0 = True
    maybe_0 = maybe_lib.Maybe(none_type_0, bool_0)
    var_0 = maybe_0.ap(none_type_0)
    var_1 = var_0.ap(bytes_0)
    var_2 = var_1.to_validation()
    maybe_1 = maybe_lib.Maybe(none_type_0, bytes_0)
    var_3 = maybe_1.get_or_else(maybe_1)
    var_4 = maybe_1.to_validation()
    var_5 = maybe_1.bind(var_4)
    var_6 = maybe_1.to_either()
    var_7 = maybe_1.ap(maybe_1)
    int_0 = -3289
    bool_1 = var_6.__eq__(var_4)
    var_8 = var_6.bind(maybe_1)
    var_9 = maybe_1.to_try()
    bool_2 = maybe_1.__eq__(var_5)
    var_10 = var_5.to_validation()
    var_9.ap(int_0)

def test_maybe_class_methods():
    bool_0 = False
    maybe_0 = maybe.Maybe(bool_0, bool_0)
    bool_1 = maybe_0.__eq__(bool_0)
    maybe_1 = maybe.Maybe(bool_0, bool_0)
    var_0 = maybe_1.to_either()
    var_1 = maybe_1.to_lazy()
    var_2 = var_1.to_validation()
    maybe_2 = maybe.Maybe(bool_0, bool_0)
    maybe_2.map(var_2)

def test_maybe_equality_and_try_validation():
    bool_0 = False
    maybe_0 = maybe_lib.Maybe(bool_0, bool_0)
    bool_1 = maybe_0.__eq__(maybe_0)
    timer_instance = maybe_0.to_try()
    timer_instance.to_validation()

