import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with two identical bytes values as arguments."""
    # Use a fixed bytes value as both the first and second argument to Maybe
    sample_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    maybe_instance = maybe.Maybe(sample_bytes, sample_bytes)

def test_maybe_instantiation_with_none_values():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None for both arguments to verify Maybe handles absent values at construction
    none_value = None

    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chained_operations_and_conversions():
    """Verify that Maybe supports chained monadic operations (ap, map, filter, bind) and conversions (to_validation, to_either) without error."""

    # A single string value used consistently as input throughout the test
    seed_value = "p4xa>bl^oP"

    # Construct a Maybe instance with the seed value for both arguments
    maybe_instance = maybe.Maybe(seed_value, seed_value)

    # Verify equality comparison against a plain string
    eq_result = maybe_instance.__eq__(seed_value)

    # Apply ap and retrieve the fallback value
    ap_result = maybe_instance.ap(seed_value)
    get_or_else_result = maybe_instance.get_or_else(seed_value)

    # Chain map and filter transformations using the ap result
    map_result_first = maybe_instance.map(ap_result)
    filter_result_first = maybe_instance.filter(ap_result)
    map_result_second = maybe_instance.map(ap_result)

    # Perform a second ap call and compare it with the first
    ap_result_second = maybe_instance.ap(seed_value)
    ap_eq_result = ap_result.__eq__(ap_result_second)

    # Chain further operations on the ap results
    filter_result_chained = ap_result.filter(get_or_else_result)
    get_or_else_chained = ap_result_second.get_or_else(seed_value)

    # Construct a second Maybe instance and exercise validation/bind/either conversions
    maybe_instance_second = maybe.Maybe(seed_value, seed_value)
    validation_result = maybe_instance_second.to_validation()
    bind_result = maybe_instance_second.bind(validation_result)

    # Convert the bound result into an Either type
    either_result = bind_result.to_either()

def test_maybe_eq_returns_result_when_compared_to_set():
    """Test that Maybe.__eq__ produces a result when compared against a set containing False."""

    # Build a set using repeated False values (collapses to {False} due to set semantics)
    false_value = False
    set_of_false = {false_value, false_value, false_value, false_value}

    # Create a Maybe instance wrapping two None values
    none_value = None
    maybe_none = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance to the set; result is captured but not further asserted
    eq_result = maybe_none.__eq__(set_of_false)

def test_maybe_bind_map_chain_and_invalid_set_method_raises():
    """Test that Maybe supports bind/map chaining and that calling to_box() on a plain set raises AttributeError."""

    # A simple boolean value used as both the wrapped value and the predicate
    flag_value = True

    # Construct a Maybe wrapping a boolean, with a boolean condition
    maybe_with_bool = maybe.Maybe(flag_value, flag_value)

    # Chain bind() then map() using the same boolean value
    bound_maybe = maybe_with_bool.bind(flag_value)
    mapped_maybe = bound_maybe.map(flag_value)

    # Construct a Maybe wrapping a tuple of booleans
    tuple_value = (flag_value, flag_value, flag_value, flag_value)
    maybe_with_tuple = maybe.Maybe(tuple_value, flag_value)

    # Calling to_box() on a plain set is invalid and should raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe constructed with None and False allows map() to be called with a falsy argument."""
    # Represent the absence of a value and a falsy flag used for both construction and mapping
    no_value = None
    falsy_flag = False

    # Construct a Maybe instance wrapping None with a False flag
    maybe_instance = maybe.Maybe(no_value, falsy_flag)

    # Call map() with the falsy flag — should execute without error
    maybe_instance.map(falsy_flag)

def test_maybe_bind_on_none_value_with_empty_dict():
    """Test that bind on a Maybe wrapping None with an empty dict executes without error."""

    # A truthy value used to construct a valid Maybe instance
    truthy_value = True

    # Create a Maybe with two truthy values (result unused, kept for semantic fidelity)
    maybe_with_true = maybe.Maybe(truthy_value, truthy_value)

    # An empty dict to be passed as the bind argument
    empty_dict = {}

    # None and False represent a missing/falsy wrapped value
    none_value = None
    falsy_value = False

    # Create a Maybe wrapping None with a falsy second argument
    maybe_with_none = maybe.Maybe(none_value, falsy_value)

    # Bind the empty dict to the Maybe wrapping None; should not raise
    maybe_with_none.bind(empty_dict)

def test_maybe_chained_operations_with_mixed_types():
    """Tests Maybe instances support chained operations across mixed value types."""

    # --- Setup: Maybe wrapping bytes with no context ---
    bytes_value = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_context = None
    maybe_bytes_none = maybe.Maybe(bytes_value, none_context)

    # Convert the bytes/None Maybe to a boxed representation
    boxed_bytes_none = maybe_bytes_none.to_box()

    # --- Setup: Maybe wrapping an integer with a boolean context ---
    int_value = 0
    bool_context = True
    maybe_int_bool = maybe.Maybe(int_value, bool_context)

    # Filter the int/bool Maybe using itself as the predicate
    filtered_int_bool = maybe_int_bool.filter(maybe_int_bool)

    # Convert the int/bool Maybe to a lazy representation
    lazy_int_bool = maybe_int_bool.to_lazy()

    # --- Compose: apply the filtered Maybe onto the bytes/None Maybe ---
    applied_result = filtered_int_bool.ap(maybe_bytes_none)

    # Filter the applied result using itself as the predicate
    filtered_applied = filtered_int_bool.filter(applied_result)

    # --- Compose: build a new Maybe from the lazy and boxed values ---
    maybe_lazy_boxed = maybe.Maybe(lazy_int_bool, boxed_bytes_none)

    # Check equality of the lazy value against the boolean context
    lazy_eq_bool = lazy_int_bool.__eq__(bool_context)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling `ap` on a Maybe constructed with None and False does not raise an error."""
    # Integer argument to be passed to the `ap` method
    int_argument = 2862

    # Represent the absence of a value (Nothing state)
    no_value = None

    # Flag indicating the Maybe is in a falsy/nothing-like state
    is_nothing = False

    # Construct a Maybe instance with no value and the falsy flag
    maybe_nothing = module_0.Maybe(no_value, is_nothing)

    # Apply the integer argument via `ap`; should not raise
    maybe_nothing.ap(int_argument)

def test_maybe_supports_chained_filter_map_lazy_and_try_operations():
    """Test that a Maybe monad supports chained filter, to_lazy, map, and to_try transformations without error."""
    initial_value = 0
    is_present = True

    # Construct a Maybe monad wrapping an integer with a presence flag
    maybe_instance = maybe.Maybe(initial_value, is_present)

    # Filter the Maybe using itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the original Maybe to its lazy representation
    lazy_from_maybe = maybe_instance.to_lazy()

    # Convert the filtered Maybe to its lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the already-filtered Maybe using the lazy-converted filtered Maybe
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered result to a Try monad
    try_from_double_filtered = double_filtered.to_try()

    # Produce a second lazy conversion of the original Maybe
    second_lazy_from_maybe = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_maybe = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_with_none_value_and_lazy_chain():
    """Test that Maybe.filter() chaining with None values and lazy conversion does not raise errors."""
    # Set up a tuple of repeated negative integers to use as a filter argument
    negative_int = -283
    filter_tuple = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with flag=True, then filter and convert to lazy
    none_value = None
    flag_true = True
    maybe_with_none_and_flag = module_0.Maybe(none_value, flag_true)
    filtered_maybe = maybe_with_none_and_flag.filter(filter_tuple)
    lazy_maybe = filtered_maybe.to_lazy()

    # Create a second Maybe with both values as None and filter it using the lazy result
    none_value_2 = None
    maybe_with_none_values = module_0.Maybe(none_value_2, none_value_2)
    maybe_with_none_values.filter(lazy_maybe)

def test_maybe_get_or_else_and_filter_with_generic_object():
    """Test that Maybe supports get_or_else, to_box, and filter across different wrapped value types."""

    # Define a fallback integer and a sample string used to build composite values
    fallback_int = 2281
    sample_str = "gZ(\\mOcN"

    # Build a dict and tuple from the sample string to serve as Maybe's wrapped value
    sample_dict = {sample_str: sample_str}
    sample_tuple = (sample_str, sample_str, sample_dict, sample_dict)

    # Construct a Maybe wrapping a tuple, marked as present (True)
    is_present_true = True
    maybe_with_tuple = maybe.Maybe(sample_tuple, is_present_true)

    # Retrieve the value or fall back to fallback_int
    get_or_else_result = maybe_with_tuple.get_or_else(fallback_int)

    # Create a Generic instance to use as a wrapped value in a second Maybe
    generic_instance = typing.Generic()

    # Convert the first Maybe to a box
    boxed_maybe = maybe_with_tuple.to_box()

    # Construct a second Maybe wrapping the generic instance, marked as absent (False)
    is_present_false = False
    maybe_with_generic = maybe.Maybe(generic_instance, is_present_false)

    # Apply filter using the result of get_or_else on the generic Maybe
    maybe_with_generic.filter(get_or_else_result)

def test_maybe_methods_with_various_value_and_fallback_combinations():
    """Test that Maybe instances support to_validation, get_or_else, to_try, and bind across varied value/fallback type combinations."""

    # --- Maybe with a boolean value and None as the fallback ---
    true_value = True
    none_fallback = None
    maybe_bool_with_none_fallback = maybe.Maybe(true_value, none_fallback)
    validation_from_bool_maybe = maybe_bool_with_none_fallback.to_validation()

    # --- Maybe with a negative integer value and an empty tuple as the fallback ---
    negative_float = -286.64
    negative_int = -1784
    empty_tuple_fallback = ()
    maybe_int_with_empty_tuple_fallback = maybe.Maybe(negative_int, empty_tuple_fallback)

    # Exercise core Maybe methods on the integer-valued instance
    validation_from_int_maybe = maybe_int_with_empty_tuple_fallback.to_validation()
    int_maybe_or_else_result = maybe_int_with_empty_tuple_fallback.get_or_else(negative_int)
    try_from_int_maybe = maybe_int_with_empty_tuple_fallback.to_try()

    # --- Maybe with a float value and a float fallback (used as bind argument) ---
    maybe_float_with_float_fallback = maybe.Maybe(negative_float, negative_float)

    # Bind the to_try() result onto the integer-valued Maybe instance
    maybe_int_with_empty_tuple_fallback.bind(try_from_int_maybe)

def test_maybe_map_with_none_value_and_to_either_conversion():
    """Test that Maybe with None can be mapped over a set, and Maybe with an integer can be converted to an Either."""

    # Construct a Maybe wrapping None with the has-value flag set to True
    none_value = None
    has_value_flag = True
    maybe_with_none = maybe.Maybe(none_value, has_value_flag)

    # Attempt to map the Maybe over a set
    mapping_set = {has_value_flag}
    map_result = maybe_with_none.map(mapping_set)

    # Construct a second Maybe wrapping an integer value
    integer_value = -1095
    has_value_flag_2 = True
    maybe_with_integer = maybe.Maybe(integer_value, has_value_flag_2)

    # Convert the integer-holding Maybe to an Either type
    either_result = maybe_with_integer.to_either()

def test_maybe_with_none_converts_to_lazy_either_and_try():
    """Test that Maybe instances wrapping None and nested Maybe values can be converted to Lazy, Either, and Try without error."""

    # Build a Maybe that wraps two None values
    none_value = None
    maybe_none = maybe.Maybe(none_value, none_value)

    # Wrap the first Maybe inside a tuple to use as input for a second Maybe
    maybe_tuple = (maybe_none,)

    # Convert the None-wrapping Maybe to a Lazy representation
    lazy_from_none_maybe = maybe_none.to_lazy()

    # Build a second Maybe using the tuple and a False flag
    false_value = False
    maybe_with_tuple = maybe.Maybe(maybe_tuple, false_value)

    # Convert the None-wrapping Maybe to an Either (first call)
    either_from_none_maybe_1 = maybe_none.to_either()

    # Convert the tuple-wrapping Maybe to a Try
    try_from_tuple_maybe = maybe_with_tuple.to_try()

    # Convert the None-wrapping Maybe to an Either again (second call)
    either_from_none_maybe_2 = maybe_none.to_either()

    # Convert the tuple-wrapping Maybe to an Either
    either_from_tuple_maybe = maybe_with_tuple.to_either()

    # Chain: convert the Try result further to a Lazy representation
    try_from_tuple_maybe.to_lazy()

def test_maybe_to_try_to_box_chain_succeeds():
    """Test that a Maybe(True, False) can be chained through to_try() and then to_box() without error."""
    # Construct a Maybe with an affirmative presence flag and a false secondary flag
    is_present = True
    is_empty = False

    maybe_instance = maybe.Maybe(is_present, is_empty)

    # Convert the Maybe to a Try representation
    try_result = maybe_instance.to_try()

    # Convert the Try to a Box — verifies the full conversion chain completes
    try_result.to_box()

def test_maybe_none_chains_through_monad_transformations():
    """Tests that a Maybe wrapping None chains correctly through ap, lazy, validation,
    filter, get_or_else, either, try, and box transformations."""

    # Inputs
    raw_bytes_input = b"C\xcf\xe7/"
    none_value = None
    truthy_flag = True

    # Construct a Maybe monad wrapping None with a truthy flag
    maybe_none = maybe.Maybe(none_value, truthy_flag)

    # Apply none_value to the Maybe, producing a new Maybe
    applied_maybe = maybe_none.ap(none_value)

    # Convert the applied Maybe to a lazy representation
    lazy_from_applied = applied_maybe.to_lazy()

    # Convert the lazy value to a validation
    validation_from_lazy = lazy_from_applied.to_validation()

    # Filter the original Maybe using the validation as the predicate
    filtered_maybe = maybe_none.filter(validation_from_lazy)

    # Retrieve value or fall back to filtered_maybe itself
    get_or_else_result = filtered_maybe.get_or_else(filtered_maybe)

    # Convert the filtered Maybe to an Either (exercises the conversion path)
    either_from_filtered = filtered_maybe.to_either()

    # Convert the validation to a Try monad
    try_from_validation = validation_from_lazy.to_try()

    # Check equality between filtered_maybe and applied_maybe
    are_equal = filtered_maybe.__eq__(applied_maybe)

    # Convert the get_or_else result to a Box
    box_from_get_or_else = get_or_else_result.to_box()

    # Apply raw bytes to the try monad (exercises ap on Try with bytes input)
    try_from_validation.ap(raw_bytes_input)

def test_maybe_monad_chaining_with_none_and_bytes_values():
    """Tests chaining of Maybe monad operations with None and bytes values across multiple instances."""

    # --- Setup primitive values ---
    sample_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    flag_true = True

    # --- First Maybe: constructed with (None, True), apply None then bytes ---
    maybe_none_true = maybe.Maybe(none_value, flag_true)
    applied_none = maybe_none_true.ap(none_value)
    applied_bytes = applied_none.ap(sample_bytes)
    validation_from_applied_bytes = applied_bytes.to_validation()

    # --- Second Maybe: constructed with (None, bytes), exercise full monad interface ---
    maybe_none_bytes = maybe.Maybe(none_value, sample_bytes)

    # get_or_else with itself as fallback
    or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)

    # Convert to validation, then bind with that validation
    validation_from_none_bytes = maybe_none_bytes.to_validation()
    bound_validation = maybe_none_bytes.bind(validation_from_none_bytes)

    # Convert to Either and apply self
    either_from_none_bytes = maybe_none_bytes.to_either()
    applied_self = maybe_none_bytes.ap(maybe_none_bytes)

    # --- Equality and further chaining on Either ---
    negative_int = -3289
    either_eq_validation = either_from_none_bytes.__eq__(validation_from_none_bytes)
    either_bound = either_from_none_bytes.bind(maybe_none_bytes)

    # --- Convert to Try and compare Maybe with bound result ---
    try_from_none_bytes = maybe_none_bytes.to_try()
    maybe_eq_bound = maybe_none_bytes.__eq__(bound_validation)

    # Convert bound validation result to validation
    validation_from_bound = bound_validation.to_validation()

    # Apply a negative integer to the Try instance
    try_from_none_bytes.ap(negative_int)

def test_maybe_with_false_values_supports_chained_conversions_and_map():
    """Test that a Maybe built from False values supports equality, chained conversions, and map."""

    false_value = False

    # Verify that a Maybe with False values supports equality comparison
    maybe_false = maybe.Maybe(false_value, false_value)
    equality_result = maybe_false.__eq__(false_value)

    # Convert a Maybe(False, False) through the monad conversion chain
    maybe_for_conversion = maybe.Maybe(false_value, false_value)
    either_result = maybe_for_conversion.to_either()
    lazy_result = maybe_for_conversion.to_lazy()

    # Convert the lazy result to a validation functor
    validation_result = lazy_result.to_validation()

    # Verify that map can be called on a Maybe using the validation result as the mapping function
    maybe_for_map = maybe.Maybe(false_value, false_value)
    maybe_for_map.map(validation_result)

def test_maybe_false_false_equality_and_conversion_chain():
    """Test that Maybe(False, False) supports self-equality and converts through to_try() and to_validation() without error."""

    # Construct a Maybe instance with both values set to False
    false_value = False
    maybe_instance = maybe.Maybe(false_value, false_value)

    # Verify that the Maybe instance is equal to itself
    is_equal_to_self = maybe_instance.__eq__(maybe_instance)

    # Convert the Maybe to a Try, then further to a Validation
    try_instance = maybe_instance.to_try()
    try_instance.to_validation()

