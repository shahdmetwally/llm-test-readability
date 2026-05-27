import pytest

import validation as validation_module
import builtins as builtins_module

def test_validation_empty_maybe_behavior():
    """Exercise Validation created with an 'empty maybe' description.

    Confirms is_success, equality with itself, is_fail, and that the fail result
    can be converted to a Maybe via to_maybe().
    """
    description = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_obj = validation_module.Validation(description, description)

    # Check success state (call for side-effects/inspection)
    is_success_result = validation_obj.is_success()

    # Check equality against itself
    equals_self = validation_obj.__eq__(validation_obj)

    # Check failure state and convert to Maybe
    is_fail_result = validation_obj.is_fail()
    is_fail_result.to_maybe()

def test_validation_eq_with_none_is_successful():
    """Ensure Validation.__eq__(None) returns an object that supports is_success()."""
    negative_value = -6891  # original input integer
    allowed_values = (3125,)  # tuple of allowed/expected values

    validation_instance = validation_module.Validation(negative_value, allowed_values)

    comparison_result = validation_instance.__eq__(None)
    # Verify that the returned object exposes an is_success() method (no exception should be raised).
    comparison_result.is_success()

def test_validation_str_reports_failure():
    """Create a Validation with empty inputs, get its string result and check failure."""
    # Use an empty mapping for both Validation parameters (preserves original input values)
    empty_mapping = {}
    # Construct the Validation instance via the imported validation_module alias
    validation = validation_module.Validation(empty_mapping, empty_mapping)
    # Call __str__() exactly as in the original test to obtain the result object/value
    result = validation.__str__()
    # Call is_fail() on the result to preserve original behavior and side effects
    result.is_fail()

def test_validation_converts_to_either_and_maybe_and_allows_repeated_to_maybe_calls():
    """Create a Validation and exercise its conversion methods: to_either and to_maybe.
    Also ensure calling to_maybe on the result of to_maybe is exercised (no-op or supported).
    """
    # Use the same empty set for both parameters (matches the original test input)
    empty_set = set()
    validation = validation_module.Validation(empty_set, empty_set)

    # Obtain an Either representation from the validation
    either_result = validation.to_either()

    # Obtain a Maybe representation from the validation
    maybe_result = validation.to_maybe()

    # Call to_maybe again on the Maybe result (preserves original call sequence)
    maybe_result.to_maybe()

def test_validation_to_either_and_fail_converts_to_maybe():
    """Ensure a Validation can be converted to an Either and a failing Validation to a Maybe."""
    description = (
        "Create empty maybe.\n\n"
        ":returns: Maybe[None]\n"
    )

    # Create a Validation instance using the same description for both params
    validation = validation_module.Validation(description, description)

    # Produce an Either representation from the Validation
    either_result = validation.to_either()
    assert either_result is not None

    # Explicitly compare the Validation to itself via __eq__
    assert validation.__eq__(validation) is True

    # Check if it's a failure-like result and convert that failure to a Maybe
    fail_result = validation.is_fail()
    # Ensure the failure-like result exposes a to_maybe method
    assert hasattr(fail_result, "to_maybe") and callable(fail_result.to_maybe)

    # Converting to Maybe should succeed and be repeatable
    maybe_first = fail_result.to_maybe()
    maybe_second = fail_result.to_maybe()
    assert maybe_first is not None
    assert maybe_second is not None

def test_validation_to_maybe_returns_object_with_to_maybe():
    """Calling to_maybe() on a Validation created from two identical sets
    yields an object on which to_maybe() can be called again."""
    # Prepare an empty set and use it for both Validation arguments
    empty_set = set()

    # Create the Validation instance using the aliased import
    validator = validation_module.Validation(empty_set, empty_set)

    # First conversion to a "maybe" value
    maybe_value = validator.to_maybe()

    # Ensure the resulting object also exposes to_maybe() (call only, no assertion)
    maybe_value.to_maybe()

def test_validation_initializes_with_none_arguments():
    """Ensure Validation can be constructed when both inputs are None."""
    first_input = None  # simulate a missing/undefined first parameter
    second_input = None  # simulate a missing/undefined second parameter

    # Instantiating the Validation class using the aliased module import.
    validation_instance = validation_module.Validation(first_input, second_input)

def test_validation_to_maybe_handles_none_inputs():
    """Ensure Validation.to_maybe() can be invoked when the Validation is constructed with None values."""
    none_value = None
    validator = validation_module.Validation(none_value, none_value)
    # Invoke to_maybe() to ensure it runs (test relies on no exception being raised)
    validator.to_maybe()

def test_validation_is_fail_called_for_same_object_pair():
    """Call is_fail() on a Validation initialized with the same object twice."""
    # Create a simple object instance via the imported builtins alias
    sample_obj = builtins_module.object()
    # Construct the Validation using the imported validation alias
    validation = validation_module.Validation(sample_obj, sample_obj)
    # Invoke the failure check (preserve original call and behavior)
    validation.is_fail()

def test_validation_map_handles_none_with_nested_structures():
    """Call Validation.map(None) when the Validation was created with nested tuple/dict data."""
    none_value = None
    negative_number = -895
    truth_flag = True

    # A tuple combining the integer and boolean, used as both key and value in the dict
    pair = (negative_number, truth_flag)
    mapping = {pair: pair}

    # The Validation is constructed with a tuple containing the dict twice and the integer
    constructor_args = (mapping, mapping, negative_number)

    validator = validation_module.Validation(constructor_args, truth_flag)
    # Invoke .map with None to verify the call succeeds (no assertions in this test)
    validator.map(none_value)

def test_validation_bind_allows_none_target():
    """Verify that Validation.bind can be called with a None target without error."""
    # Prepare a bytes payload used for both constructor parameters.
    payload = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Create a Validation instance using the payload for both arguments.
    validator = validation_module.Validation(payload, payload)

    # Bind a None target to the validator (should run without raising).
    none_target = None
    validator.bind(none_target)

def test_validation_ap_with_false_initial_and_all_true_list():
    """Call Validation.ap when the Validation is initialized with False and a list of True values."""
    # initial boolean provided to the Validation constructor
    initial_flag = False
    # the list passed to both the constructor and the .ap() call: four True values
    true_list = [True, True, True, True]

    # Create the Validation instance using the imported alias
    validator = validation_module.Validation(initial_flag, true_list)

    # Invoke the .ap() method with the same list (preserve original call/behavior)
    validator.ap(true_list)

def test_validation_to_box_invokes_is_success_with_true_flags():
    """Ensure Validation.to_box().is_success() is exercised when initialized with True flags."""
    # Use the same boolean inputs as the original test
    flag = True

    # Create a Validation instance using the aliased import
    validation_obj = validation_module.Validation(flag, flag)

    # Convert to a box and call is_success() (no assertion in original test)
    result_box = validation_obj.to_box()
    result_box.is_success()

def test_validation_to_lazy_bind_with_none_roundtrips():
    """Ensure a Validation can be converted to lazy, bound with None, and converted again without error."""
    # Inputs: a None value and an empty list used for both Validation parameters
    none_value = None
    empty_list = []

    # Create the Validation instance (both args intentionally the same empty list)
    validator = validation_module.Validation(empty_list, empty_list)

    # Convert the validator to a lazy representation
    lazy_validator = validator.to_lazy()

    # Bind None into the lazy validator
    bound_lazy = lazy_validator.bind(none_value)

    # Convert the bound result to lazy again to ensure round-trip conversion works
    bound_lazy.to_lazy()

def test_validation_lazy_to_try_and_apply():
    """Exercise Validation.to_lazy(), .to_try(), .ap(...) and .is_success() calls."""
    # Use a single empty dict as both parameters (preserve original inputs)
    input_map = {}

    # Create a Validation instance from the validation module
    validation_instance = validation_module.Validation(input_map, input_map)

    # Convert to lazy validation (deferred evaluation)
    lazy_validation = validation_instance.to_lazy()

    # Convert the lazy validation to a 'try' variant
    try_validation = lazy_validation.to_try()

    # Apply the original validation to the lazy validation (preserve original call)
    applied_validation = lazy_validation.ap(validation_instance)

    # Invoke is_success() on the try-version (no assertion, just exercise the method)
    try_validation.is_success()

def test_validation_to_try_invokes_is_success_for_zero_and_list():
    """Exercise Validation.to_try() followed by is_success() for a zero value in a single-item list."""
    value = 0
    values = [value]  # single-element list containing the value
    validation = validation_module.Validation(value, values)  # construct the Validation instance
    result = validation.to_try()  # obtain the try-like result object
    result.is_success()  # call is_success() to ensure it runs without error

def test_validation_various_conversions_and_mapping():
    """Exercise several Validation conversions and a final map call to ensure no regressions.

    This test creates Validation objects with the same byte sequences and None, then
    performs a series of conversions (to_box, to_either, to_try, to_lazy) and stringification,
    finally calling map(...) on the result of an equality check. The sequence and values
    are preserved exactly to keep behaviour identical.
    """
    # Raw inputs (kept as literals from the original test)
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # A dictionary keyed by None and by the bytes, values are the bytes (same as original)
    sample_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Validation constructed with None and the dict
    validation_none_dict = validation_module.Validation(none_value, sample_dict)

    # Call __eq__ explicitly and store the result (kept as a direct call)
    eq_result = validation_none_dict.__eq__(validation_none_dict)

    # Convert the validation to a box
    boxed = validation_none_dict.to_box()

    # Another Validation using bytes for both parameters
    validation_bytes = validation_module.Validation(sample_bytes, sample_bytes)

    # Convert boxed to either
    either_from_box = boxed.to_either()

    # Check is_fail on the bytes-based validation
    is_fail_flag = validation_bytes.is_fail()

    # Convert either to try
    try_from_either = either_from_box.to_try()

    # Create a Validation from the is_fail flag and bytes
    validation_flag_bytes = validation_module.Validation(is_fail_flag, sample_bytes)

    # Stringify that validation (result will be passed to map at the end)
    validation_flag_bytes_str = validation_flag_bytes.__str__()

    # Convert the bytes-based validation to lazy
    lazy_from_bytes = validation_bytes.to_lazy()

    # Create another Validation with the same bytes inputs
    validation_bytes_2 = validation_module.Validation(sample_bytes, sample_bytes)

    # Repeat converting boxed to either (matches original call order)
    either_again = boxed.to_either()

    # Convert the flag/bytes validation to lazy
    lazy_from_flag_bytes = validation_flag_bytes.to_lazy()

    # Combine lazy result and another validation into a new Validation
    combined_validation = validation_module.Validation(lazy_from_flag_bytes, validation_bytes_2)

    # Call is_fail again on the bytes-based validation (preserve original call)
    is_fail_again = validation_bytes.is_fail()

    # Finally, call map on the result of the equality check with the stringified validation
    eq_result.map(validation_flag_bytes_str)

def test_validation_equality_to_maybe_and_bind_with_bytes_and_none():
    """Exercise Validation equality, to_maybe and bind using byte payload and None key."""
    # Sample binary data used as both key and value in the payload
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    # Explicit None value to use as a dict key
    none_value = None

    # Create a dict where None maps to the bytes and the bytes map to themselves
    payload = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Instantiate a Validation with None key and the payload
    first_validation = validation_module.Validation(none_value, payload)

    # Check equality method against itself (side-effect: ensure __eq__ can be called)
    equality_result = first_validation.__eq__(first_validation)

    # Convert the validation to a Maybe-like representation (ensure method can be called)
    maybe_result = first_validation.to_maybe()

    # Instantiate another Validation using the bytes for both parameters and bind with bytes
    second_validation = validation_module.Validation(sample_bytes, sample_bytes)
    second_validation.bind(sample_bytes)

def test_validation_eq_and_to_box_with_none_and_bytes():
    """Verify that Validation.__eq__ and the resulting object's to_box() can be called
    when instances are constructed using None and a specific bytes payload.
    """
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Construct a payload mapping with None and the bytes value as keys
    payload = {none_value: raw_bytes, raw_bytes: raw_bytes}

    # Instantiate two Validation objects with different argument orders
    validation_left = validation_module.Validation(none_value, payload)
    validation_right = validation_module.Validation(raw_bytes, none_value)

    # Call the equality method explicitly and then invoke to_box() on the result
    equality_result = validation_left.__eq__(validation_right)
    equality_result.to_box()

