import validation as valid
import builtins as builtins

def test_validation_is_success_and_is_fail():
    str_0 = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_0 = valid.Validation(str_0, str_0)
    var_0 = validation_0.is_success()
    var_1 = validation_0.__eq__(validation_0)
    var_2 = validation_0.is_fail()
    var_2.to_maybe()

def test_validation_equality_with_none():
    none_type = None
    int_0 = -6891
    int_1 = 3125
    tuple_0 = (int_1,)
    validation_0 = valid.Validation(int_0, tuple_0)
    result = validation_0.__eq__(none_type)
    assert not result.is_success()

def test_validation_str_is_fail():
    data = {}
    validation = valid.Validation(data, data)
    result = validation.__str__()
    assert isinstance(result, str)
    is_fail = result.is_fail()
    assert isinstance(is_fail, bool)

def test_validation_to_either_and_maybe():
    empty_set = set()
    validation = valid.Validation(empty_set, empty_set)
    either = validation.to_either()
    maybe = validation.to_maybe()
    assert isinstance(either, builtins.Left)
    assert isinstance(maybe, builtins.Nothing)

def test_validation_is_fail():
    str_0 = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_0 = valid.Validation(str_0, str_0)
    var_2 = validation_0.is_fail()
    assert isinstance(var_2.to_maybe(), builtins.Maybe)

def test_validation_to_maybe():
    empty_set = set()
    validation = valid.Validation(empty_set, empty_set)
    maybe = validation.to_maybe()
    assert isinstance(maybe, builtins.Maybe)

def test_case_6_validation_object_creation_with_none_values():
    none_value = None
    validation_object = valid.Validation(none_value, none_value)
    assert isinstance(validation_object, valid.Validation)

def test_validation_to_maybe_new():
    none_type = None
    validation = valid.Validation(none_type, none_type)
    maybe = validation.to_maybe()
    assert isinstance(maybe, builtins.Maybe)

def test_validation_is_fail_returns_false_when_validation_is_valid():
    obj = builtins.object()
    validation_object = valid.Validation(obj, obj)
    assert not validation_object.is_fail()

def test_validation_map_with_none():
    none_value = None
    int_value = -895
    bool_value = True
    tuple_value = (int_value, bool_value)
    dict_value = {tuple_value: tuple_value}
    tuple_values = (dict_value, dict_value, int_value)
    validation = valid.Validation(tuple_values, bool_value)
    validation.map(none_value)

def test_validation_bind_with_none():
    bytes_data = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validation = valid.Validation(bytes_data, bytes_data)
    none_value = None
    validation.bind(none_value)

def test_validation_ap_method():
    valid_value = False
    invalid_values = [True, True, True, True]
    validation = valid.Validation(valid_value, invalid_values)
    validation.ap(invalid_values)

def test_validation_to_box_is_success():
    bool_0 = True
    validation_0 = valid.Validation(bool_0, bool_0)
    var_0 = validation_0.to_box()
    assert var_0.is_success()

def test_lazy_validation_bind_and_to_lazy():
    none_type_value = None
    empty_list = []
    validation = valid.Validation(empty_list, empty_list)
    lazy_validation = validation.to_lazy()
    bind_result = lazy_validation.bind(none_type_value)
    final_lazy_result = bind_result.to_lazy()
    assert final_lazy_result is not None

def test_lazy_validation_to_try_and_ap_and_is_success():
    empty_dict = {}
    validation = valid.Validation(empty_dict, empty_dict)
    lazy_obj = validation.to_lazy()
    try_obj = lazy_obj.to_try()
    applied_obj = try_obj.ap(validation)
    assert applied_obj.is_success()

def test_validation_to_try_is_success_new():
    zero = 0
    list_of_zero = [zero]
    validation = valid.Validation(zero, list_of_zero)
    try_result = validation.to_try()
    assert try_result.is_success()

def test_validation_equality_and_conversions():
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = valid.Validation(none_type_0, dict_0)
    var_0 = validation_0.__eq__(validation_0)
    var_1 = validation_0.to_box()
    validation_1 = valid.Validation(bytes_0, bytes_0)
    var_2 = var_1.to_either()
    var_3 = validation_1.is_fail()
    var_4 = var_2.to_try()
    validation_2 = valid.Validation(var_3, bytes_0)
    var_5 = validation_2.__str__()
    var_6 = validation_1.to_lazy()
    validation_3 = valid.Validation(bytes_0, bytes_0)
    var_7 = var_1.to_either()
    var_8 = validation_2.to_lazy()
    validation_4 = valid.Validation(var_8, validation_3)
    var_9 = validation_1.is_fail()
    var_0.map(var_5)

def test_validation_equality_and_bind_methods():
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = valid.Validation(none_type_0, dict_0)
    var_0 = validation_0.__eq__(validation_0)
    var_1 = validation_0.to_maybe()
    validation_1 = valid.Validation(bytes_0, bytes_0)
    validation_1.bind(bytes_0)
    assert var_0 == True
    assert isinstance(var_1, builtins.Maybe)

def test_validation_equality_new():
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = valid.Validation(none_type_0, dict_0)
    validation_1 = valid.Validation(bytes_0, none_type_0)
    assert validation_0.__eq__(validation_1)
    validation_0.__eq__(validation_1).to_box()