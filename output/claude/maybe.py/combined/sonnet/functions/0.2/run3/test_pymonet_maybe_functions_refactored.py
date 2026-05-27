import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with a bytes object passed as both arguments."""
    # Use the same raw bytes value for both constructor arguments
    raw_bytes_value = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    maybe_instance = maybe.Maybe(raw_bytes_value, raw_bytes_value)

def test_maybe_instantiation_with_none_values():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None as both arguments to verify the constructor accepts absent values
    none_value = None

    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chained_operations_with_bind_and_conversions():
    """Test that a Maybe instance supports chained ap, map, filter, bind, to_validation, and to_either operations with consistent equality semantics."""

    # A single string used as both the wrapped value and the fallback/default
    sample_value = "p4xa>bl^oP"

    # Construct the primary Maybe instance wrapping the sample value
    maybe_instance = maybe.Maybe(sample_value, sample_value)

    # Equality check between the Maybe instance and the raw string
    eq_result = maybe_instance.__eq__(sample_value)

    # Apply ap and get_or_else on the primary instance
    ap_result = maybe_instance.ap(sample_value)
    get_or_else_result = maybe_instance.get_or_else(sample_value)

    # Chain map and filter using the ap result as the transformation argument
    map_result_1 = maybe_instance.map(ap_result)
    filter_result_1 = maybe_instance.filter(ap_result)

    # Repeat map and ap to produce additional derived values
    map_result_2 = maybe_instance.map(ap_result)
    ap_result_2 = maybe_instance.ap(sample_value)

    # Compare the two ap results for equality
    ap_eq_result = ap_result.__eq__(ap_result_2)

    # Apply filter on the first ap result using get_or_else_result as the predicate
    filter_result_2 = ap_result.filter(get_or_else_result)

    # Retrieve the fallback value from the second ap result
    get_or_else_result_2 = ap_result_2.get_or_else(sample_value)

    # Construct a second Maybe instance for bind and conversion chain
    maybe_instance_2 = maybe.Maybe(sample_value, sample_value)

    # Convert to validation, then bind with the validation result, then convert to Either
    validation_result = maybe_instance_2.to_validation()
    bind_result = maybe_instance_2.bind(validation_result)
    either_result = bind_result.to_either()

def test_maybe_eq_returns_value_when_compared_to_set_of_false():
    """Test that Maybe.__eq__ produces a result when comparing a Maybe(None, None) instance to a set containing False."""
    # Build a set of False values (deduplicates to {False})
    false_value = False
    set_of_false = {false_value, false_value, false_value, false_value}

    # Construct a Maybe instance wrapping two None values
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance to the set; result is stored but not asserted
    eq_result = maybe_with_none.__eq__(set_of_false)

def test_maybe_bind_map_chain_and_set_missing_method_raises_attribute_error():
    """Test that Maybe bind/map chaining works and that calling .to_box() on a plain set raises AttributeError."""

    # Use a simple boolean as the seed value for Maybe construction
    true_value = True

    # Create a Maybe wrapping a boolean value
    maybe_with_bool = maybe.Maybe(true_value, true_value)

    # Bind the boolean value through the Maybe
    bound_maybe = maybe_with_bool.bind(true_value)

    # Map the boolean value over the bound Maybe
    mapped_maybe = bound_maybe.map(true_value)

    # Create a tuple of four True values to use as a compound Maybe input
    quad_true_tuple = (true_value, true_value, true_value, true_value)

    # Create a second Maybe wrapping the tuple
    maybe_with_tuple = maybe.Maybe(quad_true_tuple, true_value)

    # Attempt to call .to_box() on a plain set — set has no such method,
    # so this will raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_does_not_raise():
    """Test that Maybe constructed with None and False can call map() with a falsy value without error."""
    # Set up a missing value and a falsy flag to represent edge-case inputs
    empty_value = None
    false_flag = False

    # Construct a Maybe monad wrapping the empty value with the falsy flag
    maybe_instance = maybe.Maybe(empty_value, false_flag)

    # Invoke map() with a falsy value to verify it executes without raising
    maybe_instance.map(false_flag)

def test_maybe_get_or_else_and_filter_with_present_and_absent_values():
    """Test that a present Maybe resolves via get_or_else and to_box, and an absent Maybe accepts filter with the resolved value."""
    # Fallback integer used when a Maybe has no value
    fallback_value = 2281

    # Build a tuple payload containing strings and dicts
    payload_str = "gZ(\\mOcN"
    payload_dict = {payload_str: payload_str}
    maybe_payload = (payload_str, payload_str, payload_dict, payload_dict)

    # Construct a present Maybe (is_present=True means the value exists)
    is_present = True
    present_maybe = maybe.Maybe(maybe_payload, is_present)

    # Resolve the present Maybe; should return the wrapped value, not the fallback
    resolved_value = present_maybe.get_or_else(fallback_value)

    # Create a Generic instance to serve as payload for the absent Maybe
    generic_instance = typing.Generic()

    # Convert the present Maybe into a box representation
    boxed_value = present_maybe.to_box()

    # Construct an absent Maybe (is_absent=False means no value is held)
    is_absent = False
    absent_maybe = maybe.Maybe(generic_instance, is_absent)

    # Apply filter on the absent Maybe using the previously resolved value
    absent_maybe.filter(resolved_value)

def test_maybe_methods_with_mixed_types_do_not_raise():
    """Test that Maybe with mixed types supports to_validation, get_or_else, to_try, and bind without errors."""

    # --- Maybe wrapping a bool value with a None fallback ---
    true_value = True
    none_fallback = None
    maybe_bool_none = maybe.Maybe(true_value, none_fallback)
    validation_from_bool_maybe = maybe_bool_none.to_validation()

    # --- Maybe wrapping an int value with an empty tuple fallback ---
    float_value = -286.64
    int_value = -1784
    empty_tuple_fallback = ()
    maybe_int_empty_tuple = maybe.Maybe(int_value, empty_tuple_fallback)

    # Convert to validation and retrieve the value via get_or_else
    validation_from_int_maybe = maybe_int_empty_tuple.to_validation()
    get_or_else_result = maybe_int_empty_tuple.get_or_else(int_value)

    # Convert to Try, then use the Try result as the bind function
    try_result = maybe_int_empty_tuple.to_try()
    maybe_int_empty_tuple.bind(try_result)

    # --- Maybe wrapping two float values (tests construction does not raise) ---
    maybe_float_float = maybe.Maybe(float_value, float_value)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test that Maybe.map() accepts a set and Maybe.to_either() converts a Maybe wrapping an integer."""

    # Construct a Maybe wrapping None with has_value=True
    none_value = None
    has_value_true = True
    maybe_with_none = maybe.Maybe(none_value, has_value_true)

    # Call map() with a set containing the boolean flag; result is captured but not asserted
    mapping_set = {has_value_true}
    map_result = maybe_with_none.map(mapping_set)

    # Construct a second Maybe wrapping a negative integer with has_value=True
    negative_int_value = -1095
    has_value_true_second = True
    maybe_with_int = maybe.Maybe(negative_int_value, has_value_true_second)

    # Convert the integer-wrapping Maybe to an Either type
    either_result = maybe_with_int.to_either()

def test_maybe_with_none_and_nested_maybe_conversions():
    """Test that Maybe instances holding None values and nested Maybe objects support chained conversions to lazy, either, and try forms."""

    # Create a Maybe wrapping two None values
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Wrap the first Maybe inside a tuple to use as a nested value
    nested_maybe_tuple = (maybe_with_none,)

    # Convert the None-holding Maybe to its lazy representation
    lazy_from_none_maybe = maybe_with_none.to_lazy()

    # Create a Maybe wrapping the nested tuple and a False value
    false_value = False
    maybe_with_nested = maybe.Maybe(nested_maybe_tuple, false_value)

    # Convert the None-holding Maybe to an Either (first call)
    either_from_none_maybe_first = maybe_with_none.to_either()

    # Convert the nested Maybe to a Try representation
    try_from_nested_maybe = maybe_with_nested.to_try()

    # Convert the None-holding Maybe to an Either again (second call, confirming repeated conversion)
    either_from_none_maybe_second = maybe_with_none.to_either()

    # Convert the nested Maybe to an Either representation
    either_from_nested_maybe = maybe_with_nested.to_either()

    # Chain to_lazy on the Try result derived from the nested Maybe
    try_from_nested_maybe.to_lazy()

def test_maybe_to_try_to_box_conversion_succeeds():
    """Test that a Maybe(True, False) can be chained through to_try() and then to_box() without error."""
    # Construct input flags for the Maybe container
    is_success = True
    is_empty = False

    # Create a Maybe instance with the given flags
    maybe_instance = maybe.Maybe(is_success, is_empty)

    # Convert the Maybe to a Try, then chain to a Box
    try_result = maybe_instance.to_try()
    try_result.to_box()

def test_maybe_none_true_chains_through_monad_transformations():
    """Test that Maybe(None, True) correctly chains through ap, lazy, validation, filter, get_or_else, either, try, and box transformations."""

    # Input values
    arbitrary_bytes = b"C\xcf\xe7/"
    none_value = None
    flag_true = True

    # Construct a Maybe monad wrapping None with a True flag
    maybe_none = maybe.Maybe(none_value, flag_true)

    # Apply ap with None — produces a new Maybe
    maybe_after_ap = maybe_none.ap(none_value)

    # Convert the ap result to a Lazy container
    lazy_from_ap = maybe_after_ap.to_lazy()

    # Convert the Lazy container to a Validation
    validation_from_lazy = lazy_from_ap.to_validation()

    # Filter the original Maybe using the Validation as the predicate
    maybe_filtered = maybe_none.filter(validation_from_lazy)

    # Retrieve the value or fall back to the filtered Maybe itself
    get_or_else_result = maybe_filtered.get_or_else(maybe_filtered)

    # Convert the filtered Maybe to an Either
    either_from_filtered = maybe_filtered.to_either()

    # Convert the Validation to a Try
    try_from_validation = validation_from_lazy.to_try()

    # Check equality between the filtered Maybe and the ap result
    eq_result = maybe_filtered.__eq__(maybe_after_ap)

    # Convert the get_or_else result to a Box
    box_from_get_or_else = get_or_else_result.to_box()

    # Invoke ap on the Try with arbitrary bytes (side-effect / error-path call)
    try_from_validation.ap(arbitrary_bytes)

def test_maybe_monad_chained_operations_with_none_and_bytes_values():
    """Test that Maybe monad operations (ap, bind, to_validation, to_either, to_try, get_or_else)
    execute without error across None-seeded and bytes-valued Maybe instances."""

    # --- Input values ---
    sample_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    flag_true = True

    # --- First Maybe instance: Maybe(None, True) ---
    # Construct a Maybe with None as the value and True as the flag
    maybe_none_true = maybe.Maybe(none_value, flag_true)

    # Chain ap calls: first with None, then with bytes
    maybe_after_ap_none = maybe_none_true.ap(none_value)
    maybe_after_ap_bytes = maybe_after_ap_none.ap(sample_bytes)

    # Convert the chained result to a Validation
    validation_from_chained = maybe_after_ap_bytes.to_validation()

    # --- Second Maybe instance: Maybe(None, bytes) ---
    # Construct a Maybe with None as the value and bytes as the flag
    maybe_none_bytes = maybe.Maybe(none_value, sample_bytes)

    # Exercise get_or_else, to_validation, bind, to_either, and ap on this instance
    get_or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)
    validation_from_none_bytes = maybe_none_bytes.to_validation()
    bound_result = maybe_none_bytes.bind(validation_from_none_bytes)
    either_from_none_bytes = maybe_none_bytes.to_either()
    ap_self_result = maybe_none_bytes.ap(maybe_none_bytes)  # ap with itself

    # --- Operations on the Either result ---
    negative_int = -3289

    # Compare Either against the Validation using __eq__
    either_eq_validation = either_from_none_bytes.__eq__(validation_from_none_bytes)

    # Bind the Either with the Maybe instance
    either_bound_result = either_from_none_bytes.bind(maybe_none_bytes)

    # --- Convert Maybe to Try and exercise further ---
    try_from_none_bytes = maybe_none_bytes.to_try()

    # Compare the original Maybe against the bound result using __eq__
    maybe_eq_bound = maybe_none_bytes.__eq__(bound_result)

    # Convert the bound result to a Validation
    validation_from_bound = bound_result.to_validation()

    # Call ap on the Try result with a negative integer (smoke test — no exception expected)
    try_from_none_bytes.ap(negative_int)

def test_maybe_false_values_chain_to_either_lazy_and_validation():
    """Test that a Maybe wrapping False values supports equality, chaining to Either/Lazy/Validation, and mapping with a Validation."""

    false_value = False

    # Create a Maybe with False for both fields and check equality with False
    maybe_with_false = maybe.Maybe(false_value, false_value)
    eq_result = maybe_with_false.__eq__(false_value)

    # Create a second Maybe and chain it through Either -> Lazy -> Validation
    maybe_for_chaining = maybe.Maybe(false_value, false_value)
    either_result = maybe_for_chaining.to_either()
    lazy_result = maybe_for_chaining.to_lazy()
    validation_from_lazy = lazy_result.to_validation()

    # Create a third Maybe and map the validation over it
    maybe_for_map = maybe.Maybe(false_value, false_value)
    maybe_for_map.map(validation_from_lazy)

def test_maybe_false_false_converts_to_try_and_validation():
    """Test that a Maybe(False, False) supports self-equality and converts through to_try() and to_validation()."""
    # Construct a Maybe with both values set to False
    false_value = False
    maybe_instance = maybe.Maybe(false_value, false_value)

    # Verify that the Maybe instance can compare equal to itself
    is_equal_to_self = maybe_instance.__eq__(maybe_instance)

    # Convert the Maybe to a Try, then further to a Validation
    try_result = maybe_instance.to_try()
    try_result.to_validation()

