import pytest
import maybe as maybe
import typing as typing

def test_maybe_constructed_with_bytes_arguments():
    """Test that Maybe can be instantiated with two identical byte string arguments."""
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Construct a Maybe instance using the same bytes value for both arguments
    result = maybe.Maybe(raw_bytes, raw_bytes)

def test_maybe_accepts_two_none_arguments():
    """Test that Maybe can be instantiated with two None values as arguments."""
    first_arg = None
    second_arg = None

    # Construct a Maybe with both arguments set to None
    maybe_0 = maybe.Maybe(first_arg, second_arg)

def test_maybe_chained_operations_with_string_value():
    """Test chaining of Maybe monad operations (map, filter, ap, bind) on a
    Just value, verifying equality, transformation, and conversion to
    Validation and Either types."""

    input_str = "p4xa>bl^oP"

    # Construct a Maybe (Just) with the input string as both value and default
    maybe_value = maybe.Maybe(input_str, input_str)

    # Check equality of Maybe with the raw string
    is_equal = maybe_value.__eq__(input_str)

    # Apply (ap) the string to the Maybe
    ap_result = maybe_value.ap(input_str)

    # Retrieve the value, falling back to the input string
    unwrapped = maybe_value.get_or_else(input_str)

    # Map and filter using the ap result (a Maybe)
    mapped_once = maybe_value.map(ap_result)
    filtered_once = maybe_value.filter(ap_result)

    # Map again and apply again to confirm repeated operations are consistent
    mapped_twice = maybe_value.map(ap_result)
    ap_result_second = maybe_value.ap(input_str)

    # Verify the two ap results are equal
    ap_results_equal = ap_result.__eq__(ap_result_second)

    # Filter the first ap result using the unwrapped value
    filtered_ap = ap_result.filter(unwrapped)

    # Get the value of the second ap result with a fallback
    ap_second_unwrapped = ap_result_second.get_or_else(input_str)

    # Construct a second Maybe instance for conversion tests
    maybe_value_2 = maybe.Maybe(input_str, input_str)

    # Convert to Validation, then bind with the validation result
    validation = maybe_value_2.to_validation()
    bound = maybe_value_2.bind(validation)

    # Convert the bound result to an Either
    either_result = bound.to_either()

def test_maybe_eq_returns_false_when_compared_to_set():
    """Test that Maybe.__eq__ returns False when compared to a set (non-Maybe value)."""
    # A set containing a single unique value (False deduplicated)
    false_value = False
    comparison_set = {false_value, false_value, false_value, false_value}

    # Create a Maybe instance with both value and fallback as None
    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Compare Maybe instance to a set; expected to return False (type mismatch)
    result = maybe_instance.__eq__(comparison_set)

def test_maybe_bind_map_then_invalid_method_on_set():
    """
    Test that chaining bind and map on a Maybe works as expected,
    and that calling a non-existent method (to_box) on a plain set
    raises an AttributeError, confirming set has no such interface.
    """
    # A simple truthy value used as both the value and the is_just flag
    is_just = True

    # Create a Maybe wrapping a truthy value, marked as 'just'
    maybe_value = maybe.Maybe(is_just, is_just)

    # Bind with a truthy callable — exercises the bind path
    bound = maybe_value.bind(is_just)

    # Map with a truthy callable — exercises the map path
    mapped = bound.map(is_just)

    # A tuple used as the wrapped value in a second Maybe
    tuple_value = (is_just, is_just, is_just, is_just)

    # Create another Maybe wrapping the tuple, marked as 'just'
    maybe_tuple = maybe.Maybe(tuple_value, is_just)

    # A plain empty set — has no to_box() method
    empty_set = set()

    # Calling to_box() on a set should raise AttributeError;
    # this exercises the error path for unsupported operations
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with a False callable on a Maybe wrapping None."""
    # Create a Maybe instance wrapping None with strict mode disabled
    none_value = None
    is_strict = False
    maybe_instance = maybe.Maybe(none_value, is_strict)

    # Attempt to map with False as the callable (exercises the map path for a None-wrapped Maybe)
    maybe_instance.map(is_strict)

def test_maybe_bind_with_empty_dict_on_none_value_maybe():
    """Test that calling bind on a Maybe wrapping None with an empty dict does not raise."""

    # Create a Maybe instance with a truthy value
    true_value = True
    maybe_with_value = maybe.Maybe(true_value, true_value)

    # Prepare an empty dict to use as the bind argument
    empty_dict = {}

    # Create a Maybe instance wrapping None with a falsy flag
    none_value = None
    false_value = False
    maybe_with_none = maybe.Maybe(none_value, false_value)

    # Bind the empty dict to the Maybe wrapping None
    maybe_with_none.bind(empty_dict)

def test_maybe_filter_and_ap_chaining_with_mixed_types():
    """
    Test chaining of filter and ap operations on Maybe instances
    constructed from mixed types (bytes, None, int, bool, lazy).
    Verifies that Maybe wrapping, filtering, lazy conversion, and
    applicative application compose without raising errors.
    """
    # Create a Maybe wrapping raw bytes with no fallback (None)
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_fallback = None
    maybe_bytes = maybe.Maybe(raw_bytes, no_fallback)

    # Convert the bytes-based Maybe to a Box
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an integer with a boolean fallback
    int_value = 0
    bool_fallback = True
    maybe_int = maybe.Maybe(int_value, bool_fallback)

    # Filter the int-based Maybe using itself as the predicate
    filtered_maybe = maybe_int.filter(maybe_int)

    # Convert the int-based Maybe to a lazy representation
    lazy_maybe = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes-based Maybe (ap combinator)
    applied_maybe = filtered_maybe.ap(maybe_bytes)

    # Filter the result of ap using the applied Maybe as the predicate
    filtered_applied = filtered_maybe.filter(applied_maybe)

    # Construct a new Maybe from the lazy value and the boxed bytes
    maybe_from_lazy = maybe.Maybe(lazy_maybe, boxed_bytes)

    # Check equality of the lazy Maybe against the boolean fallback
    lazy_eq_bool = lazy_maybe.__eq__(bool_fallback)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() on a Maybe wrapping None (with False flag) with an integer argument executes without error."""
    integer_value = 2862
    none_value = None
    is_something = False

    # Create a Maybe instance wrapping None with the 'is_something' flag set to False
    maybe_instance = maybe.Maybe(none_value, is_something)

    # Apply the integer value to the Maybe instance via ap()
    maybe_instance.ap(integer_value)

def test_maybe_filter_and_lazy_map_chaining():
    """Test chaining of filter, to_lazy, and map operations on Maybe instances,
    including nested filtering and conversion to Try."""

    # Create a Maybe wrapping integer 0 with a truthy flag
    initial_value = 0
    is_present = True
    maybe_instance = maybe.Maybe(initial_value, is_present)

    # Apply filter using the Maybe instance itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the original Maybe to a lazy representation
    lazy_from_original = maybe_instance.to_lazy()

    # Convert the filtered Maybe to a lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Apply filter on the filtered Maybe using the lazy version as predicate
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered result to a Try
    try_result = double_filtered.to_try()

    # Convert original Maybe to lazy again (independent chain)
    lazy_from_original_again = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself as the mapping function
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_on_none_value_with_lazy_conversion():
    """Test that filtering a Maybe wrapping None (with bool flag True) and converting
    to lazy, then filtering again from a Maybe wrapping None/None, does not raise
    and completes without error."""

    # Construct a tuple of repeated negative ints to use as the filter argument
    negative_int = -283
    filter_arg = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with the 'some' flag set to True
    none_value = None
    some_flag = True
    maybe_none_with_flag = maybe.Maybe(none_value, some_flag)

    # Apply filter with the tuple argument; result is still a Maybe
    filtered_maybe = maybe_none_with_flag.filter(filter_arg)

    # Convert the filtered Maybe to a lazy representation
    lazy_maybe = filtered_maybe.to_lazy()

    # Create a second Maybe wrapping None with no flag (both args None)
    none_value_2 = None
    maybe_none_plain = maybe.Maybe(none_value_2, none_value_2)

    # Filter the plain None Maybe using the lazy Maybe as argument
    maybe_none_plain.filter(lazy_maybe)

def test_maybe_get_or_else_and_filter_with_complex_values():
    """
    Test that Maybe correctly handles get_or_else on a tuple-based Maybe (present=True),
    and that filter can be applied on a Maybe wrapping a Generic instance (present=False).
    """
    # A fallback integer used with get_or_else
    fallback_int = 2281

    # A raw string value used to populate the tuple payload
    raw_str = "gZ(\\mOcN"
    nested_dict = {raw_str: raw_str}

    # Construct a tuple payload containing the string and nested dicts
    payload_tuple = (raw_str, raw_str, nested_dict, nested_dict)

    # Create a Maybe that is present (bool=True) wrapping the tuple payload
    is_present = True
    maybe_with_value = maybe.Maybe(payload_tuple, is_present)

    # get_or_else should return the wrapped value since the Maybe is present
    resolved_value = maybe_with_value.get_or_else(fallback_int)

    # A generic object used as the value for an absent Maybe
    generic_obj = typing.Generic()

    # Create a Maybe that is absent (bool=False) wrapping the generic object
    is_absent = False
    var_1 = maybe_with_value.to_box()

    maybe_absent = maybe.Maybe(generic_obj, is_absent)

    # Apply filter using the resolved value from the present Maybe
    maybe_absent.filter(resolved_value)

def test_maybe_to_validation_and_chained_operations():
    """
    Test that Maybe wrapping various value/error combinations correctly
    supports to_validation(), get_or_else(), to_try(), and bind() operations
    across multiple Maybe instances.
    """
    # Create a Maybe with a truthy value and no error
    is_valid = True
    no_error = None
    maybe_valid = maybe.Maybe(is_valid, no_error)
    validation_from_valid = maybe_valid.to_validation()

    # Create a Maybe with a negative integer value and an empty tuple as error
    negative_int = -1784
    empty_tuple = ()
    maybe_int = maybe.Maybe(negative_int, empty_tuple)

    # Exercise core Maybe operations on the integer-valued instance
    validation_from_int = maybe_int.to_validation()
    fallback_value = maybe_int.get_or_else(negative_int)
    try_from_int = maybe_int.to_try()

    # Create a Maybe with a float value and a float error (both same value)
    negative_float = -286.64
    maybe_float = maybe.Maybe(negative_float, negative_float)

    # Bind the try result onto the integer Maybe
    maybe_int.bind(try_from_int)

def test_maybe_map_with_none_value_and_maybe_to_either_with_int():
    """
    Test that Maybe.map() can be called with a non-callable (set) when wrapping None,
    and that Maybe.to_either() works correctly when wrapping a negative integer.
    """
    # Create a Maybe wrapping None with has_value=True
    none_value = None
    has_value = True
    maybe_wrapping_none = maybe.Maybe(none_value, has_value)

    # Attempt to map over the Maybe using a set (non-callable mapper)
    mapper_set = {has_value}
    map_result = maybe_wrapping_none.map(mapper_set)

    # Create a Maybe wrapping a negative integer with has_value=True
    negative_int = -1095
    has_value_2 = True
    maybe_wrapping_int = maybe.Maybe(negative_int, has_value_2)

    # Convert the Maybe wrapping an integer to an Either
    either_result = maybe_wrapping_int.to_either()

def test_maybe_conversions_with_none_and_nested_maybe():
    """
    Test that Maybe instances constructed with None values and nested Maybe
    values can be converted to lazy, either, and try representations without
    error, and that the resulting Try can also be converted to lazy.
    """
    # Create a Maybe wrapping two None values
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Wrap the first Maybe in a tuple to use as a value in a second Maybe
    nested_maybe_tuple = (maybe_with_none,)

    # Convert the
# (Truncated by extractor)