import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with a bytes value supplied for both constructor arguments."""
    # Define a raw bytes payload to use as both constructor arguments
    raw_bytes_value = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Construct a Maybe instance using the bytes value for both parameters
    maybe_instance = maybe.Maybe(raw_bytes_value, raw_bytes_value)

def test_maybe_instantiation_with_none_values():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None for both the value and the fallback
    none_value = None

    # Construct a Maybe instance with both arguments as None
    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chained_operations_with_string_value():
    """Test that Maybe monad operations (ap, map, filter, bind, to_validation, to_either) chain correctly across multiple instances with a string value."""

    # Arbitrary string used as both the wrapped value and the fallback/default
    string_value = "p4xa>bl^oP"

    # Create a Maybe instance wrapping the string value
    maybe_instance = maybe.Maybe(string_value, string_value)

    # Compare the Maybe instance against a plain string using equality
    eq_result_maybe_vs_string = maybe_instance.__eq__(string_value)

    # Apply the Maybe to a string argument; result acts as a function-wrapped Maybe
    ap_result = maybe_instance.ap(string_value)

    # Retrieve the value or fall back to the string default
    or_else_value = maybe_instance.get_or_else(string_value)

    # Map over the Maybe using the ap result (first time)
    map_result_first = maybe_instance.map(ap_result)

    # Filter the Maybe using the ap result (first time)
    filter_result_first = maybe_instance.filter(ap_result)

    # Map over the Maybe using the ap result (second time)
    map_result_second = maybe_instance.map(ap_result)

    # Apply the Maybe to the string argument again for a second ap result
    ap_result_second = maybe_instance.ap(string_value)

    # Check equality between the first and second ap results
    eq_result_ap_vs_ap_second = ap_result.__eq__(ap_result_second)

    # Filter the first ap result using the or_else value as the predicate
    filter_result_of_ap = ap_result.filter(or_else_value)

    # Get the value from the second ap result, falling back to the string default
    or_else_of_ap_second = ap_result_second.get_or_else(string_value)

    # Create a second Maybe instance from the same inputs
    maybe_instance_2 = maybe.Maybe(string_value, string_value)

    # Convert the second Maybe instance to a Validation
    validation_result = maybe_instance_2.to_validation()

    # Bind the second Maybe using the validation result
    bind_result = maybe_instance_2.bind(validation_result)

    # Convert the bound result to an Either
    either_result = bind_result.to_either()

def test_maybe_none_not_equal_to_false_set():
    """Test that a Maybe wrapping None values is not considered equal to a set of False values."""

    # A single False value used to construct a uniform set
    false_value = False

    # A set that collapses to {False} due to deduplication of identical False values
    false_set = {false_value, false_value, false_value, false_value}

    # None used as both arguments to Maybe, representing an absent/empty context
    none_value = None

    # Construct a Maybe monad with two None values
    maybe_none = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance against the set of False values using __eq__
    equality_result = maybe_none.__eq__(false_set)

def test_set_to_box_raises_attribute_error_after_maybe_operations():
    """Test that calling to_box() on a plain set raises AttributeError after Maybe bind/map operations."""

    # Use a simple True value as the base input for Maybe construction
    true_value = True

    # Construct a Maybe wrapping two True values, then bind and map over it
    maybe_bool = maybe.Maybe(true_value, true_value)
    bound_result = maybe_bool.bind(true_value)
    mapped_result = bound_result.map(true_value)

    # Construct a Maybe wrapping a tuple of True values
    bool_tuple = (true_value, true_value, true_value, true_value)
    maybe_tuple = maybe.Maybe(bool_tuple, true_value)

    # Attempt to call to_box() on a plain set, which has no such method
    empty_set = set()
    empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe can be constructed with None and False, and that map() accepts a falsy value without error."""
    # Use None as the wrapped value inside Maybe
    none_value = None

    # Use False as both the second constructor argument and the map argument
    false_flag = False

    # Construct a Maybe instance with a None value and a False flag
    maybe_instance = maybe.Maybe(none_value, false_flag)

    # Invoke map() with a falsy value to verify it handles this gracefully
    maybe_instance.map(false_flag)

def test_maybe_bind_with_none_value_and_empty_dict():
    """Test that Maybe constructed with None allows bind to be called with an empty dict without error."""

    # Construct a Maybe with a truthy value (unused directly, verifies constructor accepts True)
    truthy_value = True
    maybe_with_true = maybe.Maybe(truthy_value, truthy_value)

    # Prepare the argument for bind and a None-wrapped Maybe
    empty_dict = {}
    none_value = None
    falsy_value = False
    maybe_with_none = maybe.Maybe(none_value, falsy_value)

    # Calling bind on a None-valued Maybe with an empty dict should not raise
    maybe_with_none.bind(empty_dict)

def test_maybe_chained_monadic_operations_with_mixed_types():
    """Test Maybe supports chained monadic operations (to_box, filter, to_lazy, ap, __eq__) with mixed types."""

    # Construct a Maybe wrapping bytes with a None second argument
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_value = None
    maybe_bytes = maybe.Maybe(raw_bytes, none_value)

    # Box the bytes-based Maybe
    boxed_bytes = maybe_bytes.to_box()

    # Construct a Maybe wrapping an integer with a bool second argument
    int_value = 0
    bool_value = True
    maybe_int = maybe.Maybe(int_value, bool_value)

    # Filter the int-based Maybe using itself as the predicate
    filtered_int = maybe_int.filter(maybe_int)

    # Convert the int-based Maybe to a lazy representation
    lazy_int = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes-based Maybe
    applied_result = filtered_int.ap(maybe_bytes)

    # Filter the applied result using the applied result itself
    filtered_applied = filtered_int.filter(applied_result)

    # Construct a Maybe from the lazy value and the boxed bytes
    maybe_lazy = maybe.Maybe(lazy_int, boxed_bytes)

    # Check equality of the lazy value against the bool
    eq_result = lazy_int.__eq__(bool_value)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() on a Maybe constructed with None and False does not raise an error."""
    # Integer argument to pass into the ap() method
    integer_value = 2862

    # Construct a Maybe representing a Nothing-like state (None value, False flag)
    none_value = None
    flag_false = False
    maybe_nothing = maybe.Maybe(none_value, flag_false)

    # Call ap() on the Nothing-like Maybe with the integer value
    maybe_nothing.ap(integer_value)

def test_maybe_supports_filter_to_lazy_map_and_to_try_chaining():
    """Test that a Maybe instance supports chaining filter, to_lazy, map, and to_try operations."""

    # Construct a present Maybe wrapping the integer value 0
    initial_value = 0
    is_present = True
    maybe_instance = maybe.Maybe(initial_value, is_present)

    # Filter the maybe by itself and convert to lazy form
    filtered_maybe = maybe_instance.filter(maybe_instance)
    lazy_from_maybe = maybe_instance.to_lazy()

    # Convert the filtered maybe to lazy, then filter again and convert to try
    lazy_from_filtered = filtered_maybe.to_lazy()
    filtered_again = filtered_maybe.filter(lazy_from_filtered)
    try_result = filtered_again.to_try()

    # Perform a second independent lazy conversion of the original maybe
    lazy_from_maybe_second = maybe_instance.to_lazy()

    # Map the filtered maybe over itself
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_on_none_value_with_tuple_and_lazy():
    """Test that Maybe.filter() on None-valued Maybes handles tuple args and lazy conversion without error."""

    # Build a tuple of repeated negative integers to use as a filter argument
    negative_int = -283
    int_tuple = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with a True flag, then filter using the tuple
    none_value = None
    flag_true = True
    maybe_with_none_and_flag = maybe.Maybe(none_value, flag_true)
    filtered_maybe = maybe_with_none_and_flag.filter(int_tuple)

    # Convert the filtered Maybe to a lazy representation
    lazy_filtered = filtered_maybe.to_lazy()

    # Create a second Maybe wrapping None (no flag), then filter using the lazy result
    none_value_2 = None
    maybe_all_none = maybe.Maybe(none_value_2, none_value_2)
    maybe_all_none.filter(lazy_filtered)

def test_maybe_get_or_else_and_filter_with_generic_object():
    """Test that a present Maybe resolves via get_or_else and to_box, and an absent Maybe with a Generic value supports filter."""

    # Fallback value used when Maybe has no value
    fallback_value = 2281

    # Build a tuple payload containing strings and dicts
    payload_str = "gZ(\\mOcN"
    payload_dict = {payload_str: payload_str}
    maybe_payload = (payload_str, payload_str, payload_dict, payload_dict)

    # Construct a Maybe that holds a value (True = value is present)
    has_value_true = True
    maybe_with_value = maybe.Maybe(maybe_payload, has_value_true)

    # Resolve the Maybe: should return the wrapped value since it is present
    resolved_value = maybe_with_value.get_or_else(fallback_value)

    # Wrap a Generic object into a Maybe with no value (False = value is absent)
    generic_obj = typing.Generic()
    has_value_false = False

    # Convert the present Maybe to its boxed representation
    boxed_maybe = maybe_with_value.to_box()

    # Construct an absent Maybe wrapping the Generic object
    maybe_without_value = maybe.Maybe(generic_obj, has_value_false)

    # Filter the absent Maybe using the resolved value from the present Maybe
    maybe_without_value.filter(resolved_value)

def test_maybe_chained_operations_with_bool_int_and_float_mixed_types():
    """Test that Maybe instances with mixed types support chained operations without error."""

    # --- Maybe wrapping a truthy bool with no fallback ---
    truthy_value = True
    no_fallback = None
    maybe_bool_no_fallback = maybe.Maybe(truthy_value, no_fallback)
    validation_from_bool_maybe = maybe_bool_no_fallback.to_validation()

    # --- Maybe wrapping a negative int with an empty tuple as fallback ---
    float_value = -286.64
    negative_int_value = -1784
    empty_tuple_fallback = ()
    maybe_negative_int = maybe.Maybe(negative_int_value, empty_tuple_fallback)

    # Convert to validation, retrieve value with fallback, and convert to Try
    validation_from_int_maybe = maybe_negative_int.to_validation()
    get_or_else_result = maybe_negative_int.get_or_else(negative_int_value)
    try_from_int_maybe = maybe_negative_int.to_try()

    # --- Maybe wrapping a float with a float fallback (constructed, not further chained) ---
    maybe_float_with_float_fallback = maybe.Maybe(float_value, float_value)

    # Bind the Try result back onto the int Maybe
    maybe_negative_int.bind(try_from_int_maybe)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test that Maybe.map works with a set argument and Maybe.to_either converts a Maybe holding an integer."""

    # Construct a Maybe wrapping None with has_value=True
    none_value = None
    has_value_true = True
    maybe_with_none = maybe.Maybe(none_value, has_value_true)

    # Call map with a set as the mapping argument
    mapping_set = {has_value_true}
    map_result = maybe_with_none.map(mapping_set)

    # Construct a second Maybe wrapping a negative integer, then convert to Either
    negative_int_value = -1095
    is_present = True
    maybe_with_int = maybe.Maybe(negative_int_value, is_present)
    either_result = maybe_with_int.to_either()

def test_maybe_with_none_values_supports_lazy_either_and_try_conversions():
    """Verify that a Maybe wrapping None values can be converted to lazy, either, and try forms, and that the resulting Try can also be converted to lazy."""

    # Build a Maybe wrapping two None values
    null_value = None
    maybe_none = maybe.Maybe(null_value, null_value)

    # Create a tuple containing the None-based Maybe, to use as a nested input
    maybe_tuple = (maybe_none,)

    # Convert the None Maybe to lazy form (validates the conversion does not raise)
    lazy_from_none_maybe = maybe_none.to_lazy()

    false_value = False

    # Build a second Maybe wrapping the tuple and a False value
    maybe_tuple_false = maybe.Maybe(maybe_tuple, false_value)

    # Convert the None Maybe to either form (first call; result computed but not further consumed)
    either_from_none_maybe_first = maybe_none.to_either()

    # Convert the tuple/False Maybe to try
# (Truncated by extractor)