import pytest

import maybe as maybe_module
import typing as typing_module

def test_maybe_initialization_with_byte_sequences():
    """Construct a Maybe with two identical byte sequences to ensure initialization succeeds."""
    # Two identical byte sequences used as inputs
    byte_sequence = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Create a Maybe instance using the maybe_module alias
    maybe_instance = maybe_module.Maybe(byte_sequence, byte_sequence)

def test_initialize_maybe_with_two_none_values():
    """Smoke test: constructing a Maybe with both arguments as None should succeed."""
    # Represent the absent values explicitly
    none_value = None
    # Construct the Maybe object using the provided module alias
    maybe_instance = maybe_module.Maybe(none_value, none_value)

def test_maybe_sequence_operations_preserve_behavior():
    """Exercise a sequence of Maybe operations to ensure chaining and conversions work as expected."""
    # Sample input value used throughout the sequence
    sample_value = "p4xa>bl^oP"

    # Create a Maybe instance with the sample value (passed twice as in the original test)
    maybe_instance = maybe_module.Maybe(sample_value, sample_value)

    # Check equality against the raw string (calls __eq__ explicitly as in the original)
    equals_to_string = maybe_instance.__eq__(sample_value)

    # Apply the sample_value (first ap)
    applied = maybe_instance.ap(sample_value)

    # Retrieve a fallback/default value using get_or_else
    fallback = maybe_instance.get_or_else(sample_value)

    # Map using the previously obtained 'applied' result (first map)
    mapped_first = maybe_instance.map(applied)

    # Filter the maybe_instance using 'applied' as predicate/value (first filter)
    filtered_first = maybe_instance.filter(applied)

    # Another map using the same 'applied' value (second map, same as before)
    mapped_second = maybe_instance.map(applied)

    # Apply again to get a second applied result
    applied_second = maybe_instance.ap(sample_value)

    # Compare the two applied results for equality
    applied_equals = applied.__eq__(applied_second)

    # Filter the first applied result using the previously retrieved fallback
    filtered_on_applied = applied.filter(fallback)

    # Get the default from the second applied result
    applied_second_default = applied_second.get_or_else(sample_value)

    # Create a second Maybe instance and convert it to a validation
    maybe_second = maybe_module.Maybe(sample_value, sample_value)
    validation = maybe_second.to_validation()

    # Bind the maybe_second with the validation and convert the result to an Either
    bound_result = maybe_second.bind(validation)
    either_result = bound_result.to_either()

def test_maybe_eq_with_set_of_duplicates():
    """Ensure Maybe.__eq__ can be invoked with a set that was built from duplicate values."""
    flag = False
    # Build a set from repeated identical entries (results in a single-element set).
    duplicate_flags_set = {flag, flag, flag, flag}
    none_value = None
    maybe_obj = maybe_module.Maybe(none_value, none_value)
    # Explicitly call the __eq__ method with the set (preserve original call form).
    equality_result = maybe_obj.__eq__(duplicate_flags_set)

def test_maybe_bind_map_and_set_boxing_behavior():
    """Exercise Maybe.bind/map chaining and calling to_box() on an empty set."""
    # Use a simple boolean flag for all truthy inputs in this scenario.
    flag = True

    # Construct a Maybe instance with two boolean arguments.
    first_maybe = maybe_module.Maybe(flag, flag)

    # Call bind with the same boolean value (preserve original call semantics).
    bound_result = first_maybe.bind(flag)

    # Then call map on the result of bind (preserve original call semantics).
    mapped_result = bound_result.map(flag)

    # Create a 4-tuple of the same boolean value and wrap it in another Maybe.
    quad_tuple = (flag, flag, flag, flag)
    second_maybe = maybe_module.Maybe(quad_tuple, flag)

    # Create an empty set and invoke its to_box() method (preserve original call).
    empty_set = set()
    empty_set.to_box()

def test_maybe_map_called_with_false_on_none():
    """Call Maybe.map on a Maybe created from None and False (verifies it runs)."""
    none_value = None
    false_value = False

    # Construct a Maybe from None and False using the aliased module
    maybe_obj = maybe_module.Maybe(none_value, false_value)

    # Invoke map with the boolean value (no assertions expected; just ensure call succeeds)
    maybe_obj.map(false_value)

def test_maybe_bind_with_none_and_empty_dict():
    """Ensure Maybe.bind can be invoked on a Maybe built with None and a boolean, using an empty dict."""
    # Mirror original setup: a Maybe with two True values (not used further)
    maybe_true_pair = maybe_module.Maybe(True, True)

    # Empty mapping to pass to bind
    empty_dict = {}

    # Maybe with None as the first value and False as the second
    maybe_with_none = maybe_module.Maybe(None, False)

    # Invoke bind with the empty dictionary (preserve original test behavior: no assertions)
    maybe_with_none.bind(empty_dict)

def test_maybe_interactions_to_box_filter_lazy_ap_and_eq():
    """Exercise Maybe: to_box, filter, to_lazy, ap, and equality check without assertions.

    This reproduces the original sequence of operations to ensure the same behavior:
    1. Create a Maybe from raw bytes and None, then box it.
    2. Create a Maybe from an int and True, then call filter with itself.
    3. Convert that Maybe to a lazy form.
    4. Apply the filtered Maybe to the bytes-Maybe, then filter again.
    5. Construct another Maybe from the lazy value and the boxed bytes.
    6. Call __eq__ on the lazy value against the original boolean.
    """
    # raw inputs
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_val = None

    # Maybe from bytes; then boxed representation
    maybe_bytes = maybe_module.Maybe(raw_bytes, none_val)
    boxed_bytes = maybe_bytes.to_box()

    # Maybe from an int and a boolean flag
    zero_int = 0
    true_flag = True
    maybe_int = maybe_module.Maybe(zero_int, true_flag)

    # filter called with the Maybe instance itself (preserve original call order/arguments)
    maybe_filtered_self = maybe_int.filter(maybe_int)

    # lazy version of the integer Maybe
    maybe_lazy = maybe_int.to_lazy()

    # apply filtered Maybe to the bytes-Maybe, then filter that result with itself
    maybe_applied = maybe_filtered_self.ap(maybe_bytes)
    maybe_filtered_applied = maybe_filtered_self.filter(maybe_applied)

    # construct another Maybe from the lazy value and the boxed bytes
    combined_maybe = maybe_module.Maybe(maybe_lazy, boxed_bytes)

    # equality check invoked (no assertion; kept to preserve original side effects/calls)
    maybe_lazy_eq_true = maybe_lazy.__eq__(true_flag)

def test_maybe_ap_with_none_initial_value_and_flag_false():
    """Ensure Maybe.ap can be invoked when the Maybe is initialized with None and the flag is False."""
    input_value = 2862
    initial_value = None
    flag_disabled = False

    # Construct the Maybe instance using the aliased module import.
    maybe_obj = maybe_module.Maybe(initial_value, flag_disabled)

    # Invoke ap with the input value; preserve the original call and execution order.
    maybe_obj.ap(input_value)

def test_maybe_filter_with_tuple_then_lazy_used_by_another_maybe():
    """Exercise Maybe.filter with a tuple, convert the result to lazy,
    and pass that lazy result into another Maybe.filter call.
    This ensures the sequence of operations runs without changing behaviour.
    """
    # A negative integer value used three times in a tuple
    negative_value = -283
    triple_values = (negative_value, negative_value, negative_value)

    # A Maybe constructed with None and True, then filtered by the tuple
    none_value = None
    flag = True
    first_maybe = maybe_module.Maybe(none_value, flag)
    filtered_maybe = first_maybe.filter(triple_values)

    # Convert the filtered result to a lazy representation
    lazy_filtered = filtered_maybe.to_lazy()

    # Another Maybe constructed with two Nones, then filtered by the lazy result
    none_value2 = None
    second_maybe = maybe_module.Maybe(none_value2, none_value2)
    second_maybe.filter(lazy_filtered)

def test_maybe_filter_converts_extracted_tuple_and_applies_filter_to_generic():
    """Exercise Maybe: extract a value, box it, create another Maybe and call filter."""
    # Setup literal inputs (kept exactly as in original test)
    fallback_value = 2281
    sample_str = "gZ(\\mOcN"
    sample_dict = {sample_str: sample_str}
    # Tuple contains two identical strings and two identical dicts (preserve order/contents)
    sample_tuple = (sample_str, sample_str, sample_dict, sample_dict)

    # Create a Maybe that is present (True) wrapping the tuple
    is_present = True
    maybe_tuple = maybe_module.Maybe(sample_tuple, is_present)

    # Extract a value from the Maybe, providing an integer fallback
    extracted_value = maybe_tuple.get_or_else(fallback_value)

    # Create an instance of Generic from the second module (kept as in original)
    generic_instance = typing_module.Generic()

    # Convert the original maybe to a boxed representation
    not_present = False
    boxed_value = maybe_tuple.to_box()

    # Create another Maybe around the generic instance (marked not present)
    maybe_generic = maybe_module.Maybe(generic_instance, not_present)

    # Call filter on the second Maybe with the previously extracted value
    maybe_generic.filter(extracted_value)

def test_maybe_bind_and_conversion_methods():
    """Exercise Maybe conversions and bind without asserting — ensure methods run without error."""
    # Create a Maybe wrapping a boolean value with an explicit None "missing" value
    is_present = True
    absent_marker = None
    maybe_bool = maybe_module.Maybe(is_present, absent_marker)
    validation_from_bool = maybe_bool.to_validation()

    # Prepare numeric values and an empty tuple used as the "missing" value for the next Maybe
    float_val = -286.64
    int_val = -1784
    empty_tuple = ()

    # Create a Maybe wrapping an int and exercise its conversion methods
    maybe_int = maybe_module.Maybe(int_val, empty_tuple)
    validation_from_int = maybe_int.to_validation()
    int_or_else = maybe_int.get_or_else(int_val)
    try_from_int = maybe_int.to_try()

    # Create another Maybe for a float value (both value and missing marker are the same float)
    maybe_float = maybe_module.Maybe(float_val, float_val)

    # Bind the int Maybe with the result of to_try() (keeps original call sequence / semantics)
    maybe_int.bind(try_from_int)

def test_maybe_map_and_to_either_behaviour():
    """Exercise Maybe.map with a None payload and Maybe.to_either with an int payload."""
    # Create a Maybe containing None with a truthy flag
    payload_none = None
    truthy_flag = True
    maybe_none = maybe_module.Maybe(payload_none, truthy_flag)

    # Map a set containing the same flag over the Maybe (call and values preserved)
    flag_set = {truthy_flag}
    mapped_result = maybe_none.map(flag_set)

    # Create another Maybe from an integer and convert it to an Either
    payload_int = -1095
    another_flag = True
    maybe_int = maybe_module.Maybe(payload_int, another_flag)
    either_result = maybe_int.to_either()

def test_maybe_conversion_sequence_with_none_and_tuple():
    """Exercise a sequence of Maybe conversions (to_lazy, to_either, to_try)
    using a Maybe built from None values and another built from a tuple and False.
    The test ensures the conversion methods are invoked in a specific order.
    """
    # Use explicit None values for the first Maybe
    none_value = None
    first_maybe = maybe_module.Maybe(none_value, none_value)

    # Put the first Maybe into a single-element tuple and call to_lazy on it
    single_tuple = (first_maybe,)
    lazy_first = first_maybe.to_lazy()

    # Create a second Maybe from the tuple and a False flag
    false_flag = False
    second_maybe = maybe_module.Maybe(single_tuple, false_flag)

    # Invoke several conversion methods in the original order to preserve behavior
    either_first_a = first_maybe.to_either()
    try_second = second_maybe.to_try()
    either_first_b = first_maybe.to_either()
    either_second = second_maybe.to_either()

    # Finally, call to_lazy on the result of second_maybe.to_try()
    try_second.to_lazy()

def test_maybe_converts_to_try_and_boxes():
    """Verify that a Maybe can be converted to a Try and then boxed."""
    # Set up boolean flags (preserve original literal values)
    is_present = True
    is_absent = False

    # Create a Maybe instance using the aliased import (maybe_module)
    maybe_value = maybe_module.Maybe(is_present, is_absent)

    # Convert the Maybe to a Try-like object, then call to_box() on the result
    try_value = maybe_value.to_try()
    try_value.to_box()

def test_maybe_conversion_chain_and_equality():
    """Exercise a chain of Maybe conversions and related helpers without asserting.

    This covers: construction, ap, lazy conversion, validation conversion,
    filtering, fallback via get_or_else, either conversion, try conversion,
    equality check, boxing, and invoking ap on the try result.
    """
    # Input values (kept identical to the original test)
    raw_bytes = b"C\xcf\xe7/"
    empty_value = None
    truthy_flag = True

    # Construct a Maybe instance with the provided None and boolean flag
    base_maybe = maybe_module.Maybe(empty_value, truthy_flag)

    # Apply the Maybe with None (preserve original call order/semantics)
    applied_maybe = base_maybe.ap(empty_value)

    # Convert the result to lazy, then to a validation
    lazy_version = applied_maybe.to_lazy()
    validation_version = lazy_version.to_validation()

    # Filter the original Maybe using the validation result
    filtered_maybe = base_maybe.filter(validation_version)

    # Use get_or_else with the filtered result itself as the fallback
    fallback_result = filtered_maybe.get_or_else(filtered_maybe)

    # Convert filtered result to Either and validation to Try
    either_result = filtered_maybe.to_either()
    try_result = validation_version.to_try()

    # Equality check between filtered and the previously applied Maybe
    equality_check = filtered_maybe.__eq__(applied_maybe)

    # Box the fallback result
    boxed_result = fallback_result.to_box()

    # Finally, call ap on the Try result with the original bytes
    try_result.ap(raw_bytes)

def test_maybe_chain_operations_ap_bind_and_conversion():
    """Exercise Maybe ap/bind and conversions to Validation/Either/Try using bytes and None."""
    # Sample inputs (kept identical to the original test data)
    sample_bytes = b"\xdbC\xcf\xe7/"  # original bytes_0
    none_value = None
    true_flag = True

    # Create a Maybe with (None, True) and apply values in sequence
    maybe_none_true = maybe_module.Maybe(none_value, true_flag)
    applied_once = maybe_none_true.ap(none_value)
    applied_twice = applied_once.ap(sample_bytes)

    # Convert the result to a Validation
    validation_from_applied = applied_twice.to_validation()

    # Create another Maybe with (None, bytes) and exercise various conversions and binds
    maybe_none_bytes = maybe_module.Maybe(none_value, sample_bytes)
    got_or_else = maybe_none_bytes.get_or_else(maybe_none_bytes)  # default is the maybe itself
    validation_b = maybe_none_bytes.to_validation()
    bound_b = maybe_none_bytes.bind(validation_b)
    either_b = maybe_none_bytes.to_either()
    applied_self = maybe_none_bytes.ap(maybe_none_bytes)

    # Work with integers and equality checks (preserve exact values and calls)
    int_negative = -3289
    eq_either_validation = either_b.__eq__(validation_b)
    bound_either = either_b.bind(maybe_none_bytes)
    try_b = maybe_none_bytes.to_try()
    eq_maybe_bound = maybe_none_bytes.__eq__(bound_b)
    validation_from_bound = bound_b.to_validation()

    # Final call as in the original test
    try_b.ap(int_negative)

def test_maybe_equality_and_transforms():
    """Verify Maybe equality method and chained conversions (to_either, to_lazy, to_validation)."""
    # Use an explicit boolean flag for clarity (same as the original False literal).
    flag = False

    # Create a Maybe and call its equality dunder method with the same flag.
    maybe_a = maybe_module.Maybe(flag, flag)
    eq_result = maybe_a.__eq__(flag)  # result intentionally unused, we only exercise the call

    # Create another Maybe and convert it through several representations.
    maybe_b = maybe_module.Maybe(flag, flag)
    either_val = maybe_b.to_either()
    lazy_val = maybe_b.to_lazy()
    validation_val = lazy_val.to_validation()

    # Create a third Maybe and map it using the obtained validation value.
    maybe_c = maybe_module.Maybe(flag, flag)
    maybe_c.map(validation_val)

def test_maybe_eq_and_conversion_chain():
    """Verify Maybe equality and that its to_try() result can be converted to validation."""
    # Arrange: create a Maybe with both parameters set to False
    false_flag = False
    maybe_value = maybe_module.Maybe(false_flag, false_flag)

    # Act & Assert: equality with itself should be True
    assert maybe_value == maybe_value

    # Convert the Maybe to a Try-like object, then convert that to a Validation-like object.
    try_result = maybe_value.to_try()
    # Ensure conversion to validation succeeds (does not raise) and returns a non-None result
    validation_result = try_result.to_validation()
    assert validation_result is not None

