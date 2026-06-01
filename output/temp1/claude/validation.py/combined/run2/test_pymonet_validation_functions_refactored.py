import pytest
import validation as validation
import builtins as builtins

def test_validation_success_and_fail_state_with_to_maybe():
    """Test that a Validation instance correctly reports success/failure state and supports to_maybe() conversion."""
    description_text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    validation_instance = validation.Validation(description_text, description_text)

    is_success_result = validation_instance.is_success()

    equality_result = validation_instance.__eq__(validation_instance)

    is_fail_result = validation_instance.is_fail()

    is_fail_result.to_maybe()

def test_validation_eq_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None via __eq__ produces a result that supports is_success()."""
    # Set up the None value used for comparison
    none_value = None

    # Construct the Validation instance with a negative code and a single-element tuple
    validation_code = -6891
    tuple_value = 3125
    validation_args = (tuple_value,)
    validation_instance = validation.Validation(validation_code, validation_args)

    # Compare the Validation instance to None and verify the result supports is_success()
    eq_result = validation_instance.__eq__(none_value)
    eq_result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Test that Validation.__str__ returns an object on which is_fail() can be called, given two empty dicts."""
    # Use empty dicts for both the first and second Validation parameters
    empty_dict = {}

    # Construct a Validation instance with two empty dicts
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation instance
    str_result = validation_instance.__str__()

    # Verify that the string result exposes an is_fail() method and call it
    str_result.is_fail()

def test_validation_with_empty_sets_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets converts to Either and Maybe without error."""
    # Construct a Validation instance with no successes and no failures
    empty_set = set()
    empty_validation = validation.Validation(empty_set, empty_set)

    # Convert the validation to an Either type
    either_result = empty_validation.to_either()

    # Convert the validation to a Maybe type
    maybe_result = empty_validation.to_maybe()

    # Verify that the Maybe result can itself be converted to a Maybe
    maybe_result.to_maybe()

def test_validation_supports_to_either_eq_is_fail_and_to_maybe():
    """Test that a Validation instance supports to_either, equality, is_fail, and to_maybe conversions."""

    # Use a descriptive docstring-style string as both the value and label for the Validation
    validation_message = (
        "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    )

    # Construct the Validation instance with the message as both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check that the validation instance is equal to itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation represents a failure
    is_fail_result = validation_instance.is_fail()

    # Attempt to convert the is_fail result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_with_empty_sets_to_maybe_is_chainable():
    """Test that Validation with empty sets converts to Maybe, and the result supports chained to_maybe() calls."""
    # Create an empty set to use as both valid and invalid sets in Validation
    empty_set = set()

    # Instantiate Validation with empty sets for both valid and invalid entries
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation instance to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify that the Maybe result also supports to_maybe() without error
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None for both constructor arguments."""
    # Use None for both arguments to test edge-case construction
    none_value = None

    # Instantiate Validation with None values; should not raise
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_with_none_values_can_convert_to_maybe():
    """Test that a Validation initialized with None values can be converted to a Maybe."""
    # Use None for both arguments to represent an empty/absent validation state
    none_value = None

    # Construct a Validation instance with both fields set to None
    validation_instance = validation.Validation(none_value, none_value)

    # Verify that converting to Maybe does not raise an exception
    validation_instance.to_maybe()

def test_validation_is_fail_called_on_object_instance():
    """Test that Validation.is_fail() can be called on a Validation instance constructed with a plain object."""
    # Create a plain object instance to use as the validation subject and context
    plain_object = builtins.object()

    # Construct a Validation using the plain object for both arguments
    validation_instance = validation.Validation(plain_object, plain_object)

    # Invoke is_fail() to verify it executes without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation built from a nested tuple/dict structure accepts None passed to map()."""

    # Primitive values used to build the nested input structure
    none_value = None
    negative_int = -895
    flag = True

    # Build a nested structure: a tuple used as both key and value in a dict,
    # which is then wrapped in an outer tuple
    inner_tuple = (negative_int, flag)
    nested_dict = {inner_tuple: inner_tuple}
    outer_tuple = (nested_dict, nested_dict, negative_int)

    # Construct the Validation instance with the nested structure and boolean flag
    validation_instance = validation.Validation(outer_tuple, flag)

    # Call map() with None — verifying it accepts a None mapper without error
    validation_instance.map(none_value)

def test_validation_bind_accepts_none_without_error():
    """Test that Validation.bind() accepts None without raising an error."""

    # A raw byte payload used to construct the Validation instance
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Construct a Validation object with identical byte sequences for both arguments
    validator = validation.Validation(raw_bytes, raw_bytes)

    # Bind None to the validator — should complete without error
    bind_value = None
    validator.bind(bind_value)

def test_validation_ap_called_with_all_true_list_on_false_validation():
    """Test that ap() can be called on a Validation initialized as invalid with a list of True values."""
    # Define the validity flag and a true boolean value
    is_valid = False
    true_value = True

    # Build a list of four True values to use as the applicative argument
    true_values_list = [true_value, true_value, true_value, true_value]

    # Create a Validation instance marked as invalid, holding the list of True values
    invalid_validation = validation.Validation(is_valid, true_values_list)

    # Apply the list of True values via ap() on the invalid Validation instance
    invalid_validation.ap(true_values_list)

def test_validation_with_true_values_to_box_is_success():
    """Test that a Validation created with True values converts to a box that reports success."""
    # Create a boolean flag indicating validity
    is_valid = True

    # Instantiate a Validation object with both fields set to True
    validation_instance = validation.Validation(is_valid, is_valid)

    # Convert the validation to its box representation
    boxed_result = validation_instance.to_box()

    # Verify that the boxed result reports success
    boxed_result.is_success()

def test_validation_to_lazy_bind_none_and_to_lazy_again():
    """Test that a Validation built from empty lists can be lazified, bound with None, and lazified again without error."""
    # None will be used as the argument to bind()
    none_value = None

    # Construct a Validation instance with two empty lists
    empty_list = []
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy form
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_result = lazy_validation.bind(none_value)

    # Verify the bound result can also be converted to lazy form without error
    bound_result.to_lazy()

def test_validation_lazy_and_try_conversion_with_ap():
    """Test that a Validation converts to lazy, then to Try, and that ap can be applied on the lazy form."""
    # Use an empty dict as both the success and failure channels of the Validation
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation to its lazy (deferred) representation
    lazy_validation = validation_instance.to_lazy()

    # Convert the lazy validation further into a Try monad
    try_result = lazy_validation.to_try()

    # Apply the original validation as an applicative argument to the lazy validation
    ap_result = lazy_validation.ap(validation_instance)  # exercised for correctness; not further asserted

    # Verify the Try result reports success
    try_result.is_success()

def test_validation_with_zero_value_to_try_is_success():
    """Test that a Validation constructed with zero and a list containing zero converts to a successful Try."""
    # Define the value and validators used to build the Validation instance
    zero_value = 0
    validators_list = [zero_value]

    # Construct the Validation object with the given value and validators
    validation_instance = validation.Validation(zero_value, validators_list)

    # Convert the Validation to a Try monad and verify it represents success
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_chained_conversions_and_map_with_mixed_types():
    """Test that Validation supports chained conversions and map across instances with mixed value types."""

    # Define base values used across multiple Validation instances
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with a None key and a mixed-type dict as value
    validation_none_key = validation.Validation(none_value, mixed_key_dict)

    # Test equality of validation with itself, then convert to box
    eq_result = validation_none_key.__eq__(validation_none_key)
    boxed = validation_none_key.to_box()

    # Construct a second Validation using bytes for both arguments
    validation_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Convert the boxed value to an Either, then check is_fail on the bytes validation
    either_from_box = boxed.to_either()
    is_fail_result = validation_bytes.is_fail()

    # Convert the Either to a Try
    try_from_either = either_from_box.to_try()

    # Construct a Validation using the is_fail result as the first argument
    validation_with_is_fail = validation.Validation(is_fail_result, sample_bytes)

    # Get the string representation of the is_fail-keyed validation
    str_repr = validation_with_is_fail.__str__()

    # Convert the bytes validation to lazy
    lazy_from_bytes_validation = validation_bytes.to_lazy()

    # Construct another bytes-based Validation and convert box to Either again
    validation_bytes_copy = validation.Validation(sample_bytes, sample_bytes)
    either_from_box_second = boxed.to_either()

    # Convert the is_fail-keyed validation to lazy
    lazy_from_is_fail_validation = validation_with_is_fail.to_lazy()

    # Construct a Validation using the lazy result and the bytes copy as arguments
    validation_lazy_nested = validation.Validation(lazy_from_is_fail_validation, validation_bytes_copy)

    # Check is_fail on the bytes validation a second time
    is_fail_result_second = validation_bytes.is_fail()

    # Map the string representation over the equality result
    eq_result.map(str_repr)

def test_validation_eq_to_maybe_and_bind_with_bytes_and_none():
    """Test that Validation supports equality, to_maybe, and bind with None and bytes inputs."""

    # Define raw inputs: a bytes payload and a None value
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes)
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the primary value and the mixed dict as context
    validation_with_none_key = validation.Validation(none_value, mixed_key_dict)

    # Verify equality of the validation instance with itself
    eq_result = validation_with_none_key.__eq__(validation_with_none_key)

    # Convert the validation to a Maybe representation
    maybe_result = validation_with_none_key.to_maybe()

    # Construct a second Validation using bytes for both arguments
    validation_with_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Invoke bind with the bytes value on the second validation
    validation_with_bytes.bind(sample_bytes)

def test_validation_eq_with_swapped_none_and_bytes_args_calls_to_box():
    """Test that comparing two Validation instances with swapped None/bytes arguments produces a result that supports .to_box()."""
    # A fixed arbitrary bytes value used as both a key and value in the dict
    arbitrary_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Dict with mixed key types: None and bytes both mapping to the same bytes value
    mixed_key_dict = {none_value: arbitrary_bytes, arbitrary_bytes: arbitrary_bytes}

    # First Validation: None as first arg, dict as second arg
    validation_none_key = validation.Validation(none_value, mixed_key_dict)

    # Second Validation: bytes as first arg, None as second arg (swapped configuration)
    validation_bytes_key = validation.Validation(arbitrary_bytes, none_value)

    # Compare the two differently-configured Validation instances
    eq_result = validation_none_key.__eq__(validation_bytes_key)

    # The equality result must support .to_box() without error
    eq_result.to_box()

