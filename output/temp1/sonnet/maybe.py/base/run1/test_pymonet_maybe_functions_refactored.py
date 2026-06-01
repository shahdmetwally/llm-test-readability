import pytest
import maybe as maybe
import typing as typing

def test_maybe_constructed_with_bytes_arguments():
    """Test that Maybe can be constructed with identical byte sequences as both arguments."""
    # Use a raw byte sequence as both the value and the second argument
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    maybe_instance = maybe.Maybe(raw_bytes, raw_bytes)

def test_maybe_instantiation_with_none_values():
    """Test that Maybe can be instantiated with None as both arguments."""
    # Both value and fallback are None, verifying Maybe accepts None inputs
    value = None
    fallback = None
    maybe_instance = maybe.Maybe(value, fallback)

def test_maybe_chained_operations_with_string_value():
    """
    Test that a Maybe monad constructed with a string value supports chained
    operations (ap, get_or_else, map, filter, bind, to_validation, to_either)
    without altering the wrapped value or raising errors.
    """
    input_str = "p4xa>bl^oP"

    # Create a Maybe instance wrapping the string value
    maybe_instance = maybe.Maybe(input_str, input_str)

    # Equality check between Maybe and the raw string
    eq_result = maybe_instance.__eq__(input_str)

    # Apply ap, get_or_else, map, and filter on the primary Maybe
    ap_result = maybe_instance.ap(input_str)
    fallback_value = maybe_instance.get_or_else(input_str)
    map_result_1 = maybe_instance.map(ap_result)
    filter_result_1 = maybe_instance.filter(ap_result)
    map_result_2 = maybe_instance.map(ap_result)

    # A second ap call to verify consistency of repeated ap invocations
    ap_result_2 = maybe_instance.ap(input_str)

    # Compare the two ap results for equality
    ap_eq = ap_result.__eq__(ap_result_2)

    # Chain filter and get_or_else on the ap results
    filtered_ap = ap_result.filter(fallback_value)
    ap_fallback = ap_result_2.get_or_else(input_str)

    # Create a second independent Maybe instance with the same value
    maybe_instance_2 = maybe.Maybe(input_str, input_str)

    # Convert to validation and then bind, followed by conversion to Either
    validation = maybe_instance_2.to_validation()
    bound_result = maybe_instance_2.bind(validation)
    either_result = bound_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set():
    """Test that Maybe.__eq__ returns False when compared to a set (non-Maybe type)."""
    # A set is not a valid Maybe value, so equality should not hold
    false_value = False
    non_maybe_set = {false_value, false_value, false_value, false_value}

    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Comparing a Maybe instance to a set should yield a non-equal result
    result = maybe_instance.__eq__(non_maybe_set)

def test_maybe_bind_and_map_then_invalid_set_operation():
    """
    Test that Maybe can be constructed and chained with bind/map,
    but calling .to_box() on a plain set raises an AttributeError,
    since set has no such method.
    """
    # Use True as a stand-in value for Maybe construction and chaining
    true_value = True

    # Create a Maybe wrapping a truthy value
    maybe_true = maybe.Maybe(true_value, true_value)

    # Bind the Maybe with the truthy value
    bound_result = maybe_true.bind(true_value)

    # Map over the bound result
    mapped_result = bound_result.map(true_value)

    # Create a tuple of truthy values to use as a compound Maybe input
    tuple_of_trues = (true_value, true_value, true_value, true_value)

    # Construct a second Maybe using the tuple and a truthy flag
    maybe_tuple = maybe.Maybe(tuple_of_trues, true_value)

    # Attempt to call .to_box() on a plain set — this is not a valid set method
    # and is expected to raise an AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with a False mapper on a Maybe wrapping None."""
    # Create a Maybe instance wrapping None with strict mode disabled
    none_value = None
    strict_mode = False
    maybe_instance = maybe.Maybe(none_value, strict_mode)

    # Invoke map with False as the mapping function (exercises the map code path)
    maybe_instance.map(strict_mode)

def test_maybe_bind_with_empty_dict_on_none_value_maybe():
    """Test that calling bind with an empty dict on a Maybe wrapping None does not raise."""

    # Create a Maybe instance wrapping a truthy value
    is_valid = True
    maybe_truthy = maybe.Maybe(is_valid, is_valid)

    # Prepare an empty dict to use as the bind argument
    empty_dict = {}
    none_value = None
    is_false = False

    # Create a Maybe instance wrapping None with a False flag
    maybe_none = maybe.Maybe(none_value, is_false)

    # Bind the empty dict to the Maybe wrapping None
    maybe_none.bind(empty_dict)

def test_maybe_filter_and_ap_chaining_with_mixed_types():
    """
    Test chaining of Maybe operations (filter, ap, to_box, to_lazy) across
    instances constructed with mixed types (bytes/None and int/bool).
    Verifies that applying filter and ap across Maybe instances does not raise
    errors and that equality comparison on a lazy value behaves as expected.
    """
    # Create a Maybe wrapping bytes with no fallback (None)
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_fallback = None
    maybe_bytes = maybe.Maybe(raw_bytes, no_fallback)
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an integer with a bool fallback
    int_value = 0
    bool_fallback = True
    maybe_int = maybe.Maybe(int_value, bool_fallback)

    # Filter maybe_int using itself as the predicate, then convert to lazy
    filtered_maybe = maybe_int.filter(maybe_int)
    lazy_maybe = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes-based Maybe
    applied_result = filtered_maybe.ap(maybe_bytes)

    # Filter the applied result using the original filtered Maybe
    double_filtered = filtered_maybe.filter(applied_result)

    # Construct a new Maybe from the lazy value and the boxed bytes
    maybe_from_lazy = maybe.Maybe(lazy_maybe, boxed_bytes)

    # Check equality of the lazy value against the bool fallback
    lazy_eq_bool = lazy_maybe.__eq__(bool_fallback)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() on a Maybe wrapping None (with False flag) with an integer does not raise unexpectedly."""
    integer_value = 2862
    wrapped_value = None
    is_some = False

    # Construct a Maybe that wraps None with the 'is_some' flag set to False
    maybe_instance = maybe.Maybe(wrapped_value, is_some)

    # Apply the integer value to the Maybe instance
    maybe_instance.ap(integer_value)

def test_maybe_filter_and_lazy_conversion_chaining():
    """Test chaining filter and to_lazy conversions on Maybe instances,
    including mapping over a filtered Maybe value."""

    # Create a Maybe wrapping integer 0 with a truthy flag
    initial_value = 0
    is_present = True
    maybe_instance = maybe.Maybe(initial_value, is_present)

    # Filter the Maybe using itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the original Maybe to a lazy representation
    lazy_from_original = maybe_instance.to_lazy()

    # Convert the filtered Maybe to a lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the already-filtered Maybe using the lazy version of it
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered Maybe to a Try
    try_result = double_filtered.to_try()

    # Convert the original Maybe to lazy again (independent call)
    lazy_from_original_again = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_with_tuple_on_none_value_then_filter_lazy():
    """Test that filtering a Maybe wrapping None with a tuple value produces a
    lazy result, and that filtering a second None-wrapped Maybe with that lazy
    result completes without error."""

    # A tuple of repeated negative integers used as the filter argument
    negative_int = -283
    filter_arg = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with strict=True, then apply the tuple filter
    none_value = None
    strict_flag = True
    maybe_with_none = maybe.Maybe(none_value, strict_flag)
    filtered_result = maybe_with_none.filter(filter_arg)

    # Convert the filtered result to a lazy representation
    lazy_result = filtered_result.to_lazy()

    # Create a second Maybe wrapping None (no strict flag) and filter with the lazy result
    second_none_value = None
    maybe_plain_none = maybe.Maybe(second_none_value, second_none_value)
    maybe_plain_none.filter(lazy_result)

def test_maybe_get_or_else_and_filter_with_nested_structures():
    """
    Test Maybe behaviour when constructed with a tuple containing mixed types
    (strings and dicts), verifying that get_or_else returns a fallback value,
    to_box wraps the result, and filter operates on a second Maybe wrapping a
    Generic object with a falsy presence flag.
    """
    fallback_int = 2281
    key_str = "gZ(\\mOcN"

    # Build a nested tuple containing repeated strings and dicts
    nested_dict = {key_str: key_str}
    nested_tuple = (key_str, key_str, nested_dict, nested_dict)

    # Create a Maybe with the nested tuple and a truthy presence flag
    is_present = True
    maybe_with_tuple = maybe.Maybe(nested_tuple, is_present)

    # Retrieve the value or fall back to the integer default
    value_or_fallback = maybe_with_tuple.get_or_else(fallback_int)

    # Create a Generic instance to use as a value in a second Maybe
    generic_value = typing.Generic()

    # Wrap the tuple Maybe in a box
    boxed_value = maybe_with_tuple.to_box()

    # Create a second Maybe with the Generic value and a falsy presence flag
    is_absent = False
    maybe_with_generic = maybe.Maybe(generic_value, is_absent)

    # Apply filter using the previously retrieved value
    maybe_with_generic.filter(value_or_fallback)

def test_maybe_to_validation_and_auxiliary_operations():
    """
    Test that Maybe instances with various value/error combinations
    support chained operations: to_validation(), get_or_else(), to_try(), and bind().
    Covers both a truthy-value Maybe and an integer-value Maybe with an empty-tuple error.
    """
    # Create a Maybe with a truthy value and no error
    is_valid = True
    no_error = None
    maybe_valid = maybe.Maybe(is_valid, no_error)

    # Convert to Validation; result is not directly asserted but exercises the method
    validation_from_valid = maybe_valid.to_validation()

    # Create a Maybe with a negative integer value and an empty-tuple error
    negative_int_value = -1784
    empty_tuple_error = ()
    maybe_int = maybe.Maybe(negative_int_value, empty_tuple_error)

    # Exercise to_validation, get_or_else, and to_try on the integer Maybe
    validation_from_int = maybe_int.to_validation()
    fallback_value = maybe_int.get_or_else(negative_int_value)
    try_result = maybe_int.to_try()

    # Create a Maybe with a float value and a float error (used as bind argument)
    float_value = -286.64
    maybe_float = maybe.Maybe(float_value, float_value)

    # Bind the try_result into the integer Maybe
    maybe_int.bind(try_result)

def test_maybe_map_with_none_value_and_to_either_with_int_value():
    """
    Test that Maybe.map() can be called with a set when the wrapped value is None,
    and that Maybe.to_either() can be called when the wrapped value is a negative integer.
    Both operations are performed with has_value=True.
    """
    # Create a Maybe wrapping None with has_value=True, then map over it with a set
    none_value = None
    has_value_true = True
    maybe_with_none = maybe.Maybe(none_value, has_value_true)
    mapped_set = {has_value_true}
    map_result = maybe_with_none.map(mapped_set)

    # Create a Maybe wrapping a negative integer with has_value=True, then convert to Either
    negative_int = -1095
    has_value_true_1 = True
    maybe_with_int = maybe.Maybe(negative_int, has_value_true_1)
    either_result = maybe_with_int.to_either()

def test_maybe_conversions_with_none_and_tuple_values():
    """
    Test chained conversions (to_lazy, to_either, to_try) on Maybe instances
    constructed with None values and a tuple containing another Maybe.
    Verifies that conversion methods can be called without error across
    different Maybe configurations, including None-initialized and tuple-initialized variants.
    """
    # Create a Maybe with both value and context set to None
    none_value = None
    maybe_none = maybe.Maybe(none_value, none_value)

    # Use the None-based Maybe as a tuple element for a second Maybe
    tuple_with_maybe = (maybe_none,)
    bool_false = False
    maybe_tuple = maybe.Maybe(tuple_with_maybe, bool_false)

    # Convert the None-based Maybe to its lazy representation
    lazy_from_none_maybe = maybe_none.to_lazy()

    # Convert the None-based Maybe to Either
    either_from_none_maybe = maybe_none.to_either()

    # Convert the tuple-based Maybe to Try
    try_from_tuple_maybe = maybe_tuple.to_try()

    # Convert the None-based Maybe to Either again (second call)
    either_from_none_maybe_again = maybe_none.to_either()

    # Convert the tuple-based Maybe to Either
    either_from_tuple_maybe = maybe_tuple.to_either()

    # Convert the Try result (from tuple-based Maybe) to its lazy representation
    try_from_tuple_maybe.to_lazy()

def test_maybe_to_try_to_box_chaining_with_true_false():
    """Test that a Maybe constructed with (True, False) can be chained through to_try() and to_box() without error."""
    has_value = True
    is_nothing = False

    # Create a Maybe instance with a truthy value and a falsy flag
    maybe_instance = maybe.Maybe(has_value, is_nothing)

    # Convert Maybe to a Try, then wrap the result in a Box
    try_instance = maybe_instance.to_try()
    try_instance.to_box()

def test_maybe_none_value_chained_transformations():
    """
    Test that a Maybe wrapping None can be chained through ap, to_lazy,
    to_validation, filter, get_or_else, to_either, to_try, and to_box
    without raising errors, preserving None-handling semantics throughout.
    """
    raw_bytes = b"C\xcf\xe7/"
    none_value = None
    include_none = True

    # Create a Maybe that explicitly holds None with permissive flag
    maybe_none = maybe.Maybe(none_value, include_none)

    # Apply None as a function via ap — should propagate the empty/None state
    maybe_after_ap = maybe_none.ap(none_value)

    # Convert to a Lazy representation
    lazy_value = maybe_after_ap.to_lazy()

    # Convert the Lazy to a Validation
    validation_value = lazy_value.to_validation()

    # Filter the original Maybe using the Validation as predicate
    maybe_filtered = maybe_none.filter(validation_value)

    # Unwrap with a fallback of itself (get_or_else with self as default)
    fallback_result = maybe_filtered.get_or_else(maybe_filtered)

    # Convert the filtered Maybe to an Either
    either_value = maybe_filtered.to_either()

    # Convert the Validation to a Try
    try_value = validation_value.to_try()

    # Check equality between filtered Maybe and the ap result
    are_equal = maybe_filtered.__eq__(maybe_after_ap)

    # Convert the fallback result to a Box
    box_value = fallback_result.to_box()

    # Apply raw bytes to the Try — exercises ap on a Try with a non-callable
    try_value.ap(raw_bytes)

def test_maybe_chained_operations_with_none_and_bytes():
    """
    Tests chained Maybe monad operations using None and bytes values,
    verifying ap, bind, to_validation, to_either, to_try, and equality
    behave correctly across multiple Maybe instances.
    """
    raw_bytes = b"\xdbC\xcf\xe7/"
    nothing = None
    is_just = True

    # Create a Maybe wrapping None (Just True internally)
    maybe_with_none = maybe.Maybe(nothing, is_just)

    # Chain ap calls: apply None then bytes to the Maybe
    applied_none = maybe_with_none.ap(nothing)
    applied_bytes = applied_none.ap(raw_bytes)

    # Convert the chained result to a Validation
    validation_from_chained = applied_bytes.to_validation()

    # Create a second Maybe wrapping bytes
    maybe_with_bytes = maybe.Maybe(nothing, raw_bytes)

    # Retrieve the value or fall back to itself
    value_or_self = maybe_with_bytes.get_or_else(maybe_with_bytes)

    # Convert to Validation and use it as a bind function
    validation_from_bytes_maybe = maybe_with_bytes.to_validation()
    bound_result = maybe_with_bytes.bind(validation_from_bytes_maybe)

    # Convert to Either and apply further operations
    either_from_maybe = maybe_with_bytes.to_either()
    applied_maybe_to_self = maybe_with_bytes.ap(maybe_with_bytes)

    negative_int = -3289

    # Check equality between Either and the Validation
    either_equals_validation = either_from_maybe.__eq__(validation_from_bytes_maybe)

    # Bind the Either with the bytes Maybe
    either_bound = either_from_maybe.bind(maybe_with_bytes)

    # Convert to Try and check equality of the bound result with the original Maybe
    try_from_maybe = maybe_with_bytes.to_try()
    maybe_equals_bound = maybe_with_bytes.__eq__(bound_result)

    # Convert the bound result to Validation
    validation_from_bound = bound_result.to_validation()

    # Apply a negative int to the Try instance
    try_from_maybe.ap(negative_int)

def test_maybe_chained_transformations_with_false_values():
    """Test chaining Maybe transformations (to_either, to_lazy, to_validation, map)
    using False as both the value and error, verifying equality and interop conversions."""

    # Create a Maybe with False as both value and error
    false_value = False
    maybe_instance = maybe.Maybe(false_value, false_value)

    # Verify equality comparison with a plain False
    is_equal = maybe_instance.__eq__(false_value)

    # Create a second Maybe instance for chained transformation
    maybe_for_conversion = maybe.Maybe(false_value, false_value)

    # Convert to Either and then to Lazy representations
    either_result = maybe_for_conversion.to_either()
    lazy_result = maybe_for_conversion.to_lazy()

    # Convert the lazy result to a Validation, to be used as a mapping function
    validation_result = lazy_result.to_validation()

    # Create a third Maybe and apply the validation result as a mapping function
    maybe_to_map = maybe.Maybe(false_value, false_value)
    maybe_to_map.map(validation_result)

def test_maybe_equality_and_conversion_chain():
    """Test that a Maybe wrapping False can be compared to itself and converted
    through to_try() and then to_validation() without errors."""

    # Create a Maybe wrapping False for both value and fallback
    falsy_value = False
    maybe_false = maybe.Maybe(falsy_value, falsy_value)

    # Compare the Maybe instance to itself (should reflect equality semantics)
    is_equal_to_self = maybe_false.__eq__(maybe_false)

    # Convert Maybe -> Try -> Validation, exercising the conversion chain
    as_try = maybe_false.to_try()
    as_validation = as_try.to_validation()

