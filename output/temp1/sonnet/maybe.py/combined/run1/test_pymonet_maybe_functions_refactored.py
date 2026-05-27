import pytest
import maybe as maybe
import typing as typing

def test_maybe_instantiation_with_bytes_arguments():
    """Test that Maybe can be instantiated with a bytes value provided as both constructor arguments."""
    # Use an arbitrary bytes literal as both positional arguments to the constructor
    sample_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Instantiate Maybe with the same bytes value for both arguments
    maybe_instance = maybe.Maybe(sample_bytes, sample_bytes)

def test_maybe_instantiation_with_none_arguments():
    """Test that Maybe can be instantiated with two None arguments."""
    # Use None for both arguments to verify the constructor handles absent values
    none_value = None

    maybe_instance = maybe.Maybe(none_value, none_value)

def test_maybe_monad_chained_operations_with_string_value():
    """Tests chained monadic operations (ap, map, filter, bind, to_validation, to_either) on Maybe instances constructed from a string value."""

    # Construct the primary string value used as both content and fallback
    string_value = "p4xa>bl^oP"

    # Create the first Maybe instance with the string value
    maybe_instance = maybe.Maybe(string_value, string_value)

    # Check equality of the Maybe instance against the raw string
    eq_result = maybe_instance.__eq__(string_value)

    # Apply ap (applicative) using the string value
    ap_result = maybe_instance.ap(string_value)

    # Retrieve the value or fall back to the string value
    get_or_else_result = maybe_instance.get_or_else(string_value)

    # Map over the Maybe using the ap result as the mapping function
    map_result_first = maybe_instance.map(ap_result)

    # Filter using the ap result as the predicate
    filter_result_first = maybe_instance.filter(ap_result)

    # Map again using the ap result (second application)
    map_result_second = maybe_instance.map(ap_result)

    # Apply ap a second time using the string value
    ap_result_second = maybe_instance.ap(string_value)

    # Check equality between the two ap results
    eq_ap_results = ap_result.__eq__(ap_result_second)

    # Filter the first ap result using the get_or_else result as predicate
    filter_on_ap = ap_result.filter(get_or_else_result)

    # Retrieve value from the second ap result, falling back to string value
    get_or_else_on_ap_second = ap_result_second.get_or_else(string_value)

    # Create a second Maybe instance with the same string value
    maybe_instance_second = maybe.Maybe(string_value, string_value)

    # Convert the second Maybe instance to a Validation
    validation_result = maybe_instance_second.to_validation()

    # Bind the second Maybe instance using the validation result
    bind_result = maybe_instance_second.bind(validation_result)

    # Convert the bound result to an Either
    either_result = bind_result.to_either()

def test_maybe_eq_returns_false_when_compared_to_set_of_false_values():
    """Test that a Maybe instance holding None values is not equal to a set of False values."""

    # A boolean False used to populate a set of uniform false values
    false_value = False

    # A set containing only False (duplicates collapse, but construction mirrors original)
    set_of_false = {false_value, false_value, false_value, false_value}

    # None used as the wrapped value for the Maybe instance
    null_value = None

    # Create a Maybe monad wrapping two None values
    maybe_with_none = maybe.Maybe(null_value, null_value)

    # Compare the Maybe instance against the set of False values using __eq__
    eq_result = maybe_with_none.__eq__(set_of_false)

def test_maybe_bind_map_chaining_and_invalid_set_method_raises_attribute_error():
    """Test that Maybe supports bind/map chaining and that calling to_box() on a plain set raises AttributeError."""

    # Use a simple boolean as the wrapped value and the bind/map argument
    flag_value = True

    # Construct a Maybe wrapping a boolean and chain bind then map
    maybe_with_bool = maybe.Maybe(flag_value, flag_value)
    bound_result = maybe_with_bool.bind(flag_value)
    mapped_result = bound_result.map(flag_value)

    # Construct a second Maybe wrapping a tuple of four boolean values
    tuple_value = (flag_value, flag_value, flag_value, flag_value)
    maybe_with_tuple = maybe.Maybe(tuple_value, flag_value)

    # Calling to_box() on a plain set is invalid and expected to raise AttributeError
    empty_set = set()
    with pytest.raises(AttributeError):
        empty_set.to_box()

def test_maybe_map_with_none_value_and_false_flag():
    """Test that Maybe constructed with None and False can have map called with a falsy value without error."""
    # Construct a Maybe monad with an absent (None) value and a False flag
    empty_value = None
    falsy_flag = False

    # Instantiate Maybe with the empty value and falsy flag
    maybe_instance = maybe.Maybe(empty_value, falsy_flag)

    # Call map with the falsy flag; expect no error to be raised
    maybe_instance.map(falsy_flag)

def test_maybe_bind_with_none_value_and_empty_dict():
    """Verify that Maybe can be constructed with truthy values and with None,
    and that bind can be called on a Maybe wrapping None with an empty dict."""

    # Construct a Maybe with a truthy value as both the wrapped value and the
    # is_some flag — verifies instantiation does not raise
    truthy_value = True
    maybe_with_true = maybe.Maybe(truthy_value, truthy_value)

    # Prepare the argument to pass to bind
    empty_dict = {}

    # Construct a Maybe wrapping None with a falsy is_some flag
    none_value = None
    falsy_value = False
    maybe_with_none = maybe.Maybe(none_value, falsy_value)

    # Call bind on the Maybe wrapping None — verifies no error is raised
    maybe_with_none.bind(empty_dict)

def test_maybe_chained_operations_with_mixed_types():
    """Tests that Maybe instances with mixed types support chained monad operations including filter, to_box, to_lazy, and ap."""

    # Construct a Maybe wrapping raw bytes with a None context
    raw_bytes_value = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_context = None
    maybe_bytes = maybe.Maybe(raw_bytes_value, none_context)

    # Box the bytes-based Maybe
    boxed_bytes = maybe_bytes.to_box()

    # Construct a Maybe wrapping an integer with a boolean context
    int_value = 0
    bool_context = True
    maybe_int = maybe.Maybe(int_value, bool_context)

    # Filter the int-based Maybe using itself as the predicate
    filtered_maybe_int = maybe_int.filter(maybe_int)

    # Lift the int-based Maybe into a lazy representation
    lazy_maybe_int = maybe_int.to_lazy()

    # Apply the filtered Maybe to the bytes-based Maybe
    applied_result = filtered_maybe_int.ap(maybe_bytes)

    # Filter the applied result using itself as the predicate
    filtered_applied = filtered_maybe_int.filter(applied_result)

    # Construct a new Maybe from the lazy and boxed representations
    maybe_lazy_boxed = maybe.Maybe(lazy_maybe_int, boxed_bytes)

    # Check equality of the lazy Maybe against the boolean context
    eq_result = lazy_maybe_int.__eq__(bool_context)

def test_maybe_ap_with_none_and_false_does_not_raise():
    """Test that calling `ap` on a `Maybe` initialized with `None` and `False` executes without error."""
    # Integer value to pass into the ap() call
    int_value = 2862

    # Initialize Maybe with None and False, representing a Nothing/falsy state
    none_value = None
    is_just = False
    nothing_maybe = maybe.Maybe(none_value, is_just)

    # Apply the integer value to the Nothing Maybe; should not raise
    nothing_maybe.ap(int_value)

def test_maybe_chained_filter_lazy_map_and_to_try_operations():
    """Test that a Maybe instance supports chaining filter, to_lazy, map, and to_try transformations."""

    # Set up the initial Maybe instance with a value of 0 and presence flag True
    initial_value = 0
    is_present = True
    maybe_instance = maybe.Maybe(initial_value, is_present)

    # Filter the Maybe using itself as the predicate
    filtered_maybe = maybe_instance.filter(maybe_instance)

    # Convert the original Maybe to a lazy representation
    lazy_from_maybe = maybe_instance.to_lazy()

    # Convert the filtered Maybe to a lazy representation
    lazy_from_filtered = filtered_maybe.to_lazy()

    # Filter the already-filtered Maybe using its own lazy form
    filtered_again = filtered_maybe.filter(lazy_from_filtered)

    # Convert the doubly-filtered Maybe to a Try
    try_from_filtered_again = filtered_again.to_try()

    # Perform a second independent to_lazy conversion on the original Maybe instance
    another_lazy_from_maybe = maybe_instance.to_lazy()

    # Map the filtered Maybe over itself
    mapped_filtered = filtered_maybe.map(filtered_maybe)

def test_maybe_filter_on_none_value_with_lazy_conversion():
    """Test that filtering a Maybe containing None produces a lazy-convertible result that can be passed as a filter argument to another Maybe instance."""

    # Set up a tuple of repeated negative integers to use as the filter argument
    negative_int = -283
    filter_tuple = (negative_int, negative_int, negative_int)

    # Create a Maybe wrapping None with is_present_flag=True, then apply filter
    none_value = None
    is_present_flag = True
    maybe_with_none_and_bool = maybe.Maybe(none_value, is_present_flag)
    filtered_maybe = maybe_with_none_and_bool.filter(filter_tuple)

    # Convert the filtered result to a lazy representation
    lazy_filtered_maybe = filtered_maybe.to_lazy()

    # Create a second Maybe wrapping None (both value and flag are None)
    none_value_2 = None
    maybe_with_none_none = maybe.Maybe(none_value_2, none_value_2)

    # Filter the second Maybe using the lazy result from the first
    maybe_with_none_none.filter(lazy_filtered_maybe)

def test_maybe_get_or_else_to_box_and_filter_with_mixed_types():
    """Test that Maybe supports get_or_else retrieval, to_box conversion, and filter on instances with differing types and presence flags."""

    # --- Setup shared primitives ---
    default_int_value = 2281
    sample_str = "gZ(\\mOcN"
    sample_dict = {sample_str: sample_str}

    # Build a tuple payload containing the string and dict entries
    tuple_value = (sample_str, sample_str, sample_dict, sample_dict)

    # --- Create a Maybe wrapping a tuple with presence=True ---
    is_present_true = True
    maybe_tuple = maybe.Maybe(tuple_value, is_present_true)

    # Retrieve the value using a default fallback integer
    retrieved_value = maybe_tuple.get_or_else(default_int_value)

    # --- Create a Generic instance for use in a second Maybe ---
    generic_instance = typing.Generic()

    # --- Convert the first Maybe to a box representation ---
    boxed_value = maybe_tuple.to_box()

    # --- Create a Maybe wrapping a Generic object with presence=False ---
    is_present_false = False
    maybe_generic = maybe.Maybe(generic_instance, is_present_false)

    # Apply a filter using the previously retrieved value
    maybe_generic.filter(retrieved_value)

def test_maybe_methods_with_mixed_types_and_empty_fallback():
    """Test that Maybe with mixed types supports to_validation, get_or_else, to_try, and bind without error."""

    # --- Maybe wrapping a bool with a None fallback ---
    bool_value = True
    none_fallback = None
    maybe_bool_none = maybe.Maybe(bool_value, none_fallback)
    validation_from_bool_none = maybe_bool_none.to_validation()

    # --- Maybe wrapping a negative int with an empty-tuple fallback ---
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()
    maybe_int_empty_tuple = maybe.Maybe(int_value, empty_tuple)

    # Convert to validation and retrieve value via get_or_else
    validation_from_int_tuple = maybe_int_empty_tuple.to_validation()
    get_or_else_result = maybe_int_empty_tuple.get_or_else(int_value)

    # Convert to Try, then use it as the callable passed to bind
    try_from_int_tuple = maybe_int_empty_tuple.to_try()

    # --- Maybe wrapping a float with itself as fallback (constructed but not bound) ---
    maybe_float_float = maybe.Maybe(float_value, float_value)

    # Bind the Try result onto the int/empty-tuple Maybe
    maybe_int_empty_tuple.bind(try_from_int_tuple)

def test_maybe_map_with_set_and_to_either_conversion():
    """Test that Maybe wrapping None can be mapped with a set, and Maybe wrapping an integer can be converted to Either."""

    # Construct a Maybe from a None value with has-value flag set to True
    none_value = None
    has_value_flag = True
    maybe_with_none = maybe.Maybe(none_value, has_value_flag)

    # Map the Maybe using a set containing the has-value flag
    mapping_set = {has_value_flag}
    map_result = maybe_with_none.map(mapping_set)

    # Construct a second Maybe wrapping an integer and convert it to Either
    integer_value = -1095
    second_has_value_flag = True
    maybe_with_integer = maybe.Maybe(integer_value, second_has_value_flag)
    either_result = maybe_with_integer.to_either()

def test_maybe_with_none_values_converts_to_lazy_either_and_try():
    """Test that Maybe instances wrapping None and nested Maybe values can be converted to Lazy, Either, and Try monadic types."""

    # Build a Maybe wrapping two None values
    none_value = None
    maybe_none = maybe.Maybe(none_value, none_value)

    # Convert the None-wrapping Maybe to a Lazy representation
    lazy_from_maybe_none = maybe_none.to_lazy()

    # Build a second Maybe wrapping a tuple (containing the first Maybe) and False
    maybe_tuple = (maybe_none,)
    false_value = False
    maybe_with_tuple = maybe.Maybe(maybe_tuple, false_value)

    # Convert the None-wrapping Maybe to Either (first call)
    either_from_maybe_none_first = maybe_none.to_either
# (Truncated by extractor)