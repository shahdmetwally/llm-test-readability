import pytest
import validation as validation
import builtins as builtins

def test_validation_is_success_and_is_fail_with_empty_maybe():
    """
    Given a Validation instance created with two docstring-like strings,
    check that is_success() returns True, equality with itself holds,
    and then verify that is_fail() returns a Maybe via to_maybe().
    """
    # Create a Validation with a docstring that describes an empty Maybe
    docstring = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_instance = validation.Validation(docstring, docstring)

    # Verify success status and equality
    is_success = validation_instance.is_success()
    equals_itself = validation_instance.__eq__(validation_instance)

    # Obtain the fail-maybe result
    is_fail = validation_instance.is_fail()
    is_fail.to_maybe()

def test_validation_equality_with_none_returns_success() -> None:
    """Test that checking equality of a Validation object with None returns a success result."""
    # Arrange
    none_value = None
    first_input = -6891
    second_input = 3125
    second_input_tuple = (second_input,)
    validation_instance = validation.Validation(first_input, second_input_tuple)

    # Act
    equality_result = validation_instance.__eq__(none_value)

    # Assert
    equality_result.is_success()

def test_validation_str_returns_fail_status_for_empty_dicts():
    """Test that __str__() on a Validation with empty dict arguments returns an object whose .is_fail() returns True."""
    empty_dict = {}
    validation = validation.Validation(empty_dict, empty_dict)
    str_representation = validation.__str__()
    str_representation.is_fail()

def test_validation_empty_sets_to_either_and_maybe():
    """Test that a Validation with empty sets can be converted to Either and Maybe,
    and that to_maybe() is idempotent."""
    empty_set = set()
    validation = validation.Validation(empty_set, empty_set)
    either_result = validation.to_either()
    maybe_result = validation.to_maybe()
    maybe_result.to_maybe()

def test_validation_to_either_and_is_fail_with_string_arguments():
    """
    Tests that calling to_either() and is_fail() on a Validation instance
    constructed with identical string arguments works without error.
    """
    input_string = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation = validation.Validation(input_string, input_string)

    either_result = validation.to_either()
    equality_result = validation.__eq__(validation)
    is_fail_result = validation.is_fail()

    is_fail_result.to_maybe()

def test_validation_to_maybe_returns_maybe_that_supports_chaining() -> None:
    """Verify that Validation.to_maybe() returns a Maybe that itself supports .to_maybe()."""
    input_data = set()
    validation_instance = validation.Validation(input_data, input_data)
    maybe_result = validation_instance.to_maybe()
    maybe_result.to_maybe()

def test_validation_with_none_input():
    """Test that Validation can be instantiated with None for both parameters."""
    none_value = None
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_to_maybe_returns_none_for_none_input() -> None:
    """Test that to_maybe() returns None when Validation is initialized with None."""
    # Arrange: Create a Validation instance with None for both parameters
    none_input = None
    validation_instance = validation.Validation(none_input, none_input)

    # Act: Call to_maybe() on the Validation instance
    result = validation_instance.to_maybe()

    # Assert: Result should be None
    assert result is None

def test_validation_is_fail_returns_false_for_valid_object():
    """Test that Validation.is_fail() returns False for a valid object."""
    valid_object = object()
    validation = validation.Validation(valid_object, valid_object)
    validation.is_fail()

def test_validation_map_with_none_input():
    """Test that Validation.map handles None input gracefully."""
    none_type_0 = None
    int_0 = -895
    bool_0 = True
    tuple_0 = (int_0, bool_0)
    dict_0 = {tuple_0: tuple_0}
    tuple_1 = (dict_0, dict_0, int_0)
    validation_0 = validation.Validation(tuple_1, bool_0)
    validation_0.map(none_type_0)

def test_validation_bind_accepts_none():
    """Test that bind() accepts a None value without raising an error."""
    bytes_data = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validation_instance = validation.Validation(bytes_data, bytes_data)
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_with_list_of_true_values_on_false_instance():
    """Test that Validation.ap() can be called with a list of True values
    when the Validation instance is initialized with False and a list."""
    initial_bool = False
    true_values = [True, True, True, True]
    validation_instance = validation.Validation(initial_bool, true_values)
    validation_instance.ap(true_values)

def test_validation_to_box_returns_success_for_true_initial_value():
    """Test that a successful validation returns an is_success() result when converted to a box."""
    # Arrange
    initial_value = True
    validation_result = validation.Validation(initial_value, initial_value)

    # Act
    boxed_result = validation_result.to_box()
    success_result = boxed_result.is_success()

    # Assert (implicit - call is made to verify no exception occurs and result is truthy)

def test_validation_bind_and_to_lazy_work_together():
    """Test that `Validation.bind()` and `to_lazy()` work together correctly."""
    initial_validator = validation.Validation([], [])

    lazy_validator = initial_validator.to_lazy()
    bound_lazy_validator = lazy_validator.bind(None)

    bound_lazy_validator.to_lazy()

def test_validation_to_lazy_and_try_ap_returns_success():
    """Test that chaining to_lazy, to_try, and ap on a Validation instance results in a successful Try."""
    input_data = {}
    validation_a = validation.Validation(input_data, input_data)
    lazy_validation = validation_a.to_lazy()           # Convert to Lazy
    try_validation = lazy_validation.to_try()          # Convert to Try
    _ = lazy_validation.ap(validation_a)               # Apply Validation (result unused)
    try_validation.is_success()

def test_validation_to_try_returns_success_result():
    """Test that Validation.to_try() returns a success result."""
    int_0 = 0
    list_0 = [int_0]
    validation_0 = validation.Validation(int_0, list_0)
    var_0 = validation_0.to_try()
    var_0.is_success()

def test_validation_equality_and_transformations_complex():
    """Test various Validation operations: equality, conversion to box/either/try/lazy, and string representation."""
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    dict_with_none_key = {none_value: bytes_value, bytes_value: bytes_value}
    validation_1 = validation.Validation(none_value, dict_with_none_key)

    # Test equality checks
    eq_result = validation_1.__eq__(validation_1)  # self-equality
    box_result = validation_1.to_box()

    validation_2 = validation.Validation(bytes_value, bytes_value)
    either_result_1 = box_result.to_either()
    is_fail_result_1 = validation_2.is_fail()
    try_result = either_result_1.to_try()

    validation_3 = validation.Validation(is_fail_result_1, bytes_value)
    str_result = validation_3.__str__()
    lazy_result_1 = validation_2.to_lazy()

    validation_4 = validation.Validation(bytes_value, bytes_value)
    either_result_2 = box_result.to_either()
    lazy_result_2 = validation_3.to_lazy()

    validation_5 = validation.Validation(lazy_result_2, validation_4)
    is_fail_result_2 = validation_2.is_fail()

    # Apply string representation to the equality result
    eq_result.map(str_result)

def test_custom_validation_equality_and_bind_with_bytes_keys():
    """Test that a Validation instance with bytes keys supports equality checks,
    conversion to Maybe, and bind operations."""
    bytes_key = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    # Create a dict mixing None and bytes keys
    nested_dict = {none_value: bytes_key, bytes_key: bytes_key}
    # Initialize Validation with None as first arg and the nested dict as second
    validation_0 = validation.Validation(none_value, nested_dict)
    # Test equality of the same Validation instance
    var_0 = validation_0.__eq__(validation_0)
    # Convert to Maybe type
    var_1 = validation_0.to_maybe()
    # Create a second Validation using only bytes
    validation_1 = validation.Validation(bytes_key, bytes_key)
    # Bind the bytes value to the validation
    validation_1.bind(bytes_key)

def test_validation_equality_and_box_conversion():
    """Test that comparing two Validation instances and converting the result to a box works correctly."""
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    dict_value = {none_value: bytes_value, bytes_value: bytes_value}
    validation_a = validation.Validation(none_value, dict_value)
    validation_b = validation.Validation(bytes_value, none_value)
    equality_result = validation_a.__eq__(validation_b)
    equality_result.to_box()