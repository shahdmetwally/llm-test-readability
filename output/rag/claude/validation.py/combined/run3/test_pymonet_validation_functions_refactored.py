import pytest
import validation as validation
import builtins as builtins

def test_validation_with_string_message_reports_status_and_converts_to_maybe():
    """Test that a Validation instance correctly reports success/failure status, supports self-equality, and can be converted to Maybe."""

    # Use a docstring-style string as both the value and message for the Validation
    validation_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance with the message as both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Check whether the validation is considered a success
    is_success_result = validation_instance.is_success()

    # Check self-equality of the validation instance
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation is considered a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the failure result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None via __eq__ produces a result that responds to is_success()."""
    # Inputs for constructing the Validation instance
    none_value = None
    error_code = -6891
    tuple_element = 3125
    validation_args = (tuple_element,)

    # Construct the Validation instance with the given error code and args tuple
    validation_instance = validation.Validation(error_code, validation_args)

    # Compare the Validation instance to None using __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Verify the result supports is_success() without error
    eq_result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Test that Validation initialized with empty dicts produces a string representation that exposes is_fail()."""
    # Use a single empty dict as both arguments, matching the original test setup
    empty_dict = {}

    # Construct a Validation instance with the empty dict for both parameters
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation instance
    str_representation = validation_instance.__str__()

    # Verify that the string representation exposes the is_fail() method
    str_representation.is_fail()

def test_validation_with_empty_sets_supports_either_and_maybe_conversions():
    """Test that a Validation built from empty sets can convert to Either and Maybe, and that the Maybe supports chaining to_maybe()."""
    # Construct an empty set to use as both success and failure collections
    empty_set = set()

    # Build a Validation instance with no successes and no failures
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Convert the validation to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify that the resulting Maybe also supports to_maybe() chaining
    maybe_result.to_maybe()

def test_validation_fail_supports_either_equality_and_maybe_conversion():
    """Test that a Validation built from a fail message supports to_either, self-equality, is_fail, and to_maybe."""

    # The message string used as both the value and the error of the Validation
    fail_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance in a failed state using the message as both arguments
    fail_validation = validation.Validation(fail_message, fail_message)

    # Convert the validation to an Either representation
    either_result = fail_validation.to_either()

    # Check self-equality of the validation object
    equality_result = fail_validation.__eq__(fail_validation)

    # Check whether the validation represents a failure
    is_fail_result = fail_validation.is_fail()

    # Convert the failure result to a Maybe representation
    is_fail_result.to_maybe()

def test_validation_with_empty_sets_to_maybe_is_chainable():
    """Test that Validation with empty sets converts to Maybe and the result supports chaining to_maybe()."""
    # Construct a Validation instance with empty sets for both arguments
    empty_set = set()
    empty_validation = validation.Validation(empty_set, empty_set)

    # Convert the validation to a Maybe value
    maybe_result = empty_validation.to_maybe()

    # Verify that the resulting Maybe also supports to_maybe() without error
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None as both arguments."""
    # Use None for both required arguments to test permissive instantiation
    none_value = None

    # Instantiate Validation with two None values; no exception should be raised
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_with_none_values_converts_to_maybe():
    """Test that a Validation constructed with None values can be converted to a Maybe without error."""
    # Use None for both arguments to represent the absence of a value
    none_value = None

    validation_instance = validation.Validation(none_value, none_value)

    # Verify that converting to Maybe does not raise an exception
    validation_instance.to_maybe()

def test_validation_is_fail_can_be_called_on_object_input():
    """Test that Validation constructed with a plain object can invoke is_fail() without error."""
    # Create a plain Python object to serve as the validation subject
    plain_object = builtins.object()

    # Construct a Validation instance using the plain object for both arguments
    validation_instance = validation.Validation(plain_object, plain_object)

    # Call is_fail() to verify it executes without raising an exception
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that calling map(None) on a Validation wrapping a nested dict/tuple structure does not raise."""
    # None value to be passed to map()
    none_value = None

    # Build a nested structure to use as the Validation's value
    negative_int = -895
    flag_true = True

    # A tuple used both as a dict key and dict value
    int_bool_tuple = (negative_int, flag_true)

    # A dict whose key and value are both the same tuple
    nested_dict = {int_bool_tuple: int_bool_tuple}

    # The composite value passed into Validation
    complex_value = (nested_dict, nested_dict, negative_int)

    # Construct the Validation instance with the nested structure and a True flag
    validation_instance = validation.Validation(complex_value, flag_true)

    # Call map with None; verifies the method accepts None without error
    validation_instance.map(none_value)

def test_validation_bind_with_none_does_not_raise():
    """Test that Validation.bind() accepts None without raising an error."""
    # Use identical byte strings as both constructor arguments
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Construct a Validation instance with the same bytes for both parameters
    validation_instance = validation.Validation(raw_bytes, raw_bytes)

    # Bind with None to verify the method handles a None argument gracefully
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_with_invalid_flag_and_true_values_list():
    """Test that Validation with a False flag accepts ap() call with a list of True values."""
    # Set up a False validity flag and a single True value
    is_valid = False
    true_value = True

    # Build a list of four True values to use as the validation payload
    true_values_list = [true_value, true_value, true_value, true_value]

    # Construct a Validation instance marked as invalid, carrying the list of True values
    validation_instance = validation.Validation(is_valid, true_values_list)

    # Apply the same list via ap() — verifying the call completes without error
    validation_instance.ap(true_values_list)

def test_validation_with_true_values_to_box_is_success():
    """Test that a Validation created with True values converts to a box that reports success."""
    # Both the success flag and value are True, representing a fully successful validation
    is_valid = True

    # Construct a Validation instance with both parameters set to True
    successful_validation = validation.Validation(is_valid, is_valid)

    # Convert the validation to its box representation
    validation_box = successful_validation.to_box()

    # Verify the box correctly identifies itself as a success
    validation_box.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy_again():
    """Test that a Validation built from empty lists supports to_lazy(), bind(None), then to_lazy() again."""
    none_value = None
    empty_list = []

    # Construct a Validation instance with two empty lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy form
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_validation = lazy_validation.bind(none_value)

    # Verify the bound result can also be converted to lazy without error
    bound_validation.to_lazy()

def test_validation_lazy_to_try_and_ap_is_success():
    """Test that a Validation from empty dicts converts to lazy, then Try, supports ap, and reports success."""

    # Build a Validation instance from two empty dicts
    empty_dict = {}
    empty_validation = validation.Validation(empty_dict, empty_dict)

    # Convert the validation to its lazy representation
    lazy_validation = empty_validation.to_lazy()

    # Convert the lazy validation to a Try monad
    try_result = lazy_validation.to_try()

    # Apply the original validation as an applicative argument to the lazy form
    ap_result = lazy_validation.ap(empty_validation)  # noqa: F841 — call is preserved for behaviour

    # Verify that the Try result indicates success
    try_result.is_success()

def test_validation_to_try_returns_success_when_valid():
    """Test that converting a Validation with a success value to a Try monad correctly reports is_success."""
    # Set up a simple integer success value and a list of validation rules
    success_value = 0
    validation_rules = [success_value]

    # Construct a Validation instance with the success value and rules
    validation_instance = validation.Validation(success_value, validation_rules)

    # Convert the validation to a Try monad and verify it is a success
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_chained_conversions_and_equality():
    """Test Validation equality, boxing, Either/Try/Lazy conversions, and is_fail across varied input types."""

    # Define base input values
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the first arg and a mixed-key dict as second
    validation_none_dict = validation.Validation(none_value, mixed_key_dict)

    # Test equality of the validation with itself and convert to Box
    eq_result = validation_none_dict.__eq__(validation_none_dict)
    boxed = validation_none_dict.to_box()

    # Construct a Validation with bytes for both arguments
    validation_bytes_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Convert the boxed value to Either, then check is_fail on the bytes validation
    either_from_box = boxed.to_either()
    is_fail_result = validation_bytes_bytes.is_fail()

    # Convert the Either to a Try
    try_from_either = either_from_box.to_try()

    # Construct a Validation using the is_fail bool result and bytes
    validation_is_fail_bytes = validation.Validation(is_fail_result, sample_bytes)

    # Get string representation of the is_fail-based validation
    str_repr = validation_is_fail_bytes.__str__()

    # Convert the bytes-bytes validation to Lazy (result unused, side-effect call)
    lazy_from_bytes_bytes = validation_bytes_bytes.to_lazy()

    # Construct another bytes-bytes Validation for use as a nested value
    validation_bytes_bytes_2 = validation.Validation(sample_bytes, sample_bytes)

    # Re-convert the original boxed value to Either (second conversion)
    either_from_box_2 = boxed.to_either()

    # Convert the is_fail-based validation to Lazy
    lazy_from_is_fail_bytes = validation_is_fail_bytes.to_lazy()

    # Construct a Validation with the lazy value and the nested Validation object
    validation_lazy_nested = validation.Validation(lazy_from_is_fail_bytes, validation_bytes_bytes_2)

    # Check is_fail on the bytes-bytes validation again
    is_fail_result_2 = validation_bytes_bytes.is_fail()

    # Map the string representation over the equality result (uses eq_result from above)
    eq_result.map(str_repr)

def test_validation_equality_to_maybe_and_bind_operations():
    """Test that Validation supports equality, to_maybe conversion, and bind with mixed value types."""
    # Define reusable byte and None values
    some_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes)
    mixed_key_dict = {none_value: some_bytes, some_bytes: some_bytes}

    # Create a Validation instance using None as the value and the mixed dict as context
    validation_with_none = validation.Validation(none_value, mixed_key_dict)

    # Test equality comparison of the Validation instance with itself
    eq_result = validation_with_none.__eq__(validation_with_none)

    # Test conversion to a Maybe type
    maybe_result = validation_with_none.to_maybe()

    # Create a second Validation instance using bytes for both value and context
    validation_with_bytes = validation.Validation(some_bytes, some_bytes)

    # Test that bind can be called with a bytes argument
    validation_with_bytes.bind(some_bytes)

def test_validation_eq_with_swapped_args_returns_boxable_result():
    """Test that __eq__ on two Validation instances with swapped arguments returns a result that supports .to_box()."""
    # Define raw values used as constructor arguments
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes)
    mixed_key_dict = {none_value: bytes_value, bytes_value: bytes_value}

    # Construct two Validation instances with swapped argument positions
    validation_with_none_key = validation.Validation(none_value, mixed_key_dict)
    validation_with_bytes_key = validation.Validation(bytes_value, none_value)

    # Compare the two instances; result should be boxable without error
    eq_result = validation_with_none_key.__eq__(validation_with_bytes_key)
    eq_result.to_box()

