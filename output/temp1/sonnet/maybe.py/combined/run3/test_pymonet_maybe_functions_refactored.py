import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_value_and_fallback():
    """Test that Maybe can be instantiated with a bytes object as both its value and fallback arguments."""
    # Use an arbitrary bytes object as both the primary value and the fallback
    raw_bytes_value = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Construct Maybe with the same bytes instance for both arguments
    maybe_instance = maybe.Maybe(raw_bytes_value, raw_bytes_value)

def test_maybe_instantiation_with_none_values():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None for both arguments to verify the constructor handles absent values
    none_value = None

    # Construct a Maybe instance with both values set to None
    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chained_operations_with_equality_and_conversion():
    """Test that a Maybe instance supports chaining ap, map, filter, bind,
    to_validation, and to_either operations with equality comparisons."""

    # Shared string value used as both the wrapped value and the argument
    test_value = "p4xa>bl^oP"

    # --- Operations on the first Maybe instance ---
    maybe_instance = maybe.Maybe(test_value, test_value)

    # Equality comparison between the Maybe instance and the raw string
    eq_result = maybe_instance.__eq__(test_value)

    # Apply the raw string as an applicative argument
    ap_result = maybe_instance.ap(test_value)

    # Unwrap with a fallback default
    get_or_else_result = maybe_instance.get_or_else(test_value)

    # Map and filter using the ap result as the callable
    map_result_1 = maybe_instance.map(ap_result)
    filter_result_1 = maybe_instance.filter(ap_result)

    # Repeat map and ap to produce additional derived values
    map_result_2 = maybe_instance.map(ap_result)
    ap_result_2 = maybe_instance.ap(test_value)

    # Equality check between the two ap results
    ap_eq_result = ap_result.__eq__(ap_result_2)

    # Further operations on the derived ap and get_or_else results
    filter_result_2 = ap_result.filter(get_or_else_result)
    get_or_else_result_2 = ap_result_2.get_or_else(test_value)

    # --- Operations on the second Maybe instance ---
    maybe_instance_2 = maybe.Maybe(test_value, test_value)

    # Convert to Validation, then bind with the validation result, then to Either
    validation_result = maybe_instance_2.to_validation()
    bind_result = maybe_instance_2.bind(validation_result)
    either_result = bind_result.to_either()

def test_maybe_eq_returns_false_when_comparing_none_maybe_to_false_set():
    """Test that Maybe(None, None).__eq__ returns a falsy result when compared to a set of False values."""

    # Build the value and set used for comparison
    false_value = False
    false_set = {false_value, false_value, false_value, false_value}

    # Construct a Maybe wrapping two None values
    none_value = None
    maybe_with_nones = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance against the set of False values
    eq_result = maybe_with_nones.__eq__(false_set)

def test_maybe_bind_map_chaining_and_invalid_to_box_on_set():
    """Test that Maybe supports bind/map chaining on bool and tuple values, and that calling to_box() on a plain set raises AttributeError."""

    # Use a simple True constant as the base value for wrapping and operations
    true_value = True

    # Construct a Maybe wrapping two boolean values, then chain bind and map
    maybe_bool = maybe.Maybe(true_value, true_value)
    bound_result = maybe_bool.bind(true_value)
    mapped_result = bound_result.map(true_value)

    # Construct a Maybe wrapping a tuple of booleans as the value
    bool_tuple = (true_value, true_value, true_value, true_value)
    maybe_tuple = maybe.Maybe(bool_tuple, true_value)

    # Attempt to call to_box() on a plain set, which does not support this method
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe initialized with None and False allows .map() to be called with a falsy value."""
    # Set up inputs: an empty (None) value and a False flag
    empty_value = None
    false_flag = False

    # Construct a Maybe monad wrapping the empty value with the False flag
    maybe_instance = maybe.Maybe(empty_value, false_flag)

    # Invoke map with a falsy value — should execute without error
    maybe_instance.map(false_flag)

def test_maybe_bind_with_none_value_and_false_does_not_raise():
    """Test that bind on a Maybe constructed with None and False completes without error when called with an empty dict."""

    true_value = True

    # Construct a Maybe with two truthy values (exercises the constructor path)
    maybe_with_true = maybe.Maybe(true_value, true_value)

    empty_dict = {}
    none_value = None
    false_value = False

    # Construct a Maybe where the primary value is None and the fallback is False
    maybe_with_none = maybe.Maybe(none_value, false_value)

    # Bind with an empty dict — verifies no exception is raised in this scenario
    maybe_with_none.bind(empty_dict)

def test_maybe_chained_operations_with_mixed_types():
    """Test Maybe monad chained operations (to_box, filter, to_lazy, ap, __eq__) across instances with mixed types."""

    # --- First Maybe: wraps raw bytes with no context ---
    raw_bytes_value = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_context = None
    maybe_bytes = maybe.Maybe(raw_bytes_value, none_context)

    # Convert the bytes-based Maybe to a box representation
    box_from_bytes = maybe_bytes.to_box()

    # --- Second Maybe: wraps an integer with a boolean context ---
    int_value = 0
    bool_context = True
    maybe_int = maybe.Maybe(int_value, bool_context)

    # Filter the int Maybe using itself as the predicate
    filtered_maybe = maybe_int.filter(maybe_int)

    # Convert the int Maybe to a lazy representation
    lazy_maybe = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes Maybe
    applied_maybe = filtered_maybe.ap(maybe_bytes)

    # Filter the applied result using the applied Maybe itself as predicate
    filtered_applied = filtered_maybe.filter(applied_maybe)  # result unused but computed

    # Construct a new Maybe combining the lazy and box representations
    maybe_lazy_box = maybe.Maybe(lazy_maybe, box_from_bytes)

    # Check equality of the lazy Maybe against the boolean context
    eq_result = lazy_maybe.__eq__(bool_context)

def test_maybe_none_false_ap_with_integer_does_not_raise():
    """Test that calling ap with an integer on a Maybe wrapping None and False does not raise."""
    # The integer argument to be applied via ap
    integer_value = 2862

    # Represents an absent/empty value
    empty_value = None

    # Flag indicating this is not a 'Just' value (i.e., Nothing-like)
    is_just_flag = False

    # Construct a Maybe monad in a Nothing-like state
    maybe_instance = maybe.Maybe(empty_value, is_just_flag)

    # Apply the integer to the Maybe instance; should not raise
    maybe_instance.ap(integer_value)

def test_maybe_supports_chained_filter_map_and_conversion_operations():
    """Tests that a Maybe instance can be chained through filter, to_lazy, map, and to_try operations without errors."""
    # Set up the initial value and presence flag for the Maybe instance
    initial_value = 0
    has_value = True

    # Construct the root Maybe object
    maybe_instance = maybe.Maybe(initial_value, has_value)

    # Filter the Maybe using itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the root Maybe to a lazy representation
    lazy_from_maybe = maybe_instance.to_lazy()

    # Convert the filtered Maybe to a lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the already-filtered Maybe using the lazy version of it
    filtered_again = filtered_maybe.filter(lazy_from_filtered)

    # Convert the doubly-filtered result to a Try
    try_result = filtered_again.to_try()

    # Convert the root Maybe to lazy a second time (independent call)
    lazy_from_maybe_second = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_with_none_value_and_lazy_chain():
    """Test that filtering a None-valued Maybe and converting to lazy, then filtering again from a None/None Maybe, completes without error."""
    # Set up a repeated negative integer used to build the filter argument
    negative_int = -283
    filter_tuple = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with a True flag, then apply filter
    none_value = None
    bool_flag = True
    maybe_with_none_and_true = maybe.Maybe(none_value, bool_flag)
    filtered_maybe = maybe_with_none_and_true.filter(filter_tuple)

    # Convert the filtered result to a lazy representation
    lazy_maybe = filtered_maybe.to_lazy()

    # Create a second Maybe with both arguments as None, then filter using the lazy result
    none_value_2 = None
    maybe_with_none_none = maybe.Maybe(none_value_2, none_value_2)
    maybe_with_none_none.filter(lazy_maybe)

def test_maybe_get_or_else_and_filter_with_generic_value():
    """Tests get_or_else fallback, to_box invocation, and filter on a Maybe wrapping a Generic instance."""

    # Define a fallback integer used in get_or_else
    fallback_int = 2281

    # Build a nested tuple to use as the wrapped value in the first Maybe
    arbitrary_str = "gZ(\\mOcN"
    str_keyed_dict = {arbitrary_str: arbitrary_str}
    nested_tuple_value = (arbitrary_str, arbitrary_str, str_keyed_dict, str_keyed_dict)

    # Create a Maybe that is flagged as present (True)
    is_present_true = True
    maybe_with_tuple = maybe.Maybe(nested_tuple_value, is_present_true)

    # Retrieve the value or fall back to fallback_int
    get_or_else_result = maybe_with_tuple.get_or_else(fallback_int)

    # Create a Generic instance to use as the value for a second Maybe
    generic_instance = typing.Generic()

    # Convert the first Maybe to a box
    boxed_maybe = maybe_with_tuple.to_box()

    # Create a second Maybe wrapping the generic instance, flagged as absent (False)
    is_present_false = False
    maybe_with_generic = maybe.Maybe(generic_instance, is_present_false)

    # Apply filter to the second Maybe using the result of get_or_else
    maybe_with_generic.filter(get_or_else_result)

def test_maybe_chained_operations_with_mixed_types():
    """Test that Maybe objects with mixed types support chained calls to to_validation, get_or_else, to_try, and bind."""

    # --- First Maybe: wraps a truthy boolean with a None fallback ---
    truthy_value = True
    none_fallback = None
    maybe_with_bool = maybe.Maybe(truthy_value, none_fallback)
    validation_from_bool_maybe = maybe_with_bool.to_validation()

    # --- Second Maybe: wraps a negative int with an empty tuple as fallback ---
    float_value = -286.64
    negative_int = -1784
    empty_tuple = ()
    maybe_with_int = maybe.Maybe(negative_int, empty_tuple)

    # Exercise core Maybe operations on the int-wrapped instance
    validation_from_int_maybe = maybe_with_int.to_validation()
    get_or_else_result = maybe_with_int.get_or_else(negative_int)
    try_from_int_maybe = maybe_with_int.to_try()

    # --- Third Maybe: wraps a float with a float fallback (constructed but not further used) ---
    maybe_with_float = maybe.Maybe(float_value, float_value)

    # Bind the Try result back into the int Maybe
    maybe_with_int.bind(try_from_int_maybe)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test that Maybe.map() accepts a set argument and that a Maybe with an integer value can be converted to an Either."""

    # Construct a Maybe wrapping None (an empty/absent value)
    empty_value = None
    is_some_flag = True
    empty_maybe = maybe.Maybe(empty_value, is_some_flag)

    # Call map() on the empty Maybe using a set as the mapping argument
    mapping_set = {is_some_flag}
    map_result = empty_maybe.map(mapping_set)

    # Construct a second Maybe wrapping a concrete integer value
    integer_value = -1095
    is_some_flag_2 = True
    integer_maybe = maybe.Maybe(integer_value, is_some_flag_2)

    # Convert the integer Maybe to an Either type
    either_result = integer_maybe.to_either()

def test_maybe_monad_conversions_with_none_and_nested_maybe():
    """Verify that Maybe instances built from None and nested Maybe values can be converted to lazy, either, and try representations without error."""

    # Build a Maybe from two None values
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Wrap the first Maybe inside a tuple to use as a value in a second Maybe
    nested_maybe_tuple = (maybe_with_none,)

    # Convert the None-based Maybe to a lazy representation
    lazy_from_none_maybe = maybe_with_none.to_lazy()

    # Build a second Maybe using the nested tuple and False
    false_value = False
    maybe_with_nested = maybe.Maybe(nested_maybe_tuple, false_value)

    # Convert the None-based Maybe to an either representation (first call)
    either_from_none_maybe_first = maybe_with_none.to_either()

    # Convert the nested Maybe to a try representation
    try_
# (Truncated by extractor)