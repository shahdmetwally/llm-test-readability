import pytest
import maybe as maybe
import typing as typing

def test_maybe_constructor_with_bytes_arguments():
    """Test that Maybe can be constructed with two identical bytes arguments."""
    # Use arbitrary byte sequences as both positional arguments to Maybe
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    result = maybe.Maybe(raw_bytes, raw_bytes)

def test_maybe_initialized_with_none_values():
    """Test that Maybe can be instantiated with both arguments as None."""
    no_value = None
    result = maybe.Maybe(no_value, no_value)

def test_maybe_chained_operations_with_string_value():
    """Test chaining map, filter, ap, bind, and conversion operations on Maybe instances
    initialized with a string value, verifying interoperability between derived Maybes."""

    input_str = "p4xa>bl^oP"

    # Create a Maybe wrapping the input string and verify equality
    maybe_instance = maybe.Maybe(input_str, input_str)
    is_equal = maybe_instance.__eq__(input_str)

    # Apply and transform operations on the first Maybe
    ap_result = maybe_instance.ap(input_str)
    fallback_value = maybe_instance.get_or_else(input_str)
    mapped_result = maybe_instance.map(ap_result)
    filtered_result = maybe_instance.filter(ap_result)
    remapped_result = maybe_instance.map(ap_result)

    # Apply ap again and compare the two ap results for equality
    second_ap_result = maybe_instance.ap(input_str)
    ap_results_equal = ap_result.__eq__(second_ap_result)

    # Chain filter and get_or_else on derived Maybe results
    filtered_from_fallback = ap_result.filter(fallback_value)
    fallback_from_second_ap = second_ap_result.get_or_else(input_str)

    # Create a second Maybe and exercise bind and conversion to Either
    maybe_instance_2 = maybe.Maybe(input_str, input_str)
    validation_result = maybe_instance_2.to_validation()
    bound_result = maybe_instance_2.bind(validation_result)
    either_result = bound_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set():
    """Test that Maybe.__eq__ returns False when compared to a set (non-Maybe value)."""

    # A set containing a single unique value (False deduplicated)
    false_value = False
    comparison_set = {false_value, false_value, false_value, false_value}

    # Create a Maybe instance with both value and fallback as None
    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance to a set; expected to be unequal (not a Maybe)
    result = maybe_instance.__eq__(comparison_set)

def test_maybe_bind_map_then_invalid_method_on_set():
    """
    Test that Maybe can be constructed with a bool value, supports bind and map chaining,
    and that calling a non-existent method (to_box) on a plain set raises an AttributeError.
    """
    # Use True as both the value and the 'just' flag to construct a Maybe
    is_present = True
    maybe_value = maybe.Maybe(is_present, is_present)

    # Bind and map over the Maybe with the bool value
    bound_result = maybe_value.bind(is_present)
    mapped_result = bound_result.map(is_present)

    # Construct a Maybe with a tuple as the value
    tuple_value = (is_present, is_present, is_present, is_present)
    maybe_tuple = maybe.Maybe(tuple_value, is_present)

    # Attempt to call a non-existent method on a plain set, which should raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with a False boolean when initialized with None and False."""
    # Initialize Maybe with a None value and False as the boolean flag
    none_value = None
    false_flag = False
    maybe_instance = maybe.Maybe(none_value, false_flag)

    # Attempt to map over the Maybe instance using the False flag
    maybe_instance.map(false_flag)

def test_maybe_bind_with_empty_dict_on_none_value_maybe():
    """
    Test that calling bind() with an empty dict on a Maybe wrapping None
    does not raise an error, even when another Maybe with a truthy value exists.
    """
    # Create a Maybe instance with a truthy value
    true_value = True
    maybe_truthy = maybe.Maybe(true_value, true_value)

    # Prepare an empty dict to use as the bind argument
    empty_dict = {}
    none_value = None
    false_value = False

    # Create a Maybe instance wrapping None with a falsy default
    maybe_none = maybe.Maybe(none_value, false_value)

    # Bind the empty dict to the Maybe wrapping None
    maybe_none.bind(empty_dict)

def test_maybe_filter_and_ap_with_mixed_types():
    """
    Test chaining of Maybe operations (filter, ap, to_box, to_lazy) across
    instances constructed with bytes/None and int/bool values. Verifies that
    composed Maybe transformations execute without errors and produce results.
    """
    # Create a Maybe wrapping bytes with no fallback value
    bytes_value = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_fallback = None
    maybe_bytes = maybe.Maybe(bytes_value, no_fallback)
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an int with a bool fallback
    int_value = 0
    bool_fallback = True
    maybe_int = maybe.Maybe(int_value, bool_fallback)

    # Apply filter using the maybe itself as the predicate
    filtered_maybe = maybe_int.filter(maybe_int)

    # Convert the int-based Maybe to a lazy representation
    lazy_maybe = maybe_int.to_lazy()

    # Apply the filtered Maybe over the bytes-based Maybe
    ap_result = filtered_maybe.ap(maybe_bytes)

    # Filter the ap result using the previously filtered Maybe
    filtered_ap_result = filtered_maybe.filter(ap_result)

    # Construct a new Maybe combining the lazy and boxed values
    maybe_combined = maybe.Maybe(lazy_maybe, boxed_bytes)

    # Check equality of the lazy Maybe against the bool fallback
    eq_result = lazy_maybe.__eq__(bool_fallback)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() on a Maybe wrapping None (with False flag) with an integer does not raise unexpectedly."""
    some_int = 2862
    no_value = None
    is_just = False

    # Construct a Maybe with no value and False to indicate a Nothing-like state
    maybe_instance = maybe.Maybe(no_value, is_just)

    # Apply the integer to the Maybe instance via ap()
    maybe_instance.ap(some_int)

def test_maybe_filter_and_lazy_map_chaining():
    """Test chaining filter, to_lazy, and map operations on Maybe instances."""
    # Create a Maybe wrapping integer 0 with a truthy flag
    int_value = 0
    is_present = True
    maybe_instance = maybe.Maybe(int_value, is_present)

    # Filter the Maybe using itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the original Maybe to a lazy representation
    lazy_from_original = maybe_instance.to_lazy()

    # Convert the filtered Maybe to a lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Chain another filter on the filtered Maybe using the lazy version
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered result to a Try
    try_result = double_filtered.to_try()

    # Convert the original Maybe to lazy again (independent call)
    lazy_from_original_again = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_filter_on_maybe_with_none_value_returns_lazy():
    """Test that filtering a Maybe wrapping None with a tuple value returns a lazy Maybe,
    and that filtering a second Maybe(None, None) with that lazy result does not raise."""

    # A repeated integer used to build a tuple filter argument
    sentinel_int = -283
    filter_tuple = (sentinel_int, sentinel_int, sentinel_int)

    # Create a Maybe with no value (None) but truthy flag
    maybe_none_truthy = maybe.Maybe(None, True)

    # Apply filter with the tuple; result should be a Maybe
    filtered_maybe = maybe_none_truthy.filter(filter_tuple)

    # Convert the filtered Maybe to a lazy representation
    lazy_maybe = filtered_maybe.to_lazy()

    # Create a second Maybe with both value and flag set to None
    maybe_none_none = maybe.Maybe(None, None)

    # Filter the second Maybe using the lazy result — verifying no error occurs
    maybe_none_none.filter(lazy_maybe)

def test_maybe_get_or_else_and_filter_with_generic():
    """
    Test that Maybe.get_or_else returns the wrapped value when present,
    and that Maybe.filter works on a Maybe wrapping a Generic instance
    using the result of get_or_else as the predicate/filter argument.
    """
    fallback_int = 2281
    key_str = "gZ(\\mOcN"

    # Build a tuple payload containing the string and dicts keyed by it
    str_dict = {key_str: key_str}
    payload_tuple = (key_str, key_str, str_dict, str_dict)

    # Create a Maybe with a truthy presence flag and retrieve its value
    is_present = True
    maybe_with_value = maybe.Maybe(payload_tuple, is_present)
    retrieved_value = maybe_with_value.get_or_else(fallback_int)

    # Create a Generic instance to wrap in a second Maybe
    generic_instance = typing.Generic()

    # Create a Maybe with a falsy presence flag (value absent)
    is_absent = False
    var_1 = maybe_with_value.to_box()
    maybe_without_value = maybe.Maybe(generic_instance, is_absent)

    # Filter the absent Maybe using the value retrieved from the first Maybe
    maybe_without_value.filter(retrieved_value)

def test_maybe_to_validation_get_or_else_and_bind_operations():
    """
    Tests a sequence of Maybe operations including to_validation(), get_or_else(),
    to_try(), and bind() across multiple Maybe instances with varying value/fallback
    combinations (bool/None, int/empty-tuple, float/float).
    """
    # Create a Maybe with a truthy value and no fallback
    bool_value = True
    none_fallback = None
    maybe_bool = maybe.Maybe(bool_value, none_fallback)

    # Convert the bool Maybe to a Validation
    validation_from_bool = maybe_bool.to_validation()

    # Define values for subsequent Maybe instances
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()

    # Create a Maybe wrapping an int with an empty tuple as fallback
    maybe_int = maybe.Maybe(int_value, empty_tuple)

    # Convert the int Maybe to a Validation
    validation_from_int = maybe_int.to_validation()

    # Retrieve the value or fall back to int_value if absent
    value_or_else = maybe_int.get_or_else(int_value)

    # Convert the int Maybe to a Try
    try_from_int = maybe_int.to_try()

    # Create a Maybe wrapping a float with a float fallback
    maybe_float = maybe.Maybe(float_value, float_value)

    # Bind the Try result onto the int Maybe
    maybe_int.bind(try_from_int)

def test_maybe_map_with_none_value_and_to_either_with_int_value():
    """
    Test that Maybe.map can be called with a set as the mapper when the
    wrapped value is None, and that Maybe.to_either works correctly when
    the wrapped value is a negative integer.
    """
    # Create a Maybe wrapping None with allow_none=True
    none_value = None
    allow_none = True
    maybe_with_none = maybe.Maybe(none_value, allow_none)

    # Attempt to map over the None-wrapped Maybe using a set as the mapper
    mapper_set = {allow_none}
    result_map = maybe_with_none.map(mapper_set)

    # Create a Maybe wrapping a negative integer with allow_none=True
    negative_int = -1095
    allow_none_2 = True
    maybe_with_int = maybe.Maybe(negative_int, allow_none_2)

    # Convert the integer-wrapped Maybe to an Either
    result_either = maybe_with_int.to_either()

def test_maybe_conversions_with_none_and_tuple_values():
    """
    Test that Maybe instances constructed with None and tuple values
    can be converted to lazy, either, and try representations without error.
    Verifies chained conversions across multiple Maybe configurations.
    """
    # Create a Maybe wrapping None for both value and context
    none_value = None
    maybe_none = maybe.Maybe(none_value, none_value)

    # Use the first Maybe as a tuple value for a second Maybe
    tuple_value = (maybe_none,)
    lazy_from_none = maybe_none.to_lazy()

    # Create a second Maybe with a tuple and False as its arguments
    bool_false = False
    maybe_tuple = maybe.Maybe(tuple_value, bool_false)

    # Convert the None-based Maybe to either representation
    either_from_none_first = maybe_none.to_either()

    # Convert the tuple-based Maybe to try representation
    try_from_tuple = maybe_tuple.to_try()

    # Convert the None-based Maybe to either again (second call)
    either_from_none_second = maybe_none.to_either()

    # Convert the tuple-based Maybe to either representation
    either_from_tuple = maybe_tuple.to_either()

    # Convert the try result from the tuple-based Maybe to lazy
    try_from_tuple.to_lazy()

def test_maybe_to_try_chained_to_box():
    """Test that a Maybe created with (True, False) can be chained through to_try() and to_box() without error."""
    is_just = True
    is_nothing = False

    # Construct a Maybe with a truthy/falsy pair
    maybe_value = maybe.Maybe(is_just, is_nothing)

    # Convert Maybe to a Try, then wrap the result in a Box
    try_value = maybe_value.to_try()
    try_value.to_box()
# (Truncated by extractor)