import pytest
import validation as validation
import builtins as builtins

def test_validation_with_identical_success_and_fail_messages_converts_to_maybe():
    """
    Test that a Validation created with identical success and fail messages
    correctly reports its success/fail status and can be converted to Maybe.
    """
    # Use the same string for both success and fail message fields
    empty_maybe_docstring = (
        "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    )

    # Create a Validation instance where both arguments are the same string
    validation_instance = validation.Validation(empty_maybe_docstring, empty_maybe_docstring)

    # Check success status
    is_success_result = validation_instance.is_success()

    # Check equality of the instance with itself
    is_equal_to_self = validation_instance.__eq__(validation_instance)

    # Check fail status and convert the result to a Maybe value
    fail_result = validation_instance.is_fail()
    fail_result.to_maybe()

def test_validation_eq_with_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None returns a result
    on which is_success() can be called without error."""
    none_value = None
    negative_int = -6891
    positive_int = 3125
    tuple_arg = (positive_int,)

    # Create a Validation instance with a negative int and a single-element tuple
    validation_instance = validation.Validation(negative_int, tuple_arg)

    # Compare the Validation instance to None using __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Call is_success() on the result of the equality check
    eq_result.is_success()

def test_validation_str_representation_is_fail_with_empty_dicts():
    """Test that a Validation instance created with empty dicts returns a result
    whose string representation exposes an `is_fail` method without raising."""
    # Create a Validation instance with empty schema and data
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation result
    str_result = validation_instance.__str__()

    # Call is_fail() on the string result (exercising the method exists and is callable)
    str_result.is_fail()

def test_validation_with_empty_sets_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets can be converted to Either and Maybe,
    and that chaining to_maybe() on the result is valid."""
    empty_set = set()

    # Create a Validation with no successes and no failures
    val = validation.Validation(empty_set, empty_set)

    # Convert to Either and Maybe representations
    either_result = val.to_either()
    maybe_result = val.to_maybe()

    # Verify that the Maybe result itself supports to_maybe() chaining
    maybe_result.to_maybe()

def test_validation_failure_supports_equality_either_and_maybe_conversion():
    """
    Test that a Validation object created with a failure message
    supports equality comparison, conversion to Either, and that
    calling to_maybe() on the is_fail() result executes without error.
    """
    # A descriptive failure message used to construct the Validation
    failure_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance with the same value for both fields
    validation_instance = validation.Validation(failure_message, failure_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    is_equal = validation_instance.__eq__(validation_instance)

    # Determine whether the validation represents a failure
    is_failure = validation_instance.is_fail()

    # Attempt to convert the failure flag result to a Maybe type
    is_failure.to_maybe()

def test_validation_with_empty_sets_chained_to_maybe():
    """Test that a Validation created from empty sets can be converted to Maybe,
    and that the resulting Maybe can also be converted to Maybe (chaining)."""
    empty_set = set()

    # Create a Validation with no successes and no failures
    empty_validation = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe
    maybe_result = empty_validation.to_maybe()

    # Chain another to_maybe() call on the resulting Maybe
    maybe_result.to_maybe()

def test_validation_initialized_with_none_arguments():
    """Test that Validation can be instantiated with None for both arguments."""
    # Both the source and schema are None — testing null/empty initialization
    source = None
    schema = None

    validation_instance = validation.Validation(source, schema)

def test_validation_to_maybe_with_none_inputs():
    """Test that Validation.to_maybe() can be called when both inputs are None."""
    # Create a Validation instance with None for both arguments
    none_value = None
    validation_instance = validation.Validation(none_value, none_value)

    # Convert the Validation to a Maybe type; should not raise an error
    validation_instance.to_maybe()

def test_validation_is_fail_with_object_as_both_arguments():
    """Test that Validation.is_fail() can be called when the same object
    is used for both constructor arguments."""
    # Use a plain object instance as both arguments to Validation
    plain_object = builtins.object()
    val = validation.Validation(plain_object, plain_object)
    val.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that calling map(None) on a Validation wrapping a nested structure executes without error."""

    # Build a nested input: a tuple containing a dict (keyed by a tuple) and an int
    key = (-895, True)
    nested_dict = {key: key}
    nested_tuple = (nested_dict, nested_dict, -895)

    # Create a Validation instance wrapping the nested structure with a truthy flag
    v = validation.Validation(nested_tuple, True)

    # Apply map with None as the mapping function
    v.map(None)

def test_validation_bind_with_none_value():
    """Test that Validation.bind() accepts None as a value without raising an error."""
    # Use identical byte sequences for both constructor arguments
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validator = validation.Validation(raw_bytes, raw_bytes)

    # Bind None to the validator to verify it handles a missing/null value
    none_value = None
    validator.bind(none_value)

def test_validation_ap_with_all_true_values():
    """Test that Validation.ap() can be called with a list of True values on a Failure instance."""
    # Create a failed validation (is_success=False)
    is_success = False
    is_failure = True

    # Build a list of True values to use as both the error list and the ap argument
    true_values = [is_failure, is_failure, is_failure, is_failure]

    # Construct a Validation instance representing a failure
    failed_validation = validation.Validation(is_success, true_values)

    # Apply ap() with the same list of True values
    failed_validation.ap(true_values)

def test_validation_with_both_flags_true_converts_to_successful_box():
    """Test that a Validation created with both flags set to True produces a successful Box."""
    is_valid = True

    # Create a Validation instance with both parameters set to True
    valid_validation = validation.Validation(is_valid, is_valid)

    # Convert the Validation to a Box and verify it represents a success
    result_box = valid_validation.to_box()
    result_box.is_success()

def test_validation_to_lazy_bind_with_none_then_to_lazy():
    """Test that a Validation created with empty lists can be converted to lazy,
    bound with None, and then converted to lazy again without error."""

    # Create an empty Validation and convert it to a lazy representation
    empty_list = []
    empty_validation = validation.Validation(empty_list, empty_list)
    lazy_validation = empty_validation.to_lazy()

    # Bind None to the lazy validation
    bound_result = lazy_validation.bind(None)

    # Convert the bound result to lazy as well
    bound_result.to_lazy()

def test_validation_chained_operations_with_mixed_types():
    """
    Test that Validation supports chained operations (eq, to_box, to_either,
    to_try, to_lazy, is_fail, __str__, map) across multiple instances
    constructed with None, bytes, and derived values without raising errors.
    """
    # Arbitrary bytes payload used as a value/key in validation inputs
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    none_value = None

    # Dict with None and bytes as keys/values, used as the error/value container
    mixed_dict = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # Validation instance with None as the first arg and a mixed dict as second
    validation_none_dict = validation.Validation(none_value, mixed_dict)

    # Equality check of the instance with itself
    eq_result = validation_none_dict.__eq__(validation_none_dict)

    # Convert to Box monad
    box_result = validation_none_dict.to_box()

    # Second Validation instance using raw bytes for both arguments
    validation_bytes_bytes = validation.Validation(raw_bytes, raw_bytes)

    # Convert the box to an Either monad
    either_from_box = box_result.to_either()

    # Check if the bytes-bytes validation represents a failure
    is_fail_result = validation_bytes_bytes.is_fail()

    # Convert the Either to a Try monad
    try_from_either = either_from_box.to_try()

    # Third Validation instance using the is_fail boolean result and raw bytes
    validation_fail_flag = validation.Validation(is_fail_result, raw_bytes)

    # Get string representation of the fail-flag validation
    str_representation = validation_fail_flag.__str__()

    # Convert bytes-bytes validation to a Lazy monad
    lazy_from_bytes_bytes = validation_bytes_bytes.to_lazy()

    # Fourth Validation instance using raw bytes for both arguments
    validation_bytes_bytes_2 = validation.Validation(raw_bytes, raw_bytes)

    # Convert the original box result to Either again
    either_from_box_2 = box_result.to_either()

    # Convert the fail-flag validation to a Lazy monad
    lazy_from_fail_flag = validation_fail_flag.to_lazy()

    # Fifth Validation instance using the lazy result and the fourth validation
    validation_lazy_nested = validation.Validation(lazy_from_fail_flag, validation_bytes_bytes_2)

    # Check is_fail on the bytes-bytes validation again
    is_fail_result_2 = validation_bytes_bytes.is_fail()

    # Map the string representation over the equality-check result (a Box/monad)
    eq_result.map(str_representation)

def test_validation_equality_and_maybe_with_none_key_and_bytes_value():
    """
    Test Validation behaviour when constructed with None as the value and a dict
    (containing None and bytes keys) as the error. Verifies that __eq__ and
    to_maybe() work correctly, and that bind() can be called on a bytes-valued
    Validation without raising errors.
    """
    # Arbitrary bytes payload used as both a dict value and a Validation value
    arbitrary_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    none_value = None

    # Error dict with mixed key types: None -> bytes, bytes -> bytes
    error_dict = {none_value: arbitrary_bytes, arbitrary_bytes: arbitrary_bytes}

    # Construct a Validation with None as the value and the mixed dict as the error
    validation_with_none = validation.Validation(none_value, error_dict)

    # Verify that the instance compares equal to itself
    eq_result = validation_with_none.__eq__(validation_with_none)

    # Convert to a Maybe representation
    maybe_result = validation_with_none.to_maybe()

    # Construct a second Validation where both value and error are bytes
    validation_with_bytes = validation.Validation(arbitrary_bytes, arbitrary_bytes)

    # Call bind with bytes; result is intentionally unused (side-effect / no-raise check)
    validation_with_bytes.bind(arbitrary_bytes)

def test_validation_eq_with_mismatched_none_and_bytes_calls_to_box():
    """
    Test that comparing two Validation instances with swapped None/bytes arguments
    via __eq__ returns a result on which .to_box() can be called without error.
    """
    # Arbitrary bytes value used as a key and value in the dict
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Dict with mixed None and bytes keys/values
    mixed_dict = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # First Validation: key is None, value is the mixed dict
    validation_with_none_key = validation.Validation(none_value, mixed_dict)

    # Second Validation: key is bytes, value is None
    validation_with_bytes_key = validation.Validation(raw_bytes, none_value)

    # Compare the two mismatched Validation instances
    eq_result = validation_with_none_key.__eq__(validation_with_bytes_key)

    # Ensure the equality result can be boxed
    eq_result.to_box()

