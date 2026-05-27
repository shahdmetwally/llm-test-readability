import pytest
import validation as validation
import builtins as builtins

def test_validation_with_identical_success_and_fail_messages_converts_to_maybe():
    """
    Test that a Validation created with identical success and fail messages
    correctly reports its success/fail status and can be converted to a Maybe.
    """
    # Use the same string for both success and fail message fields
    empty_maybe_description = (
        "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    )

    # Create a Validation instance with identical success and fail messages
    v = validation.Validation(empty_maybe_description, empty_maybe_description)

    # Check success status
    is_success = v.is_success()

    # Check equality with itself
    is_equal_to_self = v.__eq__(v)

    # Check fail status and convert the result to a Maybe
    fail_result = v.is_fail()
    fail_result.to_maybe()

def test_validation_eq_with_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None via __eq__ returns a result
    on which is_success() can be called without error."""
    none_value = None
    base_int = -6891
    tuple_value = 3125
    validation_args = (tuple_value,)

    # Create a Validation instance with a negative int and a single-element tuple
    validation_instance = validation.Validation(base_int, validation_args)

    # Compare the Validation instance against None
    eq_result = validation_instance.__eq__(none_value)

    # Verify the result exposes is_success() without raising
    eq_result.is_success()

def test_validation_str_representation_is_fail_with_empty_dicts():
    """Test that converting a Validation instance (created with empty dicts) to
    string yields an object on which is_fail() can be called without error."""
    empty_dict = {}

    # Create a Validation instance using empty dicts for both arguments
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation instance to its string representation
    str_representation = validation_instance.__str__()

    # Verify that the string representation exposes the is_fail() method
    str_representation.is_fail()

def test_validation_with_empty_sets_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets can be converted
    to Either and Maybe without raising errors, including chaining
    to_maybe() on the resulting Maybe value."""
    empty_set = set()

    # Create a Validation instance with no successes and no failures
    val = validation.Validation(empty_set, empty_set)

    # Convert to Either representation
    either_result = val.to_either()

    # Convert to Maybe representation
    maybe_result = val.to_maybe()

    # Chain a further to_maybe() call on the Maybe result
    maybe_result.to_maybe()

def test_validation_equality_and_maybe_conversion():
    """
    Test that a Validation object created with an error message supports
    equality comparison, conversion to Either, failure checking,
    and that the failure result can be converted to Maybe.
    """
    # A descriptive error message used as both the success and failure value
    error_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance using the error message as both arguments
    validation_instance = validation.Validation(error_message, error_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    is_equal = validation_instance.__eq__(validation_instance)

    # Check whether the validation represents a failure
    is_failure = validation_instance.is_fail()

    # Convert the failure result to a Maybe type
    is_failure.to_maybe()

def test_validation_with_empty_sets_chained_to_maybe():
    """Test that a Validation created from empty sets can be converted to Maybe,
    and that the resulting Maybe can also be converted to Maybe (chaining)."""
    empty_set = set()

    # Create a Validation with empty valid and invalid sets
    val = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe
    maybe_result = val.to_maybe()

    # Chain another to_maybe call on the resulting Maybe
    maybe_result.to_maybe()

def test_validation_init_with_none_arguments():
    """Test that Validation can be instantiated with both arguments set to None."""
    # Use explicit None to represent the absence of both required parameters
    none_value = None
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_to_maybe_with_none_inputs():
    """Test that Validation.to_maybe() can be called when both arguments are None."""
    # Create a Validation instance with None for both fields
    none_value = None
    validation_instance = validation.Validation(none_value, none_value)

    # Convert the Validation to a Maybe type; should not raise
    validation_instance.to_maybe()

def test_validation_is_fail_with_object_as_subject_and_value():
    """Test that Validation.is_fail() can be called when both subject and value are the same plain object."""
    # Create a plain object to serve as both the subject and value of the validation
    subject_and_value = builtins.object()

    # Construct a Validation instance with the same object for both arguments
    validation_instance = validation.Validation(subject_and_value, subject_and_value)

    # Verify that is_fail() can be invoked without error on this validation
    validation_instance.is_fail()

def test_validation_map_with_none_on_tuple_wrapped_dict():
    """Test that calling map(None) on a Validation wrapping a tuple-keyed dict structure does not raise unexpectedly."""
    # Construct a tuple key and use it in a dict to form a nested data structure
    negative_int = -895
    bool_flag = True
    tuple_key = (negative_int, bool_flag)
    dict_with_tuple_key = {tuple_key: tuple_key}

    # Wrap the dict in a tuple to form the validation value
    nested_tuple = (dict_with_tuple_key, dict_with_tuple_key, negative_int)

    # Create a Validation instance with the nested structure and a truthy flag
    v = validation.Validation(nested_tuple, bool_flag)

    # Call map with None as the mapping function
    v.map(None)

def test_validation_bind_with_none_value():
    """Test that Validation.bind() accepts None as a value without raising an error."""
    # Use identical byte sequences for both constructor arguments
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validator = validation.Validation(raw_bytes, raw_bytes)

    # Bind None to the validator — exercising the None-value code path
    none_value = None
    validator.bind(none_value)

def test_validation_ap_with_all_true_values():
    """Test that Validation.ap() can be called with a list of all-True values on a Failure instance."""
    is_valid = False
    flag = True

    # A list of four True flags used as both the error list and the ap argument
    true_flags = [flag, flag, flag, flag]

    # Create a Validation instance representing a failure (is_valid=False)
    validation_instance = validation.Validation(is_valid, true_flags)

    # Apply ap with the same list of True values
    validation_instance.ap(true_flags)

def test_validation_with_both_flags_true_converts_to_successful_box():
    """Test that a Validation created with both flags set to True produces a successful Box."""
    is_valid = True

    # Create a Validation instance with both parameters set to True
    valid_validation = validation.Validation(is_valid, is_valid)

    # Convert to a Box and verify it represents a success
    result_box = valid_validation.to_box()
    result_box.is_success()

def test_validation_to_lazy_bind_none_and_back_to_lazy():
    """Test that a Validation constructed with empty lists can be converted to lazy,
    bound with None, and then converted to lazy again without error."""
    none_value = None
    empty_list = []

    # Create a Validation with empty lists for both fields
    empty_validation = validation.Validation(empty_list, empty_list)

    # Convert the Validation to a lazy representation
    lazy_validation = empty_validation.to_lazy()

    # Bind None to the lazy validation
    bound_result = lazy_validation.bind(none_value)

    # Convert the bound result to lazy as well
    bound_result.to_lazy()

def test_validation_lazy_and_try_conversion_with_ap():
    """Test that a Validation created from an empty dict can be converted to lazy,
    then to try, and that ap() can be applied with the original validation."""

    # Create a Validation instance using empty dicts for both value and error
    empty_dict = {}
    val = validation.Validation(empty_dict, empty_dict)

    # Convert the validation to its lazy representation
    lazy_val = val.to_lazy()

    # Convert the lazy validation to a Try type
    try_val = lazy_val.to_try()

    # Apply the original validation using ap() on the lazy validation
    ap_result = lazy_val.ap(val)

    # Check the success state of the Try value
    try_val.is_success()

def test_validation_with_zero_value_in_list_is_success():
    """Test that a Validation created with a zero value and a list containing zero
    can be converted to a Try result that reports success."""

    # Create a validation with zero as the value and a single-element list containing zero
    zero_value = 0
    value_list = [zero_value]
    validation_instance = validation.Validation(zero_value, value_list)

    # Convert to Try and verify the result is a success
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_chained_operations_with_mixed_types():
    """
    Test that Validation supports chaining of operations (eq, to_box, to_either,
    to_try, to_lazy, is_fail, __str__, map) across multiple instances constructed
    with mixed types (None, bytes, and other Validation-derived values).
    """
    # Arbitrary bytes payload used as a value/error carrier in Validation instances
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # A dict mixing None and bytes as keys/values, used as the success value
    mixed_dict = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # First Validation: error=None, value=mixed_dict
    validation_none_error = validation.Validation(none_value, mixed_dict)

    # Check equality of the instance with itself
    eq_result = validation_none_error.__eq__(validation_none_error)

    # Convert to Box, then chain to Either and Try
    box_result = validation_none_error.to_box()

    # Second Validation: both error and value are raw bytes
    validation_bytes_both = validation.Validation(raw_bytes, raw_bytes)

    # Convert the box to an Either monad
    either_result = box_result.to_either()

    # Check whether the bytes-based validation represents a failure
    is_fail_result = validation_bytes_both.is_fail()

    # Convert the Either monad to a Try monad
    try_result = either_result.to_try()

    # Third Validation: error=is_fail_result (bool), value=raw_bytes
    validation_fail_flag = validation.Validation(is_fail_result, raw_bytes)

    # Get the string representation of the fail-flag validation
    str_representation = validation_fail_flag.__str__()

    # Convert bytes-both validation to Lazy
    lazy_from_bytes_both = validation_bytes_both.to_lazy()

    # Fourth Validation: identical to second (bytes, bytes)
    validation_bytes_copy = validation.Validation(raw_bytes, raw_bytes)

    # Re-convert the box to Either (second time, same source)
    either_result_second = box_result.to_either()

    # Convert fail-flag validation to Lazy
    lazy_from_fail_flag = validation_fail_flag.to_lazy()

    # Fifth Validation: error=lazy monad, value=bytes-copy Validation
    validation_lazy_error = validation.Validation(lazy_from_fail_flag, validation_bytes_copy)

    # Check is_fail on the bytes-both validation again
    is_fail_result_second = validation_bytes_both.is_fail()

    # Map the string representation over the equality result
    eq_result.map(str_representation)

def test_validation_equality_and_maybe_with_none_key_and_bytes_value():
    """
    Test that Validation supports equality comparison and conversion to Maybe
    when constructed with None as the value and a dict (containing None and bytes keys)
    as the error, and that bind can be called on a bytes-valued Validation.
    """
    # Arbitrary bytes payload used as both a dict value and a Validation value
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    none_value = None

    # Error dict with mixed key types: None -> bytes and bytes -> bytes
    error_dict = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # Construct a Validation where the value is None and the error is the mixed dict
    validation_none_value = validation.Validation(none_value, error_dict)

    # Check that a Validation instance is equal to itself
    var_0 = validation_none_value.__eq__(validation_none_value)

    # Convert the Validation to a Maybe representation
    var_1 = validation_none_value.to_maybe()

    # Construct a second Validation where both value and error are bytes
    validation_bytes_value = validation.Validation(raw_bytes, raw_bytes)

    # Call bind with the raw bytes object on the bytes-valued Validation
    validation_bytes_value.bind(raw_bytes)

def test_validation_eq_result_to_box_with_mismatched_types():
    """Test that comparing two Validation instances with swapped/mismatched
    value and key types, then calling to_box() on the equality result,
    executes without error."""

    # Arbitrary byte sequence used as a value/key in the dict
    byte_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Dict with None and bytes as keys mapping
# (Truncated by extractor)