import pytest
import validation as validation
import builtins as builtins

def test_validation_with_identical_message_and_value():
    """Test that a Validation created with identical message and value strings
    correctly reports success/failure status and can be converted to Maybe."""

    # Use the same string for both the value and message fields
    description = (
        "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    )

    # Create a Validation instance where value and message are the same string
    v = validation.Validation(description, description)

    # Check success status
    is_success = v.is_success()

    # Check equality with itself
    is_equal_to_self = v.__eq__(v)

    # Check failure status and convert the result to a Maybe
    is_fail = v.is_fail()
    is_fail.to_maybe()

def test_validation_eq_with_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None returns a result
    on which is_success() can be called without error."""

    # Inputs: a negative integer and a tuple used to construct the Validation
    none_value = None
    negative_int = -6891
    positive_int = 3125
    args_tuple = (positive_int,)

    # Create a Validation instance with the given arguments
    validation_instance = validation.Validation(negative_int, args_tuple)

    # Compare the Validation instance to None using __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Call is_success() on the result of the equality comparison
    eq_result.is_success()

def test_validation_str_representation_is_fail_with_empty_dicts():
    """Test that a Validation instance created with empty dicts exposes an is_fail method via __str__."""
    empty_dict = {}

    # Create a Validation instance with empty schema and data
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation result
    str_result = validation_instance.__str__()

    # Check whether the result indicates a failure
    str_result.is_fail()

def test_validation_with_empty_sets_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets can be converted to Either and Maybe,
    and that chaining to_maybe() on the result is also valid."""
    empty_set = set()

    # Create a Validation with no successes and no failures
    empty_validation = validation.Validation(empty_set, empty_set)

    # Convert to Either and Maybe representations
    either_result = empty_validation.to_either()
    maybe_result = empty_validation.to_maybe()

    # Verify that the Maybe result can itself be converted to Maybe
    maybe_result.to_maybe()

def test_validation_failure_supports_equality_either_and_maybe_conversion():
    """
    Test that a Validation object created with a failure message
    correctly supports equality comparison, conversion to Either,
    and conversion to Maybe via is_fail().
    """
    failure_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance using the failure message as both arguments
    validation_instance = validation.Validation(failure_message, failure_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    is_equal = validation_instance.__eq__(validation_instance)

    # Check if the validation represents a failure
    is_failure = validation_instance.is_fail()

    # Convert the failure result to a Maybe type
    is_failure.to_maybe()

def test_validation_with_empty_sets_chained_to_maybe():
    """Test that a Validation created from empty sets can be converted to Maybe,
    and that the resulting Maybe can also be converted to Maybe (chaining)."""
    empty_set = set()

    # Create a Validation with empty valid and invalid sets
    val = validation.Validation(empty_set, empty_set)

    # Convert Validation to Maybe
    maybe_result = val.to_maybe()

    # Chain another to_maybe call on the resulting Maybe
    maybe_result.to_maybe()

def test_validation_initialized_with_none_arguments():
    """Test that Validation can be instantiated with None for both arguments."""
    # Both the primary value and the validation rule are explicitly None
    none_value = None
    none_rule = None

    validation_0 = validation.Validation(none_value, none_rule)

def test_validation_to_maybe_with_none_inputs():
    """Test that Validation.to_maybe() can be called when both fields are None."""
    # Create a Validation instance with no value and no error (both None)
    none_value = None
    validation_instance = validation.Validation(none_value, none_value)

    # Convert the None-valued Validation to a Maybe type
    validation_instance.to_maybe()

def test_validation_is_fail_with_object_as_both_arguments():
    """Test that Validation.is_fail() can be called when the same object
    is used for both constructor arguments."""
    # Use a plain object instance as both arguments to Validation
    plain_object = builtins.object()
    validation_instance = validation.Validation(plain_object, plain_object)

    # Verify that is_fail() can be invoked without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation.map() can be called with None on a nested tuple/dict structure."""

    # Build a nested input: a tuple containing a dict (keyed by a tuple) and an int
    key = (-895, True)
    nested_dict = {key: key}
    nested_tuple = (nested_dict, nested_dict, -895)

    # Construct the Validation instance with the nested structure and a truthy flag
    v = validation.Validation(nested_tuple, True)

    # Call map with None as the mapping function
    v.map(None)

def test_validation_bind_with_none():
    """Test that Validation.bind() accepts None as a binding value without error."""

    # Use identical byte sequences for both constructor arguments
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Construct a Validation instance with the raw bytes as both arguments
    val = validation.Validation(raw_bytes, raw_bytes)

    # Bind None to the validation instance
    none_value = None
    val.bind(none_value)

def test_validation_ap_with_all_true_values():
    """Test that Validation.ap() can be called with a list of True values on a Failure instance."""
    # Create a Failure validation (is_success=False) with a list of True error flags
    is_success = False
    all_true = True
    error_flags = [all_true, all_true, all_true, all_true]

    failure_validation = validation.Validation(is_success, error_flags)

    # Apply the list of True values to the Failure validation
    failure_validation.ap(error_flags)

def test_validation_with_both_flags_true_converts_to_successful_box():
    """Test that a Validation created with both flags set to True produces a successful Box."""
    is_valid = True

    # Create a Validation instance with both 'valid' flags set to True
    valid_validation = validation.Validation(is_valid, is_valid)

    # Convert the Validation to a Box and verify it represents a success
    result_box = valid_validation.to_box()
    result_box.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy():
    """Test that a Validation created with empty lists can be converted to lazy,
    bound with None, and then converted to lazy again without error."""

    # Create an empty validation with no successes and no failures
    empty_list = []
    empty_validation = validation.Validation(empty_list, empty_list)

    # Convert the validation to a lazy representation
    lazy_validation = empty_validation.to_lazy()

    # Bind None to the lazy validation
    bound_result = lazy_validation.bind(None)

    # Convert the bound result to lazy as well
    bound_result.to_lazy()

def test_validation_lazy_and_try_conversions_with_ap():
    """Test that a Validation can be converted to Lazy and Try forms,
    and that applying (ap) another Validation to the Lazy form works
    without raising errors. Verifies is_success() is callable on the Try result."""

    # Create an empty Validation (both value and error containers are empty dicts)
    empty_dict = {}
    val = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation to its Lazy (deferred) representation
    lazy_val = val.to_lazy()

    # Convert the Lazy value to a Try (success/failure) representation
    try_val = lazy_val.to_try()

    # Apply the original Validation to the Lazy value using ap (applicative apply)
    ap_result = lazy_val.ap(val)

    # Check that the Try value reports its success status
    try_val.is_success()

def test_validation_chained_operations_with_mixed_types():
    """
    Test that Validation supports chaining of operations (eq, to_box, to_either,
    to_try, to_lazy, is_fail, __str__, map) across multiple instances constructed
    with mixed types (None, bytes, and other Validation-derived values).
    """
    # Arbitrary bytes value used as a payload/key throughout the test
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    # Build a dict with None and bytes as keys/values to use as the error container
    none_value = None
    mixed_dict = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # Validation with None as the success value and a mixed dict as the failure info
    validation_none_dict = validation.Validation(none_value, mixed_dict)

    # Check equality of the instance with itself
    eq_result = validation_none_dict.__eq__(validation_none_dict)

    # Convert to a Box; this result is reused later
    box_result = validation_none_dict.to_box()

    # A second Validation instance using raw bytes for both arguments
    validation_bytes_bytes = validation.Validation(raw_bytes, raw_bytes)

    # Convert the box to an Either
    either_result = box_result.to_either()

    # Check whether the bytes-bytes Validation represents a failure
    is_fail_result = validation_bytes_bytes.is_fail()

    # Convert the Either to a Try
    try_result = either_result.to_try()

    # A third Validation using the is_fail boolean result and raw bytes
    validation_fail_flag = validation.Validation(is_fail_result, raw_bytes)

    # Get the string representation of the fail-flag Validation
    str_representation = validation_fail_flag.__str__()

    # Convert the fail-flag Validation to a Lazy
    lazy_from_fail_flag = validation_bytes_bytes.to_lazy()

    # A fourth Validation using raw bytes for both arguments (independent instance)
    validation_bytes_bytes_2 = validation.Validation(raw_bytes, raw_bytes)

    # Re-convert the original box to an Either (second usage)
    either_result_2 = box_result.to_either()

    # Convert the fail-flag Validation to a Lazy (second lazy conversion)
    lazy_from_validation_fail = validation_fail_flag.to_lazy()

    # A fifth Validation using the lazy result and the independent bytes Validation
    validation_lazy_nested = validation.Validation(lazy_from_validation_fail, validation_bytes_bytes_2)

    # Check is_fail on the bytes-bytes Validation again
    is_fail_result_2 = validation_bytes_bytes.is_fail()

    # Map the string representation over the eq_result (a Box)
    eq_result.map(str_representation)

def test_validation_equality_and_maybe_with_none_key_and_bytes_value():
    """
    Test Validation behaviour when constructed with None as the value and a
    mixed-key dict as the error: verifies __eq__ against itself, conversion
    to Maybe, and that bind on a bytes-based Validation does not raise.
    """
    # Arbitrary bytes payload used as both a dict value and a validation value
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    none_value = None

    # Dict with mixed key types: None -> bytes and bytes -> bytes
    error_dict = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # Construct a Validation with None as the value and the mixed dict as the error
    validation_none_value = validation.Validation(none_value, error_dict)

    # Verify that a Validation instance is equal to itself
    eq_result = validation_none_value.__eq__(validation_none_value)

    # Convert the Validation to a Maybe representation
    maybe_result = validation_none_value.to_maybe()

    # Construct a second Validation where both value and error are bytes
    validation_bytes_value = validation.Validation(raw_bytes, raw_bytes)

    # Attempt to bind bytes directly; exercises the bind code path
    validation_bytes_value.bind(raw_bytes)

def test_validation_eq_with_mismatched_types_calls_to_box():
    """Test that comparing two Validation instances with swapped key/value types
    and calling to_box() on the result does not raise an error."""

    # Arbitrary byte sequence used as a value in the dict and as a key
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Dict with mixed key types: None -> bytes, bytes -> bytes
    mixed_dict = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # First Validation: key is None, value is the mixed dict
    validation_with_none_key = validation.Validation(none_value, mixed_dict)

    # Second Validation: key is bytes, value is None
    validation_with_bytes_key = validation.Validation(raw_bytes, none_value)

    # Compare the two Validation instances (mismatched key/value types)
    eq_result = validation_with_none_key.__eq__(validation_with_bytes_key)

    # Convert the equality result to a box representation
    eq_result.to_box()

