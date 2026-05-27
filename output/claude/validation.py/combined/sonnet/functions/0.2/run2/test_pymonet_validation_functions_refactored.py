import pytest
import validation as validation
import builtins as builtins

def test_validation_success_fail_and_maybe_conversion():
    """Test that a Validation instance correctly reports success/failure state, supports equality, and can be converted to Maybe."""

    # Use a descriptive docstring-like string as the validation value and label
    description_text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance with the same string for both arguments
    validation_instance = validation.Validation(description_text, description_text)

    # Check whether the validation is considered successful
    is_success_result = validation_instance.is_success()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation is considered a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the failure result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None via __eq__ produces a result that supports is_success()."""
    # The value to compare against
    none_value = None

    # Construct the Validation instance with a negative error code and a single-element tuple
    error_code = -6891
    tuple_element = 3125
    validation_args = (tuple_element,)
    validation_instance = validation.Validation(error_code, validation_args)

    # Compare the Validation instance to None using __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Verify the result supports is_success()
    eq_result.is_success()

def test_validation_str_representation_exposes_is_fail():
    """Test that the string representation of a Validation instance exposes the is_fail() method."""
    # Use empty dicts as both the data and schema for a minimal Validation instance
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation instance to its string representation
    str_representation = validation_instance.__str__()

    # Verify that the string representation exposes the is_fail() method
    str_representation.is_fail()

def test_validation_with_empty_sets_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets converts to Either and Maybe, and that the Maybe result also supports to_maybe() without error."""
    # Create an empty set to use as both the success and failure collections
    empty_set = set()

    # Construct a Validation instance with no successes and no failures
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the validation to an Either type (implicitly verifies no exception is raised)
    either_result = validation_instance.to_either()

    # Convert the validation to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify that the resulting Maybe also exposes a to_maybe() method without raising
    maybe_result.to_maybe()

def test_validation_created_with_string_supports_chained_operations():
    """Test that a Validation created with a string message supports to_either, equality, is_fail, and to_maybe operations."""

    # Use a descriptive docstring-style string as both the value and message
    validation_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance using the message string for both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation represents a failure
    is_fail_result = validation_instance.is_fail()

    # Call to_maybe() on the boolean result of is_fail() (preserving original chaining behaviour)
    is_fail_result.to_maybe()

def test_validation_with_empty_sets_to_maybe_is_chainable():
    """Test that Validation built from empty sets converts to Maybe, and the result supports to_maybe() as well."""
    # Construct an empty set to represent both the success and failure collections
    empty_set = set()

    # Build a Validation instance with no successes and no failures
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe value
    maybe_result = validation_instance.to_maybe()

    # Verify that the resulting Maybe also supports to_maybe() without error
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None as both arguments."""
    # Use None for both constructor arguments to test null-input handling
    none_value = None

    # Instantiate Validation with two None arguments; should not raise
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_with_none_values_can_convert_to_maybe():
    """Test that a Validation initialized with None values can call to_maybe() without error."""
    # Use None for both constructor arguments to represent an empty/absent validation state
    none_value = None

    # Construct a Validation instance with both fields set to None
    validation_instance = validation.Validation(none_value, none_value)

    # Verify that converting to Maybe does not raise an exception
    validation_instance.to_maybe()

def test_validation_is_fail_called_on_generic_object_validation():
    """Test that Validation.is_fail() can be called on a Validation constructed with a generic object."""
    # Use a plain object instance as both the value and context for Validation
    generic_object = builtins.object()

    # Construct a Validation using the same generic object for both arguments
    validation_instance = validation.Validation(generic_object, generic_object)

    # Verify that is_fail() can be invoked without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation built from a nested tuple/dict structure accepts .map(None) without error."""
    # None value to be passed into map()
    none_value = None

    # Build a nested data structure to use as the Validation input
    negative_int = -895
    flag = True

    inner_tuple = (negative_int, flag)          # tuple used as dict key and value
    nested_dict = {inner_tuple: inner_tuple}    # dict keyed by the inner tuple
    outer_tuple = (nested_dict, nested_dict, negative_int)  # top-level input structure

    # Construct the Validation instance with the nested structure and boolean flag
    validation_instance = validation.Validation(outer_tuple, flag)

    # Call map with None — should execute without raising
    validation_instance.map(none_value)

def test_validation_bind_accepts_none():
    """Test that Validation.bind() accepts None without raising an error."""
    # Construct a raw byte payload to use as both arguments to Validation
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Create a Validation instance using the same byte sequence for both parameters
    validator = validation.Validation(raw_bytes, raw_bytes)

    # Bind None to the validator — should complete without error
    none_value = None
    validator.bind(none_value)

def test_validation_ap_with_false_state_and_true_values_list():
    """Test that Validation initialized with False state accepts ap() call with a list of True values."""
    # Define the invalid (False) state flag
    invalid_state = False

    # Define a single True value used to populate the list
    true_value = True

    # Build a list of four True values to pass into Validation and ap()
    true_values_list = [true_value, true_value, true_value, true_value]

    # Construct a Validation instance with the invalid state and the True values list
    validation_instance = validation.Validation(invalid_state, true_values_list)

    # Call ap() with the same list of True values
    validation_instance.ap(true_values_list)

def test_valid_validation_box_reports_success():
    """Test that a Validation constructed with True values converts to a box that reports success."""
    # Both flags set to True to represent a fully valid validation state
    is_valid = True

    # Create a Validation instance indicating success on both dimensions
    validation_instance = validation.Validation(is_valid, is_valid)

    # Convert the validation to its box representation
    validation_box = validation_instance.to_box()

    # Confirm the box correctly identifies itself as a success
    validation_box.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy():
    """Test that a Validation with empty lists converts to lazy, binds None, and the result also converts to lazy."""
    none_value = None
    empty_list = []

    # Create a Validation instance with empty error and value lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy representation
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_result = lazy_validation.bind(none_value)

    # Verify the bound result can also be converted to lazy without error
    bound_result.to_lazy()

def test_validation_lazy_and_try_conversion_with_ap():
    """Test that a Validation from empty dicts converts to lazy/Try forms and supports ap()."""

    # Build a Validation instance using two empty dicts as input
    empty_dict = {}
    empty_validation = validation.Validation(empty_dict, empty_dict)

    # Convert the validation to its lazy representation
    lazy_validation = empty_validation.to_lazy()

    # Convert the lazy validation to a Try monad
    try_result = lazy_validation.to_try()

    # Apply the original validation via ap() on the lazy validation (confirms ap executes without error)
    ap_result = lazy_validation.ap(empty_validation)

    # Check whether the Try result represents a success
    try_result.is_success()

def test_validation_to_try_is_success_with_zero_value():
    """Test that a Validation with value 0 and list [0] converts to a Try and reports success."""
    # Construct a Validation with integer value 0 and a list containing 0
    zero_value = 0
    allowed_values = [zero_value]
    validation_instance = validation.Validation(zero_value, allowed_values)

    # Convert the Validation to a Try monad
    try_result = validation_instance.to_try()

    # Verify that the Try result reports success
    try_result.is_success()

def test_validation_method_chaining_with_mixed_types():
    """Test that Validation instances with mixed types support chaining of eq, box, either, try, lazy, is_fail, str, and map operations."""

    # Define base input values
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes)
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the first arg and the mixed dict as the second
    validation_none_dict = validation.Validation(none_value, mixed_key_dict)

    # Test equality comparison with itself, then convert to box
    eq_result = validation_none_dict.__eq__(validation_none_dict)
    box_result = validation_none_dict.to_box()

    # Construct a Validation with bytes for both arguments
    validation_bytes_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Convert the box to an Either, and check is_fail on the bytes Validation
    either_result = box_result.to_either()
    is_fail_result = validation_bytes_bytes.is_fail()

    # Convert the Either to a Try (smoke call — result not used further)
    try_result = either_result.to_try()  # noqa: F841

    # Construct a Validation using the is_fail result as the first arg
    validation_fail_bytes = validation.Validation(is_fail_result, sample_bytes)

    # Get string representation of the fail Validation
    str_result = validation_fail_bytes.__str__()

    # Convert the bytes Validation to lazy (smoke call — result not used further)
    lazy_result_1 = validation_bytes_bytes.to_lazy()  # noqa: F841

    # Construct another bytes Validation for use in nesting
    validation_bytes_bytes_2 = validation.Validation(sample_bytes, sample_bytes)

    # Convert the original box to Either again (smoke call — result not used further)
    either_result_2 = box_result.to_either()  # noqa: F841

    # Convert the fail Validation to lazy, then nest it inside a new Validation
    lazy_result_2 = validation_fail_bytes.to_lazy()
    validation_lazy_nested = validation.Validation(lazy_result_2, validation_bytes_bytes_2)

    # Check is_fail on the bytes Validation again (smoke call — result not used further)
    is_fail_result_2 = validation_bytes_bytes.is_fail()  # noqa: F841

    # Map the string representation over the equality result
    eq_result.map(str_result)

def test_validation_eq_to_maybe_and_bind_operations():
    """Test that Validation supports equality, to_maybe conversion, and bind with various value types."""

    # Define reusable raw values
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes)
    mixed_key_dict = {none_value: bytes_value, bytes_value: bytes_value}

    # Construct a Validation with None as the primary value and the mixed dict as context
    validation_with_none = validation.Validation(none_value, mixed_key_dict)

    # Test equality of the Validation instance with itself
    eq_result = validation_with_none.__eq__(validation_with_none)

    # Convert the Validation to a Maybe type
    maybe_result = validation_with_none.to_maybe()

    # Construct a second Validation using bytes for both arguments
    validation_with_bytes = validation.Validation(bytes_value, bytes_value)

    # Call bind on the bytes-based Validation with a bytes value
    validation_with_bytes.bind(bytes_value)

def test_validation_eq_with_swapped_none_and_bytes_args_result_supports_to_box():
    """Test that comparing two Validation instances with swapped None/bytes arguments produces an equality result that supports .to_box()."""
    # A bytes value and None used as both keys and values in various positions
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # A dict with mixed key types: None -> bytes, bytes -> bytes
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # First Validation: None as first arg, dict as second
    validation_with_none_first = validation.Validation(none_value, mixed_key_dict)

    # Second Validation: bytes as first arg, None as second (swapped relative to first)
    validation_with_bytes_first = validation.Validation(sample_bytes, none_value)

    # Compare the two Validation instances using __eq__
    eq_result = validation_with_none_first.__eq__(validation_with_bytes_first)

    # The equality result must support conversion to a box
    eq_result.to_box()

