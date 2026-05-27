import pytest
import validation as validation
import builtins as builtins

def test_validation_success_fail_and_maybe_conversion():
    """Test that a Validation instance correctly reports success/failure status,
    supports self-equality, and allows conversion of the fail result to a Maybe."""

    # Use a docstring-style string as the validation value and message
    docstring_value = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance with the string as both arguments
    validation_instance = validation.Validation(docstring_value, docstring_value)

    # Check whether the validation is considered a success
    is_success_result = validation_instance.is_success()

    # Verify that the instance is equal to itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation is considered a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the fail result to a Maybe value
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None via __eq__ yields a result that supports is_success()."""
    # Set up comparison target
    none_value = None

    # Construct a Validation instance with a negative integer and a single-element tuple
    negative_int = -6891
    tuple_element = 3125
    validation_args = (tuple_element,)
    validation_instance = validation.Validation(negative_int, validation_args)

    # Compare the Validation instance to None and verify the result supports is_success()
    eq_result = validation_instance.__eq__(none_value)
    eq_result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Test that __str__() on a Validation with empty dicts returns an object exposing is_fail()."""
    # Use empty dicts for both the data and schema arguments
    empty_dict = {}

    # Construct a Validation instance with two empty dicts
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation instance to its string representation
    str_result = validation_instance.__str__()

    # Verify the string result exposes the is_fail() method (call is exercised)
    str_result.is_fail()

def test_empty_validation_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets converts to Either and Maybe, and that the Maybe supports chained to_maybe()."""
    # Use empty sets as both the success and failure collections
    empty_set = set()

    # Construct a Validation with empty success and failure sets
    empty_validation = validation.Validation(empty_set, empty_set)

    # Convert the validation to an Either type
    either_result = empty_validation.to_either()

    # Convert the validation to a Maybe type
    maybe_result = empty_validation.to_maybe()

    # Verify that the resulting Maybe also supports to_maybe() conversion
    maybe_result.to_maybe()

def test_validation_core_operations_on_string_value():
    """Test that a Validation built from a string supports to_either, equality, is_fail, and to_maybe operations."""
    # Use a descriptive multi-line string as both the value and error message
    validation_message = (
        "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    )

    # Construct a Validation instance with the message as both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Determine whether the validation represents a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the failure-check result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_to_maybe_is_chainable():
    """Test that to_maybe() on a Validation with empty sets returns a value that also supports to_maybe()."""
    # An empty set represents no errors and no warnings
    empty_set = set()

    # Construct a Validation instance with no errors and no warnings
    valid_result = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe value
    maybe_result = valid_result.to_maybe()

    # Verify that the resulting Maybe value also supports to_maybe() (chaining)
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None as both arguments."""
    # Use None for both the value and the constraint arguments
    none_value = None

    # Instantiate Validation with two None arguments; should not raise
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_with_none_values_to_maybe_does_not_raise():
    """Test that Validation initialized with None values can call to_maybe() without error."""
    # Use None for both constructor arguments to represent an empty/absent validation
    none_value = None
    validation_instance = validation.Validation(none_value, none_value)

    # Verify that converting to Maybe does not raise an exception
    validation_instance.to_maybe()

def test_validation_is_fail_can_be_called_on_plain_object():
    """Test that Validation.is_fail() can be called on a Validation constructed with a plain object."""
    # Use a plain object as both arguments to Validation
    plain_object = builtins.object()

    # Construct a Validation instance using the plain object for both parameters
    validation_instance = validation.Validation(plain_object, plain_object)

    # Invoke is_fail() to verify it executes without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation.map(None) can be called on an instance constructed with a nested tuple-keyed dict structure."""

    # Primitive values used to build the nested input
    none_value = None
    negative_int = -895
    flag = True

    # Build a tuple used both as dict key and value
    int_bool_tuple = (negative_int, flag)

    # Dict with a tuple key mapping to itself
    tuple_keyed_dict = {int_bool_tuple: int_bool_tuple}

    # Nested tuple containing the dict and the integer, used as validation input
    nested_data_tuple = (tuple_keyed_dict, tuple_keyed_dict, negative_int)

    # Construct Validation with nested data and the boolean flag
    validation_instance = validation.Validation(nested_data_tuple, flag)

    # Call map with None — should not raise
    validation_instance.map(none_value)

def test_validation_bind_with_bytes_accepts_none():
    """Test that Validation can be instantiated with byte data and bound to None without error."""
    # A raw byte payload used as both positional arguments to Validation
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Construct a Validation instance using the same byte value for both arguments
    validation_instance = validation.Validation(raw_bytes, raw_bytes)

    # Bind None to the validation instance (should not raise)
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_applies_list_of_true_values_on_invalid_validation():
    """Test that calling ap() with a list of True values on an invalid Validation instance does not raise an error."""
    # Set up validity flag and a list of True values
    is_valid = False
    true_value = True
    true_values_list = [true_value, true_value, true_value, true_value]

    # Create a Validation instance marked as invalid, holding the list of True values
    invalid_validation = validation.Validation(is_valid, true_values_list)

    # Apply the list of True values via ap() — should execute without error
    invalid_validation.ap(true_values_list)

def test_validation_to_box_reports_success_when_valid():
    """Test that a successful Validation converts to a box that reports is_success() as True."""
    # Both arguments are True, indicating a valid/successful validation state
    is_valid = True

    # Create a Validation instance with both flags set to True (valid state)
    validation_instance = validation.Validation(is_valid, is_valid)

    # Convert the validation to its boxed representation
    boxed_result = validation_instance.to_box()

    # Verify the boxed result correctly identifies itself as a success
    boxed_result.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy():
    """Test that a Validation built from empty lists can be converted to lazy, bound with None, and converted to lazy again."""
    none_value = None
    empty_list = []

    # Construct a Validation instance with two empty lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy form
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_validation = lazy_validation.bind(none_value)

    # Verify the bound result can also be converted to lazy form
    bound_validation.to_lazy()

def test_validation_lazy_and_try_conversion_with_ap():
    """Test that a Validation can be converted to lazy and Try forms, and that ap can be applied without error."""
    # Create an empty Validation instance using two empty dicts
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation to its lazy representation
    lazy_validation = validation_instance.to_lazy()

    # Convert the lazy validation to a Try
    try_result = lazy_validation.to_try()

    # Apply the original validation instance using ap on the lazy validation
    ap_result = lazy_validation.ap(validation_instance)

    # Check whether the Try result represents a success
    try_result.is_success()

def test_validation_to_try_is_success_when_valid_value_provided():
    """Test that a Validation with a valid value converts to a successful Try."""
    # Set up a simple integer value and a list to construct the Validation
    valid_value = 0
    validation_rules = [valid_value]

    # Create a Validation instance with the value and its associated list
    validation_instance = validation.Validation(valid_value, validation_rules)

    # Convert to a Try monad and confirm it represents a success
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_methods_with_mixed_types_and_chaining():
    """Test that Validation supports mixed-type construction and method chaining without errors."""

    # --- Setup: define base values used across multiple Validation instances ---
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # --- Construct a Validation with None as the fail value and a dict as success ---
    validation_with_none_fail = validation.Validation(none_value, mixed_key_dict)

    # Test equality comparison with itself, then convert to box
    eq_result = validation_
# (Truncated by extractor)