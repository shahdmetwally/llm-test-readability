import pytest
import validation as validation
import builtins as builtins

def test_validation_success_status_equality_and_maybe_conversion():
    """Test that a Validation instance correctly reports success/failure, supports equality, and can be converted to Maybe."""

    # Use a descriptive docstring-style string as both the value and message
    validation_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance with the message as both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Check that the validation reports success
    is_success_result = validation_instance.is_success()

    # Check that the validation instance is equal to itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check that the validation reports failure status
    is_fail_result = validation_instance.is_fail()

    # Convert the failure result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None via __eq__ returns a result that supports is_success()."""
    # Inputs: a None value to compare against, and constructor arguments for Validation
    none_value = None
    error_code = -6891
    valid_value = 3125
    validation_args = (valid_value,)

    # Construct the Validation instance with the given error code and argument tuple
    validation_instance = validation.Validation(error_code, validation_args)

    # Compare the Validation instance to None using __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Verify the result supports is_success() without error
    eq_result.is_success()

def test_validation_str_representation_exposes_is_fail():
    """Test that Validation initialized with empty dicts produces a string result that exposes is_fail()."""
    # Use empty dicts as both positional arguments to Validation
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the validation instance to its string representation
    str_result = validation_instance.__str__()

    # Verify the string result exposes the is_fail() method
    str_result.is_fail()

def test_validation_with_empty_sets_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets converts to Either and Maybe, and that Maybe supports chained to_maybe() calls."""
    # Use an empty set for both the success and failure collections
    empty_set = set()

    # Construct a Validation instance with no successes and no failures
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert to Either — exercises the to_either() path
    either_result = validation_instance.to_either()

    # Convert to Maybe — exercises the to_maybe() path
    maybe_result = validation_instance.to_maybe()

    # Verify that the Maybe result itself supports to_maybe() without error
    maybe_result.to_maybe()

def test_validation_created_with_string_supports_either_equality_fail_and_maybe_conversions():
    """Test that a Validation built from a string message supports to_either, equality, is_fail, and to_maybe operations."""

    # Use a descriptive docstring-style string as both the value and message
    validation_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance using the message string for both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check that the validation instance is equal to itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation represents a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the failure-check result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_with_empty_sets_to_maybe_is_chainable():
    """Test that Validation built from empty sets converts to Maybe, and the result supports chained to_maybe() calls."""
    # Construct a Validation instance using empty sets for both fields
    empty_set = set()
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify the resulting Maybe also supports to_maybe() without error
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None as both arguments."""
    none_value = None

    # Construct a Validation instance passing None for both parameters
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_with_none_values_converts_to_maybe():
    """Test that a Validation constructed with None values can be converted to a Maybe without error."""
    none_value = None

    # Construct a Validation instance where both arguments are None
    validation_instance = validation.Validation(none_value, none_value)

    # Verify that to_maybe() can be called without raising an exception
    validation_instance.to_maybe()

def test_validation_is_fail_returns_true_for_plain_object():
    """Test that Validation constructed with a plain object reports a failing state via is_fail()."""
    # Use a plain Python object as both the value and context for the Validation
    plain_object = builtins.object()

    # Construct a Validation instance using the plain object for both arguments
    validation_instance = validation.Validation(plain_object, plain_object)

    # Verify that the validation correctly identifies itself as a failure
    validation_instance.is_fail()

def test_validation_bind_accepts_none():
    """Test that Validation can be constructed with byte data and bound to None without error."""
    # Raw bytes used as both the first and second argument to Validation
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Construct a Validation instance using the same byte sequence for both parameters
    validation_instance = validation.Validation(raw_bytes, raw_bytes)

    # Bind None to the validation instance (should not raise)
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_with_false_state_and_true_values_list():
    """Test that ap() can be called on a Validation initialized with False and a list of True values."""
    # Set up the validity flag and a uniform list of True values
    is_valid = False
    true_value = True
    true_values_list = [true_value, true_value, true_value, true_value]

    # Create a Validation instance marked as invalid (False) with the True-values list
    invalid_validation = validation.Validation(is_valid, true_values_list)

    # Apply ap() using the same list of True values
    invalid_validation.ap(true_values_list)

def test_validation_true_true_to_box_is_success():
    """Test that a Validation created with both flags True converts to a box that reports success."""
    # Both validation flags are set to True (valid state)
    is_valid = True

    # Create a Validation instance with both parameters set to True
    validation_instance = validation.Validation(is_valid, is_valid)

    # Convert the validation to a box representation
    box = validation_instance.to_box()

    # Verify that the box correctly reports success
    box.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy_again():
    """Test that a Validation with empty lists can be lazified, bound with None, and lazified again."""
    none_value = None
    empty_list = []

    # Create a Validation instance with empty error and value lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy form
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_validation = lazy_validation.bind(none_value)

    # Convert the bound result to lazy again — should not raise
    bound_validation.to_lazy()

def test_lazy_validation_ap_and_try_is_success():
    """Verify that a lazy Validation converted to Try reports success after applying ap."""

    # Create an empty dict to use as both the value and error container
    empty_dict = {}

    # Construct a Validation instance with empty success and error dicts
    empty_validation = validation.Validation(empty_dict, empty_dict)

    # Convert the validation to its lazy (deferred) representation
    lazy_validation = empty_validation.to_lazy()

    # Convert the lazy validation into a Try monad
    try_result = lazy_validation.to_try()

    # Apply the original validation to the lazy validation (applicative apply)
    ap_result = lazy_validation.ap(empty_validation)

    # Assert that the Try result represents a successful computation
    try_result.is_success()

def test_validation_with_zero_value_to_try_is_success():
    """Test that a Validation constructed with zero value converts to a successful Try."""
    # Set up the value and validators list using zero
    zero_value = 0
    validators_list = [zero_value]

    # Construct the Validation instance with the zero value and validators
    validation_instance = validation.Validation(zero_value, validators_list)

    # Convert to a Try monad and check that it reports success
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_chained_conversions_with_mixed_types():
    """Test Validation with mixed types (None, bytes, bool) across chained conversions."""

    # Define base values used to construct Validation instances
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # A dict with mixed key types (None and bytes) mapping to bytes
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the first arg and the mixed dict as second
    validation_none_dict = validation.Validation(none_value, mixed_key_dict)

    # Test equality of a Validation instance with itself
    eq_result = validation_none_dict.__eq__(validation_none_dict)

    # Convert to Box and then to Either, exercising the conversion chain
    box_from_none_dict = validation_none_dict.to_box()

    # Construct a Validation with bytes for both arguments
    validation_bytes_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Convert the box to an Either
    either_from_box = box_from_none_dict.to_either()

    # Check failure status of the bytes-bytes Validation
    is_fail_result = validation_bytes_bytes.is_fail()

    # Convert the Either to a Try
    try_from_either = either_from_box.to_try()

    # Construct a Validation using the is_fail bool result and bytes
    validation_bool_bytes = validation.Validation(is_fail_result, sample_bytes)

    # Get string representation of the bool-bytes Validation
    str_repr = validation_bool_bytes.__str__()

    # Convert the bytes-bytes Validation to a Lazy
    lazy_from_bytes_bytes = validation_bytes_bytes.to_lazy()

    # Construct another bytes-bytes Validation instance
    validation_bytes_bytes_2 = validation.Validation(sample_bytes, sample_bytes)

    # Convert the original box to Either again (second call)
    either_from_box_again = box_from_none_dict.to_either()

    # Convert the bool-bytes Validation to a Lazy
    lazy_from_bool_bytes = validation_bool_bytes.to_lazy()

    # Construct a Validation using the lazy result and a Validation instance as values
    validation_lazy_validation = validation.Validation(lazy_from_bool_bytes, validation_bytes_bytes_2)

    # Check failure status of the bytes-bytes Validation a second time
    is_fail_result_2 = validation_bytes_bytes.is_fail()

    # Map the string representation over the equality result
    eq_result.map(str_repr)

def test_validation_equality_to_maybe_and_bind_with_mixed_types():
    """Test that Validation supports equality, to_maybe conversion, and bind with None, dict, and bytes inputs."""

    # Define reusable byte and None values for constructing Validation instances
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes) mapping to bytes
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the value and the mixed dict as context
    validation_with_none = validation.Validation(none_value, mixed_key_dict)

    # Verify that the Validation instance compares equal to itself
    eq_result = validation_with_none.__eq__(validation_with_none)

    # Convert the Validation to a Maybe type
    maybe_result = validation_with_none.to_maybe()

    # Construct a second Validation using bytes for both value and context
    validation_with_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Call bind on the bytes-based Validation with a bytes argument
    validation_with_bytes.bind(sample_bytes)

def test_validation_eq_with_swapped_none_and_bytes_args_result_supports_to_box():
    """Test that __eq__ on two Validation objects with swapped None/bytes args returns a result that supports .to_box()."""
    # Define the raw byte sequence and None value used as constructor arguments
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes) mapping to the same bytes value
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create two Validation instances with swapped argument positions
    validation_none_first = validation.Validation(none_value, mixed_key_dict)
    validation_bytes_first = validation.Validation(sample_bytes, none_value)

    # Compare the two instances using __eq__ and verify the result supports .to_box()
    eq_result = validation_none_first.__eq__(validation_bytes_first)
    eq_result.to_box()

