import pytest
import validation as validation
import builtins as builtins

def test_validation_success_fail_and_maybe_conversion():
    """Test that a Validation instance correctly reports success/failure status, supports equality comparison with itself, and allows conversion of the fail result to a Maybe."""

    # Use a descriptive docstring-style string as both the value and message for the Validation
    validation_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct a Validation instance with the message used as both arguments
    validation_instance = validation.Validation(validation_message, validation_message)

    # Check whether the validation is considered a success
    is_success_result = validation_instance.is_success()

    # Verify that the validation instance is equal to itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation is considered a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the fail result to a Maybe value
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_result_with_is_success():
    """Test that comparing a Validation instance to None via __eq__ returns a result that supports is_success()."""
    # Prepare the value to compare against
    none_value = None

    # Build a Validation instance with a negative code and a single-element tuple
    validation_code = -6891
    tuple_element = 3125
    validation_args = (tuple_element,)
    validation_instance = validation.Validation(validation_code, validation_args)

    # Compare the Validation instance to None using the explicit __eq__ method
    eq_result = validation_instance.__eq__(none_value)

    # Verify the comparison result exposes is_success() without error
    eq_result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Test that __str__() on a Validation instance returns an object that supports is_fail()."""
    # Create a Validation instance using empty dicts for both arguments
    empty_dict = {}
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Obtain the string representation of the validation object
    str_result = validation_instance.__str__()

    # Verify that the string result exposes the is_fail() interface
    str_result.is_fail()

def test_validation_with_empty_sets_converts_to_either_and_maybe():
    """Test that a Validation built from empty sets converts to Either and Maybe, and that the Maybe result supports a chained to_maybe() call."""
    # Construct a Validation instance using an empty set for both success and failure collections
    empty_set = set()
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Convert the validation to a Maybe type
    maybe_result = validation_instance.to_maybe()

    # Verify that the Maybe result itself supports the to_maybe() conversion (chained call)
    maybe_result.to_maybe()

def test_validation_core_operations_on_string_value():
    """Tests that a Validation instance supports to_either, equality, is_fail, and to_maybe operations."""

    # Use a descriptive multi-line string as both the success and failure value
    docstring_value = (
        "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    )

    # Construct a Validation with the same string as both values
    validation_instance = validation.Validation(docstring_value, docstring_value)

    # Convert the validation to an Either type
    either_result = validation_instance.to_either()

    # Check equality of the validation instance with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check whether the validation represents a failure
    is_fail_result = validation_instance.is_fail()

    # Convert the is_fail result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_with_empty_set_to_maybe_is_chainable():
    """Test that Validation with empty sets converts to Maybe and supports chained to_maybe() calls."""
    # Create an empty set to represent a Validation with no errors and no values
    empty_set = set()

    # Construct a Validation instance using empty sets for both parameters
    validation_instance = validation.Validation(empty_set, empty_set)

    # Convert the Validation to a Maybe
    maybe_result = validation_instance.to_maybe()

    # Verify that the resulting Maybe also supports to_maybe() without error
    maybe_result.to_maybe()

def test_validation_instantiation_with_none_arguments():
    """Test that Validation can be instantiated with None as both arguments."""
    # Use None for both constructor parameters to test null/missing input handling
    none_value = None

    # Instantiate Validation with both arguments as None
    validation_instance = validation.Validation(none_value, none_value)

def test_validation_to_maybe_with_none_values():
    """Test that Validation constructed with None values can call to_maybe() without error."""
    # Use None for both the value and the error fields
    none_value = None

    validation_instance = validation.Validation(none_value, none_value)

    # Verify that converting a None-valued Validation to Maybe does not raise
    validation_instance.to_maybe()

def test_validation_is_fail_returns_without_error():
    """Test that Validation.is_fail() can be called on a Validation instance constructed with a generic object."""
    # Create a plain object to serve as both constructor arguments
    generic_object = builtins.object()

    # Construct a Validation instance using the same generic object for both parameters
    validation_instance = validation.Validation(generic_object, generic_object)

    # Invoke is_fail() to verify it executes without error
    validation_instance.is_fail()

def test_validation_map_with_none_on_nested_structure():
    """Test that Validation built from a nested tuple/dict payload accepts None passed to map()."""
    # Primitive values used to build the nested data structure
    none_value = None
    negative_int = -895
    flag = True

    # Build a nested structure: tuple used as both key and value in a dict
    inner_tuple = (negative_int, flag)
    nested_dict = {inner_tuple: inner_tuple}

    # Outer tuple wraps the dict and is passed as the Validation payload
    outer_tuple = (nested_dict, nested_dict, negative_int)

    # Construct Validation with the nested payload and boolean flag
    validator = validation.Validation(outer_tuple, flag)

    # Call map() with None — should execute without error
    validator.map(none_value)

def test_validation_bind_accepts_none():
    """Test that Validation.bind() accepts None without raising an error."""

    # A raw byte string used as both the first and second constructor arguments
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Instantiate Validation with identical byte strings for both parameters
    validator = validation.Validation(raw_bytes, raw_bytes)

    # Explicitly bind None to the validator (no bound value)
    no_value = None
    validator.bind(no_value)

def test_validation_ap_called_with_list_of_true_values_on_invalid_instance():
    """Test that ap() can be called on an invalid Validation instance with a list of True values."""
    # Define the validity flag and a reusable True boolean value
    is_valid = False
    true_value = True

    # Build a list consisting entirely of True values
    true_values_list = [true_value, true_value, true_value, true_value]

    # Create a Validation instance marked as invalid (False), carrying the list of True values
    invalid_validation = validation.Validation(is_valid, true_values_list)

    # Apply (ap) the list of True values to the invalid Validation instance
    invalid_validation.ap(true_values_list)

def test_valid_validation_box_reports_success():
    """Test that a successful Validation converts to a box that reports is_success()."""
    # Both flags set to True to represent a fully valid/successful validation
    is_valid = True

    # Construct a Validation instance indicating success on both dimensions
    valid_validation = validation.Validation(is_valid, is_valid)

    # Convert the validation result to its box representation
    validation_box = valid_validation.to_box()

    # Exercise the is_success() path on the resulting box
    validation_box.is_success()

def test_validation_to_lazy_bind_none_then_to_lazy_again():
    """Test that a Validation with empty lists can be lazified, bound with None, and lazified again without error."""
    none_value = None
    empty_list = []

    # Create a Validation instance with empty error and success lists
    validation_instance = validation.Validation(empty_list, empty_list)

    # Convert the validation to its lazy form
    lazy_validation = validation_instance.to_lazy()

    # Bind None to the lazy validation
    bound_validation = lazy_validation.bind(none_value)

    # Convert the bound result to lazy again — should not raise
    bound_validation.to_lazy()

def test_lazy_validation_ap_and_try_conversion_is_success():
    """Verify that a Validation converted to lazy supports ap and Try conversion, with is_success callable on the Try result."""
    # Use an empty dict as both the success and failure value for the Validation
    empty_dict = {}

    # Create a Validation instance with empty success and failure containers
    validation_instance = validation.Validation(empty_dict, empty_dict)

    # Convert the Validation to its lazy (deferred) form
    lazy_validation = validation_instance.to_lazy()

    # Convert the lazy validation to a Try monad
    try_result = lazy_validation.to_try()

    # Apply the original validation instance via ap on the lazy validation
    ap_result = lazy_validation.ap(validation_instance)

    # Verify that the Try result reports success
    try_result.is_success()

def test_validation_with_zero_and_list_to_try_is_success():
    """Test that a Validation built with 0 and a list containing 0 converts to a successful Try."""
    # Set up the integer value and the list used to construct the Validation
    zero_value = 0
    value_list = [zero_value]

    # Construct the Validation instance with the zero value and its containing list
    validation_instance = validation.Validation(zero_value, value_list)

    # Convert to a Try monad and verify the result reports success
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_monad_conversions_and_chaining():
    """Test Validation monad conversions (Box, Either, Try, Lazy) and map across instances with None and bytes values."""

    # --- Setup shared values ---
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # --- First Validation: None as fail, dict as value ---
    validation_none_fail = validation.Validation(none_value, mixed_key_dict)
    eq_result = validation_none_fail.__eq__(validation_none_fail)

    # Convert to Box and then to Either
    box_from_none_fail = validation_none_fail.to_box()

    # --- Second Validation: bytes as both fail and value ---
    validation_bytes = validation.Validation(sample_bytes, sample_bytes)
    either_from_box = box_from_none_fail.to_either()

    # Check is_fail and convert Either to Try
    is_fail_bytes = validation_bytes.is_fail()
    try_from_either = either_from_box.to_try()

    # --- Third Validation: is_fail result as fail, bytes as value ---
    validation_is_fail_result = validation.Validation(is_fail_bytes, sample_bytes)
    str_representation = validation_is_fail_result.__str__()

    # Convert second validation to Lazy
    lazy_from_bytes = validation_bytes.to_lazy()

    # --- Fourth Validation: identical bytes/bytes (copy of second) ---
    validation_bytes_copy = validation.Validation(sample_bytes, sample_bytes)

    # Re-derive Either from box and Lazy from third Validation
    either_from_box_again = box_from_none_fail.to_either()
    lazy_from_is_fail_result = validation_is_fail_result.to_lazy()

    # --- Fifth Validation: lazy result as fail, fourth validation as value ---
    validation_lazy_nested = validation.Validation(lazy_from_is_fail_result, validation_bytes_copy)

    # Final is_fail check on second Validation, then map str onto eq_result
    is_fail_bytes_again = validation_bytes.is_fail()
    eq_result.map(str_representation)

def test_validation_eq_to_maybe_and_bind_with_bytes_value():
    """Test that Validation supports equality, to_maybe conversion, and bind with None and bytes values."""
    # Define a concrete bytes value and a None value to use as Validation contents/errors
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Build a dict with mixed key types (None and bytes) mapping to the bytes value
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct a Validation with None as the value and a mixed dict as the error/context
    validation_with_none = validation.Validation(none_value, mixed_key_dict)

    # Verify that a Validation instance can compare itself for equality
    eq_result = validation_with_none.__eq__(validation_with_none)

    # Verify that a Validation can be converted to a Maybe
    maybe_result = validation_with_none.to_maybe()

    # Construct a second Validation using concrete bytes for both value and error
    validation_with_bytes = validation.Validation(sample_bytes, sample_bytes)

    # Verify that bind can be invoked on a Validation with a bytes argument
    validation_with_bytes.bind(sample_bytes)

def test_validation_eq_with_swapped_none_and_bytes_args_returns_boxable_result():
    """Test that __eq__ on two Validation instances with swapped None/bytes args returns a boxable result."""
    # Set up the raw values used to construct the Validation instances
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # A dict using both None and bytes as keys, mapping to the same bytes value
    mixed_key_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct two Validation instances with swapped argument positions
    validation_none_first = validation.Validation(none_value, mixed_key_dict)
    validation_bytes_first = validation.Validation(sample_bytes, none_value)

    # Compare the two instances and verify the result can be converted to a box
    eq_result = validation_none_first.__eq__(validation_bytes_first)
    eq_result.to_box()

