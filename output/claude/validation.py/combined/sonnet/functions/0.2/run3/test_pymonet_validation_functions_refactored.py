import pytest
import validation as validation
import builtins as builtins

def test_validation_success_fail_and_maybe_conversion():
    """Test that a Validation instance correctly reports success/failure status, supports equality comparison, and allows conversion of the failure result to a Maybe."""

    # Use a descriptive multi-line string as the input value for both constructor arguments
    description_text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance with the same string used for both arguments
    validation_instance = validation.Validation(description_text, description_text)

    # Check whether the validation is considered successful
    is_success_result = validation_instance.is_success()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation is considered a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the failure result to a Maybe value
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_success_checkable_result():
    """Test that comparing a Validation instance to None via __eq__ returns a result that supports is_success()."""
    # Prepare the value to compare against
    none_value = None

    # Construct the Validation instance with a negative error code and a single-element tuple
    error_code = -6891
    tuple_element = 3125
    validation_args = (tuple_element,)
    validation_instance = validation.Validation(error_code, validation_args)

    # Compare the Validation instance to None using __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Verify the result supports the is_success() interface
    eq_result.is_success()

def test_validation_str_representation_exposes_is_fail():
    """Test that Validation initialized with empty dicts produces a string result that exposes is_fail()."""
    # Use an empty dict as both the data and schema inputs
    empty_dict = {}

    # Construct a Validation instance with empty inputs
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation instance
    str_result = validation_instance.__str__()

    # Verify the string result exposes the is_fail() method
    str_result.is_fail()

def test_validation_with_empty_sets_supports_to_either_to_maybe_and_chained_to_maybe():
    """Test that a Validation built from empty sets can be converted to Either and Maybe, and that the Maybe result supports to_maybe()."""
    # Construct a Validation instance using two empty sets (no errors, no successes)
    empty_set = set()
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation to an Either type
    either_result = validation_instance.to_either()

    # Convert the Validation to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify that the Maybe result itself supports to_maybe()
    maybe_result.to_maybe()

def test_validation_with_string_message_supports_either_equality_and_maybe_conversion():
    """Test that a Validation built from a string message supports to_either, equality, is_fail, and to_maybe conversions."""

    # Use a descriptive docstring-style string as both the value and message
    validation_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance using the message as both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation represents a failure state
    is_fail_result = validation_instance.is_fail()

    # Convert the failure-state result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_with_empty_sets_to_maybe_is_chainable():
    """Test that Validation built from empty sets converts to Maybe, and the result supports chained to_maybe() calls."""
    # Construct a Validation instance using empty sets for both fields
    empty_set = set()
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe and verify chained to_maybe() is callable without error
    maybe_result = validation_instance.to_maybe()
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None as both arguments."""
    # Use None for both the value and the schema/config argument
    none_value = None

    # Instantiate Validation with two None arguments to verify it does not raise
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_with_none_values_can_convert_to_maybe():
    """Test that Validation constructed with None values can call to_maybe() without error."""
    # Use None as both constructor arguments to represent the absence of values
    none_value = None

    # Construct a Validation instance with None for both parameters
    validation_instance = validation.Validation(none_value, none_value)

    # Verify that to_maybe() can be called without raising an exception
    validation_instance.to_maybe()

def test_validation_is_fail_callable_with_generic_object():
    """Test that Validation.is_fail() can be called on a Validation constructed with a generic object."""
    # Create a plain generic object to serve as both constructor arguments
    generic_object = builtins.object()

    # Construct a Validation instance using the generic object for both parameters
    validation_instance = validation.Validation(generic_object, generic_object)

    # Invoke is_fail() to verify it executes without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation.map() accepts None when constructed with a deeply nested tuple/dict structure."""
    # The None value that will be passed to .map()
    none_value = None

    # Build a nested structure: int and bool form a tuple used as both key and value in a dict
    base_int = -895
    is_valid_flag = True

    inner_tuple = (base_int, is_valid_flag)          # used as dict key and value
    nested_dict = {inner_tuple: inner_tuple}          # dict keyed by the inner tuple
    outer_tuple = (nested_dict, nested_dict, base_int)  # outer container passed to Validation

    # Construct the Validation instance with the nested structure and the boolean flag
    validation_instance = validation.Validation(outer_tuple, is_valid_flag)

    # Call map() with None — verifies the method handles None without error
    validation_instance.map(none_value)

def test_validation_bind_accepts_none_argument():
    """Test that Validation.bind() can be called with None without raising an error."""
    # Use a raw bytes value as both constructor arguments
    raw_bytes_payload = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Instantiate Validation with the bytes payload for both parameters
    validation_instance = validation.Validation(raw_bytes_payload, raw_bytes_payload)

    # Bind with None to verify the method accepts a None argument
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_with_invalid_state_and_true_values_list():
    """Test that ap() can be called on an invalid Validation instance initialized with a list of True values."""
    # Define the validity flag and a reusable True boolean
    is_valid = False
    true_value = True

    # Build a list of four True values to use as the validation data
    true_values_list = [true_value, true_value, true_value, true_value]

    # Create a Validation instance in an invalid state with the True values list
    invalid_validation = validation.Validation(is_valid, true_values_list)

    # Apply ap() using the same list of True values
    invalid_validation.ap(true_values_list)

def test_validation_true_true_to_box_is_success():
    """Test that a Validation constructed with True values converts to a box that reports success."""
    # Both the validity flag and the value flag are set to True
    is_valid = True

    # Construct a Validation instance with both parameters set to True
    validation_instance = validation.Validation(is_valid, is_valid)

    # Convert the validation to a box representation
    box = validation_instance.to_box()

    # Verify that the box correctly reports a successful state
    box.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy():
    """Test that a Validation built from empty lists can be lazified, bound with None, and the result lazified again."""
    none_value = None
    empty_list = []

    # Create a Validation instance with two empty lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy representation
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_result = lazy_validation.bind(none_value)

    # Verify the bound result can also be converted to lazy form
    bound_result.to_lazy()

def test_lazy_validation_ap_and_try_is_success():
    """Test that a lazy Validation supports ap() and converts to a successful Try."""

    # Use empty dicts as both the value and error container for the Validation
    empty_dict = {}
    empty_validation = validation.Validation(empty_dict, empty_dict)

    # Convert the validation to its lazy form
    lazy_validation = empty_validation.to_lazy()

    # Convert the lazy validation to a Try monad
    try_result = lazy_validation.to_try()

    # Apply the original validation using the applicative ap() method
    ap_result = lazy_validation.ap(empty_validation)

    # Verify that the Try result reports success
    try_result.is_success()

def test_validation_zero_value_converts_to_try_reports_success():
    """Test that a Validation with a zero value and single-element list converts to a Try and reports success status."""
    # Set up a zero integer value and a list containing it as the validators
    zero_value = 0
    validators_list = [zero_value]

    # Construct a Validation instance with the zero value and validators list
    validation_instance = validation.Validation(zero_value, validators_list)

    # Convert the Validation to a Try monad
    try_result = validation_instance.to_try()

    # Check whether the Try result reports success
    try_result.is_success()

def test_validation_method_chaining_with_mixed_types():
    """Test that Validation supports method chaining across mixed types (None, bytes, bool) without errors."""

    # Define base values used to construct Validation instances
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # A dict with mixed key types (None and bytes) mapping to bytes
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the first arg and the mixed dict as second
    validation_none_dict = validation.Validation(none_value, mixed_key_dict)

    # Test equality comparison of a Validation with itself
    eq_result = validation_none_dict.__eq__(validation_none_dict)

    # Convert to Box and retain for further chaining
    box_from_none_dict = validation_none_dict.to_box()

    # Construct a Validation with bytes for both arguments
    validation_bytes_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Convert the box to an Either
    either_from_box = box_from_none_dict.to_either()

    # Check whether the bytes-bytes Validation is a failure
    is_fail_bytes = validation_bytes_bytes.is_fail()

    # Convert the Either to a Try
    try_from_either = either_from_box.to_try()

    # Construct a Validation using the is_fail bool result and bytes
    validation_isfail_bytes = validation.Validation(is_fail_bytes, sample_bytes)

    # Get the string representation of the is_fail Validation
    str_of_isfail_validation = validation_isfail_bytes.__str__()

    # Convert bytes-bytes Validation to lazy (result not used further — exercises the method)
    lazy_from_bytes_bytes = validation_bytes_bytes.to_lazy()

    # Construct another bytes-bytes Validation
    validation_bytes_bytes_2 = validation.Validation(sample_bytes, sample_bytes)

    # Convert the box to Either again (result not used further — exercises the method)
    either_from_box_again = box_from_none_dict.to_either()

    # Convert the is_fail Validation to lazy for use as a nested value
    lazy_from_isfail_validation = validation_isfail_bytes.to_lazy()

    # Construct a Validation using the lazy result and a nested Validation instance
    validation_lazy_nested = validation.Validation(lazy_from_isfail_validation, validation_bytes_bytes_2)

    # Check is_fail on the bytes-bytes Validation again (result not used further — exercises the method)
    is_fail_bytes_2 = validation_bytes_bytes.is_fail()

    # Map the string representation over the eq_result
    eq_result.map(str_of_isfail_validation)

def test_validation_equality_to_maybe_and_bind_with_bytes_and_none_values():
    """Test that Validation supports equality, to_maybe conversion, and bind with None and bytes inputs."""

    # Define raw byte and None values used as Validation inputs
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes) mapping to bytes
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the primary value and the mixed dict as context
    validation_with_none_key = validation.Validation(none_value, mixed_key_dict)

    # Test equality of the Validation instance with itself
    eq_result = validation_with_none_key.__eq__(validation_with_none_key)

    # Convert the Validation to a Maybe representation
    maybe_result = validation_with_none_key.to_maybe()

    # Construct a second Validation using bytes for both arguments
    validation_with_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Call bind on the bytes-based Validation with the bytes value
    validation_with_bytes.bind(sample_bytes)

def test_validation_eq_with_swapped_args_returns_boxable_result():
    """Test that __eq__ on two Validation objects with swapped args produces a result that supports .to_box()."""
    # Define reusable raw byte value and a None placeholder
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes) mapping to the same bytes value
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create two Validation instances with swapped positional arguments
    validation_with_none_key = validation.Validation(none_value, mixed_key_dict)
    validation_with_bytes_key = validation.Validation(sample_bytes, none_value)

    # Compare the two instances using __eq__ and verify the result supports .to_box()
    eq_result = validation_with_none_key.__eq__(validation_with_bytes_key)
    eq_result.to_box()

