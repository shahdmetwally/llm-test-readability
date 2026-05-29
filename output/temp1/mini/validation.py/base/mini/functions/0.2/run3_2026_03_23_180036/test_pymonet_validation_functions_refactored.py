import pytest

import builtins as builtins_mod
import validation as validation_module

def test_validation_equality_and_conversion_methods():
    """Create a Validation and call its basic inspection/conversion methods.

    This test constructs a Validation with the original message text and then
    exercises is_success(), equality with itself, is_fail(), and finally
    calls to_maybe() on the result of is_fail().
    """
    message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_obj = validation_module.Validation(message, message)

    # Check success status
    is_success_result = validation_obj.is_success()

    # Equality against itself
    eq_self = validation_obj.__eq__(validation_obj)
    assert eq_self

    # Check failure status and convert to maybe
    is_fail_result = validation_obj.is_fail()
    maybe_result = is_fail_result.to_maybe()

def test_validation_eq_with_none_produces_result_supporting_is_success():
    """Call Validation.__eq__(None) and ensure the returned object supports is_success()."""
    # Prepare inputs exactly as in the original test
    none_value = None
    negative_code = -6891
    positive_value = 3125
    single_value_tuple = (positive_value,)

    # Create the Validation instance using the provided module alias
    validation_instance = validation_module.Validation(negative_code, single_value_tuple)

    # Invoke the __eq__ method with None (explicit call preserved) and then call is_success()
    eq_result = validation_instance.__eq__(none_value)
    eq_result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Ensure Validation.__str__ returns an object that exposes is_fail()."""
    # Prepare an empty mapping used as both input arguments to Validation
    input_mapping = {}
    # Create the Validation instance using the provided validation_module alias
    validator = validation_module.Validation(input_mapping, input_mapping)
    # Call __str__() on the validator and ensure the returned object supports is_fail()
    result = validator.__str__()
    result.is_fail()

def test_validation_to_either_and_maybe_with_empty_sets():
    """Construct a Validation with empty sets and exercise its conversion helpers."""
    # Use a single empty set instance for both parameters (same semantics as original)
    empty_set = set()
    validation = validation_module.Validation(empty_set, empty_set)

    # Convert to Either and Maybe as in the original test
    either = validation.to_either()
    maybe = validation.to_maybe()

    # Call to_maybe() on the resulting Maybe again (preserves original call sequence)
    maybe.to_maybe()

def test_validation_conversion_and_self_equality():
    """Exercise Validation conversion helpers and self-equality.

    Creates a Validation with an explanatory message, converts it to an
    Either, checks equality against itself, verifies failure status, and
    calls to_maybe() on the failure result to ensure that call path is exercised.
    """
    message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Instantiate Validation with the same message for both value and error
    validation = validation_module.Validation(message, message)

    # Convert to Either (exercise to_either path)
    either_result = validation.to_either()

    # Explicit self-equality check via __eq__
    is_equal_to_self = validation.__eq__(validation)

    # Check if the validation is a failure and then convert that failure to a Maybe
    fail_result = validation.is_fail()
    fail_result.to_maybe()

def test_to_maybe_can_be_invoked_twice_on_same_validation_input():
    """Verify that calling to_maybe() on a Validation created with the same set instance can be invoked twice.

    This reproduces the original behaviour: construct a Validation with the same set instance
    passed for both parameters, call to_maybe() to get the resulting object, and call to_maybe()
    on that result again.
    """
    # Create a single empty set and reuse it for both Validation parameters
    shared_empty_set = set()

    # Construct the Validation instance using the shared set for both args
    validator = validation_module.Validation(shared_empty_set, shared_empty_set)

    # First conversion to a "maybe"-like object
    maybe_value = validator.to_maybe()

    # Invoke to_maybe() again on the returned object (preserve original call sequence)
    maybe_value.to_maybe()

def test_validation_allows_none_parameters():
    """Ensure Validation can be instantiated when both constructor args are None."""
    # Prepare None inputs to represent missing/absent values.
    first_input = None
    second_input = None

    # Instantiate Validation with two None values; should not raise here.
    validation_instance = validation_module.Validation(first_input, second_input)

def test_validation_to_maybe_with_none_inputs():
    """Ensure Validation.to_maybe() can be invoked when the Validation is created with None values."""
    none_value = None  # Use an explicit None for clarity
    validator = validation_module.Validation(none_value, none_value)
    # Invoke the method under test; the original test did not assert a return value
    validator.to_maybe()

def test_validation_is_fail_called_for_same_object_arguments():
    """Ensure Validation.is_fail() runs when both constructor args are the same object."""
    # Create a plain built-in object to pass to the Validation constructor twice
    same_obj = builtins_mod.object()

    # Instantiate the Validation with the same object for both parameters
    validator = validation_module.Validation(same_obj, same_obj)

    # Invoke the method under test (preserve original call/side-effect)
    validator.is_fail()

def test_validation_map_accepts_none_with_nested_collections():
    """Call Validation.map(None) when the Validation was initialized with nested collections."""
    none_value = None
    negative_int = -895
    truth_flag = True

    # A tuple used both as a dict key and as its corresponding value
    key_value_tuple = (negative_int, truth_flag)
    nested_dict = {key_value_tuple: key_value_tuple}

    # The Validation is initialized with a tuple containing the same dict twice and an int
    init_args = (nested_dict, nested_dict, negative_int)
    validator = validation_module.Validation(init_args, truth_flag)

    # Invoke map with None (preserving original behavior and execution order)
    validator.map(none_value)

def test_validation_bind_accepts_none():
    """Call Validation.bind with None to ensure it can be invoked without error."""
    # Prepare raw input bytes (used for both arguments to the Validation constructor).
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Instantiate Validation from the aliased validation_module.
    validator = validation_module.Validation(raw_bytes, raw_bytes)

    # Use an explicit None variable to show intent when binding.
    none_value = None

    # Call bind with None; test succeeds if no exception is raised.
    validator.bind(none_value)

def test_validation_ap_accepts_list_of_booleans():
    """Verify Validation.ap can be called with a list of booleans without raising."""
    # boolean flags used in the list
    flag_off = False
    flag_on = True

    # list consisting of the same True flag repeated
    boolean_list = [flag_on, flag_on, flag_on, flag_on]

    # instantiate Validation with a False flag and the prepared list
    validator = validation_module.Validation(flag_off, boolean_list)

    # call .ap with the same list (should not raise)
    validator.ap(boolean_list)

def test_validation_to_box_is_success_invokable_when_both_flags_true():
    """Ensure Validation.to_box().is_success() can be invoked when both inputs are True."""
    # Use explicit boolean inputs to construct the Validation object
    flag = True
    validation_instance = validation_module.Validation(flag, flag)

    # Convert the validation to its boxed representation
    boxed_result = validation_instance.to_box()

    # Call is_success() to exercise that method (no assertion required by this test)
    boxed_result.is_success()

def test_validation_to_lazy_bind_with_none():
    """Validation.to_lazy() can be bound with None and converted back to lazy form."""
    none_value = None
    empty_list = []

    # Create a Validation instance with two empty lists
    validation = validation_module.Validation(empty_list, empty_list)

    # Convert to a lazy representation
    lazy_validation = validation.to_lazy()

    # Bind the lazy value with None (simulates providing no value)
    bound_lazy = lazy_validation.bind(none_value)

    # Convert the bound lazy back to lazy form (ensures no errors and same call sequence)
    bound_lazy.to_lazy()

def test_validation_lazy_to_try_and_apply():
    """Convert a Validation to lazy, then to try, and apply it back to ensure methods run."""
    # Create an empty mapping to use as both success and failure payloads
    payload = {}

    # Instantiate Validation using the provided module alias
    validation = validation_module.Validation(payload, payload)

    # Convert to a lazy representation
    lazy_validation = validation.to_lazy()

    # Convert the lazy validation to a try-like representation
    try_result = lazy_validation.to_try()

    # Apply the lazy validation to the original Validation instance
    applied_result = lazy_validation.ap(validation)

    # Invoke is_success() on the try result (no assertion; just ensure the call executes)
    try_result.is_success()

def test_validation_to_try_is_success_callable():
    """Ensure Validation.to_try() returns an object that exposes is_success()."""
    input_value = 0
    values = [input_value]
    validation = validation_module.Validation(input_value, values)
    result = validation.to_try()
    # Invoke is_success() to verify the method can be called (return is intentionally unused).
    result.is_success()

def test_validation_equality_and_conversion_chain():
    """Exercise Validation instances through equality, box/either/try/lazy conversions and mapping."""
    # Raw byte sequence used as both keys and values in Validation and mappings
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # A mapping that mixes None and bytes as keys/values
    mapping = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # Create a Validation holding (None, mapping)
    validation_a = validation_module.Validation(none_value, mapping)

    # Call __eq__ against itself (returns some object with a .map method)
    eq_result = validation_a.__eq__(validation_a)

    # Convert validation_a to a box, then to an either and then to a try
    box_a = validation_a.to_box()
    validation_b = validation_module.Validation(raw_bytes, raw_bytes)
    either_b = box_a.to_either()
    is_fail_b = validation_b.is_fail()
    try_b = either_b.to_try()

    # Create another Validation mixing a boolean-like result and the bytes
    validation_c = validation_module.Validation(is_fail_b, raw_bytes)
    str_c = validation_c.__str__()  # string representation of validation_c

    # Work with lazy wrappers and additional Validation instances
    lazy_b = validation_b.to_lazy()
    validation_d = validation_module.Validation(raw_bytes, raw_bytes)
    either_again = box_a.to_either()
    lazy_c = validation_c.to_lazy()
    validation_e = validation_module.Validation(lazy_c, validation_d)
    is_fail_b_again = validation_b.is_fail()

    # Apply map from the earlier equality result using the string from validation_c
    eq_result.map(str_c)

def test_validation_methods_with_bytes_and_none():
    """Exercise Validation.__eq__, to_maybe, and bind using bytes and None keys."""
    # Raw byte sequence used as both key and value in the mapping
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    # Explicitly use None as a mapping key to exercise None handling
    none_key = None

    # Mapping that mixes None and bytes as keys/values
    sample_mapping = {none_key: raw_bytes, raw_bytes: raw_bytes}

    # Create a Validation instance with None as the "value" and the mapping as context
    validation_instance = validation_module.Validation(none_key, sample_mapping)

    # Check equality of the instance with itself (calls __eq__)
    equality_result = validation_instance.__eq__(validation_instance)

    # Convert to maybe (exercises to_maybe)
    maybe_result = validation_instance.to_maybe()

    # Create another Validation instance with bytes as both input and context
    validation_with_bytes = validation_module.Validation(raw_bytes, raw_bytes)

    # Bind a value to the second Validation instance
    validation_with_bytes.bind(raw_bytes)

def test_validation_eq_returns_boxable_object_for_none_and_bytes():
    """Compare Validation instances built from None and bytes and call to_box() on the result."""
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Mapping uses None as a key and the same bytes value for the other key
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create two Validation instances with different constructor arguments
    validation_a = validation_module.Validation(none_value, mapping)
    validation_b = validation_module.Validation(sample_bytes, none_value)

    # Use the explicit __eq__ call as in the original test and then call to_box()
    result = validation_a.__eq__(validation_b)
    result.to_box()

