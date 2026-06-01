import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with a bytes value as both arguments."""
    # Use a raw bytes value as both the first and second argument to Maybe
    raw_bytes_value = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Instantiate Maybe with the same bytes value for both parameters
    maybe_instance = maybe.Maybe(raw_bytes_value, raw_bytes_value)

def test_maybe_constructed_with_none_none():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None for both arguments to exercise the minimal construction path
    none_value = None

    # Construct Maybe with two None values; should not raise
    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chaining_operations_with_string_value():
    """Verify that a Maybe monad supports chaining of ap, map, filter, get_or_else, bind, to_validation, and to_either operations."""

    # Use a fixed string as both the wrapped value and the fallback/argument
    string_value = "p4xa>bl^oP"

    # Create the primary Maybe instance wrapping the string value
    maybe_instance = maybe.Maybe(string_value, string_value)

    # Check equality of the Maybe instance against the raw string
    eq_result = maybe_instance.__eq__(string_value)

    # Apply the string as an argument via ap
    ap_result = maybe_instance.ap(string_value)

    # Extract the value, falling back to string_value if absent
    extracted_value = maybe_instance.get_or_else(string_value)

    # Map over the Maybe using the ap result as a function
    mapped_result = maybe_instance.map(ap_result)

    # Filter the Maybe using the ap result as a predicate
    filtered_result = maybe_instance.filter(ap_result)

    # Map again to confirm repeated mapping is stable
    remapped_result = maybe_instance.map(ap_result)

    # Apply the string a second time via ap
    second_ap_result = maybe_instance.ap(string_value)

    # Compare the two ap results for equality
    ap_equality_check = ap_result.__eq__(second_ap_result)

    # Filter the first ap result using the extracted value as a predicate
    filtered_ap_result = ap_result.filter(extracted_value)

    # Extract from the second ap result with string_value as fallback
    ap_extracted_value = second_ap_result.get_or_else(string_value)

    # Create a second independent Maybe instance with the same inputs
    second_maybe_instance = maybe.Maybe(string_value, string_value)

    # Convert the second Maybe to a Validation
    validation_result = second_maybe_instance.to_validation()

    # Bind the second Maybe using the validation result
    bound_result = second_maybe_instance.bind(validation_result)

    # Convert the bound result to an Either
    either_result = bound_result.to_either()

def test_maybe_eq_returns_result_when_compared_to_set_of_false():
    """Test that Maybe.__eq__ produces a result when comparing a Maybe(None, None) instance to a set of False values."""

    # A boolean False used to populate the set
    false_value = False

    # A set containing only False (duplicates collapse, but literals are preserved as written)
    set_of_false = {false_value, false_value, false_value, false_value}

    # None used as both arguments to Maybe
    none_value = None

    # Construct a Maybe instance with no values (both slots are None)
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Compare the Maybe instance to the set of False; capture the equality result
    eq_result = maybe_with_none.__eq__(set_of_false)

def test_maybe_bind_map_with_bool_and_invalid_set_method_raises_attribute_error():
    """Test that Maybe bind/map operations work with booleans, and that calling to_box() on a plain set raises AttributeError."""

    # Use a simple True value as both the wrapped value and the function argument
    true_value = True

    # Create a Maybe wrapping a boolean, then chain bind and map with the same bool
    maybe_with_bool = maybe.Maybe(true_value, true_value)
    bound_maybe = maybe_with_bool.bind(true_value)
    mapped_maybe = bound_maybe.map(true_value)

    # Create a tuple of four booleans to use as a wrapped value in a second Maybe
    bool_quadruple = (true_value, true_value, true_value, true_value)
    maybe_with_tuple = maybe.Maybe(bool_quadruple, true_value)

    # Attempt to call to_box() on a plain set, which has no such method
    empty_set = set()
    empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag_does_not_raise():
    """Test that Maybe constructed with None and False allows .map() to be called with a falsy value without error."""
    # Use None as the wrapped value (empty/absent) and False as the 'is some' flag
    empty_value = None
    is_some_flag = False

    # Construct a Maybe instance with no value and a falsy flag
    maybe_instance = maybe.Maybe(empty_value, is_some_flag)

    # Call map with the same falsy flag (acts as the mapping argument)
    maybe_instance.map(is_some_flag)

def test_maybe_bind_with_none_value_and_empty_dict():
    """Test that bind on a Maybe wrapping None with an empty dict executes without error."""
    truthy_value = True

    # Construct a Maybe with two truthy values (verifies construction does not raise)
    maybe_with_true = maybe.Maybe(truthy_value, truthy_value)

    empty_dict = {}
    none_value = None
    falsy_value = False

    # Construct a Maybe wrapping None and call bind with an empty dict
    maybe_with_none = maybe.Maybe(none_value, falsy_value)
    maybe_with_none.bind(empty_dict)

def test_maybe_chained_operations_with_mixed_types():
    """Test that Maybe instances support chained operations (to_box, filter, to_lazy, ap) across mixed value types including bytes, int, and bool."""

    # --- Setup: Maybe wrapping raw bytes with no context ---
    raw_bytes_value = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    no_context = None
    maybe_bytes = maybe.Maybe(raw_bytes_value, no_context)

    # Convert the bytes-Maybe to a box representation
    boxed_bytes = maybe_bytes.to_box()

    # --- Setup: Maybe wrapping an integer zero with a True context ---
    zero_value = 0
    true_context = True
    maybe_int = maybe.Maybe(zero_value, true_context)

    # Filter maybe_int using itself as the predicate
    filtered_maybe_int = maybe_int.filter(maybe_int)

    # Convert maybe_int to a lazy representation
    lazy_maybe_int = maybe_int.to_lazy()

    # Apply the filtered maybe_int against the bytes-Maybe
    applied_result = filtered_maybe_int.ap(maybe_bytes)

    # Filter the applied result using filtered_maybe_int as the predicate
    filtered_applied = filtered_maybe_int.filter(applied_result)

    # --- Compose: Maybe wrapping the lazy and boxed results ---
    maybe_lazy_boxed = maybe.Maybe(lazy_maybe_int, boxed_bytes)

    # Check equality of the lazy representation against the True context
    lazy_eq_true = lazy_maybe_int.__eq__(true_context)

def test_maybe_ap_with_none_value_and_false_flag():
    """Test that calling ap() on a Maybe wrapping None with is_applicative=False does not raise."""
    # The integer value to be passed to ap()
    applicative_value = 2862

    # None represents the absence of a wrapped value
    empty_value = None

    # False indicates the Maybe is not in applicative mode
    is_applicative = False

    # Construct a Maybe instance wrapping None
    maybe_none_instance = maybe.Maybe(empty_value, is_applicative)

    # Apply the integer value via ap(); should not raise
    maybe_none_instance.ap(applicative_value)

def test_maybe_supports_filter_to_lazy_map_and_to_try_chaining():
    """Test that Maybe supports chained filter, to_lazy, map, and to_try operations without error."""

    # Construct a Maybe instance wrapping an integer with an explicit has-value flag
    initial_value = 0
    has_value_flag = True
    maybe_instance = maybe.Maybe(initial_value, has_value_flag)

    # Filter the Maybe using itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the original Maybe to its lazy representation
    lazy_from_maybe = maybe_instance.to_lazy()

    # Convert the filtered Maybe to its lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the already-filtered Maybe using its own lazy form
    double_filtered = filtered_maybe.filter(lazy_from_filtered)

    # Convert the double-filtered result to a Try
    try_from_double_filtered = double_filtered.to_try()

    # Produce a second lazy conversion of the original Maybe (independent of the chain above)
    second_lazy_from_maybe = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself as the mapping function
    mapped_maybe = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_on_none_value_with_tuple_and_lazy():
    """Test that filter() on a Maybe wrapping None chains correctly into a lazy value and can be passed to another Maybe's filter."""
    # Construct a tuple of repeated negative integers to use as a filter argument
    negative_int = -283
    int_tuple = (negative_int, negative_int, negative_int)

    # Create a Maybe with no value (None) but with a True flag
    no_value = None
    flag_true = True
    maybe_none_with_flag = maybe.Maybe(no_value, flag_true)

    # Apply filter with the integer tuple; result is still a Maybe
    filtered_maybe = maybe_none_with_flag.filter(int_tuple)

    # Convert the filtered Maybe into a lazy representation
    lazy_filtered = filtered_maybe.to_lazy()

    # Create a second Maybe with no value and no flag
    no_value_alt = None
    maybe_all_none = maybe.Maybe(no_value_alt, no_value_alt)

    # Filter the all-None Maybe using the lazy value from the first chain
    maybe_all_none.filter(lazy_filtered)

def test_maybe_get_or_else_to_box_and_filter_with_generic():
    """Test that Maybe wrapping a tuple supports get_or_else and to_box, and that a Maybe wrapping a Generic with False supports filter using the resolved value."""

    # Set up a fallback integer and a string used to build composite structures
    fallback_int = 2281
    key_str = "gZ(\\mOcN"

    # Build a dict and tuple from the string, to be wrapped in a Maybe
    str_keyed_dict = {key_str: key_str}
    maybe_tuple_value = (key_str, key_str, str_keyed_dict, str_keyed_dict)

    # Create a Maybe with a tuple value and presence flag True
    is_present_true = True
    maybe_with_tuple = maybe.Maybe(maybe_tuple_value, is_present_true)

    # Resolve the Maybe value, falling back to fallback_int if absent
    maybe_value_or_fallback = maybe_with_tuple.get_or_else(fallback_int)

    # Create a Generic instance to wrap in a second Maybe
    generic_instance = typing.Generic()

    # Convert the first Maybe to a box (result not further used)
    boxed_maybe = maybe_with_tuple.to_box()  # noqa: F841

    # Create a second Maybe wrapping the generic instance with presence flag False
    is_present_false = False
    maybe_with_generic = maybe.Maybe(generic_instance, is_present_false)

    # Apply filter to the second Maybe using the resolved value from the first
    maybe_with_generic.filter(maybe_value_or_fallback)

def test_maybe_monad_methods_with_mixed_types():
    """Test that Maybe instances with mixed types support to_validation, get_or_else, to_try, and bind without error."""

    # --- Maybe wrapping a truthy boolean with None as fallback ---
    truthy_value = True
    absent_fallback = None
    maybe_with_truthy = maybe.Maybe(truthy_value, absent_fallback)

    # Convert to Validation; result is not asserted but must not raise
    validation_from_truthy = maybe_with_truthy.to_validation()

    # --- Maybe wrapping an integer with an empty tuple as fallback ---
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()
    maybe_with_int = maybe.Maybe(int_value, empty_tuple)

    # Convert to Validation; result is not asserted but must not raise
    validation_from_int = maybe_with_int.to_validation()

    # Retrieve the wrapped value, falling back to int_value if absent
    or_else_result = maybe_with_int.get_or_else(int_value)

    # Convert to Try; result is passed to bind below
    try_result = maybe_with_int.to_try()

    # --- Maybe wrapping a float with a float fallback (created but not further used) ---
    maybe_with_float = maybe.Maybe(float_value, float_value)

    # Bind the try_result into maybe_with_int; exercises the bind pathway
    maybe_with_int.bind(try_result)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test that Maybe wrapping None can map over a set, and Maybe wrapping an integer converts to Either."""

    # Build a Maybe that wraps None, indicating an empty/absent value
    empty_value = None
    has_value_flag = True
    maybe_with_none = maybe.Maybe(empty_value, has_value_flag)

    # Apply map with a set as the mapping argument
    mapping_set = {has_value_flag}
    map_result = maybe_with_none.map(mapping_set)

    # Build a second Maybe that wraps an integer value
    integer_value = -1095
    second_has_value_flag = True
    maybe_with_integer = maybe.Maybe(integer_value, second_has_value_flag)

    # Convert the integer-wrapping Maybe to an Either type
    either_result = maybe_with_integer.to_either()

def test_maybe_with_none_and_nested_maybe_conversions():
    """Test that Maybe instances with None and nested Maybe values support chained conversions to lazy, either, and try."""

    # Create a Maybe wrapping two None values
    none_value = None
    maybe_with_none = maybe.Maybe(none_value, none_value)

    # Wrap the first Maybe in a tuple to use as a value in a second Maybe
    nested_maybe_tuple = (maybe_with_none,)

    # Convert the None-based Maybe to a lazy representation
    lazy_from_none_maybe = maybe_with_none.to_lazy()

    # Create a second Maybe using the nested tuple and a False flag
    false_value = False
    maybe_with_tuple = maybe.Maybe(nested_maybe_tuple, false_value)

    # Convert the None-based Maybe to an Either (first call)
    either_from_none_maybe_first = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to a Try, then chain to lazy
    try_from_tuple_maybe = maybe_with_tuple.to_try()

    # Convert the None-based Maybe to an Either again (intentional repeated call)
    either_from_none_maybe_second = maybe_with_none.to_either()

    # Convert the tuple-based Maybe to an Either
    either_from_tuple_maybe = maybe_with_tuple.to_either()

    # Chain to_lazy on the Try result
    try_from_tuple_maybe.to_lazy()

def test_maybe_to_try_to_box_conversion_succeeds():
    """Test that a Maybe built with True and False converts cleanly to a Try and then to a Box."""
    # Construct a Maybe with a truthy success flag and a falsy value flag
    is_success = True
    is_value_present = False

    maybe_instance = maybe.Maybe(is_success, is_value_present)

    # Convert the Maybe to a Try representation
    try_result = maybe_instance.to_try()

    # Convert the Try further to a Box — should complete without error
    try_result.to_box()

def test_maybe_none_value_chains_through_monad_transformations():
    """Test that a Maybe wrapping None chains through ap, lazy, validation, filter, either, try, and box transformations without error."""

    # Input values
    arbitrary_bytes = b"C\xcf\xe7/"
    none_value = None
    use_value_flag = True

    # Construct a Maybe wrapping None
    maybe_none = maybe.Maybe(none_value, use_value_flag)

    # Apply None as a function via ap — produces another Maybe-like result
    maybe_after_ap = maybe_none.ap(none_value)

    # Convert through lazy and validation representations
    lazy_value = maybe_after_ap.to_lazy()
    validation_value = lazy_value.to_validation()

    # Filter the original maybe using the validation value
    filtered_maybe = maybe_none.filter(validation_value)

    # Resolve with a fallback (itself), and convert to either
    fallback_value = filtered_maybe.get_or_else(filtered_maybe)
    either_value = filtered_maybe.to_either()

    # Convert the validation value to a try container
    try_value = validation_value.to_try()

    # Check equality between filtered maybe and the ap result
    equality_result = filtered_maybe.__eq__(maybe_after_ap)

    # Wrap the fallback value in a box
    boxed_value = fallback_value.to_box()

    # Apply arbitrary bytes to the try container
    try_value.ap(arbitrary_bytes)

def test_maybe_monad_chained_operations_with_none_and_bytes():
    """Test that Maybe monad chained operations (ap, bind, to_validation, to_either,
    to_try, get_or_else) work without errors when constructed with None and bytes values."""

    # --- Setup primitive values ---
    byte_value = b"\xdbC\xcf\xe7/"
    none_value = None
    flag_true = True

    # --- Build a Maybe from None with a True flag, then chain ap calls ---
    maybe_none_flagged = maybe.Maybe(none_value, flag_true)
    ap_none_result = maybe_none_flagged.ap(none_value)       # apply None as function
    ap_bytes_result = ap_none_result.ap(byte_value)          # apply bytes as function
    validation_from_chained_ap = ap_bytes_result.to_validation()  # convert to Validation

    # --- Build a Maybe from None with a bytes value ---
    maybe_none_bytes = maybe.Maybe(none_value, byte_value)

    # --- Exercise core Maybe operations on maybe_none_bytes ---
    get_or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)   # fallback to self
    validation_from_maybe_none_bytes = maybe_none_bytes.to_validation()   # convert to Validation
    bind_result = maybe_none_bytes.bind(validation_from_maybe_none_bytes) # bind with validation
    either_result = maybe_none_bytes.to_either()                          # convert to Either
    ap_self_result = maybe_none_bytes.ap(maybe_none_bytes)                # apply self as function

    # --- Perform equality and further chaining on derived structures ---
    negative_int = -3289
    either_eq_validation = either_result.__eq__(validation_from_maybe_none_bytes)  # compare Either to Validation
    either_bind_result = either_result.bind(maybe_none_bytes)                      # bind Either with Maybe
    try_result = maybe_none_bytes.to_try()                                         # convert to Try
    maybe_eq_bind = maybe_none_bytes.__eq__(bind_result)                           # compare Maybe to bind result
    validation_from_bind = bind_result.to_validation()                             # convert bind result to Validation
    try_result.ap(negative_int)                                                    # apply negative int to Try

def test_maybe_false_values_chain_conversions_and_map():
    """Test that a Maybe with False values supports equality, chained conversions, and mapping."""

    false_value = False

    # Verify that a Maybe created with False values supports equality comparison
    maybe_with_false = maybe.Maybe(false_value, false_value)
    equality_result = maybe_with_false.__eq__(false_value)

    # Chain conversions: Maybe → Either → Lazy → Validation
    maybe_for_conversion = maybe.Maybe(false_value, false_value)
    either_value = maybe_for_conversion.to_either()
    lazy_value = maybe_for_conversion.to_lazy()
    validation_value = lazy_value.to_validation()

    # Use the resulting Validation as a mapping function over a new Maybe
    maybe_to_map = maybe.Maybe(false_value, false_value)
    maybe_to_map.map(validation_value)

def test_maybe_false_false_supports_equality_and_converts_to_try_and_validation():
    """Test that a Maybe(False, False) supports self-equality and can be converted to Try and then to Validation."""

    false_value = False

    # Construct a Maybe instance with both value and flag set to False
    maybe_false = maybe.Maybe(false_value, false_value)

    # Verify the Maybe instance considers itself equal to itself
    is_equal_to_self = maybe_false.__eq__(maybe_false)

    # Convert the Maybe to a Try container
    try_result = maybe_false.to_try()

    # Further convert the Try result to a Validation container
    try_result.to_validation()

