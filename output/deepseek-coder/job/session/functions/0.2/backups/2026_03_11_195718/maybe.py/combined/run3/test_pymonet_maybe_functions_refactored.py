import maybe as mb
import typing as tp

def test_maybe_class_initialization():
    """Tests the initialization of the Maybe class"""
    input_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    maybe_instance = mb.Maybe(input_bytes, input_bytes)

def test_maybe_instance_with_none_values():
    """Test the creation of a Maybe instance with None values."""
    none_value = None
    maybe_instance = mb.Maybe(none_value, none_value)

def test_maybe_class_functionality():
    """Test the functionality of the Maybe class in module_0"""
    string_0 = "p4xa>bl^oP"
    maybe_instance = mb.Maybe(string_0, string_0)
    equality_result = maybe_instance.__eq__(string_0)
    applied_result = maybe_instance.ap(string_0)
    or_else_result = maybe_instance.get_or_else(string_0)
    mapped_result = maybe_instance.map(applied_result)
    filter_result = maybe_instance.filter(or_else_result)
    mapped_result_2 = maybe_instance.map(applied_result)
    applied_result_2 = maybe_instance.ap(string_0)
    equality_result_2 = applied_result.__eq__(applied_result_2)
    filter_result_2 = applied_result.filter(or_else_result)
    or_else_result_2 = applied_result_2.get_or_else(string_0)
    maybe_instance_2 = mb.Maybe(string_0, string_0)
    validation_result = maybe_instance_2.to_validation()
    bind_result = maybe_instance_2.bind(validation_result)
    either_result = bind_result.to_either()

def test_maybe_eq_set():
    """Test the __eq__ method of the Maybe class when comparing to a set of booleans."""
    bool_value = False
    set_of_bools = {bool_value, bool_value, bool_value, bool_value}
    none_value = None
    maybe_instance = mb.Maybe(none_value, none_value)
    is_equal = maybe_instance.__eq__(set_of_bools)

def test_maybe_class_and_methods():
    initial_value = True
    maybe_instance = mb.Maybe(initial_value, initial_value)
    bound_instance = maybe_instance.bind(initial_value)
    mapped_instance = bound_instance.map(initial_value)
    tuple_value = (initial_value, initial_value, initial_value, initial_value)
    maybe_instance_2 = mb.Maybe(tuple_value, initial_value)
    set_instance = set()
    set_instance.to_box()

def test_maybe_map_method():
    """Test the map method of the Maybe class in the module_0 module."""
    none_value = None
    bool_value = False
    module_under_test = mb.Maybe(none_value, bool_value)
    maybe_instance = module_under_test.map(bool_value)

def test_maybe_class_behavior():
    bool_value_1 = True
    maybe_instance_1 = mb.Maybe(bool_value_1, bool_value_1)
    empty_dict = {}
    none_value = None
    bool_value_2 = False
    maybe_instance_2 = mb.Maybe(none_value, bool_value_2)
    maybe_instance_2.bind(empty_dict)

def test_maybe_class_functionality_2():
    bytes_data = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_data = None
    maybe_instance_0 = mb.Maybe(bytes_data, none_data)
    box_data = maybe_instance_0.to_box()
    int_data = 0
    bool_data = True
    maybe_instance_1 = mb.Maybe(int_data, bool_data)
    filtered_data = maybe_instance_1.filter(maybe_instance_1)
    lazy_data = maybe_instance_1.to_lazy()
    applied_data = filtered_data.ap(maybe_instance_0)
    filtered_applied_data = filtered_data.filter(applied_data)
    maybe_instance_2 = mb.Maybe(lazy_data, box_data)
    equality_result = lazy_data.__eq__(bool_data)

def test_maybe_class_ap_method_behavior():
    """Test the behavior of the 'ap' method in the Maybe class."""
    integer = 2862
    none_value = None
    boolean_value = False
    maybe_instance = mb.Maybe(none_value, boolean_value)
    maybe_instance.ap(integer)

def test_maybe_class_behavior_2():
    """Tests the behavior of the Maybe class in the module_0 module."""
    int_value = 0
    bool_value = True
    maybe_instance = mb.Maybe(int_value, bool_value)
    filtered_maybe = maybe_instance.filter(maybe_instance)
    maybe_lazy = filtered_maybe.to_lazy()
    filtered_maybe_lazy = maybe_instance.to_lazy()
    filtered_filtered_maybe = filtered_maybe.filter(filtered_maybe_lazy)
    filtered_filtered_maybe_try = filtered_filtered_maybe.to_try()
    maybe_lazy_2 = maybe_instance.to_lazy()
    mapped_maybe = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_and_to_lazy():
    """Test the `filter` and `to_lazy` methods of the `Maybe` class."""
    int_value = -283
    tuple_value = (int_value, int_value, int_value)
    none_type_value = None
    bool_value = True
    maybe_instance = mb.Maybe(none_type_value, bool_value)
    filtered_maybe = maybe_instance.filter(tuple_value)
    lazy_maybe = filtered_maybe.to_lazy()
    none_type_value_1 = None
    maybe_instance_1 = mb.Maybe(none_type_value_1, none_type_value_1)
    maybe_instance_1.filter(lazy_maybe)

def test_maybe_class_behavior_2():
    initial_value = 2281
    string_value = "gZ(\\mOcN"
    dictionary_value = {string_value: string_value}
    tuple_value = (string_value, string_value, dictionary_value, dictionary_value)
    boolean_value = True
    maybe_instance = mb.Maybe(tuple_value, boolean_value)
    get_or_else_result = maybe_instance.get_or_else(initial_value)
    generic_value = tp.Generic()
    second_boolean_value = False
    to_box_result = maybe_instance.to_box()
    second_maybe_instance = mb.Maybe(generic_value, second_boolean_value)
    second_maybe_instance.filter(get_or_else_result)

def test_maybe_class_functionality_2():
    is_timer_running = True
    no_timer_running = None
    timer_instance = mb.Maybe(is_timer_running, no_timer_running)
    timer_validation = timer_instance.to_validation()
    timer_duration = -286.64
    timer_start_time = -1784
    no_timer_running_tuple = ()
    timer_instance_2 = mb.Maybe(timer_start_time, no_timer_running_tuple)
    timer_validation_2 = timer_instance_2.to_validation()
    timer_start_time_2 = timer_instance_2.get_or_else(timer_start_time)
    timer_try = timer_instance_2.to_try()
    timer_instance_3 = mb.Maybe(timer_duration, timer_duration)
    timer_instance_2.bind(timer_try)

def test_maybe_class_behavior_2():
    none_type = None
    bool_value = True
    maybe_instance = mb.Maybe(none_type, bool_value)
    set_value = {bool_value}
    map_result = maybe_instance.map(set_value)
    int_value = -1095
    bool_value_2 = True
    maybe_instance_2 = mb.Maybe(int_value, bool_value_2)
    either_result = maybe_instance.to_either()
    try_value = maybe_instance_2.to_try()
    either_value_2 = maybe_instance.to_either()
    either_value_3 = maybe_instance_2.to_either()
    try_value.to_lazy()

def test_maybe_to_try_and_box():
    """Test that the Maybe class can be converted to a Try and then to a Box."""
    bool_true = True
    bool_false = False
    maybe_instance = mb.Maybe(bool_true, bool_false)
    try_instance = maybe_instance.to_try()
    try_instance.to_box()

def test_maybe_class_behavior_2():
    binary_data = b"C\xcf\xe7/"
    none_value = None
    bool_value = True
    maybe_instance = mb.Maybe(none_value, bool_value)
    applied_maybe = maybe_instance.ap(none_value)
    lazy_maybe = applied_maybe.to_lazy()
    validation_maybe = lazy_maybe.to_validation()
    filtered_maybe = maybe_instance.filter(validation_maybe)
    either_maybe = filtered_maybe.to_either()
    try_maybe = validation_maybe.to_try()
    either_value = maybe_instance.to_either()
    applied_value = maybe_instance.ap(maybe_instance)
    int_value = -3289
    equality_result = tp.eq(either_value, validation_maybe)
    bound_value_2 = filtered_maybe.bind(maybe_instance)
    try_value = maybe_instance.to_try()
    equality_result_2 = tp.eq(maybe_instance, bound_value_2)
    validation_result_2 = filtered_maybe.to_validation()
    applied_value_3 = try_value.ap(int_value)

def test_maybe_class_methods():
    """Tests the functionality of the Maybe class methods."""
    bytes_data = b"\xdbC\xcf\xe7/"
    none_type = None
    bool_value = True
    maybe_instance = mb.Maybe(none_type, bool_value)
    applied_value = maybe_instance.ap(none_type)
    validation_value = applied_value.to_validation()
    maybe_instance_2 = mb.Maybe(none_type, bytes_data)
    or_else_value = maybe_instance_2.get_or_else(maybe_instance_2)
    validation_value_2 = maybe_instance_2.to_validation()
    bound_value = maybe_instance_2.bind(validation_value_2)
    either_value = maybe_instance_2.to_either()
    applied_value_2 = maybe_instance_2.ap(maybe_instance_2)
    int_value = -3289
    equality_result = tp.eq(either_value, validation_value_2)
    bound_value_2 = bound_value.bind(maybe_instance_2)
    try_value = maybe_instance_2.to_try()
    equality_result_2 = tp.eq(maybe_instance_2, bound_value)
    validation_result_2 = bound_value.to_validation()
    applied_value_3 = try_value.ap(int_value)

def test_maybe_class_functionality_3():
    """Tests the functionality of the Maybe class in the maybe module."""
    none_value = None
    maybe_instance = mb.Maybe(none_value, none_value)
    tuple_value = (maybe_instance,)
    lazy_value = maybe_instance.to_lazy()
    bool_value = False
    maybe_instance_2 = mb.Maybe(tuple_value, bool_value)
    either_value = maybe_instance.to_either()
# (Truncated by extractor)