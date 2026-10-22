import validation as validate
import builtins as builtins
import pytest

def test_is_success_equality_is_fail_to_maybe():
    str_value = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation = validate.Validation(str_value, str_value)

    assert validation.is_success() is True, "Expected is_success to be True"
    assert validation == validation, "Expected validation to be equal"
    assert validation.is_fail() != validation, "Expected is_fail to be not equal"
    assert validation.is_fail().to_maybe() is None, "Expected to_maybe to be None"

def test_validation_eq_operation_with_none_input():
    int_val = -6891
    tuple_value = (3125,)
    validation = validate.Validation(int_val, tuple_value)
    compare_result = validation.__eq__(None)

    assert compare_result.is_success(), "Test case: test_is_success_equality_is_fail_to_maybe"

def test_validation_object_string_representation_fails():
    empty_dict = {}
    validation_object = validate.Validation(empty_dict, empty_dict)
    validation_object_string = str(validation_object)

    with pytest.raises(AttributeError):
        validation_object_string.is_fail()

def test_validation_conversions():
    empty_set = set()
    validation = validate.Validation(empty_set, empty_set)
    validation.to_either()
    validation.to_maybe()
    validation.to_maybe().to_maybe()

def test_create_empty_maybe_valid_maybe():
    maybe_expression = "Create empty maybe."
    validation = validate.Validation(maybe_expression, maybe_expression)
    validation_either = validation.to_either()

    assert validation_either.is_right()
    assert validation_either.get() is None
    is_same_validation = validation.__eq__(validation)

    assert is_same_validation is True
    is_fail = validation.is_fail()

    assert is_fail is False
    maybe_is_fail = is_fail.to_maybe()

    assert maybe_is_fail.is_nothing()

def test_validation_to_maybe_returns_a_maybe():
    set_0 = set()
    validation_0 = validate.Validation(set_0, set_0)
    maybe_0 = validation_0.to_maybe()

    assert isinstance(maybe_0, builtins.Maybe)

def test_validation_initialization_none_none():
    none_value = None
    validation = validate.Validation(none_value, none_value)

    assert validation is not None, "Object initialization failed with None and None"

def test_validation_to_maybe_new_name():
    none_type = None
    validation_0 = validate.Validation(none_type, none_type)
    validation_0.to_maybe()

def test_validation_fails_when_objects_dont_match_other_version():
    list_false = [False, False, False, False]
    validation_instance = validate.Validation(list_false, list_false)

    with pytest.raises(ValueError, match=r"Invalid value.*"):
        validation_instance.ap(list_false)

    list_true = [True, True, True]
    validation_instance.ap(list_true)

def test_user_maps_none_to_validation():
    current_user = None
    validation_cohorts_id = -895
    current_user_is_active = True
    cohorts = (validation_cohorts_id, current_user_is_active)
    user_cohorts_map = {cohorts: cohorts}
    validation_cohorts = (user_cohorts_map, user_cohorts_map, validation_cohorts_id)
    current_validation = validate.Validation(validation_cohorts, current_user_is_active)
    current_validation.map(current_user)

    assert current_validation.user_id == builtins.NoneType

def test_timer_sets_last():
    with builtins.Timer(logger=None) as timer:
        waste_time()

    assert timer.last >= 0.02

def test_case_12():
    bool_false = False
    bool_true = True
    list_false = [bool_false, bool_false, bool_false, bool_false]
    validation_instance = builtins.Validation(bool_false, list_false)

    with pytest.raises(ValueError, match=r"Invalid value.*"):
        validation_instance.ap(list_false)

    list_true = [bool_true, bool_true, bool_true]
    validation_instance.ap(list_true)

def test_box_is_success_on_valid_validation():
    bool_0 = True
    validation_0 = validate.Validation(bool_0, bool_0)
    validation_box_0 = validation_0.to_box()

    assert validation_box_0.is_success() is True

def test_validation_to_lazy_and_bind_lazy_version():
    none_type_0 = None
    empty_list = []
    validation = validate.Validation(empty_list, empty_list)
    lazy_validation = validation.to_lazy()
    bound_lazy_validation = lazy_validation.bind(none_type_0)
    bound_lazy_validation.to_lazy()

def test_validation_ap_try_is_success():
    inputs = {}
    validation_under_test = validate.Validation(inputs, inputs)
    lazy_transformed = validation_under_test.to_lazy()
    try_transformed = lazy_transformed.to_try()
    validation_ap_result = validation_under_test.ap(validation_under_test)
    validation_try_result = try_transformed.is_success()

    assert validation_try_result == 1
    assert isinstance(validation_try_result, builtins.bool)
    assert isinstance(validation_ap_result, validate.Validation)
    assert isinstance(validation_try_result, builtins.bool)
    assert isinstance(validation_try_result, builtins.bool)
    assert isinstance(validation_try_result, builtins.bool)

def test_successful_validation():
    input_value = 0
    valid_list = [input_value]
    validation = validate.Validation(input_value, valid_list)
    result = validation.to_try()

    assert result.is_success()

def test_validation_operations_modified():
    bytes_input = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_input = None
    dict_input = {none_type_input: bytes_input, bytes_input: bytes_input}
    validation_0 = validate.Validation(none_type_input, dict_input)
    equality_check_0 = validation_0.__eq__(validation_0)
    box_0 = validation_0.to_box()
    validation_1 = validate.Validation(bytes_input, bytes_input)
    either_1 = validation_1.to_either()
    fail_check_1 = validation_1.is_fail()
    validation_2 = validate.Validation(fail_check_1, bytes_input)
    lazy_2 = validation_2.to_lazy()
    validation_3 = validate.Validation(bytes_input, bytes_input)
    either_3 = validation_3.to_either()
    fail_check_3 = validation_3.is_fail()
    validation_4 = validate.Validation(fail_check_3, validation_3)
    string_rep_4 = validation_4.__str__()
    equality_check_0.map(string_rep_4)

def test_validation_equality_and_to_maybe():
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = validate.Validation(none_type_0, dict_0)
    validation_1 = validate.Validation(bytes_0, bytes_0)
    validation_condition = (validation_0 == validation_1)

    assert validation_condition is False
    result_box = validation_0.to_box()

    assert result_box is not None

def test_validation_objects_not_equal_when_not_same_elements():
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = validate.Validation(none_type_0, dict_0)
    validation_1 = validate.Validation(bytes_0, none_type_0)
    validation_condition = (validation_0 == validation_1)

    assert validation_condition is False

    result_box = validation_0.to_box()
    assert result_box is not None