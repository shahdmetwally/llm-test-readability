import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with identical bytes values for both arguments."""
    # Use a raw bytes object as both arguments to Maybe
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

    # Apply ap, get_or_else, map, and filter operations on the first Maybe
    ap_result = maybe_instance.ap(raw_value)
    unwrapped_value = maybe_instance.get_or_else(raw_value)
    mapped_result = maybe_instance.map(ap_result)
    filtered_result = maybe_instance.filter(ap_result)

    # Repeat map and ap to verify consistent behaviour
    remapped_result = maybe_instance.map(ap_result)
    reapplied_result = maybe_instance.ap(raw_value)

    # Verify equality between two ap results
    ap_results_equal = ap_result.__eq__(reapplied_result)

    # Chain filter and get_or_else on the ap results
    filtered_ap = ap_result.filter(unwrapped_value)
    fallback_value = reapplied_result.get_or_else(raw_value)

    # Create a second Maybe instance and convert to validation, then bind and to_either
    maybe_instance_2 = maybe.Maybe(raw_value, raw_value)
    validation_result = maybe_instance_2.to_validation()
    bound_result = maybe_instance_2.bind(validation_result)
    either_result = bound_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set():
    """Test that Maybe.__eq__ returns False when compared to a set (non-Maybe value)."""

    # A set containing a single unique value (False deduplicated)
    false_value = False
    comparison_set = {false_value, false_value, false_value, false_value}

    # Create a Maybe instance with both value and default set to None
    none_value = None
    maybe_instance = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance to a set; expected to be unequal (not a Maybe)
    result = maybe_instance.__eq__(comparison_set)

def test_maybe_bind_map_then_invalid_method_on_set():
    """
    Test that Maybe can be constructed with a bool, supports bind and map chaining,
    and that calling a non-existent method (to_box) on a plain set raises AttributeError.
    """
    # Use True as a stand-in value for both the value and is_just flag
    is_just = True

    # Create a Maybe wrapping a truthy value
    maybe_value = maybe.Maybe(is_just, is_just)

    # Bind with a truthy value (bool acts as the transform here)
    bound = maybe_value.bind(is_just)

    # Map over the bound result with a truthy value
    mapped = bound.map(is_just)

    # Create a tuple of booleans to use as a compound value
    tuple_value = (is_just, is_just, is_just, is_just)

    # Construct another Maybe using the tuple as the value
    maybe_tuple = maybe.Maybe(tuple_value, is_just)

    # Attempt to call a non-existent method on a plain set — expected to raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe.map can be called with a False bool when initialized with None and False."""
    # Initialize Maybe with a None value and False as the boolean flag
    none_value = None
    flag = False
    maybe_instance = maybe.Maybe(none_value, flag)

    # Invoke map with the False flag; verifies map accepts a falsy argument without error
    maybe_instance.map(flag)

def test_maybe_bind_on_none_value_maybe():
    """Test that calling bind on a Maybe wrapping None does not raise,
    even when the other Maybe wraps a valid truthy value."""

    # Create a Maybe wrapping a truthy value (both value and flag are True)
    truthy_value = True
    maybe_with_value = maybe.Maybe(truthy_value, truthy_value)

    # Prepare an empty dict to use as the bind argument
    empty_dict = {}

    # Create a Maybe wrapping None with a False flag
    none_value = None
    falsy_flag = False
    maybe_with_none = maybe.Maybe(none_value, falsy_flag)

    # Bind the empty dict to the Maybe that wraps None
    maybe_with_none.bind(empty_dict)

def test_maybe_filter_and_ap_chaining_with_mixed_types():
    """
    Test chaining of filter and ap operations on Maybe instances
    constructed with mixed value/context types (bytes, None, int, bool).
    Verifies that filter and ap can be composed without raising errors,
    and that equality comparison on a lazy Maybe works as expected.
    """
    # Create a Maybe wrapping bytes with no context (None)
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_context = None
    maybe_bytes = maybe.Maybe(raw_bytes, no_context)
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an integer with a boolean context
    int_value = 0
    bool_context = True
    maybe_int = maybe.Maybe(int_value, bool_context)

    # Apply filter using maybe_int itself as the predicate
    filtered_maybe = maybe_int.filter(maybe_int)

    # Convert maybe_int to a lazy representation
    lazy_maybe = maybe_int.to_lazy()

    # Apply the filtered Maybe as a function over the bytes Maybe
    applied_result = filtered_maybe.ap(maybe_bytes)

    # Filter the applied result using the previously applied result
    double_filtered = filtered_maybe.filter(applied_result)

    # Construct a new Maybe from the lazy value and the boxed bytes
    maybe_from_lazy = maybe.Maybe(lazy_maybe, boxed_bytes)

    # Check equality of the lazy Maybe against the boolean context
    lazy_eq_bool = lazy_maybe.__eq__(bool_context)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() on a Maybe wrapping None (with False flag) with an integer does not raise unexpectedly."""
    int_value = 2862
    none_value = None
    is_valid = False

    # Construct a Maybe wrapping None with the False flag
    maybe_instance = maybe.Maybe(none_value, is_valid)

    # Apply the integer value to the Maybe instance
    maybe_instance.ap(int_value)

def test_maybe_filter_and_lazy_map_chaining():
    """Test chaining filter, to_lazy, and map operations on Maybe instances
    with a truthy boolean value, verifying that intermediate lazy and
    filtered results can be further composed without error."""

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

    # Filter the filtered Maybe using the lazy version of the filtered Maybe
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered result to a Try
    try_result = double_filtered.to_try()

    # Convert the original Maybe to lazy again (independent call)
    lazy_from_original_again = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_filter_on_maybe_with_none_value_returns_lazy():
    """Test that filtering a Maybe wrapping None with a tuple value produces
    a lazy result, and that filtering another None-valued Maybe with that
    lazy result completes without error."""

    # Construct a tuple to use as the filter argument
    sentinel_int = -283
    filter_arg = (sentinel_int, sentinel_int, sentinel_int)

    # Create a Maybe wrapping None with truthy flag, then filter with the tuple
    none_value = None
    truthy_flag = True
    maybe_with_none = maybe.Maybe(none_value, truthy_flag)
    filter_result = maybe_with_none.filter(filter_arg)

    # Convert the filter result to a lazy representation
    lazy_result = filter_result.to_lazy()

    # Create a second Maybe wrapping None (no truthy flag), then filter with the lazy result
    none_value_2 = None
    maybe_all_none = maybe.Maybe(none_value_2, none_value_2)
    maybe_all_none.filter(lazy_result)

def test_maybe_get_or_else_and_filter_with_generic():
    """
    Test that Maybe wrapping a tuple returns the default value via get_or_else,
    and that a second Maybe wrapping a Generic can be filtered using that result.
    """
    default_int = 2281
    raw_str = "gZ(\\mOcN"
    str_dict = {raw_str: raw_str}

    # A tuple payload containing strings and dicts, used to construct a truthy Maybe
    tuple_payload = (raw_str, raw_str, str_dict, str_dict)
    is_present = True
    maybe_with_tuple = maybe.Maybe(tuple_payload, is_present)

    # get_or_else should return the wrapped value (or default if absent)
    resolved_value = maybe_with_tuple.get_or_else(default_int)

    # A Generic instance used as the payload for a second Maybe
    generic_instance = typing.Generic()
    is_absent = False
    maybe_with_tuple.to_box()

    # A second Maybe wrapping a Generic, filtered using the resolved value
    maybe_with_generic = maybe.Maybe(generic_instance, is_absent)
    maybe_with_generic.filter(resolved_value)

def test_maybe_to_validation_and_bind_with_various_types():
    """
    Test that Maybe instances with different value/fallback types correctly
    support to_validation(), get_or_else(), to_try(), and bind() operations.
    """
    # Create a Maybe with a truthy value and no fallback
    is_valid = True
    no_fallback = None
    maybe_truthy = maybe.Maybe(is_valid, no_fallback)
    validation_from_truthy = maybe_truthy.to_validation()

    # Create a Maybe with a negative integer value and an empty tuple as fallback
    negative_int = -1784
    empty_tuple = ()
    maybe_int = maybe.Maybe(negative_int, empty_tuple)

    # Exercise core Maybe operations on the integer Maybe
    validation_from_int = maybe_int.to_validation()
    value_or_default = maybe_int.get_or_else(negative_int)
    try_from_int = maybe_int.to_try()

    # Create a Maybe with a float value and float fallback
    negative_float = -286.64
    maybe_float = maybe.Maybe(negative_float, negative_float)

    # Bind the try result onto the integer Maybe
    maybe_int.bind(try_from_int)

def test_maybe_map_with_none_value_and_to_either_conversion():
    """
    Test that Maybe.map() can be called with a non-callable (set) when the
    wrapped value is None, and that Maybe.to_either() works correctly when
    wrapping a negative integer value.
    """
    # Create a Maybe wrapping None with has_value=True
    none_value = None
    has_value = True
    maybe_with_none = maybe.Maybe(none_value, has_value)

    # Attempt to map over the Maybe using a set (non-callable) as the mapper
    mapper_set = {has_value}
    result_map = maybe_with_none.map(mapper_set)

    # Create a Maybe wrapping a negative integer with has_value=True
    negative_int = -1095
    has_value_2 = True
    maybe_with_int = maybe.Maybe(negative_int, has_value_2)

    # Convert the Maybe wrapping a negative integer to an Either
    result_either = maybe_with_int.to_either()

def test_maybe_conversions_with_none_and_false_values():
    """
    Test that Maybe instances constructed with None and False values
    can be converted to lazy, either, and try representations without error.
    Verifies chaining of to_lazy(), to_either(), and to_try() on Maybe objects
    holding None (as both value and fallback) and a tuple with False as fallback.
    """
    # Create a Maybe with None as both value and fallback
    maybe_none = maybe.Maybe(None, None)

    # Wrap the first Maybe in a tuple to use as a value in a second Maybe
    tuple_containing_maybe = (maybe_none,)

    # Convert the None-valued Maybe to a lazy representation
    lazy_from_none_maybe = maybe_none.to_lazy()

    # Create a Maybe with a tuple value and False as the fallback
    maybe_tuple_with_false = maybe.Maybe(tuple_containing_maybe, False)

    # Convert the None-valued Maybe to an either representation
    either_from_none_maybe = maybe_none.to_either()

    # Convert the tuple-valued Maybe to a try representation
    try_from_tuple_maybe = maybe_tuple_with_false.to_try()

    # Convert the None-valued Maybe to either again (second call)
    either_from_none_maybe_again = maybe_none.to_either()

    # Convert the tuple-valued Maybe to an either representation
    either_from_tuple_maybe = maybe_tuple_with_false.to_either()

    # Convert the try result to a lazy representation (chained conversion)
    try_from_tuple_maybe.to_lazy()

def test_maybe_to_try_then_to_box():
    """Test that a Maybe created with (True, False) can be converted to a Try and then to a Box."""
    is_value_present = True
    is_error = False

    # Create a Maybe with a positive value flag and no error
    maybe_instance = maybe.Maybe(is_value_present, is_error)

    # Convert the Maybe to a Try, then chain to a Box
    try_instance = maybe_instance.to_try()
    try_instance.to_box()

def test_maybe_ap_with_none_chains_through_lazy_validation_and_either():
    """
    Test that a Maybe constructed with None and True correctly chains through
    ap, to_lazy, to_validation, filter, get_or_else, to_either, to_try, and to_box,
    verifying interoperability between Maybe and related monadic types.
    """
    # Raw bytes value used as an argument to ap on the Try instance
    raw_bytes = b"C\xcf\xe7/"

    none_value = None
    flag = True

    # Construct a Maybe with no value (None) but a truthy flag
    maybe_instance = maybe.Maybe(none_value, flag)

    # Apply None as a function argument to the Maybe; result is another Maybe
    maybe_after_ap = maybe_instance.ap(none_value)

    # Convert the Maybe to a Lazy representation
    lazy_instance = maybe_after_ap.to_lazy()

    # Convert the Lazy instance to a Validation
    validation_instance = lazy_instance.to_validation()

    # Filter the original Maybe using the Validation as the predicate
    filtered_maybe = maybe_instance.filter(validation_instance)

    # Retrieve the value or fall back to the filtered Maybe itself
    value_or_else = filtered_maybe.get_or_else(filtered_maybe)

    # Convert the filtered Maybe to an Either
    either_instance = filtered_maybe.to_either()

    # Convert the Validation to a Try
    try_instance = validation_instance.to_try()

    # Check equality between the filtered Maybe and the Maybe-after-ap
    are_equal = filtered_maybe.__eq__(maybe_after_ap)

    # Convert the get_or_else result to a Box
    box_instance = value_or_else.to_box()

    # Apply raw bytes to the Try instance
    try_instance.ap(raw_bytes)

def test_maybe_chaining_with_none_value_and_bytes():
    """
    Test chaining of Maybe monad operations where the value is None or bytes.
    Verifies that ap, bind, to_validation, to_either, and to_try work correctly
    when Maybe wraps None or a bytes value, including equality checks across types.
    """
    raw_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    is_just = True

    # Create a Maybe with None value and is_just=True, then chain ap calls
    maybe_none_just = maybe.Maybe(none_value, is_just)
    ap_result_none = maybe_none_just.ap(none_value)
    ap_result_bytes = ap_result_none.ap(raw_bytes)
    validation_from_none_just = ap_result_bytes.to_validation()

    # Create a Maybe wrapping bytes directly
    maybe_bytes = maybe.Maybe(none_value, raw_bytes)

    # Exercise get_or_else, to_validation, bind, to_either, ap on maybe_bytes
    get_or_else_result = maybe_bytes.get_or_else(maybe_bytes)
    validation_from_bytes = maybe_bytes.to_validation()
    bind_result = maybe_bytes.bind(validation_from_bytes)
    either_result = maybe_bytes.to_either()
    ap_result_self = maybe_bytes.ap(maybe_bytes)

    negative_int = -3289

    # Check equality between either and validation results
    eq_either_validation = either_result.__eq__(validation_from_bytes)

    # Bind maybe_bytes into the either result
    either_bind_result = either_result.bind(maybe_bytes)

    # Convert maybe_bytes to Try and check equality with bind result
    try_result = maybe_bytes.to_try()
    eq_maybe_bind = maybe_bytes.__eq__(bind_result)

    # Convert bind result to validation
    validation_from_bind = bind_result.to_validation()

    # Apply a negative int to the try result (result intentionally unused)
    try_result.ap(negative_int)

def test_maybe_chained_transformations_with_false_values():
    """
    Test that a Maybe constructed with False values supports equality checks,
    conversion to Either, conversion to Lazy, and chained transformation to
    Validation, followed by mapping over another Maybe instance.
    """
    false_value = False

    # Create a Maybe with both 'value' and 'is_just' set to False
    maybe_false = maybe.Maybe(false_value, false_value)

    # Verify equality comparison with a False value
    eq_result = maybe_false.__eq__(false_value)

    # Create a second Maybe with False values and convert to Either
    maybe_for_conversion = maybe.Maybe(false_value, false_value)
    either_result = maybe_for_conversion.to_either()

    # Convert the same Maybe to a Lazy representation
    lazy_result = maybe_for_conversion.to_lazy()

    # Convert the Lazy result to a Validation
    validation_result = lazy_result.to_validation()

    # Create a third Maybe with False values and map the Validation over it
    maybe_for_mapping = maybe.Maybe(false_value, false_value)
    maybe_for_mapping.map(validation_result)

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

