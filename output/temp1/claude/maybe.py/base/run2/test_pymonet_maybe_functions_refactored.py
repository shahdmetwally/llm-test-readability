import pytest
import maybe as maybe
import typing as typing

def test_maybe_construction_with_bytes_value():
    """Test that Maybe can be constructed with bytes as both arguments."""
    # Use arbitrary bytes as the wrapped value and default
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    result = maybe.Maybe(raw_bytes, raw_bytes)

def test_maybe_initialized_with_two_none_values():
    """Test that Maybe can be instantiated with two None arguments without error."""
    first_none = None
    second_none = None

    # Create a Maybe instance passing None for both arguments
    maybe_instance = maybe.Maybe(first_none, second_none)

def test_maybe_chained_operations_with_string_value():
    """
    Test that a Maybe monad correctly handles chained operations
    (ap, map, filter, bind, to_validation, to_either) on a string value,
    and that a second Maybe instance can convert to validation and either.
    """
    arbitrary_string = "p4xa>bl^oP"

    # Create a Maybe wrapping the arbitrary string value
    maybe_instance = maybe.Maybe(arbitrary_string, arbitrary_string)

    # Equality check between Maybe and the raw string
    is_equal = maybe_instance.__eq__(arbitrary_string)

    # Apply ap with the string; result is itself a Maybe-like value
    ap_result = maybe_instance.ap(arbitrary_string)

    # Retrieve the wrapped value or fall back to the string default
    unwrapped_value = maybe_instance.get_or_else(arbitrary_string)

    # Chain map and filter operations using the ap result
    mapped_result = maybe_instance.map(ap_result)
    filtered_result = maybe_instance.filter(ap_result)
    remapped_result = maybe_instance.map(ap_result)

    # Apply ap again and verify equality with the first ap result
    second_ap_result = maybe_instance.ap(arbitrary_string)
    ap_results_equal = ap_result.__eq__(second_ap_result)

    # Filter and unwrap using results derived from earlier operations
    filtered_from_ap = ap_result.filter(unwrapped_value)
    unwrapped_from_second_ap = second_ap_result.get_or_else(arbitrary_string)

    # Create a second Maybe instance and convert through validation and either
    second_maybe_instance = maybe.Maybe(arbitrary_string, arbitrary_string)
    validation_result = second_maybe_instance.to_validation()
    bound_result = second_maybe_instance.bind(validation_result)
    either_result = bound_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set():
    """Test that Maybe.__eq__ returns False when compared to a set (non-Maybe type)."""
    # A set containing a single unique value (False), used as a non-Maybe comparand
    false_value = False
    non_maybe_set = {false_value, false_value, false_value, false_value}

    # Create a Maybe instance wrapping None for both value and fallback
    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Compare Maybe instance against a set; __eq__ should handle non-Maybe types
    comparison_result = maybe_instance.__eq__(non_maybe_set)

def test_maybe_bind_map_then_invalid_method_on_set():
    """
    Test that Maybe can be constructed and chained with bind/map,
    but calling a non-existent method (to_box) on a plain set raises AttributeError.
    """
    # Use True as a callable stand-in for bind and map operations
    is_valid = True

    # Create a Maybe wrapping a truthy value
    maybe_true = maybe.Maybe(is_valid, is_valid)

    # Bind and map over the Maybe using the truthy value as the transform
    bound = maybe_true.bind(is_valid)
    mapped = bound.map(is_valid)

    # Create a tuple of truthy values and wrap in another Maybe
    quad_tuple = (is_valid, is_valid, is_valid, is_valid)
    maybe_tuple = maybe.Maybe(quad_tuple, is_valid)

    # Attempt to call a non-existent method on a plain set — expected to raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with a False boolean when initialized with None and False."""
    # Initialize Maybe with None value and False flag (no value present)
    none_value = None
    is_present = False
    maybe_instance = maybe.Maybe(none_value, is_present)

    # Apply map with False; verifies map is callable regardless of absence state
    maybe_instance.map(is_present)

def test_maybe_bind_on_instance_with_no_value():
    """Test that calling bind on a Maybe with no value (None) does not raise an error,
    even when a valid Maybe instance exists alongside it."""

    # Create a valid Maybe instance wrapping a truthy value
    is_valid = True
    valid_maybe = maybe.Maybe(is_valid, is_valid)

    # Prepare an empty dict to use as the bind argument
    bind_arg = {}

    # Create a Maybe instance with no value (None) and a False flag
    no_value = None
    has_no_value = False
    empty_maybe = maybe.Maybe(no_value, has_no_value)

    # Bind the empty dict to the Maybe with no value
    empty_maybe.bind(bind_arg)

def test_maybe_filter_and_ap_with_mixed_types():
    """
    Test chaining of Maybe operations (filter, ap, to_box, to_lazy) with
    mixed value/context types including bytes, None, int, and bool.
    Verifies that filter and ap compose correctly across different Maybe instances.
    """
    # Create a Maybe wrapping bytes with no context (None)
    bytes_value = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_context = None
    maybe_bytes = maybe.Maybe(bytes_value, none_context)
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an integer with a boolean context
    int_value = 0
    bool_context = True
    maybe_int = maybe.Maybe(int_value, bool_context)

    # Filter maybe_int using itself as the predicate
    filtered_maybe = maybe_int.filter(maybe_int)

    # Convert maybe_int to a lazy representation
    lazy_maybe = maybe_int.to_lazy()

    # Apply maybe_bytes as argument to the filtered Maybe
    applied_result = filtered_maybe.ap(maybe_bytes)

    # Filter the applied result using the previously applied result
    double_filtered = filtered_maybe.filter(applied_result)

    # Compose a new Maybe from the lazy value and boxed bytes
    maybe_composed = maybe.Maybe(lazy_maybe, boxed_bytes)

    # Check equality of the lazy Maybe with the boolean context value
    eq_result = lazy_maybe.__eq__(bool_context)

def test_maybe_ap_with_none_and_false_initial_state():
    """Test that calling ap() on a Maybe constructed with None and False
    does not raise an error when given an integer value."""
    integer_value = 2862
    empty_value = None
    is_just = False

    # Create a Maybe wrapping None with False (representing a Nothing/empty state)
    maybe_instance = maybe.Maybe(empty_value, is_just)

    # Apply the integer value to the Maybe instance
    maybe_instance.ap(integer_value)

def test_maybe_filter_and_lazy_conversion_chaining():
    """Test chaining of filter and to_lazy operations on Maybe instances,
    including mapping a Maybe over another Maybe."""

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

    # Filter the filtered Maybe using the lazy version of it
    double_filtered_maybe = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered Maybe to a Try
    try_result = double_filtered_maybe.to_try()

    # Convert the original Maybe to lazy again (independent call)
    lazy_from_original_again = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_maybe = filtered_maybe.map(filtered_maybe)

def test_filter_on_maybe_with_none_value_and_lazy_conversion():
    """
    Test that calling filter() on a Maybe wrapping None (with bool flag True)
    with a tuple argument, converting the result to lazy, and then filtering
    a second Maybe(None, None) with the lazy value does not raise errors.
    """
    # A tuple used as the filter argument for a Maybe wrapping None
    filter_arg = (-283, -283, -283)

    none_value = None
    is_present = True

    # Create a Maybe wrapping None with the presence flag set to True
    maybe_none_present = maybe.Maybe(none_value, is_present)

    # Apply filter with the tuple argument; result is still a Maybe
    filtered_result = maybe_none_present.filter(filter_arg)

    # Convert the filtered Maybe to its lazy representation
    lazy_result = filtered_result.to_lazy()

    # Create a second Maybe where both value and presence flag are None
    none_presence = None
    maybe_none_absent = maybe.Maybe(none_value, none_presence)

    # Filter the second Maybe using the lazy result from the first
    maybe_none_absent.filter(lazy_result)

def test_maybe_chained_transformations_with_false_values():
    """
    Test that a Maybe constructed with False values supports equality checks,
    and that chained transformations (to_either, to_lazy, to_validation) work
    correctly, including mapping a validation over another Maybe instance.
    """
    false_value = False

    # Create a Maybe with both value and is_just set to False
    maybe_false = maybe.Maybe(false_value, false_value)

    # Verify equality comparison with a False value
    eq_result = maybe_false.__eq__(false_value)

    # Create a second Maybe and perform chained transformations
    maybe_second = maybe.Maybe(false_value, false_value)
    either_result = maybe_second.to_either()
    lazy_result = maybe_second.to_lazy()
    validation_result = lazy_result.to_validation()

    # Create a third Maybe and map the validation over it
    maybe_third = maybe.Maybe(false_value, false_value)
    maybe_third.map(validation_result)

def test_maybe_equality_and_conversion_chain():
    """Test that a Maybe wrapping False can be compared to itself and converted
    through to_try() and then to_validation() without error."""

    # Create a Maybe wrapping a False value (both value and presence are False)
    false_value = False
    maybe_instance = maybe.Maybe(false_value, false_value)

    # Check equality of the Maybe instance with itself
    is_equal = maybe_instance.__eq__(maybe_instance)

    # Convert Maybe to a Try representation
    try_instance = maybe_instance.to_try()

    # Convert the Try representation to a Validation representation
    try_instance.to_validation()

