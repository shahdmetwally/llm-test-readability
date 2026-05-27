import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with a bytes value provided as both constructor arguments."""
    # A raw bytes literal used as both positional arguments to Maybe
    raw_bytes_value = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Construct the Maybe instance — verifies no exception is raised during instantiation
    maybe_instance = maybe.Maybe(raw_bytes_value, raw_bytes_value)

def test_maybe_instantiation_with_none_arguments():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None as both arguments to verify the constructor accepts absent values
    none_value = None

    # Construct the Maybe instance with two None values
    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chaining_operations_with_string_value():
    """Test that a Maybe monad supports chaining of ap, map, filter, bind, to_validation, and to_either operations."""

    # Seed value used as both the value and default throughout the chain
    string_value = "p4xa>bl^oP"

    # Construct the primary Maybe instance with the string as both arguments
    maybe_instance = maybe.Maybe(string_value, string_value)

    # Check equality of the Maybe instance against the raw string
    eq_result = maybe_instance.__eq__(string_value)

    # Apply ap, get_or_else, map, and filter operations on the primary instance
    ap_result = maybe_instance.ap(string_value)
    get_or_else_result = maybe_instance.get_or_else(string_value)
    map_result_first = maybe_instance.map(ap_result)
    filter_result_first = maybe_instance.filter(ap_result)

    # Repeat map and ap to produce additional derived values
    map_result_second = maybe_instance.map(ap_result)
    ap_result_second = maybe_instance.ap(string_value)

    # Check equality between the two ap results
    ap_eq_result = ap_result.__eq__(ap_result_second)

    # Chain filter and get_or_else on the derived ap results
    filter_from_ap = ap_result.filter(get_or_else_result)
    get_or_else_from_ap_second = ap_result_second.get_or_else(string_value)

    # Construct a second Maybe instance and exercise to_validation, bind, and to_either
    maybe_instance_second = maybe.Maybe(string_value, string_value)
    validation_result = maybe_instance_second.to_validation()
    bind_result = maybe_instance_second.bind(validation_result)
    either_result = bind_result.to_either()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe constructed with None and False allows map() to be called with False without error."""
    # Prepare inputs: a None value and a False flag
    none_value = None
    false_flag = False

    # Construct a Maybe instance wrapping None with the False flag
    maybe_instance = maybe.Maybe(none_value, false_flag)

    # Invoke map() with the False flag — should execute without raising
    maybe_instance.map(false_flag)

def test_maybe_bind_with_none_value_and_empty_dict():
    """Test that bind can be called on a Maybe wrapping None with an empty dict argument."""

    # Construct a Maybe with a truthy value (created as part of the test setup)
    true_value = True
    maybe_with_true = maybe.Maybe(true_value, true_value)  # noqa: F841 — constructed but not further used

    # Prepare the argument to pass to bind
    empty_dict = {}

    # Construct a Maybe wrapping None with a falsy second argument
    none_value = None
    false_value = False
    maybe_with_none = maybe.Maybe(none_value, false_value)

    # Call bind on the Maybe wrapping None — should not raise
    maybe_with_none.bind(empty_dict)

def test_maybe_chained_monadic_operations_with_mixed_types():
    """Test that Maybe supports chained monadic operations (to_box, filter, to_lazy, ap, __eq__) across instances with mixed input types."""

    # Construct a Maybe wrapping a bytes value with no default
    raw_bytes_value = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_default = None
    maybe_bytes = maybe.Maybe(raw_bytes_value, no_default)

    # Convert the bytes Maybe to a boxed representation
    boxed_bytes = maybe_bytes.to_box()

    # Construct a Maybe wrapping an integer value with a boolean default
    zero_value = 0
    true_default = True
    maybe_int = maybe.Maybe(zero_value, true_default)

    # Filter maybe_int using itself as the predicate
    filtered_maybe_int = maybe_int.filter(maybe_int)

    # Convert maybe_int to a lazy representation
    lazy_maybe_int = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes Maybe
    applied_result = filtered_maybe_int.ap(maybe_bytes)

    # Filter the filtered Maybe using the applied result as the predicate
    filtered_applied = filtered_maybe_int.filter(applied_result)

    # Construct a Maybe wrapping the lazy and boxed results
    maybe_lazy_boxed = maybe.Maybe(lazy_maybe_int, boxed_bytes)

    # Compare the lazy Maybe to the boolean default using __eq__
    lazy_eq_true = lazy_maybe_int.__eq__(true_default)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() with an integer on a Maybe wrapping None and False does not raise."""
    # Integer argument to be passed to the ap() method
    int_argument = 2862

    # Construct a Maybe instance with None as the value and False as the flag
    none_value = None
    is_something = False
    maybe_instance = maybe.Maybe(none_value, is_something)

    # Call ap() with the integer argument on the Maybe instance
    maybe_instance.ap(int_argument)

def test_maybe_supports_chained_filter_lazy_map_and_to_try_operations():
    """Test that a Maybe instance correctly chains filter, to_lazy, map, and to_try operations."""
    # Set up the initial wrapped value and presence flag
    initial_value = 0
    is_present = True

    # Create a Maybe monad wrapping the initial integer value
    maybe_instance = maybe.Maybe(initial_value, is_present)

    # Filter the maybe using itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the original maybe to a lazy representation
    lazy_from_maybe = maybe_instance.to_lazy()

    # Convert the filtered maybe to a lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the filtered maybe using the lazy-filtered version as predicate
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered result to a Try
    try_result = double_filtered.to_try()

    # Convert the original maybe to lazy a second time
    lazy_from_maybe_again = maybe_instance.to_lazy()

    # Map the filtered maybe over itself
    mapped_result = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_with_none_value_and_lazy_conversion():
    """Test that filtering a None-valued Maybe and converting to lazy works,
    and that a fully-None Maybe can safely filter a lazy value."""

    # Set up a tuple of repeated negative integers to use as a filter argument
    negative_int = -283
    repeated_int_tuple = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with a True flag, then filter with the tuple
    none_value = None
    flag_true = True
    maybe_with_none_and_flag = maybe.Maybe(none_value, flag_true)
    filtered_maybe = maybe_with_none_and_flag.filter(repeated_int_tuple)

    # Convert the filtered result to a lazy representation
    lazy_filtered_maybe = filtered_maybe.to_lazy()

    # Create a fully-None Maybe and filter it using the lazy value
    none_value_2 = None
    maybe_with_all_none = maybe.Maybe(none_value_2, none_value_2)
    maybe_with_all_none.filter(lazy_filtered_maybe)

def test_maybe_get_or_else_and_filter_on_present_and_absent():
    """Test that a present Maybe resolves via get_or_else and to_box, and that filter can be called on an absent Maybe."""

    # Default fallback value used if Maybe is absent
    default_value = 2281

    # Build a tuple to use as the wrapped value inside a present Maybe
    sample_string = "gZ(\\mOcN"
    sample_dict = {sample_string: sample_string}
    wrapped_tuple = (sample_string, sample_string, sample_dict, sample_dict)

    # Construct a present Maybe (is_present=True) wrapping the tuple
    is_present = True
    present_maybe = maybe.Maybe(wrapped_tuple, is_present)

    # Resolve the present Maybe; should return the wrapped value, not the default
    resolved_value = present_maybe.get_or_else(default_value)

    # Create a Generic instance to serve as the value for an absent Maybe
    generic_instance = typing.Generic()

    # Convert the present Maybe to a Box representation
    boxed_value = present_maybe.to_box()

    # Construct an absent Maybe (is_absent=False) wrapping the generic instance
    is_absent = False
    absent_maybe = maybe.Maybe(generic_instance, is_absent)

    # Apply filter on the absent Maybe using the previously resolved value
    absent_maybe.filter(resolved_value)

def test_maybe_chained_operations_with_mixed_types():
    """Test that Maybe objects with mixed types support chained operations: to_validation, get_or_else, to_try, and bind."""

    # --- Maybe wrapping a bool value with a None fallback ---
    truthy_value = True
    none_fallback = None
    maybe_bool_none = maybe.Maybe(truthy_value, none_fallback)
    validation_from_bool_maybe = maybe_bool_none.to_validation()

    # --- Maybe wrapping an int value with an empty tuple fallback ---
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()
    maybe_int_empty_tuple = maybe.Maybe(int_value, empty_tuple)

    # Convert to validation and retrieve value via get_or_else
    validation_from_int_maybe = maybe_int_empty_tuple.to_validation()
    get_or_else_result = maybe_int_empty_tuple.get_or_else(int_value)

    # Convert to Try, then use the Try result as the bind argument
    try_result = maybe_int_empty_tuple.to_try()
    maybe_int_empty_tuple.bind(try_result)

    # --- Maybe wrapping a float value with a float fallback (construction only) ---
    maybe_float_float = maybe.Maybe(float_value, float_value)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test that Maybe wrapping None can be mapped with a set, and Maybe wrapping an integer can be converted to an Either."""

    # Construct a Maybe with no value (None) and a valid flag of True
    no_value = None
    is_valid = True
    maybe_none = maybe.Maybe(no_value, is_valid)

    # Map the Maybe using a set containing the valid flag
    mapping_set = {is_valid}
    map_result = maybe_none.map(mapping_set)

    # Construct a second Maybe wrapping an integer value
    integer_value = -1095
    is_valid_second = True
    maybe_integer = maybe.Maybe(integer_value, is_valid_second)

    # Convert the integer-wrapping Maybe to an Either type
    either_result = maybe_integer.to_either()

def test_maybe_conversions_with_none_and_nested_maybe():
    """Test that Maybe instances built from None and nested Maybe values can be converted to lazy, either, and try forms without error."""

    # Build a Maybe from two None values
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Wrap the first Maybe in a tuple to use as a value in a second Maybe
    maybe_tuple = (maybe_with_none,)

    # Convert the None-based Maybe to its lazy representation
    lazy_from_none_maybe = maybe_with_none.to_lazy()

    false_value = False

    # Build a second Maybe whose value is a tuple containing the first Maybe
    maybe_with_tuple = maybe.Maybe(maybe_tuple, false_value)

    # Convert the None-based Maybe to an Either (first call)
    either_from_none_maybe_first = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to a Try
    try_from_tuple_maybe = maybe_with_tuple.to_try()

    # Convert the None-based Maybe to an Either again (repeated conversion check)
    either_from_none_maybe_second = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to an Either
    either_from_tuple_maybe = maybe_with_tuple.to_either()

    # Verify the Try value can itself be converted to a lazy representation
    try_from_tuple_maybe.to_lazy()

def test_maybe_to_try_to_box_conversion_succeeds():
    """Test that a Maybe instance can be chained through to_try() and then to_box() without error."""
    # Define the boolean flags used to construct the Maybe instance
    is_present = True
    is_empty = False

    # Create a Maybe instance with the given boolean values
    maybe_instance = maybe.Maybe(is_present, is_empty)

    # Convert the Maybe to a Try, then chain to a Box
    try_result = maybe_instance.to_try()
    try_result.to_box()

def test_maybe_none_true_chained_transformations_and_ap():
    """Test chained Maybe transformations starting from Maybe(None, True), verifying ap, lazy, validation, filter, get_or_else, either, try, eq, and box conversions."""

    # Inputs
    raw_bytes = b"C\xcf\xe7/"
    none_value = None
    flag_true = True

    # Construct a Maybe wrapping None with a True flag
    maybe_none_true = maybe.Maybe(none_value, flag_true)

    # Apply None as an argument via ap
    maybe_after_ap = maybe_none_true.ap(none_value)

    # Convert the ap result to a lazy representation
    lazy_value = maybe_after_ap.to_lazy()

    # Convert the lazy value to a validation
    validation_value = lazy_value.to_validation()

    # Filter the original maybe using the validation value as the predicate
    filtered_maybe = maybe_none_true.filter(validation_value)

    # Retrieve the value or fall back to filtered_maybe itself
    get_or_else_result = filtered_maybe.get_or_else(filtered_maybe)

    # Convert filtered_maybe to an Either type
    either_value = filtered_maybe.to_either()

    # Convert the validation to a Try type
    try_value = validation_value.to_try()

    # Check equality between filtered_maybe and the ap result
    eq_result = filtered_maybe.__eq__(maybe_after_ap)

    # Convert the get_or_else result to a Box type
    box_value = get_or_else_result.to_box()

    # Apply raw bytes via ap on the try value
    try_value.ap(raw_bytes)

def test_maybe_monad_chained_operations_with_none_and_bytes_values():
    """Test chained Maybe monad operations (ap, bind, to_validation, to_either, to_try) with None and bytes values."""

    # Define primitive inputs
    sample_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    flag_true = True

    # Build a Maybe wrapping None with a True flag, then chain ap calls
    maybe_none_true = maybe.Maybe(none_value, flag_true)
    maybe_ap_none = maybe_none_true.ap(none_value)       # apply None to the Maybe
    maybe_ap_bytes = maybe_ap_none.ap(sample_bytes)      # apply bytes to the chained result
    validation_from_ap_chain = maybe_ap_bytes.to_validation()  # convert to Validation

    # Build a second Maybe wrapping None with bytes as the value
    maybe_none_bytes = maybe.Maybe(none_value, sample_bytes)

    # Exercise get_or_else: fallback to itself when value is absent
    get_or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)

    # Convert to Validation and use it as a bind target
    validation_from_maybe_none_bytes = maybe_none_bytes.to_validation()
    bound_result = maybe_none_bytes.bind(validation_from_maybe_none_bytes)

    # Convert to Either and apply ap with itself
    either_result = maybe_none_bytes.to_either()
    maybe_ap_self = maybe_none_bytes.ap(maybe_none_bytes)

    # Equality check: Either vs Validation
    negative_int = -3289
    either_eq_validation = either_result.__eq__(validation_from_maybe_none_bytes)

    # Bind the Either with the original Maybe
    either_bound = either_result.bind(maybe_none_bytes)

    # Convert to Try and check equality of Maybe with bound result
    try_result = maybe_none_bytes.to_try()
    maybe_eq_bound = maybe_none_bytes.__eq__(bound_result)

    # Convert the bound result to Validation
    validation_from_bound = bound_result.to_validation()

    # Apply the Try with a negative integer (result intentionally unused)
    try_result.ap(negative_int)

def test_maybe_false_values_chain_to_either_lazy_and_validation():
    """Test that a Maybe wrapping False values supports equality, chaining to Either/Lazy/Validation, and mapping with a Validation."""

    false_value = False

    # Create a Maybe with False values and verify equality comparison works
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

def test_maybe_false_false_equality_and_conversion_chain():
    """Test that a Maybe(False, False) supports self-equality and converts through to_try() and to_validation() without error."""
    # Construct a Maybe instance with both values set to False
    false_value = False
    maybe_instance = maybe.Maybe(false_value, false_value)

    # Explicitly invoke __eq__ to check that the instance equals itself
    is_equal_to_self = maybe_instance.__eq__(maybe_instance)

    # Convert the Maybe to a Try, then further to a Validation
    try_result = maybe_instance.to_try()
    try_result.to_validation()

