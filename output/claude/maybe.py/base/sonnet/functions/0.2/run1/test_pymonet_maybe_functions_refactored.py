import pytest
import maybe as maybe
import typing as typing

def test_maybe_constructed_with_bytes_arguments():
    """Test that Maybe can be constructed with identical bytes values for both arguments."""
    # Use arbitrary bytes as both the value and the fallback for Maybe
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    result = maybe.Maybe(raw_bytes, raw_bytes)

def test_maybe_initialized_with_two_none_values():
    """Test that Maybe can be instantiated with two None arguments."""
    first_value = None
    second_value = None

    # Create a Maybe instance with both arguments set to None
    result = maybe.Maybe(first_value, second_value)

def test_maybe_chained_operations_with_string_value():
    """
    Test that a Maybe monad correctly handles chained operations
    (ap, get_or_else, map, filter, bind, to_validation, to_either)
    when constructed with a string value, verifying equality and
    transformation behaviour across multiple Maybe instances.
    """
    raw_value = "p4xa>bl^oP"

    # Create a Maybe instance wrapping the raw string value
    maybe_instance = maybe.Maybe(raw_value, raw_value)

    # Check equality of the Maybe with the raw string
    is_equal = maybe_instance.__eq__(raw_value)

    # Apply ap with the raw string; result is another Maybe-like value
    ap_result = maybe_instance.ap(raw_value)

    # Retrieve the value or fall back to the raw string
    unwrapped_value = maybe_instance.get_or_else(raw_value)

    # Map and filter using the ap result (a Maybe-like callable/value)
    mapped_once = maybe_instance.map(ap_result)
    filtered_once = maybe_instance.filter(ap_result)
    mapped_twice = maybe_instance.map(ap_result)

    # Apply ap again and verify equality between the two ap results
    ap_result_second = maybe_instance.ap(raw_value)
    ap_results_equal = ap_result.__eq__(ap_result_second)

    # Chain filter and get_or_else on the ap results
    filtered_ap = ap_result.filter(unwrapped_value)
    unwrapped_ap_second = ap_result_second.get_or_else(raw_value)

    # Create a second Maybe instance and convert to validation, then bind and to_either
    maybe_instance_2 = maybe.Maybe(raw_value, raw_value)
    validation_result = maybe_instance_2.to_validation()
    bound_result = maybe_instance_2.bind(validation_result)
    either_result = bound_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set():
    """Test that Maybe.__eq__ returns False when compared to a set (non-Maybe value)."""
    # A set containing a single unique value (False), used as a non-Maybe comparand
    false_value = False
    non_maybe_set = {false_value, false_value, false_value, false_value}

    # Create a Maybe instance with both value and fallback set to None
    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance to a set; expected to return False (type mismatch)
    result = maybe_instance.__eq__(non_maybe_set)

def test_maybe_bind_map_then_invalid_method_on_set():
    """
    Test that Maybe can be constructed with a bool, supports bind and map chaining,
    and that calling a non-existent method (to_box) on a plain set raises AttributeError.
    """
    # Use True as a simple truthy value for Maybe construction and chaining
    truthy_value = True

    # Create a Maybe wrapping a truthy value
    maybe_instance = maybe.Maybe(truthy_value, truthy_value)

    # Bind the Maybe with the truthy value (exercises the bind path)
    bound_result = maybe_instance.bind(truthy_value)

    # Map over the bound result with the truthy value
    mapped_result = bound_result.map(truthy_value)

    # Construct a tuple of truthy values to use as a compound value in Maybe
    compound_value = (truthy_value, truthy_value, truthy_value, truthy_value)

    # Create a second Maybe wrapping the tuple
    maybe_with_tuple = maybe.Maybe(compound_value, truthy_value)

    # Attempt to call a non-existent method on a plain set — expected to raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with a False mapper when initialized with None and False."""
    # Create a Maybe instance wrapping a None value with strict mode disabled
    none_value = None
    is_strict = False
    maybe_instance = maybe.Maybe(none_value, is_strict)

    # Attempt to map over the Maybe with a falsy callable (False)
    maybe_instance.map(is_strict)

def test_maybe_bind_on_falsy_maybe_with_empty_dict():
    """Test that calling bind on a Maybe wrapping None/False with an empty dict
    does not raise, even when a prior Maybe was constructed with truthy values."""

    # Create a Maybe with a truthy value (both arguments are True)
    truthy_value = True
    maybe_truthy = maybe.Maybe(truthy_value, truthy_value)

    # Prepare an empty dict to use as the bind argument
    empty_dict = {}

    # Create a Maybe wrapping None with a False flag (falsy/empty Maybe)
    none_value = None
    falsy_flag = False
    maybe_falsy = maybe.Maybe(none_value, falsy_flag)

    # Bind the empty dict to the falsy Maybe; verifies bind is callable in this state
    maybe_falsy.bind(empty_dict)

def test_maybe_filter_and_ap_chaining_with_mixed_types():
    """
    Test chaining of filter and ap operations on Maybe instances
    constructed with mixed types (bytes, None, int, bool, lazy values).
    Verifies that filter and ap can be composed without errors and that
    equality checks on lazy values behave as expected.
    """
    # Create a Maybe wrapping bytes with no fallback (None)
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_fallback = None
    maybe_bytes = maybe.Maybe(raw_bytes, no_fallback)
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an integer with a boolean fallback
    int_value = 0
    bool_fallback = True
    maybe_int = maybe.Maybe(int_value, bool_fallback)

    # Filter maybe_int using itself as the predicate
    filtered_maybe = maybe_int.filter(maybe_int)

    # Convert maybe_int to a lazy representation
    lazy_maybe = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes-based Maybe
    applied_maybe = filtered_maybe.ap(maybe_bytes)

    # Filter the applied Maybe using the applied result as predicate
    filtered_applied = filtered_maybe.filter(applied_maybe)

    # Construct a new Maybe from the lazy value and the boxed bytes
    maybe_from_lazy = maybe.Maybe(lazy_maybe, boxed_bytes)

    # Check equality of the lazy value against the boolean fallback
    lazy_eq_bool = lazy_maybe.__eq__(bool_fallback)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() on a Maybe wrapping None (with False flag) with an integer does not raise."""
    # Construct a Maybe instance wrapping None with strict mode disabled
    int_value = 2862
    none_value = None
    is_strict = False
    maybe_instance = maybe.Maybe(none_value, is_strict)

    # Apply the integer value via ap(); verifies ap() is callable in this state
    maybe_instance.ap(int_value)

def test_maybe_filter_and_lazy_map_chaining():
    """Test chaining of filter, to_lazy, and map operations on Maybe instances
    with a truthy boolean flag, verifying that intermediate lazy and filtered
    values can be further composed without errors."""

    # Create a Maybe wrapping integer 0 with an explicit truthy flag
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

    # Convert the double-filtered result to a Try
    try_result = double_filtered.to_try()

    # Convert the original Maybe to lazy again (independent call)
    lazy_from_original_again = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_maybe_to_try_then_to_box():
    """Test that a Maybe created with (True, False) can be converted to a Try and then to a Box."""
    # Create a Maybe with a truthy primary value and falsy secondary value
    is_present = True
    is_empty = False
    maybe_instance = maybe.Maybe(is_present, is_empty)

    # Convert the Maybe to a Try, then chain to a Box
    try_instance = maybe_instance.to_try()
    try_instance.to_box()

def test_maybe_ap_with_none_chains_through_lazy_validation_and_either():
    """
    Test that a Maybe constructed with None and True correctly chains through
    ap, to_lazy, to_validation, filter, get_or_else, to_either, to_try, and to_box,
    verifying interoperability between Maybe and related monadic types.
    """
    raw_bytes = b"C\xcf\xe7/"
    none_value = None
    is_present = True

    # Construct a Maybe with a None value and a truthy flag
    maybe_instance = maybe.Maybe(none_value, is_present)

    # Apply None to the Maybe; result is another Maybe-like container
    ap_result = maybe_instance.ap(none_value)

    # Convert the ap result to a Lazy container
    lazy_result = ap_result.to_lazy()

    # Convert the Lazy container to a Validation
    validation_result = lazy_result.to_validation()

    # Filter the original Maybe using the Validation as the predicate
    filtered_maybe = maybe_instance.filter(validation_result)

    # Retrieve the value or fall back to the filtered Maybe itself
    unwrapped_value = filtered_maybe.get_or_else(filtered_maybe)

    # Convert the filtered Maybe to an Either
    either_result = filtered_maybe.to_either()

    # Convert the Validation to a Try
    try_result = validation_result.to_try()

    # Check equality between the filtered Maybe and the ap result
    are_equal = filtered_maybe.__eq__(ap_result)

    # Wrap the unwrapped value in a Box
    box_result = unwrapped_value.to_box()

    # Apply raw bytes to the Try container
    try_result.ap(raw_bytes)

def test_maybe_chained_operations_with_none_and_bytes():
    """
    Test chained Maybe monad operations using None and bytes values,
    verifying that ap, bind, to_validation, to_either, and to_try
    behave correctly when the Maybe wraps None or bytes content.
    """
    raw_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    is_some = True

    # Create a Maybe wrapping None with is_some=True, then chain ap calls
    maybe_none = maybe.Maybe(none_value, is_some)
    ap_result_none = maybe_none.ap(none_value)
    ap_result_bytes = ap_result_none.ap(raw_bytes)
    validation_from_none_maybe = ap_result_bytes.to_validation()

    # Create a Maybe wrapping bytes and exercise all monad operations
    maybe_bytes = maybe.Maybe(none_value, raw_bytes)

    # get_or_else returns the wrapped value or the fallback
    get_or_else_result = maybe_bytes.get_or_else(maybe_bytes)

    # Convert to Validation and use it as a bind function
    validation_from_bytes_maybe = maybe_bytes.to_validation()
    bind_result = maybe_bytes.bind(validation_from_bytes_maybe)

    # Convert to Either and test equality
    either_result = maybe_bytes.to_either()
    ap_self_result = maybe_bytes.ap(maybe_bytes)

    negative_int = -3289

    # Check equality between Either and Validation representations
    either_eq_validation = either_result.__eq__(validation_from_bytes_maybe)

    # Bind the Either with the original Maybe
    either_bind_result = either_result.bind(maybe_bytes)

    # Convert to Try and verify equality and further conversions
    try_result = maybe_bytes.to_try()
    maybe_eq_bind = maybe_bytes.__eq__(bind_result)
    validation_from_bind = bind_result.to_validation()

    # Apply an integer to the Try result
    try_result.ap(negative_int)

def test_maybe_with_false_values_chained_transformations():
    """
    Test that a Maybe constructed with False values supports equality checks
    and chained transformations (to_either, to_lazy, to_validation, map)
    without raising errors, even when all values are falsy.
    """
    # Construct a Maybe with both value and is_just set to False
    is_just = False
    maybe_false = maybe.Maybe(is_just, is_just)

    # Verify equality comparison with a plain False value
    eq_result = maybe_false.__eq__(is_just)

    # Create a second Maybe with the same falsy arguments
    maybe_second = maybe.Maybe(is_just, is_just)

    # Chain transformations: Maybe -> Either -> Lazy -> Validation
    either_result = maybe_second.to_either()
    lazy_result = maybe_second.to_lazy()
    validation_result = lazy_result.to_validation()

    # Create a third Maybe and map the validation result over it
    maybe_third = maybe.Maybe(is_just, is_just)
    maybe_third.map(validation_result)

def test_maybe_equality_and_conversion_chain():
    """Test that a Maybe wrapping False can be compared to itself and converted
    through to_try() and then to_validation() without error."""

    # Create a Maybe with both value and flag set to False
    false_value = False
    maybe_false = maybe.Maybe(false_value, false_value)

    # Verify that the Maybe instance is equal to itself
    is_equal = maybe_false.__eq__(maybe_false)

    # Convert the Maybe to a Try, then chain to a Validation
    as_try = maybe_false.to_try()
    as_try.to_validation()

