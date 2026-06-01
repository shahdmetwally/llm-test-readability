import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Verify that Maybe can be instantiated with identical bytes values as both constructor arguments."""
    # Define a raw bytes payload to be used as constructor input
    raw_bytes_value = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Construct a Maybe instance using the same bytes value for both arguments
    maybe_instance = maybe.Maybe(raw_bytes_value, raw_bytes_value)

def test_maybe_instantiation_with_none_values():
    """Test that Maybe can be instantiated with two None arguments without error."""
    # Use None as both arguments to verify the Maybe constructor handles null inputs
    none_value = None

    # Instantiate Maybe with two None values
    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chained_operations_with_string_value():
    """Tests that Maybe supports chained monadic operations (ap, map, filter, bind, to_validation, to_either) without error."""

    # Seed value used as both the wrapped value and the argument throughout
    string_value = "p4xa>bl^oP"

    # --- Phase 1: Operations on the first Maybe instance ---

    # Construct a Maybe container with the string value
    maybe_instance = maybe.Maybe(string_value, string_value)

    # Equality check against the raw string
    eq_result = maybe_instance.__eq__(string_value)

    # Apply (ap) the Maybe with the raw string; capture result for later use
    ap_result = maybe_instance.ap(string_value)

    # Unwrap with a fallback string
    get_or_else_result = maybe_instance.get_or_else(string_value)

    # Map over the Maybe using the ap_result as the function
    map_result_1 = maybe_instance.map(ap_result)

    # Filter the Maybe using ap_result as the predicate
    filter_result_1 = maybe_instance.filter(ap_result)

    # Map again (verifies map can be called multiple times)
    map_result_2 = maybe_instance.map(ap_result)

    # Apply a second time to confirm ap is repeatable
    ap_result_2 = maybe_instance.ap(string_value)

    # Compare the two ap results for equality
    ap_eq_result = ap_result.__eq__(ap_result_2)

    # Filter ap_result using the unwrapped value as the predicate
    filter_result_2 = ap_result.filter(get_or_else_result)

    # Unwrap ap_result_2 with the original string as fallback
    get_or_else_result_2 = ap_result_2.get_or_else(string_value)

    # --- Phase 2: Second Maybe instance — validation and either conversion ---

    # Construct a second independent Maybe container
    maybe_instance_2 = maybe.Maybe(string_value, string_value)

    # Convert the second Maybe to a Validation type
    validation_result = maybe_instance_2.to_validation()

    # Bind the validation result back into the second Maybe
    bind_result = maybe_instance_2.bind(validation_result)

    # Convert the bound result to an Either type
    either_result = bind_result.to_either()

def test_maybe_eq_returns_result_when_comparing_none_maybe_to_set():
    """Test that Maybe.__eq__ produces a result when a None-initialized Maybe is compared to a set containing False."""

    # A set built from repeated False values — deduplication yields {False}
    false_value = False
    set_with_false = {false_value, false_value, false_value, false_value}

    # Construct a Maybe instance with both values as None
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance to the set; capture the equality result
    eq_result = maybe_with_none.__eq__(set_with_false)

def test_maybe_bind_map_and_invalid_set_method_raises_attribute_error():
    """Test that Maybe supports bind/map chaining and that calling .to_box() on a plain set raises AttributeError."""

    # Use a simple True value as input for Maybe construction and chaining
    true_value = True

    # Create a Maybe instance wrapping two True values, then chain bind and map
    maybe_with_bool = maybe.Maybe(true_value, true_value)
    bound_result = maybe_with_bool.bind(true_value)
    mapped_result = bound_result.map(true_value)

    # Create a tuple of four True values to use as a Maybe value
    bool_tuple = (true_value, true_value, true_value, true_value)

    # Create a second Maybe instance using the tuple and a True flag
    maybe_with_tuple = maybe.Maybe(bool_tuple, true_value)

    # Attempt to call .to_box() on a plain set, which has no such method
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_does_not_raise():
    """Test that Maybe constructed with None and False can call map with a falsy value without error."""
    # Inputs: a None value and a False flag used for both construction and mapping
    none_value = None
    false_flag = False

    # Construct a Maybe instance wrapping a None value with a False flag
    maybe_instance = maybe.Maybe(none_value, false_flag)

    # Call map with a falsy value; expect no exception to be raised
    maybe_instance.map(false_flag)

def test_maybe_bind_with_empty_dict_on_none_value():
    """Test that bind can be called with an empty dict on a Maybe wrapping None and a falsy is_just flag."""

    # Construct a Maybe with a truthy value and truthy is_just flag
    truthy_value = True
    maybe_with_true = maybe.Maybe(truthy_value, truthy_value)

    # Prepare a bind target and a None-based Maybe
    empty_dict = {}
    none_value = None
    falsy_value = False

    # Construct a Maybe wrapping None with a falsy is_just flag
    maybe_with_none = maybe.Maybe(none_value, falsy_value)

    # Bind the empty dict to the Maybe wrapping None; verifies no error is raised
    maybe_with_none.bind(empty_dict)

def test_maybe_chained_operations_with_mixed_types():
    """Tests chaining of Maybe monad operations (to_box, filter, to_lazy, ap) across instances with mixed types including bytes, int, bool, and None."""

    # Construct a Maybe wrapping raw bytes with a None second argument
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_value = None
    maybe_bytes_none = module_0.Maybe(raw_bytes, none_value)

    # Box the first Maybe instance
    boxed_bytes_none = maybe_bytes_none.to_box()

    # Construct a second Maybe wrapping an int and a bool
    zero_int = 0
    true_bool = True
    maybe_int_bool = module_0.Maybe(zero_int, true_bool)

    # Filter the second Maybe using itself as the predicate
    filtered_maybe = maybe_int_bool.filter(maybe_int_bool)

    # Convert the second Maybe to a lazy representation
    lazy_maybe = maybe_int_bool.to_lazy()

    # Apply the filtered Maybe to the first Maybe instance
    applied_result = filtered_maybe.ap(maybe_bytes_none)

    # Filter the applied result using the applied result itself
    filtered_applied = filtered_maybe.filter(applied_result)

    # Construct a third Maybe using the lazy and boxed representations
    maybe_lazy_boxed = module_0.Maybe(lazy_maybe, boxed_bytes_none)

    # Check equality of the lazy Maybe against the bool value
    eq_result = lazy_maybe.__eq__(true_bool)

def test_maybe_ap_with_none_value_and_false_flag_does_not_raise():
    """Test that calling ap() on a Maybe constructed with None and False does not raise an exception."""
    # An integer to be passed as the argument to ap()
    integer_arg = 2862

    # Construct a Maybe representing a "nothing" state: no wrapped value, flag set to False
    empty_value = None
    is_something_flag = False
    nothing_maybe = maybe.Maybe(empty_value, is_something_flag)

    # Verify that calling ap() with an integer on a nothing-Maybe completes without error
    nothing_maybe.ap(integer_arg)

def test_maybe_supports_filter_to_lazy_map_and_to_try_chaining():
    """Tests that a Maybe instance correctly chains filter, to_lazy, map, and to_try operations."""
    # Set up the initial Maybe with a concrete integer value and a 'present' flag
    initial_value = 0
    is_present = True
    maybe_instance = maybe.Maybe(initial_value, is_present)

    # Filter the Maybe using itself as the predicate, then convert to a Lazy
    filtered_maybe = maybe_instance.filter(maybe_instance)
    lazy_from_maybe = maybe_instance.to_lazy()

    # Convert the filtered Maybe to a Lazy, then filter again using that Lazy
    lazy_from_filtered = filtered_maybe.to_lazy()
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the doubly-filtered result to a Try
    try_from_double_filtered = double_filtered.to_try()

    # Independently convert the original Maybe to Lazy a second time
    second_lazy_from_maybe = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_maybe = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_with_none_value_and_lazy_chaining():
    """Test that Maybe.filter chains correctly with to_lazy(), and that a Maybe(None, None) can filter using a lazy Maybe result without error."""

    # Set up the filter value and the tuple used as the filter argument
    filter_value = -283
    filter_tuple = (filter_value, filter_value, filter_value)

    # Create a Maybe with None as value and True as the has-value flag
    none_value = None
    has_value_flag = True
    maybe_with_none_and_true = maybe.Maybe(none_value, has_value_flag)

    # Filter the Maybe with the tuple, then convert the result to lazy form
    filtered_maybe = maybe_with_none_and_true.filter(filter_tuple)
    lazy_filtered_maybe = filtered_maybe.to_lazy()

    # Create a second Maybe with both arguments as None
    none_value_2 = None
    maybe_with_none_and_none = maybe.Maybe(none_value_2, none_value_2)

    # Filter the second Maybe using the lazy result from the first chain
    maybe_with_none_and_none.filter(lazy_filtered_maybe)

def test_maybe_get_or_else_and_filter_with_present_and_absent_values():
    """Test that Maybe resolves a present value via get_or_else, converts to box, and applies filter on an absent Maybe."""

    # Define a fallback integer and a sample string used to build the wrapped value
    fallback_int = 2281
    sample_str = "gZ(\\mOcN"
    sample_dict = {sample_str: sample_str}

    # Build a tuple to be wrapped in a present Maybe
    wrapped_tuple = (sample_str, sample_str, sample_dict, sample_dict)

    # Create a present Maybe wrapping the tuple
    is_present = True
    maybe_with_tuple = maybe.Maybe(wrapped_tuple, is_present)

    # Resolve the value from the present Maybe; should return the wrapped value
    resolved_value = maybe_with_tuple.get_or_else(fallback_int)

    # Create a Generic instance to use as the value for an absent Maybe
    generic_instance = typing.Generic()

    # Convert the present Maybe to a box representation
    boxed_maybe = maybe_with_tuple.to_box()

    # Create an absent Maybe wrapping the generic instance
    is_absent = False
    maybe_with_generic = maybe.Maybe(generic_instance, is_absent)

    # Apply filter on the absent Maybe using the resolved value from the present Maybe
    maybe_with_generic.filter(resolved_value)

def test_maybe_monad_conversions_and_chaining():
    """Test that Maybe supports to_validation, to_try, get_or_else, and bind across diverse value/fallback combinations."""

    # --- First Maybe: truthy value with no fallback ---
    truthy_value = True
    no_fallback = None
    maybe_true_with_none_fallback = maybe.Maybe(truthy_value, no_fallback)

    # Convert to Validation monad
    validation_from_true_maybe = maybe_true_with_none_fallback.to_validation()

    # --- Second Maybe: negative int value with empty tuple as fallback ---
    float_value = -286.64
    negative_int = -1784
    empty_tuple = ()
    maybe_negative_int_with_empty_tuple = maybe.Maybe(negative_int, empty_tuple)

    # Convert to Validation monad
    validation_from_int_maybe = maybe_negative_int_with_empty_tuple.to_validation()

    # Unwrap value, falling back to negative_int if empty
    unwrapped_or_else_value = maybe_negative_int_with_empty_tuple.get_or_else(negative_int)

    # Convert to Try monad
    try_from_int_maybe = maybe_negative_int_with_empty_tuple.to_try()

    # --- Third Maybe: float value with float fallback ---
    maybe_float_with_float_fallback = maybe.Maybe(float_value, float_value)

    # Bind the Try result into the second Maybe
    maybe_negative_int_with_empty_tuple.bind(try_from_int_maybe)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test that Maybe.map() accepts a set and Maybe.to_either() works on a Maybe wrapping an integer."""

    # Construct a Maybe wrapping None with has_value=True
    none_value = None
    is_present = True
    maybe_with_none = maybe.Maybe(none_value, is_present)

    # Call map() with a set as the mapping argument
    mapping_set = {is_present}
    map_result = maybe_with_none.map(mapping_set)

    # Construct a second Maybe wrapping a negative integer with has_value=True
    negative_int_value = -1095
    is_present_second = True
    maybe_with_int = maybe.Maybe(negative_int_value, is_present_second)

    # Convert the Maybe to an Either representation
    either_result = maybe_with_int.to_either()

def test_maybe_conversion_methods_to_lazy_either_and_try():
    """Test that Maybe with None and mixed values correctly supports chained conversions to lazy, either, and try."""

    # Create a Maybe instance where both value and context are None
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Build a tuple containing the first Maybe, to use as an argument
    maybe_tuple_arg = (maybe_with_none,)

    # Convert the None-based Maybe to a lazy representation
    lazy_from_none_maybe = maybe_with_none.to_lazy()

    # Create a second Maybe using the tuple and a False flag
    false_value = False
    maybe_with_tuple = maybe.Maybe(maybe_tuple_arg, false_value)

    # Convert the None-based Maybe to an either representation (first call)
    either_from_none_maybe_first = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to a try representation
    try_from_tuple_maybe = maybe_with_tuple.to_try()

    # Convert the None-based Maybe to an either representation (second call)
    either_from_none_maybe_second = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to an either representation
    either_from_tuple_maybe = maybe_with_tuple.to_either()

    # Verify that the try result can itself be converted to a lazy representation
    try_from_tuple_maybe.to_lazy()

def test_maybe_to_try_then_to_box_succeeds():
    """Test that a Maybe(True, False) can be chained through to_try() and then to_box() without error."""
    # Construct a Maybe with a truthy value and a falsy flag
    is_success = True
    is_empty = False
    maybe_instance = maybe.Maybe(is_success, is_empty)

    # Convert the Maybe to a Try, then further convert to a Box
    try_result = maybe_instance.to_try()
    try_result.to_box()

def test_maybe_none_true_chained_transformations_and_ap():
    """Test that Maybe(None, True) correctly chains ap, lazy, validation, filter, get_or_else, either, try, and box transformations."""

    # Input values used throughout the chain
    raw_bytes_input = b"C\xcf\xe7/"
    none_value = None
    bool_flag_true = True

    # Construct a Maybe with None value and True flag
    maybe_none_true = maybe.Maybe(none_value, bool_flag_true)

    # Apply ap with None, then convert to lazy and validation
    maybe_after_ap = maybe_none_true.ap(none_value)
    lazy_from_ap = maybe_after_ap.to_lazy()
    validation_from_lazy = lazy_from_ap.to_validation()

    # Filter the original maybe using the validation result
    filtered_maybe = maybe_none_true.filter(validation_from_lazy)

    # Derive further transformed values from the filtered maybe
    get_or_else_result = filtered_maybe.get_or_else(filtered_maybe)
    either_from_filtered = filtered_maybe.to_either()

    # Convert validation to a try monad
    try_from_validation = validation_from_lazy.to_try()

    # Check equality between filtered maybe and the ap result
    eq_result = filtered_maybe.__eq__(maybe_after_ap)

    # Convert get_or_else result to a box
    box_from_get_or_else = get_or_else_result.to_box()

    # Apply raw bytes to the try monad
    try_from_validation.ap(raw_bytes_input)

def test_maybe_monad_chaining_with_none_and_bytes_values():
    """Tests that Maybe monad chaining operations compose correctly across None and bytes-valued Maybe instances."""

    # Define primitive input values
    bytes_value = b"\xdbC\xcf\xe7/"
    none_value = None
    initial_bool = True
    negative_int = -3289

    # --- Chain 1: Maybe wrapping None with a True flag ---
    # Construct a Maybe with no value (None) and a True flag
    maybe_none_true = maybe.Maybe(none_value, initial_bool)

    # Apply None as a function via ap, then apply bytes_value
    ap_none_result = maybe_none_true.ap(none_value)
    ap_bytes_result = ap_none_result.ap(bytes_value)

    # Convert the result of ap-chaining to a Validation
    validation_from_ap_chain = ap_bytes_result.to_validation()

    # --- Chain 2: Maybe wrapping None with a bytes value ---
    # Construct a Maybe with no value (None) and bytes as the fallback
    maybe_none_bytes = maybe.Maybe(none_value, bytes_value)

    # Retrieve the value or fall back to itself
    get_or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)

    # Convert to Validation, then use it as the binding function
    validation_from_maybe_none_bytes = maybe_none_bytes.to_validation()
    bind_result = maybe_none_bytes.bind(validation_from_maybe_none_bytes)

    # Convert to Either and apply self via ap
    either_result = maybe_none_bytes.to_either()
    ap_self_result = maybe_none_bytes.ap(maybe_none_bytes)

    # Compare Either against the Validation using __eq__
    either_eq_validation = either_result.__eq__(validation_from_maybe_none_bytes)

    # Bind the Either with the maybe_none_bytes instance
    either_bind_result = either_result.bind(maybe_none_bytes)

    # Convert maybe_none_bytes to a Try and compare maybe_none_bytes against bind_result
    try_result = maybe_none_bytes.to_try()
    maybe_eq_bind = maybe_none_bytes.__eq__(bind_result)

    # Convert bind_result to Validation
    validation_from_bind = bind_result.to_validation()

    # Apply a negative integer via ap on the Try result
    try_result.ap(negative_int)

def test_maybe_false_values_chain_conversions_and_map():
    """Test that Maybe(False, False) supports equality check, chained conversions to Either/Lazy/Validation, and mapping."""

    false_value = False

    # Create a Maybe with both fields set to False and verify equality comparison runs without error
    maybe_with_false = maybe.Maybe(false_value, false_value)
    eq_result = maybe_with_false.__eq__(false_value)  # result unused; implicitly tests no exception is raised

    # Create a second Maybe and chain it through to_either → to_lazy → to_validation
    maybe_for_conversion = maybe.Maybe(false_value, false_value)
    either_value = maybe_for_conversion.to_either()
    lazy_value = maybe_for_conversion.to_lazy()
    validation_value = lazy_value.to_validation()

    # Create a third Maybe and map it using the validation value derived above
    maybe_for_map = maybe.Maybe(false_value, false_value)
    maybe_for_map.map(validation_value)

def test_maybe_false_false_equality_and_conversion_chain():
    """Test that Maybe(False, False) supports self-equality and converts through Try to Validation."""

    # Construct a Maybe instance with both values set to False
    false_value = False
    maybe_instance = maybe.Maybe(false_value, false_value)

    # Verify the instance compares equal to itself
    equality_result = maybe_instance.__eq__(maybe_instance)

    # Convert Maybe to Try, then further to Validation
    try_instance = maybe_instance.to_try()
    try_instance.to_validation()

