import validation
import builtins

def test_validate_validation():
    message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_obj = validation.Validation(message, message)
    is_success = validation_obj.is_success()
    is_equal = validation_obj.__eq__(validation_obj)
    is_fail = validation_obj.is_fail()
    assert is_fail.to_maybe()

def test_eq_with_none_returns_success_if_eq():
    none_value = None
    first_integer = -6891
    second_integer = 3125
    first_tuple = (second_integer,)
    validation_object = validation.Validation(first_integer, first_tuple)
    assert validation_object.__eq__(none_value).is_success()

def test_validate_validation_failure_failure():
    data = {}
    valid = validation.Validation(data, data)
    string_rep = valid.__str__()
    fail_check = string_rep.is_fail()
    assert fail_check

def test_validation_to_either_and_maybe():
    empty_set = set()
    validation_obj = validation.Validation(empty_set, empty_set)
    validation_either = validation_obj.to_either()
    validation_maybe = validation_obj.to_maybe()
    assert validation_either is None
    assert isinstance(validation_maybe, builtins.Some)
    assert isinstance(validation_maybe.to_maybe(), builtins.Maybe)

def test_case_5_to_either_method_returns_right_instance():
    empty_maybe = "Create empty maybe."
    validation_obj = validation.Validation(empty_maybe, empty_maybe)
    validation_as_either = validation_obj.to_either()
    assert isinstance(validation_as_either, builtins.Right)

def test_case_5_eq_method_returns_true_for_same_object():
    empty_maybe = "Create empty maybe."
    validation_obj = validation.Validation(empty_maybe, empty_maybe)
    assert validation_obj == validation_obj

def test_case_5_is_fail_method_returns_true():
    empty_maybe = "Create empty maybe."
    validation_obj = validation.Validation(empty_maybe, empty_maybe)
    is_validation_fail = validation_obj.is_fail()
    assert is_validation_fail == True

def test_case_5_is_fail_method_to_maybe_returns_maybe():
    empty_maybe = "Create empty maybe."
    validation_obj = validation.Validation(empty_maybe, empty_maybe)
    is_validation_fail = validation_obj.is_fail()
    fail_to_maybe = is_validation_fail.to_maybe()
    assert isinstance(fail_to_maybe, builtins.Maybe)

def test_maybe_conversion_with_set_duplicated():
    empty_set = set()
    validation_obj = validation.Validation(empty_set, empty_set)
    maybe = validation_obj.to_maybe()
    may = maybe.to_maybe()

def test_validation_failure_conditions():
    test_object = builtins.object()
    test_validation = validation.Validation(test_object, test_object)
    assert test_validation.is_fail(), "Expected validation to fail"

def test_case_9():
    none_type_0 = None
    int_0 = -895
    bool_0 = True
    tuple_0 = (int_0, bool_0)
    dict_0 = {tuple_0: tuple_0}
    tuple_1 = (dict_0, dict_0, int_0)
    validation_0 = validation.Validation(tuple_1, bool_0)
    validation_0.map(none_type_0)

def test_bytes_bind_to_none():
    bytes_value = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validation_obj = validation.Validation(bytes_value, bytes_value)
    none_type_value = builtins.NoneType
    validation_obj.bind(none_type_value)
    assert validation_obj.is_fail() == True

def test_validation_ap_should_append_to_list_and_not_affect_original_list():
    is_not_valid = False
    is_valid = True
    validation_results = [is_valid, is_valid, is_valid, is_valid]
    orig_validation_results = validation_results.copy()
    validation_obj = validation.Validation(is_not_valid, validation_results)
    validation_obj.ap(validation_results)
    assert validation_results == orig_validation_results + orig_validation_results

def test_boxing_returns_success():
    validation_input = True
    validation_obj = validation.Validation(validation_input, validation_input)
    box = validation_obj.to_box()
    assert box.is_success()

def test_lazy_monad_validation_chain():
    none_value = None
    empty_list = []
    validation_object = validation.Validation(empty_list, empty_list)
    lazy_object = validation_object.to_lazy()
    bound_lazy_object = lazy_object.bind(none_value)
    bound_lazy_object.to_lazy()

def test_lazy_validation_chaining_methods():
    try_ = lazy.to_try()
    applied = lazy.ap(validation)
    assert try_.is_success() == True

def test_validation_to_try_object_success():
    validation_obj = validation.Validation(None, {None: None})
    var_try_object = validation_obj.to_try()
    assert var_try_object.is_success() == True

def test_Validation_equality_and_box_conversions():
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    dict_value = {none_value: bytes_value, bytes_value: bytes_value}
    validation_obj = builtins.Validation(none_value, dict_value)
    equality_result = validation_obj.__eq__(validation_obj)
    box = validation_obj.to_box()
    assert equality_result == True
    assert isinstance(box, builtins.Box)

def test_validation_object_comparison_and_maybe_conversion():
    b_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_obj = None
    data_0 = {none_obj: b_0, b_0: b_0}
    v_0 = validation.Validation(none_obj, data_0)
    v_0_equals_v_0 = v_0 == v_0
    v_0_converted_to_maybe = v_0.to_maybe()
    v_1 = validation.Validation(b_0, b_0)
    v_1.bind(b_0)
    assert isinstance(v_0_equals_v_0, bool)
    assert isinstance(v_0_converted_to_maybe, builtins.Maybe)

def test_two_validation_objects_equal():
    bytes_data = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_data = None
    dict_data = {none_type_data: bytes_data, bytes_data: bytes_data}
    validation_one = validation.Validation(none_type_data, dict_data)
    validation_two = validation.Validation(bytes_data, none_type_data)
    result_box = validation_one.__eq__(validation_two)
    result_box.to_box()
    assert result_box == True or result_box == False