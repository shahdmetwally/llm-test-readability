import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with bytes values as both arguments."""
    # Use the same bytes value for both constructor arguments
    sample_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    maybe_instance = maybe.Maybe(sample_bytes, sample_bytes)

def test_maybe_instantiation_with_none_values():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None for both the value and the fallback arguments
    none_value = None

    # Construct a Maybe instance with two None arguments
    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chaining_operations_with_string_value():
    """Tests that a Maybe monad supports chaining of ap, map, filter, bind, to_validation, and to_either operations."""

    # Use a fixed string as both the value and the default/fallback throughout
    string_value = "p4xa>bl^oP"

    # Construct a Maybe instance wrapping the string value
    maybe_instance = maybe.Maybe(string_value, string_value)

    # Check equality of the Maybe instance against the raw string
    eq_result = maybe_instance.__eq__(string_value)

    # Apply ap, get_or_else, map, and filter operations on the primary instance
    ap_result = maybe_instance.ap(string_value)
    get_or_else_result = maybe_instance.get_or_else(string_value)
    map_result = maybe_instance.map(ap_result)
    filter_result = maybe_instance.filter(ap_result)

    # Repeat map and ap to verify consistent chaining behaviour
    second_map_result = maybe_instance.map(ap_result)
    second_ap_result = maybe_instance.ap(string_value)

    # Verify equality between two independently produced ap results
    ap_eq_result = ap_result.__eq__(second_ap_result)

    # Chain filter and get_or_else on the derived ap results
    ap_filter_result = ap_result.filter(get_or_else_result)
    ap_get_or_else_result = second_ap_result.get_or_else(string_value)

    # Construct a second Maybe instance and exercise to_validation and bind
    second_maybe_instance = maybe.Maybe(string_value, string_value)
    validation_result = second_maybe_instance.to_validation()
    bind_result = second_maybe_instance.bind(validation_result)

    # Convert the bound result to an Either type
    either_result = bind_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set_of_false_values():
    """Test that Maybe.__eq__ returns a falsy result when compared to a set containing only False values."""

    # Define the boolean value used to populate the set
    false_value = False

    # Build a set of False values (deduplicates to {False} at runtime, preserving original literal structure)
    set_of_false_values = {false_value, false_value, false_value, false_value}

    # Use None as both arguments to construct a Maybe with no values
    none_value = None
    maybe_with_none_values = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance against the set of False values
    eq_result = maybe_with_none_values.__eq__(set_of_false_values)

def test_maybe_bind_map_chain_and_set_missing_method_raises():
    """Test that Maybe supports bind/map chaining and that calling to_box() on a plain set raises AttributeError."""

    # Use a simple boolean as the base value for Maybe construction
    true_value = True

    # Create a Maybe wrapping a boolean value and chain bind then map
    maybe_bool_instance = maybe.Maybe(true_value, true_value)
    bound_result = maybe_bool_instance.bind(true_value)
    mapped_result = bound_result.map(true_value)

    # Create a Maybe wrapping a tuple of booleans
    bool_tuple = (true_value, true_value, true_value, true_value)
    maybe_tuple_instance = maybe.Maybe(bool_tuple, true_value)

    # Calling to_box() on a plain set is invalid and raises AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_does_not_raise():
    """Test that Maybe constructed with None and False can call map() with a falsy value without error."""
    # Use None as the wrapped value and False as the flag to construct a Maybe
    empty_value = None
    falsy_flag = False

    # Construct a Maybe instance with an absent value and a falsy flag
    maybe_instance = maybe.Maybe(empty_value, falsy_flag)

    # Call map() with a falsy value; expect no exception to be raised
    maybe_instance.map(falsy_flag)

def test_maybe_get_or_else_and_filter_with_generic_object():
    """Test that Maybe.get_or_else returns a fallback, to_box wraps the value, and filter can be applied to a Maybe wrapping a Generic object."""

    # Set up a fallback integer and a reusable string for building the wrapped value
    fallback_int = 2281
    sample_str = "gZ(\\mOcN"

    # Build a dict and tuple to serve as the value wrapped by the first Maybe
    sample_dict = {sample_str: sample_str}
    maybe_value_tuple = (sample_str, sample_str, sample_dict, sample_dict)

    # Construct a Maybe with the tuple and is_present=True
    is_present_true = True
    maybe_with_tuple = maybe.Maybe(maybe_value_tuple, is_present_true)

    # Retrieve the value or fall back to fallback_int
    get_or_else_result = maybe_with_tuple.get_or_else(fallback_int)

    # Construct a Generic instance to use as the value for the second Maybe
    generic_instance = typing.Generic()

    # Construct a Maybe with the generic object and is_present=False
    is_present_false = False
    boxed_value = maybe_with_tuple.to_box()
    maybe_with_generic = maybe.Maybe(generic_instance, is_present_false)

    # Apply filter using the result from get_or_else
    maybe_with_generic.filter(get_or_else_result)

def test_maybe_methods_execute_across_various_type_combinations():
    """Test that Maybe methods (to_validation, get_or_else, to_try, bind) execute correctly across varied type combinations."""

    # --- Maybe wrapping a bool value with None as fallback ---
    truthy_value = True
    none_fallback = None
    maybe_bool_none = maybe.Maybe(truthy_value, none_fallback)
    validation_from_bool_maybe = maybe_bool_none.to_validation()

    # --- Maybe wrapping an int value with an empty tuple as fallback ---
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()
    maybe_int_tuple = maybe.Maybe(int_value, empty_tuple)
    validation_from_int_maybe = maybe_int_tuple.to_validation()

    # Retrieve the wrapped value, falling back to int_value if absent
    get_or_else_result = maybe_int_tuple.get_or_else(int_value)

    # Convert the Maybe to a Try monad
    try_from_int_maybe = maybe_int_tuple.to_try()

    # --- Maybe wrapping a float value with another float as fallback ---
    maybe_float_float = maybe.Maybe(float_value, float_value)

    # Bind the Try result into the int/tuple Maybe to exercise the bind method
    maybe_int_tuple.bind(try_from_int_maybe)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test Maybe.map() with a set argument and Maybe.to_either() on an integer-valued Maybe."""

    # Construct a Maybe wrapping None with has-value flag set to True
    none_value = None
    has_value_flag = True
    maybe_with_none = maybe.Maybe(none_value, has_value_flag)

    # Call map() on the Maybe using a set as the mapping argument
    mapping_set = {has_value_flag}
    map_result = maybe_with_none.map(mapping_set)

    # Construct a second Maybe wrapping an integer and convert it to an Either
    integer_value = -1095
    has_value_flag_2 = True
    maybe_with_int = maybe.Maybe(integer_value, has_value_flag_2)
    either_result = maybe_with_int.to_either()

def test_maybe_monad_conversions_with_none_and_nested_maybe():
    """Test that Maybe monads built from None and nested Maybe values can be converted to lazy, either, and try forms without error."""

    # Build a Maybe from two None values
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Wrap the first Maybe in a tuple to use as a value in a second Maybe
    maybe_tuple = (maybe_with_none,)

    # Convert the None-based Maybe to a lazy form
    lazy_from_none_maybe = maybe_with_none.to_lazy()

    # Build a second Maybe using the tuple and a False flag
    false_value = False
    maybe_with_tuple = maybe.Maybe(maybe_tuple, false_value)

    # Convert the None-based Maybe to an either form (first call)
    either_from_none_maybe_first = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to a try form
    try_from_tuple_maybe = maybe_with_tuple.to_try()

    # Convert the None-based Maybe to an either form (second call)
    either_from_none_maybe_second = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to an either form
    either_from_tuple_maybe = maybe_with_tuple.to_either()

    # Convert the try result to a lazy form (validates no exception is raised)
    try_from_tuple_maybe.to_lazy()

def test_maybe_to_try_to_box_conversion_succeeds():
    """Test that a Maybe(True, False) can be chained through to_try() and then to_box() without error."""
    # Construct a Maybe with a present value flag and a non-empty flag
    has_value = True
    is_empty = False

    maybe_instance = maybe.Maybe(has_value, is_empty)

    # Convert the Maybe to a Try, then further convert to a Box
    try_result = maybe_instance.to_try()
    try_result.to_box()

def test_maybe_none_true_chains_through_monad_transformations():
    """Test that a Maybe(None, True) monad correctly chains through ap, lazy, validation, filter, get_or_else, either, try, and box transformations."""

    # Arbitrary byte value used as input to ap() on the try monad
    arbitrary_bytes = b"C\xcf\xe7/"
    none_value = None
    flag_true = True

    # Construct a Maybe monad with None as the value and True as the flag
    maybe_none_true = maybe.Maybe(none_value, flag_true)

    # Apply ap(None) to the Maybe — result is another Maybe-like container
    maybe_after_ap = maybe_none_true.ap(none_value)

    # Convert the ap result to a lazy representation
    lazy_from_ap = maybe_after_ap.to_lazy()

    # Convert the lazy representation to a validation container
    validation_from_lazy = lazy_from_ap.to_validation()

    # Filter the original Maybe using the validation as the predicate
    maybe_filtered = maybe_none_true.filter(validation_from_lazy)

    # Retrieve the value or fall back to the filtered Maybe itself
    get_or_else_result = maybe_filtered.get_or_else(maybe_filtered)

    # Convert the filtered Maybe to an Either container
    either_from_filtered = maybe_filtered.to_either()

    # Convert the validation to a Try container
    try_from_validation = validation_from_lazy.to_try()

    # Check equality between the filtered Maybe and the ap result
    eq_result = maybe_filtered.__eq__(maybe_after_ap)

    # Convert the get_or_else result to a Box container
    box_from_get_or_else = get_or_else_result.to_box()

    # Apply arbitrary bytes to the try container
    try_from_validation.ap(arbitrary_bytes)

def test_maybe_monad_chaining_with_none_and_bytes_value():
    """Tests Maybe monad chaining (ap, bind, to_validation, to_either, to_try) across None and bytes-valued instances."""

    # Input values used to construct Maybe instances
    bytes_value = b"\xdbC\xcf\xe7/"
    none_value = None
    is_just_flag = True

    # Construct a Maybe with a None value, marked as Just
    maybe_with_none_just = maybe.Maybe(none_value, is_just_flag)

    # Chain ap calls: first with None, then with bytes
    ap_none_result = maybe_with_none_just.ap(none_value)
    ap_bytes_result = ap_none_result.ap(bytes_value)

    # Convert the ap chain result to a Validation
    validation_from_ap_chain = ap_bytes_result.to_validation()

    # Construct a Maybe wrapping a bytes value
    maybe_with_bytes = maybe.Maybe(none_value, bytes_value)

    # Exercise get_or_else using the Maybe itself as the fallback
    get_or_else_result = maybe_with_bytes.get_or_else(maybe_with_bytes)

    # Convert maybe_with_bytes to Validation, then bind it back into maybe_with_bytes
    validation_from_maybe_bytes = maybe_with_bytes.to_validation()
    bind_validation_result = maybe_with_bytes.bind(validation_from_maybe_bytes)

    # Convert maybe_with_bytes to Either
    either_from_maybe_bytes = maybe_with_bytes.to_either()

    # Apply maybe_with_bytes to itself via ap
    ap_self_result = maybe_with_bytes.ap(maybe_with_bytes)

    # Negative integer used as argument to ap on the Try result
    negative_int = -3289

    # Compare Either against Validation using __eq__
    either_eq_validation = either_from_maybe_bytes.__eq__(validation_from_maybe_bytes)

    # Bind maybe_with_bytes into the Either
    either_bind_result = either_from_maybe_bytes.bind(maybe_with_bytes)

    # Convert maybe_with_bytes to Try
    try_from_maybe_bytes = maybe_with_bytes.to_try()

    # Compare maybe_with_bytes against the bind result using __eq__
    maybe_eq_bind_result = maybe_with_bytes.__eq__(bind_validation_result)

    # Convert the bind result to Validation
    validation_from_bind = bind_validation_result.to_validation()

    # Call ap on the Try result with a negative integer
    try_from_maybe_bytes.ap(negative_int)

def test_maybe_false_chains_to_either_lazy_validation_and_maps():
    """Test that Maybe(False, False) chains through Either, Lazy, and Validation, and maps onto another Maybe."""

    # Use False as the base value for all Maybe constructions
    false_value = False

    # Create a Maybe and check equality with the base false value (result unused further)
    maybe_for_eq_check = maybe.Maybe(false_value, false_value)
    eq_result = maybe_for_eq_check.__eq__(false_value)

    # Create a second Maybe and chain it through to_either -> to_lazy -> to_validation
    maybe_for_chaining = maybe.Maybe(false_value, false_value)
    either_result = maybe_for_chaining.to_either()
    lazy_result = maybe_for_chaining.to_lazy()
    validation_result = lazy_result.to_validation()

    # Create a third Maybe and use the validation result as the mapping function
    maybe_for_mapping = maybe.Maybe(false_value, false_value)
    maybe_for_mapping.map(validation_result)

def test_maybe_false_false_equality_and_conversion_chain():
    """Test that Maybe(False, False) supports self-equality and converts through to_try() and to_validation()."""

    # Construct a Maybe instance with both values set to False
    false_value = False
    maybe_false_false = maybe.Maybe(false_value, false_value)

    # Exercise self-equality comparison (result is computed but not asserted)
    equality_result = maybe_false_false.__eq__(maybe_false_false)

    # Convert the Maybe to a Try, then further convert to a Validation
    try_result = maybe_false_false.to_try()
    try_result.to_validation()

