import pytest

import validation as validation_module
import builtins as builtins_module

def test_validation_self_equality_and_fail_conversion():
    """Create a Validation and exercise success check, self-equality, and fail->Maybe conversion."""
    # The description string is preserved exactly as in the original test.
    description = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct the Validation object with identical arguments (same as original).
    validation = validation_module.Validation(description, description)

    # Call is_success() to exercise success-path check.
    is_success_result = validation.is_success()

    # Check equality against itself by calling __eq__ explicitly (same as original).
    equals_self = validation.__eq__(validation)

    # Call is_fail() and then convert the resulting failure to a Maybe via to_maybe().
    is_fail_result = validation.is_fail()
    is_fail_result.to_maybe()

def test_validation_eq_compared_with_none_exposes_result_is_success():
    """Comparing a Validation instance with None via __eq__ returns an object exposing is_success()."""
    # Preserve original literal values
    none_value = None
    negative_value = -6891
    positive_value = 3125

    # The tuple originally passed to Validation
    singleton_tuple = (positive_value,)

    # Create the Validation instance using the provided validation_module alias
    validation_instance = validation_module.Validation(negative_value, singleton_tuple)

    # Call __eq__ with None exactly as in the original test
    eq_result = validation_instance.__eq__(none_value)

    # Preserve original behaviour: invoke is_success() on the result
    eq_result.is_success()

def test_validation_str_returns_object_with_is_fail():
    """Ensure Validation.__str__ returns an object that exposes is_fail()."""
    # Use the same empty dict for both constructor arguments (matches original test)
    input_data = {}

    # Construct the Validation object (module alias per provided imports)
    validation = validation_module.Validation(input_data, input_data)

    # Call __str__ and then call is_fail() on the returned object to exercise the API
    result = validation.__str__()
    result.is_fail()

def test_validation_to_either_and_maybe_idempotent():
    """Ensure Validation.to_either and to_maybe can be invoked and that calling to_maybe on its result is valid."""
    # Use an empty set for both constructor parameters (same as original test)
    empty_set = set()

    # Instantiate the Validation object under test
    validation_obj = validation_module.Validation(empty_set, empty_set)

    # Preserve original call order: first to_either(), then to_maybe()
    either_result = validation_obj.to_either()
    maybe_result = validation_obj.to_maybe()

    # Call to_maybe() again on the result to mirror the original test behavior
    maybe_result.to_maybe()

def test_validation_to_either_equality_and_is_fail_to_maybe_call_sequence():
    """Exercise Validation.to_either, self-equality (__eq__), is_fail and to_maybe in sequence."""
    # Original description text used to construct the Validation instance
    text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    # Create a Validation instance with the same text for both params (matches original)
    validation = validation_module.Validation(text, text)

    # Call to_either() as in the original test
    either_result = validation.to_either()
    assert either_result is not None

    # Check equality of the object with itself by using __eq__ (self-equality)
    assert validation == validation

    # Call is_fail() and then call to_maybe() on its result (preserve original call sequence)
    fail_result = validation.is_fail()
    # Ensure the result exposes a to_maybe method and that it can be called
    assert hasattr(fail_result, "to_maybe") and callable(getattr(fail_result, "to_maybe"))
    maybe_result = fail_result.to_maybe()
    # Accept any return value from to_maybe but ensure the call completed
    assert True

def test_validation_to_maybe_is_idempotent():
    """Ensure that calling to_maybe on a Validation (and then again on the result) is safe/idempotent."""
    # Create an empty input set (same object passed twice to the Validation)
    input_set = set()

    # Construct the Validation object using the provided validation module alias
    validator = validation_module.Validation(input_set, input_set)

    # First conversion to a "maybe" representation
    maybe_result = validator.to_maybe()

    # Call to_maybe again on the result to ensure calling it twice is safe
    maybe_result_twice = maybe_result.to_maybe()

    # Idempotence: converting to maybe again should produce an equal result (no error and stable outcome)
    assert maybe_result == maybe_result_twice

def test_validation_init_allows_none_inputs():
    """Ensure Validation can be instantiated when both inputs are None."""
    # Represent missing/absent inputs explicitly with None
    input_value = None

    # Instantiate Validation with two None values (preserves original behaviour)
    validation_instance = validation_module.Validation(input_value, input_value)

def test_validation_to_maybe_handles_none_inputs():
    """Create a Validation with None values and call to_maybe() — should not raise an error."""
    none_value = None

    # Construct the Validation with None for both parameters (preserve order/values)
    validation_instance = validation_module.Validation(none_value, none_value)

    # Invoke the method under test; success is simply not raising an exception
    validation_instance.to_maybe()

def test_validation_is_fail_invocable_with_same_object():
    """Ensure Validation.is_fail() can be invoked when both parameters are the same object."""
    # Create a basic object instance to pass to the Validation constructor
    sample_obj = builtins_module.object()
    # Instantiate Validation with the same object for both parameters
    validator = validation_module.Validation(sample_obj, sample_obj)
    # Call is_fail(); test passes if this call completes without raising
    validator.is_fail()

def test_validation_map_accepts_none_with_nested_init():
    """Validation.map should accept None when Validation is initialized with nested containers."""
    # Prepare literal values used in the nested initializer
    negative_int = -895
    flag = True

    # Use a tuple of (int, bool) as both the key and value inside the mapping
    pair = (negative_int, flag)
    nested_mapping = {pair: pair}

    # Initialize Validation with a tuple containing two identical dicts and the integer
    init_value = (nested_mapping, nested_mapping, negative_int)
    validator = validation_module.Validation(init_value, flag)

    # Ensure calling map with None does not raise
    validator.map(None)

def test_validation_bind_accepts_none_without_raising() -> None:
    """Ensure Validation.bind accepts None without raising an exception."""
    # sample input bytes used to construct the Validation instance
    sample_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # create a Validation instance with the same bytes for both parameters
    validation_instance = validation_module.Validation(sample_bytes, sample_bytes)

    # bind a None value; the test passes if this does not raise
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_accepts_list_of_boolean_flags():
    """Ensure Validation.ap can be invoked with a list of boolean flags without error."""
    initial_flag = False
    flags = [True, True, True, True]

    validation_instance = validation_module.Validation(initial_flag, flags)
    # Call .ap with the same flags list to ensure this code path executes without raising.
    validation_instance.ap(flags)

def test_validation_to_box_reports_success():
    """Ensure a Validation built with True values can be boxed and its is_success() method invoked."""
    # Setup input flag used for both constructor parameters
    flag = True

    # Create a Validation instance using the provided module alias
    validation = validation_module.Validation(flag, flag)

    # Convert the Validation into its boxed representation
    boxed = validation.to_box()

    # Invoke is_success() on the boxed result to exercise that API path
    # (No assertion is made here to preserve original test behavior.)
    boxed.is_success()

def test_validation_to_lazy_bind_none_and_to_lazy_no_error():
    """Verify Validation.to_lazy() can be bound with None and to_lazy() called again without error."""
    # Prepare inputs: an empty list (same object passed twice to the constructor)
    empty_list = []

    # Create the Validation instance using the provided validation module
    validation_instance = validation_module.Validation(empty_list, empty_list)

    # Convert to a lazy representation
    lazy_validation = validation_instance.to_lazy()

    # Bind the lazy validation with None (ensuring .bind accepts None)
    bound_lazy_validation = lazy_validation.bind(None)

    # Calling to_lazy() on the bound result should also be callable without raising
    bound_lazy_validation.to_lazy()

def test_validation_lazy_to_try_and_applies():
    """Ensure a Validation can be converted to lazy, to Try, and applied to itself."""
    empty_mapping = {}

    validation_obj = validation_module.Validation(empty_mapping, empty_mapping)
    lazy_validation = validation_obj.to_lazy()

    try_result = lazy_validation.to_try()
    applied_result = lazy_validation.ap(validation_obj)

    # Verify is_success is callable on the Try result (return value intentionally ignored)
    _ = try_result.is_success()

def test_validation_to_try_calls_is_success():
    """Ensure Validation.to_try() returns an object on which is_success() can be invoked."""
    # Use a zero value as in the original test
    value_zero = 0

    # Preserve original input by wrapping it in a list
    original_inputs = [value_zero]

    # Instantiate the Validation object using the provided validation_module alias
    validation_instance = validation_module.Validation(value_zero, original_inputs)

    # Call to_try() and then call is_success() on the result (preserve original call sequence)
    try_result = validation_instance.to_try()
    try_result.is_success()

def test_validation_chaining_and_map_invocation():
    """Exercise a series of Validation conversions and call map on the equality result."""
    # Raw input bytes used to construct various Validation instances
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    # None value preserved as in the original test
    none_value = None

    # Map that uses None and the raw bytes as keys/values
    input_map = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # Validation constructed with None as the "failure" part and a dict as the "success" part
    validation_none_map = validation_module.Validation(none_value, input_map)

    # Call __eq__ on the validation (original code used __eq__ and then .map on its result)
    equality_result = validation_none_map.__eq__(validation_none_map)

    # Convert the validation to a "box" representation
    box_result = validation_none_map.to_box()

    # Another validation built from raw bytes for further method calls
    validation_bytes = validation_module.Validation(raw_bytes, raw_bytes)

    # Convert box to either representation
    either_from_box = box_result.to_either()

    # Check if validation_bytes indicates failure
    is_fail_flag = validation_bytes.is_fail()

    # Convert either to a "try" representation
    try_from_either = either_from_box.to_try()

    # Build a validation using the is_fail_flag and raw bytes
    validation_from_flag = validation_module.Validation(is_fail_flag, raw_bytes)

    # Get string representation of the validation_from_flag (used later in map)
    validation_from_flag_str = validation_from_flag.__str__()

    # Convert validation_bytes to a lazy representation
    lazy_validation_bytes = validation_bytes.to_lazy()

    # Another validation built from raw bytes (second instance)
    validation_bytes_2 = validation_module.Validation(raw_bytes, raw_bytes)

    # Repeat conversion of box_result to either (preserve the original duplicated call)
    either_from_box_again = box_result.to_either()

    # Convert validation_from_flag to lazy
    lazy_validation_from_flag = validation_from_flag.to_lazy()

    # Nested validation combining lazy validation and another validation instance
    validation_nested = validation_module.Validation(lazy_validation_from_flag, validation_bytes_2)

    # Re-check is_fail on validation_bytes (preserve original duplicate call)
    is_fail_flag_again = validation_bytes.is_fail()

    # Finally, call map on the result of the equality operation with the string from validation_from_flag
    equality_result.map(validation_from_flag_str)

def test_validation_self_equality_to_maybe_and_bind():
    """
    Ensure Validation can compare to itself, convert to a maybe representation,
    and bind a value without raising exceptions.
    """
    # sample bytes used as both key and value in one of the mappings
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    # explicit None value to use as a dict key (mirrors original test)
    none_value = None

    # mapping that uses None as a key and sample_bytes as both key and value
    mapping_with_none_key = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # create a Validation where the "value" part is a mapping containing None as a key
    validation_with_none_key = validation_module.Validation(none_value, mapping_with_none_key)

    # call __eq__ comparing the instance to itself (should be truthy/harmless)
    is_equal_to_self = validation_with_none_key.__eq__(validation_with_none_key)
    assert is_equal_to_self is True

    # convert the validation to a "maybe" representation
    maybe_result = validation_with_none_key.to_maybe()
    assert maybe_result is not None

    # create another Validation with sample_bytes used for both parameters
    validation_with_bytes_pair = validation_module.Validation(sample_bytes, sample_bytes)

    # bind a value to the second Validation instance (should not raise)
    validation_with_bytes_pair.bind(sample_bytes)

def test_validation_eq_to_box_with_bytes_and_none_swapped_positions():
    """Ensure that comparing two Validation objects (one created with None and bytes) and converting the comparison result to a box completes without error."""
    # A bytes literal used as key/value in the payload
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    # Explicit None used to mirror original test inputs
    none_value = None

    # Construct a mapping that uses None as a key and bytes as both key and value
    payload_map = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create two Validation instances with swapped None/bytes positions (preserve original construction order)
    left_validation = validation_module.Validation(none_value, payload_map)
    right_validation = validation_module.Validation(sample_bytes, none_value)

    # Compare the two Validation instances using the same explicit method call as the original
    equality_result = left_validation.__eq__(right_validation)

    # Convert the equality result to a box (preserve original call)
    equality_result.to_box()

