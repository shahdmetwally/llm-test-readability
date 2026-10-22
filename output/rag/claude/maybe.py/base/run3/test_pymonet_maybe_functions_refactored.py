import pytest
import maybe as maybe
import typing as typing

def test_maybe_constructed_with_bytes_arguments():
    """Test that Maybe can be instantiated with identical byte sequences as both arguments."""

    # Use a raw byte sequence as both positional arguments to Maybe
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    result = maybe.Maybe(raw_bytes, raw_bytes)

def test_maybe_initialized_with_none_values():
    """Test that Maybe can be instantiated with None as both arguments."""
    first_value = None
    second_value = None

    # Create a Maybe instance with both arguments set to None
    result = maybe.Maybe(first_value, second_value)

def test_maybe_chained_operations_with_string_value():
    """
    Test that a Maybe monad instance correctly supports chained operations
    (ap, get_or_else, map, filter, bind, to_validation, to_either)
    when constructed with a string value, and that derived Maybe instances
    behave consistently across equality checks and transformations.
    """
    input_str = "p4xa>bl^oP"

    # Create a Maybe wrapping the input string
    maybe_instance = maybe.Maybe(input_str, input_str)

    # Check equality of the Maybe with the raw string
    is_equal = maybe_instance.__eq__(input_str)

    # Apply ap, get_or_else, map, and filter on the primary Maybe
    ap_result = maybe_instance.ap(input_str)
    unwrapped_value = maybe_instance.get_or_else(input_str)
    mapped_result = maybe_instance.map(ap_result)
    filtered_result = maybe_instance.filter(ap_result)

    # Repeated map and ap to verify consistent behaviour
    mapped_result_2 = maybe_instance.map(ap_result)
    ap_result_2 = maybe_instance.ap(input_str)

    # Verify equality between two ap results
    ap_results_equal = ap_result.__eq__(ap_result_2)

    # Filter the first ap result using the unwrapped value
    filtered_ap = ap_result.filter(unwrapped_value)

    # Retrieve the fallback value from the second ap result
    ap_2_fallback = ap_result_2.get_or_else(input_str)

    # Create a second Maybe instance and convert it through validation and bind
    maybe_instance_2 = maybe.Maybe(input_str, input_str)
    validation = maybe_instance_2.to_validation()
    bound_result = maybe_instance_2.bind(validation)

    # Convert the bound result to an Either type
    either_result = bound_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set():
    """Test that Maybe.__eq__ returns False when compared to a set (non-Maybe value)."""
    # A set is not a valid Maybe value, so equality should not hold
    false_value = False
    non_maybe_set = {false_value, false_value, false_value, false_value}

    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Comparing a Maybe instance to a plain set should yield a falsy/non-equal result
    result = maybe_instance.__eq__(non_maybe_set)

def test_maybe_bind_and_map_with_invalid_set_operation():
    """
    Test that Maybe.bind and Maybe.map behave correctly with a True value,
    and that calling an undefined method (to_box) on a plain set raises AttributeError.
    """
    # Use True as the wrapped value and default for Maybe
    true_value = True
    maybe_instance = maybe.Maybe(true_value, true_value)

    # Bind the Maybe with the same boolean value
    bound_result = maybe_instance.bind(true_value)

    # Map over the bound result
    mapped_result = bound_result.map(true_value)

    # Create a tuple of True values to use as the wrapped value
    true_tuple = (true_value, true_value, true_value, true_value)
    maybe_with_tuple = maybe.Maybe(true_tuple, true_value)

    # Attempt to call a non-existent method on a plain set — expected to raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with False when initialized with None and False."""
    # Initialize Maybe with a None value and False to indicate no value is present
    none_value = None
    is_present = False
    maybe_instance = maybe.Maybe(none_value, is_present)

    # Attempt to map over the Maybe instance using False as the mapping function
    maybe_instance.map(is_present)

def test_maybe_bind_on_falsy_maybe_with_empty_dict():
    """Test that calling bind on a Maybe wrapping None/False with an empty dict
    does not raise and behaves consistently with a falsy Maybe value."""

    # Create a truthy Maybe instance (both value and flag are True)
    truthy_maybe = maybe.Maybe(True, True)

    # Prepare an empty dict to use as the bind argument
    empty_dict = {}

    # Create a falsy Maybe instance with None as value and False as the flag
    falsy_maybe = maybe.Maybe(None, False)

    # Bind the empty dict to the falsy Maybe; no assertion expected,
    # verifying the call completes without error
    falsy_maybe.bind(empty_dict)

def test_maybe_filter_and_ap_with_mixed_types():
    """
    Test that Maybe correctly handles filter and ap operations
    when constructed with mixed types (bytes/None and int/bool),
    including chaining filter with ap and equality checks on lazy values.
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

    # Filter the int Maybe using itself as the predicate
    filtered_int = maybe_int.filter(maybe_int)

    # Convert the int Maybe to a lazy representation
    lazy_int = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes Maybe
    applied_result = filtered_int.ap(maybe_bytes)

    # Filter the filtered Maybe using the applied result
    filtered_again = filtered_int.filter(applied_result)

    # Create a Maybe wrapping the lazy value and the boxed bytes
    maybe_lazy = maybe.Maybe(lazy_int, boxed_bytes)

    # Check equality of the lazy value against the bool fallback
    lazy_eq_bool = lazy_int.__eq__(bool_fallback)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that Maybe.ap() can be called on a Maybe wrapping None with
    strict=False, using an integer as the applicative argument."""
    int_value = 2862
    none_value = None
    is_strict = False

    # Construct a Maybe with no value and strict mode disabled
    maybe_instance = maybe.Maybe(none_value, is_strict)

    # Apply the integer argument to the Maybe instance
    maybe_instance.ap(int_value)

def test_maybe_filter_and_lazy_chaining_with_map():
    """Test chaining filter, to_lazy, and map operations on Maybe instances."""
    # Create a Maybe wrapping integer 0 with a truthy flag
    int_val = 0
    is_present = True
    maybe_val = maybe.Maybe(int_val, is_present)

    # Apply filter using maybe_val itself as the predicate
    filtered_maybe = maybe_val.filter(maybe_val)

    # Convert original maybe to lazy
    lazy_from_maybe = maybe_val.to_lazy()

    # Convert filtered result to lazy
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Apply filter on filtered_maybe using the lazy version as predicate
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert double-filtered result to a Try
    try_val = double_filtered.to_try()

    # Convert original maybe to lazy again (independent chain)
    lazy_from_maybe_again = maybe_val.to_lazy()

    # Map filtered_maybe over itself
    mapped_val = filtered_maybe.map(filtered_maybe)

def test_filter_on_none_valued_maybe_returns_lazy_and_filters_again():
    """
    Test that filtering a Maybe wrapping None with a tuple value produces a
    lazy result, and that a second Maybe wrapping None can be filtered with
    that lazy result without error.
    """
    negative_int = -283
    filter_tuple = (negative_int, negative_int, negative_int)

    # Create a Maybe with no value (None) but marked as having a value (True)
    maybe_with_none_value = maybe.Maybe(None, True)

    # Filter the Maybe using the tuple; result represents a filtered Maybe
    filtered_maybe = maybe_with_none_value.filter(filter_tuple)

    # Convert the filtered result to a lazy representation
    lazy_filtered = filtered_maybe.to_lazy()

    # Create a second Maybe where both value and flag are None
    empty_maybe = maybe.Maybe(None, None)

    # Filter the empty Maybe using the lazy filtered result
    empty_maybe.filter(lazy_filtered)

def test_maybe_chained_operations_with_false_values():
    """
    Test that Maybe can be constructed with False values and that chained
    operations (equality check, to_either, to_lazy, to_validation, and map)
    execute without error when all inputs are False/falsy.
    """
    false_value = False

    # Create a Maybe with False for both arguments and check equality
    maybe_false = maybe.Maybe(false_value, false_value)
    eq_result = maybe_false.__eq__(false_value)

    # Create a second Maybe and convert it through the monad chain
    maybe_second = maybe.Maybe(false_value, false_value)
    either_result = maybe_second.to_either()
    lazy_result = maybe_second.to_lazy()

    # Convert the lazy result to a validation object
    validation_result = lazy_result.to_validation()

    # Create a third Maybe and map the validation over it
    maybe_third = maybe.Maybe(false_value, false_value)
    maybe_third.map(validation_result)

def test_maybe_equality_and_chain_to_try_to_validation():
    """Test that a Maybe wrapping False can be compared to itself,
    converted to a Try, and then converted to a Validation without error."""

    # Create a Maybe wrapping False for both value and error slots
    false_value = False
    maybe_instance = maybe.Maybe(false_value, false_value)

    # Verify the Maybe considers itself equal to itself
    is_equal = maybe_instance.__eq__(maybe_instance)

    # Convert Maybe to Try, then chain to Validation
    try_instance = maybe_instance.to_try()
    try_instance.to_validation()

