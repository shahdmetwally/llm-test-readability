import maybe as mb
import typing as tp

def test_maybe_class_creation():
    input_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    maybe_instance = mb.Maybe(input_bytes, input_bytes)
    assert maybe_instance.value == input_bytes
    assert maybe_instance.error == input_bytes

def test_maybe_object_creation_1():
    """Test the creation of a Maybe object"""
    none_value = None
    maybe_instance = mb.Maybe(none_value, none_value)

def test_maybe_class_functionality_1():
    """Tests the functionality of the Maybe class in the module_0 module."""
    string_input = "p4xa>bl^oP"
    maybe_instance = mb.Maybe(string_input, string_input)
    equality_result = maybe_instance.__eq__(string_input)
    applied_result = maybe_instance.ap(string_input)
    get_or_else_result = maybe_instance.get_or_else(string_input)
    mapped_result = maybe_instance.map(applied_result)
    filtered_result = maybe_instance.filter(get_or_else_result)
    mapped_result_2 = maybe_instance.map(applied_result)
    applied_result_2 = maybe_instance.ap(string_input)
    equality_result_2 = applied_result.__eq__(applied_result_2)
    filtered_result_2 = get_or_else_result.filter(get_or_else_result)
    get_or_else_result_2 = applied_result_2.get_or_else(string_input)
    maybe_instance_2 = mb.Maybe(string_input, string_input)
    to_validation_result = maybe_instance_2.to_validation()
    bind_result = maybe_instance_2.bind(to_validation_result)
    to_either_result = bind_result.to_either()

def test_maybe_eq_method_with_set():
    bool_value = False
    set_value = {bool_value, bool_value, bool_value, bool_value}
    none_value = None
    maybe_instance = mb.Maybe(none_value, none_value)
    comparison_result = maybe_instance.__eq__(set_value)

def test_maybe_class_functionality_2():
    """Test the functionality of the Maybe class"""
    bool_value = True
    maybe_instance = mb.Maybe(bool_value, bool_value)
    bound_maybe = maybe_instance.bind(bool_value)
    mapped_maybe = bound_maybe.map(bool_value)
    tuple_value = (bool_value, bool_value, bool_value, bool_value)
    maybe_instance_2 = mb.Maybe(tuple_value, bool_value)
    set_instance = set()
    set_instance.to_box()

def test_maybe_map_method_1():
    none_value = None
    bool_value = False
    maybe_instance = mb.Maybe(none_value, bool_value)
    maybe_instance.map(bool_value)

def test_maybe_class_behavior():
    """Test the behavior of the Maybe class in module_0"""
    bool_value_0 = True
    maybe_instance_0 = mb.Maybe(bool_value_0, bool_value_0)
    empty_dict = {}
    none_value = None
    bool_value_1 = False
    maybe_instance_1 = mb.Maybe(none_value, bool_value_1)
    maybe_instance_1.bind(empty_dict)

def test_maybe_class_functionality_3():
    """Test the functionality of the Maybe class in module_0"""

    bytes_data = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_type = None
    maybe_instance_0 = mb.Maybe(bytes_data, none_type)
    box_instance = maybe_instance_0.to_box()
    int_data = 0
    bool_data = True
    maybe_instance_1 = mb.Maybe(int_data, bool_data)
    filtered_maybe_instance = maybe_instance_1.filter(maybe_instance_1)
    lazy_instance = maybe_instance_1.to_lazy()
    applied_maybe_instance = filtered_maybe_instance.ap(maybe_instance_0)
    filtered_applied_maybe_instance = filtered_maybe_instance.filter(applied_maybe_instance)
    maybe_instance_2 = mb.Maybe(lazy_instance, box_instance)
    equality_check = lazy_instance.__eq__(bool_data)

def test_maybe_ap_method_applies_function_to_value():
    input_value = 2862
    none_value = None
    bool_value = False
    maybe_instance = mb.Maybe(none_value, bool_value)
    maybe_instance.ap(input_value)

def test_maybe_class_functionality_4():
    """Test the functionality of the Maybe class in module_0."""
    int_value = 0
    bool_value = True
    maybe_instance = mb.Maybe(int_value, bool_value)
    filter_result = maybe_instance.filter(maybe_instance)
    maybe_lazy = maybe_instance.to_lazy()
    none = None
    filtered_lazy_timer = mb.Maybe(none, none)
    filtered_lazy_timer.filter(lazy_maybe)

def test_timer_start_stops_correctly():
    start_time = -283
    timer_duration = (start_time, start_time, start_time)
    none = None
    timer_running = True
    timer_instance = mb.Maybe(none, timer_running)
    filtered_timer = timer_instance.filter(timer_duration)
    lazy_timer = filtered_timer.to_lazy()
    none = None
    filtered_lazy_timer = mb.Maybe(none, none)
    filtered_lazy_timer.filter(lazy_timer)

def test_maybe_class_behavior_1():
    timer_start_time = 2281
    timer_name = "gZ(\\mOcN"
    timer_settings = {timer_name: timer_name}
    timer_data = (timer_name, timer_name, timer_settings, timer_settings)
    timer_is_running = True
    timer_instance = mb.Maybe(timer_data, timer_is_running)
    timer_instance_or_default = timer_instance.get_or_else(timer_start_time)
    generic_object = tp.Generic()
    filter_condition = False
    timer_instance_box = timer_instance.to_box()
    filtered_timer_instance = mb.Maybe(generic_object, filter_condition)
    filtered_timer_instance.filter(timer_instance_or_default)

def test_maybe_class_functionality_3():
    """Test the functionality of the Maybe class"""
    bool_value = True
    none_value = None
    maybe_instance = mb.Maybe(bool_value, none_value)
    validation_result = maybe_instance.to_validation()
    float_value = -286.64
    int_value = -1784
    tuple_value = ()
    maybe_instance_2 = mb.Maybe(int_value, tuple_value)
    validation_result_2 = maybe_instance_2.to_validation()
    or_else_result = maybe_instance_2.get_or_else(int_value)
    try_result = maybe_instance_2.to_try()
    maybe_instance_3 = mb.Maybe(float_value, float_value)
    maybe_instance_2.bind(try_result)

def test_maybe_class_methods_1():
    none_type = None
    bool_value = True
    maybe_instance = mb.Maybe(none_type, bool_value)
    set_value = {bool_value}
    map_result = maybe_instance.map(set_value)
    int_value = -1095
    bool_value_1 = True
    maybe_instance_1 = mb.Maybe(int_value, bool_value_1)
    either_result = maybe_instance_1.to_either()

def test_maybe_class_functionality_3():
    none_type = None
    maybe_none = mb.Maybe(none_type, none_type)
    maybe_tuple = (maybe_none,)
    maybe_lazy = maybe_none.to_lazy()
    bool_value = False
    maybe_bool = mb.Maybe(maybe_tuple, bool_value)
    maybe_either = maybe_none.to_either()
    maybe_try = maybe_bool.to_try()
    maybe_lazy = maybe_try.to_lazy()
    maybe_either_2 = maybe_none.to_either()
    maybe_either_3 = maybe_bool.to_either()

def test_maybe_to_try_to_box():
    """Test that the Maybe class can be converted to a Try and then to a Box."""
    bool_true = True
    bool_false = False
    maybe_instance = mb.Maybe(bool_true, bool_false)
    try_instance = maybe_instance.to_try()
    try_instance.to_box()

def test_maybe_class_behavior_1():
    bytes_data = b"C\xcf\xe7/"
    none_value = None
    bool_value = True
    maybe_instance = mb.Maybe(none_value, bool_value)
    applied_maybe = maybe_instance.ap(none_value)
    lazy_instance = applied_maybe.to_lazy()
    validation_instance = lazy_instance.to_validation()
    filtered_maybe = maybe_instance.filter(validation_instance)
    alternative_value = filtered_maybe.get_or_else(filtered_maybe)
    either_instance = filtered_maybe.to_either()
    try_instance = validation_instance.to_try()
    equality_result = filtered_maybe.__eq__(maybe_instance)
    box_instance = alternative_value.to_box()
    try_instance.ap(bytes_data)

def test_maybe_class_functionality_5():
    """Test the functionality of the Maybe class in module_0"""
    input_bytes = b"\xdbC\xcf\xe7/"
    none_input = None
    bool_input = True
    maybe_instance_0 = mb.Maybe(none_input, bool_input)
    applied_maybe_0 = maybe_instance_0.ap(none_input)
    applied_maybe_1 = applied_maybe_0.ap(input_bytes)
    maybe_validation_0 = applied_maybe_1.to_validation()
    maybe_instance_1 = mb.Maybe(none_input, input_bytes)
    maybe_or_else_result = maybe_instance_1.get_or_else(maybe_instance_1)
    maybe_instance_1_validation = maybe_instance_1.to_validation()
    bound_maybe_1 = maybe_instance_1.bind(maybe_instance_1_validation)
    maybe_instance_1_either = maybe_instance_1.to_either()
    applied_maybe_1 = maybe_instance_1.ap(maybe_instance_1)
    input_int = -3289
    equality_check_result = maybe_instance_1_either.__eq__(maybe_instance_1_validation)
    bound_maybe_1 = maybe_instance_1.bind(maybe_instance_1)
    maybe_instance_1_try = maybe_instance_1.to_try()
    equality_check_result_2 = maybe_instance_1.__eq__(bound_maybe_1)
    bound_maybe_1_validation = bound_maybe_1.to_validation()
    maybe_instance_1_try.ap(input_int)

def test_maybe_class_functionality_6():
    """Test the functionality of the Maybe class."""
    bool_value = False
    maybe_instance = mb.Maybe(bool_value, bool_value)
    comparison_result = maybe_instance.__eq__(bool_value)
    maybe_instance_2 = mb.Maybe(bool_value, bool_value)
    either_instance = maybe_instance_2.to_either()
    lazy_instance = maybe_instance_2.to_lazy()
    validation_instance = lazy_instance.to_validation()
    maybe_instance_3 = mb.Maybe(bool_value, bool_value)
    maybe_instance_3.map(validation_instance)

def test_maybe_equality_and_try_validation():
    """Test the equality method and validation of Maybe class"""
    bool_value = False
    maybe_instance = mb.Maybe(bool_value, bool_value)
    equality_result = maybe_instance.__eq__(maybe_instance)
    maybe_try = maybe_instance.to_try()
    maybe_validation = maybe_try.to_validation()