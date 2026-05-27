import maybe as maybe
import typing as typing

def test_maybe_instance_creation():
    bytes_0 = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    maybe_instance = maybe.Maybe(bytes_0, bytes_0)

def test_maybe_instance_creation_with_none_values():
    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_equality_and_application_1():
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

def test_maybe_equality_with_set():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    none_type_0 = None
    maybe_0 = maybe.Maybe(none_type_0, none_type_0)
    bool_1 = maybe_0.__eq__(set_0)

def test_maybe_bind_and_map():
    bool_0 = True
    maybe_0 = maybe.Maybe(bool_0, bool_0)
    var_0 = maybe_0.bind(bool_0)
    var_1 = var_0.map(bool_0)
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    maybe_1 = maybe.Maybe(tuple_0, bool_0)
    set_0 = set()
    set_0.to_box()

def test_maybe_map_function_2():
    none_type_0 = None
    bool_0 = False
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
    assert maybe_0.map(bool_0) == bool_0

def test_maybe_class_behavior():
    bool_0 = True
    maybe_0 = maybe.Maybe(bool_0, bool_0)
    dict_0 = {}
    none_type_0 = None
    bool_1 = False
    maybe_1 = maybe.Maybe(none_type_0, bool_1)
    maybe_1.bind(dict_0)

def test_maybe_class_behavior():
    bytes_0 = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_type_0 = None
    maybe_0 = maybe.Maybe(bytes_0, none_type_0)
    box_0 = maybe_0.to_box()
    int_0 = 0
    bool_0 = True
    maybe_1 = maybe.Maybe(int_0, bool_0)
    filtered_maybe_1 = maybe_1.filter(maybe_1)
    lazy_2 = maybe_1.to_lazy()
    applied_maybe_3 = filtered_maybe_1.ap(maybe_0)
    filtered_maybe_4 = filtered_maybe_1.filter(applied_maybe_3)
    maybe_2 = maybe.Maybe(lazy_2, box_0)
    bool_1 = lazy_2.__eq__(bool_0)

def test_maybe_ap_method_updates_value():
    int_0 = 2862
    none_type_0 = None
    bool_0 = False
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
    maybe_0.ap(int_0)
    assert maybe_0.value == int_0

def test_maybe_filter_and_to_lazy():
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

def test_maybe_filter_and_lazy():
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

def test_maybe_class_behavior_1():
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

def test_maybe_to_validation_and_get_or_else():
    bool_0 = True
    none_type_0 = None
    maybe_0 = maybe.Maybe(bool_0, none_type_0)
    var_0 = maybe_0.to_validation()
    float_0 = -286.64
    int_0 = -1784
    tuple_0 = ()
    maybe_1 = maybe.Maybe(int_0, tuple_0)
    var_1 = maybe_1.to_validation()
    var_2 = maybe_1.get_or_else(int_0)
    var_3 = maybe_1.to_try()
    maybe_2 = maybe.Maybe(float_0, float_0)
    maybe_1.bind(var_3)

def test_maybe_map_and_to_either():
    none_type_0 = None
    bool_0 = True
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
    set_0 = {bool_0}
    timer_instance = maybe_0.map(set_0)
    int_0 = -1095
    bool_1 = True
    maybe_1 = maybe.Maybe(int_0, bool_1)
    either_instance = maybe_1.to_either()

def test_maybe_behavior_2():
    none_type_0 = None
    maybe_0 = maybe.Maybe(none_type_0, none_type_0)
    tuple_0 = (maybe_0,)
    lazy_0 = maybe_0.to_lazy()
    bool_0 = False
    maybe_1 = maybe.Maybe(tuple_0, bool_0)
    either_1 = maybe_0.to_either()
    try_2 = maybe_1.to_try()
    either_3 = maybe_0.to_either()
    either_4 = maybe_1.to_either()
    lazy_2 = try_2.to_lazy()

def test_maybe_to_try_to_box():
    bool_0 = True
    bool_1 = False
    maybe_0 = maybe.Maybe(bool_0, bool_1)
    try_0 = maybe_0.to_try()
    try_0.to_box()

def test_maybe_filter_and_to_either():
    bytes_0 = b"C\xcf\xe7/"
    none_type_0 = None
    bool_0 = True
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
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

def test_maybe_monad_behavior():
    bytes_0 = b"\xdbC\xcf\xe7/"
    none_type_0 = None
    bool_0 = True
    maybe_0 = maybe.Maybe(none_type_0, bool_0)
    var_0 = maybe_0.ap(none_type_0)
    var_1 = var_0.ap(bytes_0)
    var_2 = var_1.to_validation()
    maybe_1 = maybe.Maybe(none_type_0, bytes_0)
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

def test_maybe_equality_and_mapping():
    bool_0 = False
    maybe_0 = maybe.Maybe(bool_0, bool_0)
    bool_1 = maybe_0.__eq__(bool_0)
    maybe_1 = maybe.Maybe(bool_0, bool_0)
    var_0 = maybe_1.to_either()
    var_1 = maybe_1.to_lazy()
    var_2 = var_1.to_validation()
    maybe_2 = maybe.Maybe(bool_0, bool_0)
    maybe_2.map(var_2)

def test_maybe_equality_and_conversion_1():
    bool_0 = False
    maybe_0 = maybe.Maybe(bool_0, bool_0)
    bool_1 = maybe_0.__eq__(maybe_0)
    var_0 = maybe_0.to_try()
    var_0.to_validation()