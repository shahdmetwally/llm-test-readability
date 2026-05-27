import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes():
    """Test that Maybe can be instantiated with bytes as both arguments."""
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    maybe_instance = maybe.Maybe(raw_bytes, raw_bytes)

def test_maybe_initialized_with_none_values():
    """Test that Maybe can be instantiated with None for both arguments."""
    # Both the value and the fallback are explicitly None
    value = None
    fallback = None

    maybe_instance = maybe.Maybe(value, fallback)

def test_maybe_chained_operations_with_string_value():
    """
    Test that a Maybe monad correctly supports chained operations (ap, map, filter,
    bind, to_validation, to_either) when constructed with a string value, and that
    equality checks between derived Maybe instances behave as expected.
    """
    input_str = "p4xa>bl^oP"

    # Construct a Maybe with a string value
    maybe_instance = maybe.Maybe(input_str, input_str)

    # Check equality of the Maybe instance against a plain string
    eq_result = maybe_instance.__eq__(input_str)

    # Apply ap, get_or_else, map, and filter on the original Maybe
    ap_result = maybe_instance.ap(input_str)
    get_or_else_result = maybe_instance.get_or_else(input_str)
    map_result_1 = maybe_instance.map(eq_result)
    filter_result_1 = maybe_instance.filter(eq_result)
    map_result_2 = maybe_instance.map(eq_result)

    # Apply a second ap and compare it against the first ap result
    ap_result_2 = maybe_instance.ap(input_str)
    eq_ap_results = ap_result.__eq__(ap_result_2)

    # Chain filter and get_or_else on the derived ap results
    filter_of_ap = ap_result.filter(get_or_else_result)
    get_or_else_of_ap2 = ap_result_2.get_or_else(input_str)

    # Construct a second Maybe and exercise bind -> to_validation -> to_either
    maybe_instance_2 = maybe.Maybe(input_str, input_str)
    validation_result = maybe_instance_2.to_validation()
    bound_result = maybe_instance_2.bind(validation_result)
    either_result = bound_result.to_either()

def test_maybe_eq_returns_false_when_comparing_with_set():
    """Test that Maybe.__eq__ returns False when compared against a set (non-Maybe value)."""

    # A set containing a single unique value (False), used as a non-Maybe comparand
    false_value = False
    non_maybe_set = {false_value, false_value, false_value, false_value}

    # Create a Maybe instance with both value and fallback as None
    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance against the set; expected to return False (or NotImplemented)
    result = maybe_instance.__eq__(non_maybe_set)

def test_maybe_bind_map_then_invalid_method_on_set():
    """
    Tests that:
    - Maybe can be constructed with a bool value and bound/mapped successfully.
    - Maybe can be constructed with a tuple value.
    - Calling a non-existent method (to_box) on a plain set raises an AttributeError.
    """
    # Use True as a simple truthy value for Maybe construction
    value = True

    # Create a Maybe wrapping a bool and bind/map it
    maybe_bool = maybe.Maybe(value, value)
    bound = maybe_bool.bind(value)
    mapped = bound.map(value)

    # Create a Maybe wrapping a tuple of bools
    tuple_value = (value, value, value, value)
    maybe_tuple = maybe.Maybe(tuple_value, value)

    # Attempt to call a non-existent method on a plain set,
    # which should raise an AttributeError
    with pytest.raises(AttributeError):
        empty_set = set()
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with a False bool when initialized with None and False."""
    # Create a Maybe instance wrapping a None value with strict mode disabled
    none_value = None
    is_strict = False
    maybe_instance = maybe.Maybe(none_value, is_strict)

    # Attempt to map over the Maybe with False; should not raise
    maybe_instance.map(is_strict)

def test_maybe_bind_with_empty_dict_on_none_value_maybe():
    """Test that calling bind with an empty dict on a Maybe wrapping None does not raise."""

    # Create a Maybe instance wrapping a truthy value
    true_value = True
    maybe_with_true = maybe.Maybe(true_value, true_value)

    # Prepare an empty dict to use as the bind argument
    empty_dict = {}
    none_value = None
    false_value = False

    # Create a Maybe instance wrapping None (no value present)
    maybe_with_none = maybe.Maybe(none_value, false_value)

    # Bind the empty dict to the Maybe that holds no value
    maybe_with_none.bind(empty_dict)

def test_maybe_filter_and_ap_chaining_with_mixed_types():
    """
    Test chaining of filter and ap operations on Maybe instances
    constructed with mixed types (bytes/None and int/bool),
    verifying that lazy conversion and equality checks behave correctly.
    """
    # Create a Maybe wrapping bytes with no fallback
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_fallback = None
    maybe_bytes = maybe.Maybe(raw_bytes, no_fallback)
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an integer with a bool fallback
    int_value = 0
    bool_fallback = True
    maybe_int = maybe.Maybe(int_value, bool_fallback)

    # Apply filter using maybe_int as the predicate (self-filter)
    filtered_int = maybe_int.filter(maybe_int)

    # Convert maybe_int to a lazy representation
    lazy_int = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes Maybe
    applied = filtered_int.ap(maybe_bytes)

    # Filter the already-filtered result using the applied value
    double_filtered = filtered_int.filter(applied)

    # Create a Maybe wrapping the lazy value and the boxed bytes
    maybe_lazy = maybe.Maybe(lazy_int, boxed_bytes)

    # Check equality of the lazy value against the bool fallback
    is_equal_to_bool = lazy_int.__eq__(bool_fallback)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling `ap` on a Maybe wrapping None (with flag=False) with an integer does not raise unexpectedly."""
    int_value = 2862
    none_value = None
    is_valid = False

    # Create a Maybe instance wrapping None with the validity flag set to False
    maybe_instance = maybe.Maybe(none_value, is_valid)

    # Apply the integer value to the Maybe instance
    maybe_instance.ap(int_value)

def test_maybe_filter_and_lazy_map_chaining():
    """Test chaining of filter, to_lazy, and map operations on Maybe instances
    starting from a truthy Maybe wrapping zero."""

    # Create a Maybe wrapping 0 with a truthy flag
    int_value = 0
    is_present = True
    maybe_value = maybe.Maybe(int_value, is_present)

    # Filter the original Maybe using itself as the predicate
    filtered_maybe = maybe_value.filter(maybe_value)

    # Convert the original Maybe to a lazy representation
    lazy_from_maybe = maybe_value.to_lazy()

    # Convert the filtered Maybe to a lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the already-filtered Maybe using the lazy version
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered result to a Try
    try_result = double_filtered.to_try()

    # Convert the original Maybe to lazy again (independent call)
    lazy_from_maybe_again = maybe_value.to_lazy()

    # Map over the filtered Maybe using itself as the mapping function
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_filter_empty_maybe_with_lazy_converted_result():
    """
    Test that filtering a Maybe wrapping None (with truthy flag) using a tuple value,
    converting the result to lazy, and then filtering a second empty Maybe with the
    lazy value does not raise errors and completes without side effects.
    """
    # Construct a tuple to use as the filter argument
    negative_int = -283
    filter_arg = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with a truthy flag, then filter with the tuple
    maybe_with_none_truthy = maybe.Maybe(None, True)
    filtered_result = maybe_with_none_truthy.filter(filter_arg)

    # Convert the filtered result to a lazy representation
    lazy_result = filtered_result.to_lazy()

    # Create a second fully-empty Maybe (None value, None flag)
    empty_maybe = maybe.Maybe(None, None)

    # Filter the empty Maybe using the lazy result
    empty_maybe.filter(lazy_result)

def test_maybe_get_or_else_and_filter_with_generic():
    """
    Test that Maybe.get_or_else returns the contained value when present,
    and that Maybe.filter can be called on a Maybe wrapping a Generic object.
    Also verifies that to_box() can be called on a Maybe instance.
    """
    # A fallback integer used as the default value for get_or_else
    fallback_int = 2281

    # A raw string value used to populate the tuple payload
    raw_str = "gZ(\\mOcN"
    str_dict = {raw_str: raw_str}
    payload_tuple = (raw_str, raw_str, str_dict, str_dict)

    # Create a Maybe with a present value (bool True indicates value is present)
    is_present = True
    maybe_with_value = maybe.Maybe(payload_tuple, is_present)

    # get_or_else should return the contained value since it is present
    resolved_value = maybe_with_value.get_or_else(fallback_int)

    # Create a Generic instance to wrap in a second Maybe
    generic_instance = typing.Generic()

    # Create a Maybe wrapping the Generic with no value present
    is_absent = False
    maybe_with_generic = maybe.Maybe(generic_instance, is_absent)

    # Convert the first Maybe to a box representation
    boxed = maybe_with_value.to_box()

    # Apply filter using the resolved value on the Maybe wrapping Generic
    maybe_with_generic.filter(resolved_value)

def test_maybe_to_validation_and_bind_with_various_types():
    """
    Test that Maybe instances can be converted to Validation and Try,
    and that bind can be called with a Try result across different value types
    (bool/None, int/empty-tuple, float/float).
    """
    # Create a Maybe with a truthy value and no fallback
    bool_value = True
    none_value = None
    maybe_bool = maybe.Maybe(bool_value, none_value)
    validation_from_bool = maybe_bool.to_validation()

    # Set up additional values for further Maybe instances
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()

    # Create a Maybe with an int value and an empty tuple as fallback
    maybe_int = maybe.Maybe(int_value, empty_tuple)
    validation_from_int = maybe_int.to_validation()

    # Retrieve the value or fall back to int_value
    value_or_else = maybe_int.get_or_else(int_value)

    # Convert the int Maybe to a Try
    try_from_int = maybe_int.to_try()

    # Create a Maybe with float values (value and fallback both floats)
    maybe_float = maybe.Maybe(float_value, float_value)

    # Bind the Try result back into the int Maybe
    maybe_int.bind(try_from_int)

def test_maybe_map_with_none_value_and_maybe_to_either_with_int():
    """
    Test that Maybe.map() can be called with a non-callable (set) when wrapping None,
    and that Maybe.to_either() works correctly when wrapping a negative integer.
    """
    # Create a Maybe wrapping None with has_value=True
    none_value = None
    has_value = True
    maybe_none = maybe.Maybe(none_value, has_value)

    # Attempt to map over the Maybe using a set (non-callable mapper)
    mapper_set = {has_value}
    result_map = maybe_none.map(mapper_set)

    # Create a Maybe wrapping a negative integer with has_value=True
    negative_int = -1095
    has_value_2 = True
    maybe_int = maybe.Maybe(negative_int, has_value_2)

    # Convert the Maybe wrapping a negative integer to an Either
    result_either = maybe_int.to_either()

def test_maybe_chained_conversions_with_none_and_nested_maybe():
    """
    Test that Maybe instances constructed with None and nested values
    can be converted to lazy, either, and try representations without errors.
    Exercises chained conversions across two Maybe instances.
    """
    # Create a Maybe with both value and context set to None
    none_value = None
    maybe_none = maybe.Maybe(none_value, none_value)

    # Wrap the None-based Maybe in a tuple to use as a value in a second Maybe
    tuple_with_maybe = (maybe_none,)

    # Convert the None-based Maybe to a lazy representation
    lazy_from_none_maybe = maybe_none.to_lazy()

    bool_false = False

    # Create a second Maybe using the tuple and False
    maybe_with_tuple = maybe.Maybe(tuple_with_maybe, bool_false)

    # Convert the None-based Maybe to an either representation
    either_from_none_maybe = maybe_none.to_either()

    # Convert the tuple-based Maybe to a try representation
    try_from_tuple_maybe = maybe_with_tuple.to_try()

    # Convert the None-based Maybe to either again
    either_from_none_maybe_again = maybe_none.to_either()

    # Convert the tuple-based Maybe to an either representation
    either_from_tuple_maybe = maybe_with_tuple.to_either()

    # Convert the try result from the tuple-based Maybe to a lazy representation
    try_from_tuple_maybe.to_lazy()
# (Truncated by extractor)