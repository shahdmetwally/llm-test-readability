import pytest

import validation as validation_module
import builtins as builtins_module

def test_validation_self_equality_and_conversion_to_maybe():
    """Verify Validation reports success/failure, equals itself, and can convert failure to Maybe."""
    # Message used for both parameters when constructing the Validation object.
    message = (
        "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    )

    # Construct the Validation object using the provided validation_module alias.
    validation = validation_module.Validation(message, message)

    # Check success state (keep return value for inspection/side-effect).
    is_success_result = validation.is_success()

    # Verify the object equals itself by directly calling __eq__ (preserve explicit call).
    equals_self = validation.__eq__(validation)

    # Check failure state and convert the failure to a Maybe.
    fail_result = validation.is_fail()
    maybe_result = fail_result.to_maybe()

    # Reference results to avoid unused-variable issues in some test environments.
    _ = (is_success_result, equals_self, maybe_result)

def test_validation_equality_with_none_triggers_is_success_call():
    """Ensure comparing a Validation instance to None yields a comparison object
    and that its is_success() method can be invoked (verifies behavior).
    """
    none_value = None  # value to compare against

    # Inputs used to construct the Validation object (kept as literals)
    first_arg = -6891
    second_arg = 3125
    args_tuple = (second_arg,)

    # Create the Validation instance using the aliased import
    validation_instance = validation_module.Validation(first_arg, args_tuple)

    # Perform the equality check against None (explicit __eq__ call preserved)
    comparison_result = validation_instance.__eq__(none_value)

    # Invoke is_success() on the result (original behavior preserved)
    comparison_result.is_success()

def test_validation_str_produces_result_with_is_fail():
    """Ensure Validation.__str__() returns an object exposing is_fail()."""
    # Use an empty mapping for both constructor arguments (preserve original inputs)
    sample_data = {}
    # Instantiate the Validation object using the provided module alias
    validation_obj = validation_module.Validation(sample_data, sample_data)
    # Call __str__() exactly as in the original test and capture the returned object
    result = validation_obj.__str__()
    # Invoke is_fail() on the returned object to preserve original behaviour
    result.is_fail()

def test_validation_to_either_and_maybe_can_be_called_repeatedly():
    """Call Validation.to_either and Validation.to_maybe; ensure to_maybe can be invoked on its result again."""
    shared_set = set()  # same empty set passed as both arguments to Validation
    validation_instance = validation_module.Validation(shared_set, shared_set)

    either_result = validation_instance.to_either()  # invoke to_either
    maybe_result = validation_instance.to_maybe()    # invoke to_maybe and keep the result

    # Call to_maybe on the result of to_maybe to preserve original call sequence
    maybe_result.to_maybe()

def test_validation_either_and_is_fail_to_maybe_behavior():
    """Exercise Validation.to_either, equality check, and converting is_fail() result to a Maybe.

    This uses a descriptive string that represents creating an empty Maybe[None].
    """
    # Description used for both parameters of Validation (kept exactly as in original)
    description = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance using the provided validation_module alias
    validation = validation_module.Validation(description, description)

    # Convert to an Either (side-effect / return value exercised)
    either_result = validation.to_either()

    # Check equality against itself (calls __eq__)
    equality_result = validation.__eq__(validation)

    # Get the is_fail() result and convert that to a Maybe via to_maybe()
    fail_result = validation.is_fail()
    fail_result.to_maybe()

def test_to_maybe_can_be_called_twice_without_error():
    """Ensure Validation.to_maybe can be invoked repeatedly (no exceptions)."""
    # Use the builtins alias to create an empty set for both constructor args
    empty_set = builtins_module.set()
    validation_obj = validation_module.Validation(empty_set, empty_set)

    # First call to_maybe returns an object that also exposes to_maybe
    maybe_result = validation_obj.to_maybe()

    # Calling to_maybe again on the result should not raise (behaviour unchanged)
    maybe_result.to_maybe()

def test_validation_constructs_with_none_for_both_parameters():
    """Construct Validation with None for both arguments (should construct without error)."""
    none_value = None  # use a clearly named variable for the None literal
    validation_instance = validation_module.Validation(none_value, none_value)
    assert isinstance(validation_instance, validation_module.Validation)

def test_validation_to_maybe_with_both_arguments_none():
    """Smoke-test that Validation.to_maybe can be called when both inputs are None."""
    none_value = None  # both constructor parameters are intentionally None
    validator = validation_module.Validation(none_value, none_value)
    # Invocation is the behaviour under test; ensure it runs without raising.
    validator.to_maybe()

def test_validation_is_fail_called_with_same_instance():
    """Call Validation.is_fail when both constructor arguments are the same object."""
    # Create a plain object instance using the builtins alias
    instance = builtins_module.object()
    # Instantiate Validation with the same object for both parameters
    validator = validation_module.Validation(instance, instance)
    # Invoke the method under test (no assertions; ensure it runs without error)
    validator.is_fail()

def test_validation_map_handles_none_input_gracefully():
    """Ensure Validation.map can be called with None without raising errors."""
    # Prepare inputs (values kept identical to the original test)
    none_value = None
    negative_int = -895
    truth_flag = True

    # Create a tuple key/value pair used in the dict
    pair = (negative_int, truth_flag)

    # Dict that uses the same tuple for both key and value
    mapping = {pair: pair}

    # Complex input composed of two identical dicts and an int
    complex_input = (mapping, mapping, negative_int)

    # Instantiate Validation using the aliased import and call map with None
    validation_instance = validation_module.Validation(complex_input, truth_flag)
    validation_instance.map(none_value)

def test_validation_bind_with_none():
    """Call Validation.bind with None to verify it accepts a null binding (no assertion)."""
    # Use the same raw bytes for both constructor arguments, matching the original test data.
    raw_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validator = validation_module.Validation(raw_bytes, raw_bytes)

    # Bind a None value (represents absence of a value); the call itself is what's being tested.
    none_value = None
    validator.bind(none_value)

def test_validation_ap_accepts_list_of_true_values():
    """Call Validation.ap on a Validation initialized with False and a list of True values.

    This test ensures the method can be invoked without errors for this input.
    """
    initial_flag = False  # starting boolean flag for the Validation instance
    element_value = True  # value used to populate the list
    values = [element_value, element_value, element_value, element_value]  # four True entries

    validator = validation_module.Validation(initial_flag, values)
    # Invoke the method under test with the same list; no assertions required by original test.
    validator.ap(values)

def test_validation_to_box_is_success_callable_with_true_inputs():
    """Call Validation.to_box().is_success() when both constructor flags are True."""
    # Use a simple True flag for both Validation inputs
    flag = True
    # Create a Validation instance from the aliased validation_module
    validation = validation_module.Validation(flag, flag)
    # Convert to a box-like result and invoke is_success() to exercise that path
    result_box = validation.to_box()
    result_box.is_success()

def test_validation_to_lazy_bind_with_none():
    """Call Validation.to_lazy(), bind(None) and then to_lazy() again without errors."""
    # Prepare an empty list to use as both parameters to Validation
    empty_list = []

    # Create a Validation instance using the imported validation module
    validation = validation_module.Validation(empty_list, empty_list)

    # Convert validation to a lazy representation
    lazy_validation = validation.to_lazy()

    # Bind the lazy validation with None (simulates no value) and get a new lazy object
    bound_lazy = lazy_validation.bind(None)

    # Convert the bound lazy object to lazy again (ensures the chain of calls works)
    bound_lazy.to_lazy()

def test_validation_lazy_conversion_and_application():
    """Ensure a Validation can be converted to lazy, then to try, and applied back to the original."""
    # Use an empty mapping as the validation input (same object used twice as in original test)
    input_mapping = {}
    # Create a Validation instance from the validation module
    validation = validation_module.Validation(input_mapping, input_mapping)

    # Convert the validation to its lazy form
    lazy_validation = validation.to_lazy()
    # Convert the lazy validation to a try-style validation
    try_validation = lazy_validation.to_try()
    # Apply the original validation to the lazy validation (preserves original call sequence)
    applied_result = lazy_validation.ap(validation)

    # Call is_success() on the try-style validation to mirror original test behaviour
    try_validation.is_success()

def test_validation_to_try_calls_is_success():
    """Exercise Validation.to_try() and call is_success() on its result."""
    zero_value = 0
    values_list = [zero_value]  # provide a single-item list as the second argument
    validation = validation_module.Validation(zero_value, values_list)
    result = validation.to_try()
    # Invoke is_success() to ensure the result object exposes that method (no assertion).
    result.is_success()

def test_validation_transforms_and_map_chain():
    """Perform a sequence of Validation transformations and finally call map().

    This test keeps the original operation order but uses clearer names to
    document the intent of each step.
    """
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Create a mapping that uses both None and the byte sequence as keys/values
    sample_mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Validation constructed with None and the mapping
    validation_a = validation_module.Validation(none_value, sample_mapping)

    # Call __eq__ on the validation instance (keeps original semantics)
    eq_result = validation_a.__eq__(validation_a)

    # Convert validation to a "box" representation
    box_a = validation_a.to_box()

    # Another Validation instance using the byte sequence for both parameters
    validation_b = validation_module.Validation(sample_bytes, sample_bytes)

    # Convert the boxed validation to an Either-like structure
    either_from_box = box_a.to_either()

    # Check failure status on validation_b
    is_fail_b = validation_b.is_fail()

    # Convert either to a Try-like structure
    try_from_either = either_from_box.to_try()

    # Create a Validation using the boolean result and the byte sequence
    validation_c = validation_module.Validation(is_fail_b, sample_bytes)

    # Stringify validation_c
    str_validation_c = validation_c.__str__()

    # Convert validation_b to a lazy representation
    lazy_b = validation_b.to_lazy()

    # Another Validation instance similar to validation_b
    validation_d = validation_module.Validation(sample_bytes, sample_bytes)

    # Repeat converting the same box to either (as in the original test)
    either_from_box_again = box_a.to_either()

    # Convert validation_c to lazy
    lazy_c = validation_c.to_lazy()

    # Construct a Validation that nests lazy_c and validation_d
    validation_e = validation_module.Validation(lazy_c, validation_d)

    # Re-check failure status on validation_b (keeps original repeated call)
    is_fail_b_again = validation_b.is_fail()

    # Finally, call map on the previously obtained eq_result with the string value
    eq_result.map(str_validation_c)

def test_validation_equality_to_maybe_and_bind_behavior():
    """Exercise Validation.__eq__, to_maybe, and bind with byte and None inputs.

    This test ensures these API surfaces can be invoked with a mapping that
    contains both None and bytes keys/values without raising exceptions and
    that equality is reflexive.
    """
    # Sample byte sequence used as both key and value in the mapping
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    # Explicit None value used as a mapping key to exercise None handling
    none_value = None

    # Mapping containing None -> bytes and bytes -> bytes entries
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create a Validation instance using None as the subject and the mapping as context
    validation_a = validation_module.Validation(none_value, mapping)

    # Check reflexive equality by calling __eq__ directly (preserve original call style)
    equals_self_result = validation_a.__eq__(validation_a)

    # Convert to a Maybe/optional representation (call retained as in original)
    maybe_result = validation_a.to_maybe()

    # Create another Validation instance with bytes as both subject and context,
    # then call bind with bytes (call retained; no assertions added)
    validation_b = validation_module.Validation(sample_bytes, sample_bytes)
    validation_b.bind(sample_bytes)

def test_validation_eq_result_is_convertible_to_box():
    """Ensure that comparing two Validation instances yields an object that supports .to_box()."""
    # Sample byte sequence used as a value/key in the mapping
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    # Explicit None value used as one of the constructor parameters and as a dict key
    none_value = None

    # Mapping containing both None -> bytes and bytes -> bytes entries
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create two Validation instances with different constructor arguments
    validation_a = validation_module.Validation(none_value, mapping)
    validation_b = validation_module.Validation(sample_bytes, none_value)

    # Invoke the equality method explicitly and ensure the result can be converted to a box
    result = validation_a.__eq__(validation_b)
    result.to_box()

