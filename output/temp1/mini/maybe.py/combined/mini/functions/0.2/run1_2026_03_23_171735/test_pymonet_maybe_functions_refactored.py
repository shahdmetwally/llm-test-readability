import pytest

import maybe as maybe_module
import typing as typing_module

def test_maybe_initializes_with_two_identical_byte_sequences():
    """Smoke test: construct Maybe with two identical byte sequences; ensure no exception is raised."""
    # Prepare a sample byte sequence (unchanged literal from the original test).
    sample_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Instantiate Maybe with the same byte sequence for both parameters.
    # This mirrors the original call but uses clearer variable names and the provided alias.
    maybe_instance = maybe_module.Maybe(sample_bytes, sample_bytes)

def test_maybe_initializes_with_none_values():
    """Ensure Maybe can be constructed with two None values (sanity check of constructor)."""
    # Explicitly name the None value to clarify intent
    none_value = None

    # Construct Maybe with two None arguments (preserve original call and argument order)
    maybe_instance = maybe_module.Maybe(none_value, none_value)

def test_maybe_equality_apply_map_filter_and_conversion_chain():
    """Exercise Maybe operations: equality, ap, map, filter, get_or_else, bind, and conversions."""
    # Sample input used throughout the test
    sample_value = "p4xa>bl^oP"

    # Create a Maybe instance initialized with the sample value (both parameters identical)
    maybe_a = maybe_module.Maybe(sample_value, sample_value)

    # Equality check between the Maybe instance and the raw sample value
    equals_sample = maybe_a.__eq__(sample_value)

    # Apply the sample value to the Maybe (ap)
    applied_once = maybe_a.ap(sample_value)

    # Retrieve default via get_or_else from the Maybe
    default_from_get_or_else = maybe_a.get_or_else(sample_value)

    # Map operation using the previously obtained applied_once (preserve original call style)
    mapped_from_applied_once_1 = maybe_a.map(applied_once)

    # Filter operation using applied_once as predicate/value
    filtered_by_applied_once = maybe_a.filter(applied_once)

    # Another map call (same as above)
    mapped_from_applied_once_2 = maybe_a.map(applied_once)

    # Second ap call to the original Maybe instance
    applied_twice = maybe_a.ap(sample_value)

    # Compare applied results for equality (applied_once == applied_twice)
    applied_equality = applied_once.__eq__(applied_twice)

    # Filter called on applied_once with the default value obtained earlier
    filtered_result_from_applied_once = applied_once.filter(default_from_get_or_else)

    # get_or_else called on applied_twice
    applied_twice_default = applied_twice.get_or_else(sample_value)

    # Construct a second Maybe instance and perform conversions/bind as in original
    maybe_b = maybe_module.Maybe(sample_value, sample_value)
    validation_from_maybe_b = maybe_b.to_validation()
    bound_maybe_b = maybe_b.bind(validation_from_maybe_b)
    either_from_bound_maybe_b = bound_maybe_b.to_either()

def test_maybe_equality_with_set_of_false_and_none():
    """Call Maybe.__eq__ with a set of repeated False values and a Maybe constructed from two None values."""
    flag_value = False
    repeated_flags_set = {flag_value, flag_value, flag_value, flag_value}

    none_value = None
    maybe_instance = maybe_module.Maybe(none_value, none_value)

    equality_result = maybe_instance.__eq__(repeated_flags_set)

def test_maybe_bind_and_map_do_not_raise():
    """Ensure Maybe.bind and Maybe.map accept boolean inputs and complete without raising."""
    flag = True

    # Initialize a Maybe with the flag as both value and condition
    maybe_instance = maybe_module.Maybe(flag, flag)

    # Call bind and then map using the boolean flag (should not raise)
    bound_result = maybe_instance.bind(flag)
    mapped_result = bound_result.map(flag)

    # Create a 4-tuple of the flag and use it as the value in another Maybe
    bool_tuple = (flag, flag, flag, flag)
    maybe_with_tuple = maybe_module.Maybe(bool_tuple, flag)

    # Call to_box on a plain set to preserve original behavior (may be monkeypatched elsewhere)
    empty_set = set()
    empty_set.to_box()

def test_maybe_map_with_none_and_false_runs_without_error():
    """Create a Maybe with None and False and call map(False) to ensure it executes without raising."""
    # Represent an absent value and a boolean flag used for mapping
    absent_value = None
    flag = False

    # Construct the Maybe instance with the absent value and flag
    maybe_instance = maybe_module.Maybe(absent_value, flag)

    # Invoke map with the boolean flag; the test passes if this call does not raise
    maybe_instance.map(flag)

def test_maybe_bind_with_none_and_false_executes_bind():
    """Construct two Maybe instances and call bind on the one with (None, False) using an empty mapping."""
    true_val = True
    false_val = False
    none_val = None

    # Create an unused Maybe from two True values to mirror original behavior
    maybe_both_true = maybe_module.Maybe(true_val, true_val)

    empty_mapping = {}

    maybe_none_false = maybe_module.Maybe(none_val, false_val)
    # Should run without raising an exception
    maybe_none_false.bind(empty_mapping)

def test_maybe_chain_operations_filter_apply_compare():
    """Exercise chained Maybe operations: boxing, filtering, applying, and equality check."""
    # Input values
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_value = None

    # Construct a Maybe from bytes and None, then box it
    maybe_bytes_none = maybe_module.Maybe(raw_bytes, none_value)
    boxed_bytes = maybe_bytes_none.to_box()

    # Construct a Maybe from 0 and True
    zero_int = 0
    true_flag = True
    maybe_zero_true = maybe_module.Maybe(zero_int, true_flag)

    # Apply filter with the maybe instance itself
    filtered_maybe = maybe_zero_true.filter(maybe_zero_true)

    # Convert to lazy representation
    lazy_maybe = maybe_zero_true.to_lazy()

    # Apply the filtered Maybe to the bytes/None Maybe
    applied_result = filtered_maybe.ap(maybe_bytes_none)

    # Filter the filtered result with the applied result
    filtered_applied_result = filtered_maybe.filter(applied_result)

    # Construct a Maybe from the lazy value and the boxed bytes
    maybe_lazy_and_boxed = maybe_module.Maybe(lazy_maybe, boxed_bytes)

    # Perform equality comparison between lazy_maybe and the True flag
    comparison_result = lazy_maybe.__eq__(true_flag)

def test_maybe_ap_with_none_initial_and_false_flag_does_not_raise():
    """Ensure Maybe.ap can be called when initial value is None and flag is False (no exception raised)."""
    # Arrange: use the same literal values as the original test to preserve behavior
    value_to_apply = 2862
    initial_value = None
    flag = False

    # Create the Maybe instance (using the provided alias `maybe_module`)
    maybe_instance = maybe_module.Maybe(initial_value, flag)

    # Act: call ap with the integer value; the original test contains no assertions,
    # so success is implied by not raising an exception.
    maybe_instance.ap(value_to_apply)

def test_maybe_filter_map_lazy_and_try_interaction():
    """Exercise a Maybe instance's filter/map/to_lazy/to_try operations to ensure method chaining works without errors."""
    # Initial inputs used to create a Maybe instance
    initial_value = 0
    present_flag = True

    # Create the Maybe instance
    maybe_instance = maybe_module.Maybe(initial_value, present_flag)

    # Apply filter using the instance itself as predicate-like argument (as in original)
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert original and filtered instances to lazy representations
    lazy_from_original = maybe_instance.to_lazy()
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the already-filtered value using the lazy value produced above
    filtered_again = filtered_maybe.filter(lazy_from_filtered)

    # Convert the result of the second filter to a Try-like representation
    try_from_filtered = filtered_again.to_try()

    # Call to_lazy again on the original Maybe (redundant in original test, preserved here)
    redundant_lazy = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself (preserve original semantics and call pattern)
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_to_lazy_composition():
    """Verify composition of Maybe.filter and Maybe.to_lazy when given None and tuple inputs."""
    # Prepare a numeric value and a tuple of three identical values
    int_value = -283
    triplet = (int_value, int_value, int_value)

    # First Maybe: constructed with (None, True)
    maybe_a = maybe_module.Maybe(None, True)

    # Apply filter with the tuple, then convert result to a lazy representation
    filtered = maybe_a.filter(triplet)
    lazy_filtered = filtered.to_lazy()

    # Second Maybe: constructed with (None, None)
    maybe_b = maybe_module.Maybe(None, None)

    # Pass the lazy result into filter of the second Maybe (preserve original call)
    maybe_b.filter(lazy_filtered)

def test_maybe_filter_handles_complex_tuple_and_generic():
    """Ensure Maybe.get_or_else, Maybe.to_box, and Maybe.filter accept complex values."""
    # Prepare literals used as payloads and defaults
    default_value = 2281
    sample_string = "gZ(\\mOcN"  # exact literal preserved from original test

    # Construct a dict and a tuple that include repeated references
    sample_mapping = {sample_string: sample_string}
    sample_tuple = (sample_string, sample_string, sample_mapping, sample_mapping)

    # Create a Maybe containing the complex tuple and indicate it's present
    is_present = True
    first_maybe = maybe_module.Maybe(sample_tuple, is_present)

    # Extract a value with a fallback default (exercises get_or_else)
    extracted_value = first_maybe.get_or_else(default_value)

    # Create a Generic instance (from typing_module) to use as a different payload
    generic_instance = typing_module.Generic()

    # Convert the first maybe to a boxed representation (exercises to_box)
    is_absent = False
    boxed_value = first_maybe.to_box()

    # Create a second Maybe around the Generic instance marked as absent/present
    second_maybe = maybe_module.Maybe(generic_instance, is_absent)

    # Call filter on the second maybe with the previously extracted value
    second_maybe.filter(extracted_value)

def test_maybe_validation_get_or_else_to_try_and_bind():
    """Verify Maybe conversions to validation/try forms, get_or_else behavior, and binding between Maybe instances."""
    # Create a Maybe from a present boolean value and an absent (None) value
    present_flag = True
    absent_value = None
    maybe_from_flag = maybe_module.Maybe(present_flag, absent_value)

    # Convert the first Maybe to a validation representation
    validation_from_flag = maybe_from_flag.to_validation()

    # Prepare numeric and empty-tuple inputs used for another Maybe
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()

    # Create a Maybe from an int and an empty tuple, then exercise conversions
    maybe_from_int = maybe_module.Maybe(int_value, empty_tuple)
    validation_from_int = maybe_from_int.to_validation()

    # Extract a fallback value and convert to a try-like representation
    fallback_from_int = maybe_from_int.get_or_else(int_value)
    try_from_int = maybe_from_int.to_try()

    # Create a Maybe from two floats (value and fallback)
    maybe_from_float = maybe_module.Maybe(float_value, float_value)

    # Bind the second Maybe with the try result from the same Maybe (preserve original behaviour)
    maybe_from_int.bind(try_from_int)

def test_maybe_map_and_to_either_no_error():
    """Exercise Maybe.map with a set and Maybe.to_either with an int to ensure no exceptions."""
    # Use explicit, descriptive variable names for clarity
    none_value = None
    flag_true = True

    # Create a Maybe containing None (with a truthy flag)
    maybe_none = maybe_module.Maybe(none_value, flag_true)

    # Map the Maybe using a set containing the True flag (preserve set literal usage)
    true_set = {flag_true}
    mapped_maybe = maybe_none.map(true_set)

    # Create a second Maybe with a negative integer and convert it to an Either
    negative_int = -1095
    maybe_int = maybe_module.Maybe(negative_int, True)
    either_result = maybe_int.to_either()

def test_maybe_conversion_chain_executes_without_error():
    """Ensure Maybe conversion methods (to_lazy, to_either, to_try) can be called/chained without raising."""
    # Prepare literal None values as in the original test
    none_value = None

    # Create a Maybe instance constructed with (None, None)
    maybe_none_none = maybe_module.Maybe(none_value, none_value)

    # Put that Maybe instance into a single-element tuple (preserves original structure)
    tuple_of_maybe = (maybe_none_none,)

    # Call to_lazy() on the first Maybe (preserves original call and order)
    lazy_from_maybe0 = maybe_none_none.to_lazy()

    # Prepare a False literal as in the original test
    bool_flag_false = False

    # Create a second Maybe instance constructed with (tuple_of_maybe, False)
    maybe_tuple_false = maybe_module.Maybe(tuple_of_maybe, bool_flag_false)

    # Call to_either() on the first Maybe (first occurrence)
    either_from_maybe0 = maybe_none_none.to_either()

    # Call to_try() on the second Maybe
    try_from_maybe1 = maybe_tuple_false.to_try()

    # Call to_either() on the first Maybe again (preserves duplicate call)
    either_from_maybe0_second = maybe_none_none.to_either()

    # Call to_either() on the second Maybe
    either_from_maybe1 = maybe_tuple_false.to_either()

    # Finally call to_lazy() on the result of try_from_maybe1 (preserves the final call)
    try_from_maybe1.to_lazy()

def test_maybe_to_try_then_to_box():
    """Ensure a Maybe created with specified booleans can be converted to a Try-like object and boxed."""
    # Prepare boolean inputs exactly as in the original test
    is_true = True
    is_false = False

    # Create the Maybe instance using the provided maybe_module alias
    maybe_instance = maybe_module.Maybe(is_true, is_false)

    # Convert to a Try-like object, then call to_box() on that result.
    # The original test did not assert any return values; it simply exercised these calls.
    try_obj = maybe_instance.to_try()
    try_obj.to_box()

def test_maybe_chain_conversions_and_ap_calls():
    """Exercise a sequence of Maybe conversions and ensure methods are callable in order."""
    # Input values (unchanged)
    sample_bytes = b"C\xcf\xe7/"
    absent = None
    truthy_flag = True

    # Create initial Maybe instance
    maybe_instance = maybe_module.Maybe(absent, truthy_flag)

    # Apply an argument to the Maybe
    applied_maybe = maybe_instance.ap(absent)

    # Convert to lazy representation, then to validation
    lazy_form = applied_maybe.to_lazy()
    validation_form = lazy_form.to_validation()

    # Filter the original maybe_instance using the validation form
    filtered_maybe = maybe_instance.filter(validation_form)

    # Use get_or_else with the filtered_maybe itself (preserve original call)
    default_or_self = filtered_maybe.get_or_else(filtered_maybe)

    # Convert to other representations as in the original test
    either_form = filtered_maybe.to_either()
    try_form = validation_form.to_try()

    # Equality check retained (no assertion; just invoking __eq__ as in original)
    equality_check = filtered_maybe.__eq__(applied_maybe)

    # Convert the result of get_or_else to a box
    boxed_value = default_or_self.to_box()

    # Final call: apply bytes to the try_form (preserve the original final call)
    try_form.ap(sample_bytes)

def test_maybe_ap_bind_to_validation_to_either_to_try_interactions():
    """Exercise chained Maybe operations (ap, bind, conversions and equality) with None, bool and bytes values."""
    # Input literals (unchanged)
    sample_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    true_flag = True

    # Create a Maybe with (None, True) and apply values step-by-step
    maybe_none_true = maybe_module.Maybe(none_value, true_flag)
    applied_once = maybe_none_true.ap(none_value)         # var_0
    applied_twice = applied_once.ap(sample_bytes)         # var_1
    validation_from_applied = applied_twice.to_validation()  # var_2

    # Create a Maybe with (None, bytes) and exercise other conversions and operations
    maybe_none_bytes = maybe_module.Maybe(none_value, sample_bytes)  # maybe_1
    get_or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)  # var_3
    validation_from_maybe = maybe_none_bytes.to_validation()  # var_4
    bound_with_validation = maybe_none_bytes.bind(validation_from_maybe)  # var_5
    either_from_maybe = maybe_none_bytes.to_either()  # var_6
    ap_result_self = maybe_none_bytes.ap(maybe_none_bytes)  # var_7

    # Additional interactions preserved in original order
    negative_int = -3289
    either_eq_validation = either_from_maybe.__eq__(validation_from_maybe)  # bool_1
    either_bound_result = either_from_maybe.bind(maybe_none_bytes)  # var_8
    try_from_maybe = maybe_none_bytes.to_try()  # var_9
    maybe_eq_bound = maybe_none_bytes.__eq__(bound_with_validation)  # bool_2
    validation_from_bound = bound_with_validation.to_validation()  # var_10

    # Final call preserved
    try_from_maybe.ap(negative_int)

def test_maybe_conversion_chain_and_map():
    """Verify Maybe can be compared, converted (Either -> Lazy -> Validation), and passed to map."""
    # Use a simple boolean flag as in the original test
    false_flag = False

    # Construct first Maybe and compare it to the boolean
    maybe_instance_1 = maybe_module.Maybe(false_flag, false_flag)
    equality_result = maybe_instance_1.__eq__(false_flag)  # exercise __eq__

    # Construct second Maybe and perform conversions: to_either, to_lazy, then to_validation
    maybe_instance_2 = maybe_module.Maybe(false_flag, false_flag)
    either_value = maybe_instance_2.to_either()
    lazy_value = maybe_instance_2.to_lazy()
    validation_value = lazy_value.to_validation()

    # Construct third Maybe and call map with the Validation obtained above
    maybe_instance_3 = maybe_module.Maybe(false_flag, false_flag)
    maybe_instance_3.map(validation_value)

def test_maybe_eq_and_conversion_methods():
    """Ensure Maybe equality works and its to_try() -> to_validation() conversion chain is invocable."""
    # Create a Maybe instance with two False flags (preserve original literals)
    flag_value = False
    maybe_instance = maybe_module.Maybe(flag_value, flag_value)

    # Call equality method comparing the instance to itself (preserve original call)
    equals_result = maybe_instance.__eq__(maybe_instance)

    # Convert to a "try" representation and invoke to_validation() on the result
    try_result = maybe_instance.to_try()
    try_result.to_validation()

