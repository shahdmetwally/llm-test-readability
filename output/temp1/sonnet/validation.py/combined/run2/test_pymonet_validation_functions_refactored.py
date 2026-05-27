import pytest
import validation as validation
import builtins as builtins

def test_validation_with_string_value_reports_success_and_fail_states():
    """Test that a Validation created with a string value correctly exposes success/fail states and supports conversion to Maybe."""

    # Use a descriptive docstring-like string as both the value and message
    docstring_text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance using the string as both arguments
    validation_instance = validation.Validation(docstring_text, docstring_text)

    # Check whether the validation reports a successful state
    is_success_result = validation_instance.is_success()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation reports a failure state
    is_fail_result = validation_instance.is_fail()

    # Convert the fail result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_callable_success_result():
    """Test that comparing a Validation instance to None via __eq__ produces a result that supports is_success()."""
    # Comparison target: None
    none_value = None

    # Construct a Validation instance with a negative error code and a single-element tuple of args
    error_code = -6891
    value = 3125
    validation_args = (value,)
    validation_instance = validation.Validation(error_code, validation_args)

    # Compare the Validation instance to None using __eq__
    eq_result = validation_instance.__eq__(none_value)

    # Verify the result supports is_success() without raising
    eq_result.is_success()

def test_validation_str_representation_exposes_is_fail_method():
    """Test that the string representation of a Validation instance exposes the is_fail method."""
    # Use empty dicts as both arguments to construct a minimal Validation instance
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation instance
    str_representation = validation_instance.__str__()

    # Verify that the string representation supports the is_fail() call
    str_representation.is_fail()

def test_validation_with_empty_sets_supports_to_either_and_to_maybe_conversions():
    """Test that a Validation built from empty sets can be converted to Either and Maybe, and that the Maybe supports chaining to_maybe()."""
    # Create a shared empty set to use as both the success and failure collections
    empty_set = set()

    # Construct a Validation instance using the empty set for both parameters
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Convert the validation to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify that the Maybe result also supports being converted to a Maybe (chaining)
    maybe_result.to_maybe()

def test_validation_basic_operations_on_string_value():
    """Tests that a Validation constructed from a string supports to_either, equality, is_fail, and to_maybe operations."""

    # Use a docstring-like string as both the value and label for the Validation
    docstring_value = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance using the string as both arguments
    validation_instance = validation.Validation(docstring_value, docstring_value)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Determine whether the validation represents a failure
    is_fail_result = validation_instance.is_fail()

    # Verify that the failure-check result exposes a to_maybe() method and call it
    is_fail_result.to_maybe()

def test_validation_with_empty_sets_to_maybe_is_chainable():
    """Test that to_maybe() on a Validation with empty sets returns a Maybe that also supports to_maybe()."""
    # Create an empty set to represent both the value and error collections
    empty_set = set()

    # Construct a Validation instance using empty sets for both arguments
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe
    maybe_result = validation_instance.to_maybe()

    # Verify the resulting Maybe also supports to_maybe() (i.e., the chain is valid)
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None for both arguments."""

    # Use None for both constructor parameters
    none_value = None

    # Instantiate Validation with two None arguments
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_with_none_args_to_maybe_does_not_raise():
    """Test that Validation constructed with None arguments can call to_maybe() without error."""
    # Use None for both constructor arguments
    none_value = None

    # Construct a Validation instance with None values
    validation_instance = validation.Validation(none_value, none_value)

    # Verify that calling to_maybe() does not raise an exception
    validation_instance.to_maybe()

def test_validation_is_fail_with_same_object_for_both_args():
    """Test that Validation.is_fail() can be called when both constructor arguments are the same object."""
    # Create a generic object to serve as both the subject and comparator
    generic_object = builtins.object()

    # Construct a Validation instance using the same object for both arguments
    validation_instance = validation.Validation(generic_object, generic_object)

    # Invoke is_fail() to verify it executes without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation.map() accepts None when constructed with a nested tuple/dict structure and a boolean flag."""
    # None value to be passed to .map()
    none_value = None

    # Build the nested input structure
    negative_int = -895
    bool_flag = True

    inner_tuple = (negative_int, bool_flag)
    nested_dict = {inner_tuple: inner_tuple}

    # Outer tuple wraps the dict and primitive values
    outer_tuple = (nested_dict, nested_dict, negative_int)

    # Construct the Validation instance with the nested structure and boolean flag
    validation_instance = validation.Validation(outer_tuple, bool_flag)

    # Call map with None — should execute without error
    validation_instance.map(none_value)

def test_validation_bind_accepts_none():
    """Test that Validation.bind() accepts None without raising an error."""
    # Use a fixed byte string as both constructor arguments
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Construct a Validation instance with identical byte inputs
    validator = validation.Validation(raw_bytes, raw_bytes)

    # Explicitly pass None to bind, verifying it is accepted
    none_value = None
    validator.bind(none_value)

def test_validation_ap_with_false_state_and_true_values_list():
    """Test that Validation initialized with False state can call ap with a list of True values."""
    # Set up the validity flag: False means the validation is in an invalid state
    is_valid = False

    # A True boolean value used to populate the input list
    true_value = True

    # A list of four True values to pass into Validation and ap
    true_values_list = [true_value, true_value, true_value, true_value]

    # Create a Validation instance with an invalid state and the list of True values
    validation_instance = validation.Validation(is_valid, true_values_list)

    # Call ap on the validation instance with the same list of True values
    validation_instance.ap(true_values_list)

def test_validation_true_true_to_box_is_success():
    """Test that a Validation constructed with True values converts to a box that reports success."""
    # Both the value and validity flag are True
    is_valid = True

    # Create a Validation instance indicating a successful/valid state
    validation_instance = validation.Validation(is_valid, is_valid)

    # Convert the validation to its boxed representation
    boxed_result = validation_instance.to_box()

    # Verify that the boxed result reports a successful outcome
    boxed_result.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy():
    """Test that a Validation with empty lists can be lazified, bound with None, and the result lazified again."""
    none_value = None
    empty_list = []

    # Create a Validation instance with two empty lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy representation
    lazy_validation = validation_instance.to_lazy()

    # Bind the lazy validation with None
    bound_result = lazy_validation.bind(none_value)

    # Verify the bound result can also be converted to lazy form
    bound_result.to_lazy()

def test_validation_lazy_and_try_conversions_with_ap():
    """Test that a Validation converts to lazy and Try forms, and that ap can be applied."""
    # Use an empty dict as both the success and error container
    empty_dict = {}

    # Create a Validation instance with empty success and error dicts
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation to its lazy (deferred) form
    lazy_validation = validation_instance.to_lazy()

    # Convert the lazy validation to a Try (either-like) structure
    try_result = lazy_validation.to_try()

    # Apply the original validation to the lazy validation via ap (applicative apply)
    ap_result = lazy_validation.ap(validation_instance)

    # Query the success state of the Try result
    try_result.is_success()

def test_validation_with_zero_value_to_try_is_success():
    """Test that a Validation with a zero value and single-element list converts to a successful Try."""
    # Construct a Validation instance with a zero integer value and a one-element validator list
    value = 0
    validators = [value]
    validation_instance = validation.Validation(value, validators)

    # Convert the Validation to a Try monad and verify it represents a success
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_method_chaining_with_mixed_value_types():
    """Test that Validation instances support method chaining across mixed value types including None, bytes, and bool."""

    # --- Setup: primitive values ---
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # --- Construct first Validation with None key and dict value ---
    validation_none_key = validation.Validation(none_value, mixed_key_dict)

    # Check equality of Validation with itself, then convert to box
    eq_result = validation_none_key.__eq__(validation_none_key)
    box_result = validation_none_key.to_box()

    # --- Construct second Validation with bytes for both fail and success ---
    validation_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Chain box to either, check is_fail, then chain either to try
    either_from_box = box_result.to_either()
    is_fail_bytes = validation_bytes.is_fail()
    try_result = either_from_box.to_try()

    # --- Construct third Validation using is_fail result as the key ---
    validation_bool_key = validation.Validation(is_fail_bytes, sample_bytes)

    # Get string representation, and convert bytes Validation to lazy
    str_result = validation_bool_key.__str__()
    lazy_from_bytes = validation_bytes.to_lazy()

    # --- Construct fourth Validation as a bytes-bytes pair (copy) ---
    validation_bytes_copy = validation.Validation(sample_bytes, sample_bytes)

    # Re-derive either from box and convert bool-key Validation to lazy
    second_either_from_box = box_result.to_either()
    lazy_from_bool = validation_bool_key.to_lazy()

    # --- Construct fifth Validation using lazy result as key ---
    validation_lazy_key = validation.Validation(lazy_from_bool, validation_bytes_copy)

    # Re-check is_fail on
# (Truncated by extractor)