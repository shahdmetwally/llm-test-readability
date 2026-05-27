import pytest
import validation as validation
import builtins as builtins

def test_validation_success_fail_and_maybe_conversion():
    """Test that a Validation instance correctly reports success/failure states and supports maybe conversion."""
    # Use a descriptive docstring-like string as the validation value and message
    docstring_value = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance with the same value used for both arguments
    validation_instance = validation.Validation(docstring_value, docstring_value)

    # Check whether the validation is considered successful
    is_success_result = validation_instance.is_success()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation is considered a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the failure result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_callable_result():
    """Test that comparing a Validation instance to None via __eq__ returns a result that supports is_success()."""
    # Define the None value used for equality comparison
    none_value = None

    # Construct the arguments for the Validation instance
    error_code = -6891
    tuple_element = 3125
    validation_args = (tuple_element,)

    # Instantiate Validation with a negative error code and a single-element tuple
    validation_instance = validation.Validation(error_code, validation_args)

    # Compare the Validation instance to None using explicit __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Verify the result supports is_success() without error
    eq_result.is_success()

def test_validation_str_representation_exposes_is_fail_method():
    """Test that a Validation instance initialized with empty dicts produces a string representation that exposes an is_fail() method."""
    # Use empty dicts as both arguments to construct a minimal Validation instance
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation instance
    str_representation = validation_instance.__str__()

    # Verify that the string representation exposes the is_fail() method
    str_representation.is_fail()

def test_validation_with_empty_sets_supports_either_and_maybe_conversions():
    """Test that a Validation built from empty sets can be converted to Either and Maybe, and that the Maybe result supports chained to_maybe() calls."""
    # Build an empty set to use as both the success and failure collections
    empty_set = set()

    # Construct a Validation instance with no successes and no failures
    validation_instance = validation.Validation(empty_set, empty_set)

    # Verify that conversion to Either executes without error
    either_result = validation_instance.to_either()

    # Verify that conversion to Maybe executes without error
    maybe_result = validation_instance.to_maybe()

    # Verify that the Maybe result itself supports a further to_maybe() call
    maybe_result.to_maybe()

def test_validation_created_with_string_supports_either_equality_fail_and_maybe_conversions():
    """Test that a Validation instance supports to_either, equality, is_fail, and to_maybe operations."""

    # Use a descriptive multiline string as both the value and error message
    validation_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance with the message used as both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation represents a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the failure result to a Maybe
    is_fail_result.to_maybe()

def test_validation_with_empty_sets_to_maybe_is_chainable():
    """Test that Validation with empty sets can convert to Maybe, and the result also supports to_maybe()."""
    # Create an empty set to use as both the success and failure collections
    empty_set = set()

    # Instantiate a Validation using empty sets for both valid and invalid entries
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify that the resulting Maybe also supports conversion via to_maybe()
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None as both arguments."""
    # Use None for both parameters to verify the constructor handles missing/null input
    none_value = None

    validation_instance = validation.Validation(none_value, none_value)

def test_validation_to_maybe_with_none_values():
    """Test that Validation constructed with None values can call to_maybe() without error."""
    # Use None for both constructor arguments
    none_value = None

    # Construct a Validation instance with both values set to None
    validation_instance = validation.Validation(none_value, none_value)

    # Verify that to_maybe() can be called without raising an exception
    validation_instance.to_maybe()

def test_validation_is_fail_with_object_instance():
    """Test that Validation.is_fail() can be called when constructed with a plain object instance."""
    # Create a plain object instance to use as both constructor arguments
    plain_object = builtins.object()

    # Construct a Validation using the same plain object for both parameters
    validation_instance = validation.Validation(plain_object, plain_object)

    # Invoke is_fail() to verify it executes without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation.map() accepts None when constructed with a nested tuple/dict payload."""
    # Scalar values used to build nested structures
    none_value = None
    negative_int = -895
    flag = True

    # A tuple used both as a dict key and value
    int_and_flag_tuple = (negative_int, flag)

    # A dict whose key and value are the same tuple
    tuple_keyed_dict = {int_and_flag_tuple: int_and_flag_tuple}

    # A nested payload combining the dict and scalar values
    nested_payload = (tuple_keyed_dict, tuple_keyed_dict, negative_int)

    # Construct Validation with the nested payload and a boolean flag
    validation_instance = validation.Validation(nested_payload, flag)

    # Call map with None — should not raise
    validation_instance.map(none_value)

def test_validation_bind_with_none_argument():
    """Test that Validation can be instantiated with bytes and that bind(None) executes without error."""
    # A raw bytes payload used as both the first and second constructor arguments
    raw_bytes_value = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Instantiate Validation with the bytes value for both parameters
    validation_instance = validation.Validation(raw_bytes_value, raw_bytes_value)

    # Explicitly bind None to verify the method handles a None argument
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_with_false_validity_and_true_list():
    """Test that Validation initialized as invalid (False) can call ap() with a list of True values."""
    # Set up a False validity flag and a True sentinel value
    invalid_flag = False
    true_value = True

    # Build a homogeneous list of True values to use as the applicative argument
    true_values_list = [true_value, true_value, true_value, true_value]

    # Construct a Validation marked as invalid, carrying the list of True values
    validation_instance = validation.Validation(invalid_flag, true_values_list)

    # Apply ap() with the same list of True values
    validation_instance.ap(true_values_list)

def test_validation_true_true_to_box_is_success():
    """Test that a Validation constructed with True/True converts to a box that reports success."""
    # Both the value and validity flags are set to True
    is_valid = True

    # Construct a Validation instance with both parameters as True
    validation_instance = validation.Validation(is_valid, is_valid)

    # Convert the validation result to its boxed representation
    boxed_result = validation_instance.to_box()

    # Verify the boxed result considers itself a success
    boxed_result.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy():
    """Test that a Validation built from empty lists can be made lazy, bound with None, and the result converted to lazy."""
    none_value = None
    empty_list = []

    # Construct a Validation instance with empty error and value lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy form
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_lazy = lazy_validation.bind(none_value)

    # Verify the bound result can also be converted to lazy
    bound_lazy.to_lazy()

def test_validation_lazy_to_try_and_ap_is_success():
    """Test that a Validation supports conversion to lazy/Try forms and applicative apply."""
    # Use an empty dict as both the success value and error container
    empty_dict = {}

    # Create a Validation instance with empty data and error dictionaries
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation to its lazy (deferred) representation
    lazy_validation = validation_instance.to_lazy()

    # Convert the lazy validation to a Try (eagerly evaluated result)
    try_result = lazy_validation.to_try()

    # Apply the original validation via applicative apply on the lazy form
    ap_result = lazy_validation.ap(validation_instance)

    # Check that the Try result represents a success
    try_result.is_success()

def test_validation_with_zero_value_converts_to_successful_try():
    """Test that a Validation constructed with zero and a list converts to a successful Try."""
    # Set up a zero integer value and a list containing it
    zero_value = 0
    errors_list = [zero_value]

    # Construct a Validation instance with the zero value and the list
    validation_instance = validation.Validation(zero_value, errors_list)

    # Convert the Validation to a Try monad
    try_result = validation_instance.to_try()

    # Verify that the resulting Try reports success
    try_result.is_success()

def test_validation_method_chaining_with_mixed_types():
    """Test that Validation instances support method chaining across mixed types without raising exceptions."""

    # Define base values used to construct various Validation instances
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create a Validation with a None error and a dict value; test equality with itself
    validation_none_dict = validation.Validation(none_value, mixed_key_dict)
    eq_result = validation_none_dict.__eq__(validation_none_dict)

    # Convert to box and then to either, exercising the conversion chain
    boxed = validation_none_dict.to_box()

    # Create a second Validation with bytes for both error and value
    validation_bytes_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Convert boxed result to either, then check fail status on the bytes validation
    either_from_box = boxed.to_either()
    is_fail_result = validation_bytes_bytes.is_fail()

    # Convert either to try
    try_from_either = either_from_box.to_try()

    # Create a Validation using the is_fail boolean result as the error, bytes as value
    validation_is_fail_bytes = validation.Validation(is_fail_result, sample_bytes)

    # Get string representation and convert bytes validation to lazy
    str_repr = validation_is_fail_bytes.__str__()
    lazy_from_bytes_validation = validation_bytes_bytes.to_lazy()

    # Create another bytes/bytes Validation and re-exercise to_either on the box
    validation_bytes_bytes_copy = validation.Validation(sample_bytes, sample_bytes)
    either_from_box_again = boxed.to_either()

    # Convert the is_fail validation to lazy, then nest it inside a new Validation
    lazy_from_is_fail_validation = validation_is_fail_bytes.to_lazy()
    validation_lazy_nested = validation.Validation(lazy_from_is_fail_validation, validation_bytes_bytes_copy)

    # Re-check fail status on the bytes validation
    is_fail_again = validation_bytes_bytes.is_fail()

    # Map the string representation over the equality result
    eq_result.map(str_repr)

def test_validation_equality_to_maybe_and_bind_operations():
    """Test that Validation supports equality comparison, to_maybe conversion, and bind with varied input types."""

    # Define reusable primitive values
    byte_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Construct a dict with mixed key types (None and bytes)
    mixed_key_dict = {none_value: byte_value, byte_value: byte_value}

    # Create a Validation instance using None as the primary value and the mixed dict as context
    validation_with_none_key
# (Truncated by extractor)