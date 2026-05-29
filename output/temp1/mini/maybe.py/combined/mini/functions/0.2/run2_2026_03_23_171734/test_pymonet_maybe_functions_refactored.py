import pytest

import maybe as maybe_module
import typing as typing_module

def test_maybe_initializes_with_two_identical_byte_values():
    """Verify that Maybe can be instantiated with two identical byte-valued arguments."""
    # Raw byte sequence used as both parameters to Maybe — keep literal unchanged.
    raw_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Construct the Maybe object with the same bytes for both arguments.
    # This mirrors the original test's behavior (no assertions; ensures construction).
    maybe_instance = maybe_module.Maybe(raw_bytes, raw_bytes)

def test_maybe_constructs_with_none_values():
    """Verify Maybe can be constructed with two None values without raising."""
    # Arrange
    none_value = None

    # Act
    maybe_instance = maybe_module.Maybe(none_value, none_value)

    # Assert: construction succeeded and returned the expected type
    assert isinstance(maybe_instance, maybe_module.Maybe)

def test_maybe_methods_chain_runs_without_error():
    """Ensure chaining common Maybe operations (ap, map, filter, bind) and conversions (to_validation, to_either) executes without error."""
    # Sample input used throughout the chain (unchanged literal from original test)
    sample_text = "p4xa>bl^oP"

    # Create a Maybe instance with the same value for both parameters
    maybe_a = maybe_module.Maybe(sample_text, sample_text)

    # Compare Maybe to a raw string using the same dunder equality call as the original
    equals_result = maybe_a.__eq__(sample_text)

    # Apply an argument to the Maybe (originally var_0)
    applied1 = maybe_a.ap(sample_text)

    # Retrieve a default value if needed
    default1 = maybe_a.get_or_else(sample_text)

    # Map the applied result (first map)
    mapped1 = maybe_a.map(applied1)

    # Filter the applied result
    filtered1 = maybe_a.filter(applied1)

    # Map again as in the original sequence (second map)
    mapped2 = maybe_a.map(applied1)

    # Apply again to produce another applied value
    applied2 = maybe_a.ap(sample_text)

    # Compare the two applied results using the same dunder equality call
    equals_between_applied = applied1.__eq__(applied2)

    # Filter applied1 using default1 as predicate/value per original call ordering
    filtered2 = applied1.filter(default1)

    # Get default from the second applied result
    default_from_applied2 = applied2.get_or_else(sample_text)

    # Create a second Maybe instance and run conversion/bind/or-either chain
    maybe_b = maybe_module.Maybe(sample_text, sample_text)
    validation = maybe_b.to_validation()
    bound = maybe_b.bind(validation)
    either = bound.to_either()

def test_maybe_eq_with_set_of_false():
    """Ensure Maybe.__eq__ can be invoked with a set containing False values."""
    # A single False value used repeatedly to construct a set (duplicates collapse).
    false_value = False
    false_values_set = {false_value, false_value, false_value, false_value}

    # Construct Maybe with None values (preserve original inputs).
    none_value = None
    maybe_instance = maybe_module.Maybe(none_value, none_value)

    # Invoke equality method with the set to ensure it can be called without error.
    equality_result = maybe_instance.__eq__(false_values_set)

def test_maybe_bind_and_map_with_booleans_and_empty_set_to_box():
    """Exercise Maybe.bind and Maybe.map using boolean values and call to_box() on an empty set."""
    # Reuse a simple boolean value to mirror the original inputs.
    flag_value = True

    # Construct a Maybe instance with two identical boolean arguments.
    maybe_bool = maybe_module.Maybe(flag_value, flag_value)

    # Call bind on the Maybe instance with the boolean value.
    bound_maybe = maybe_bool.bind(flag_value)

    # Call map on the result of bind with the boolean value.
    mapped_maybe = bound_maybe.map(flag_value)

    # Construct another Maybe from a tuple of boolean values and a boolean flag.
    bool_tuple = (flag_value, flag_value, flag_value, flag_value)
    maybe_from_tuple = maybe_module.Maybe(bool_tuple, flag_value)

    # Create an empty set and invoke to_box() (kept as in original to respect test fixtures).
    empty_set = set()
    empty_set.to_box()

def test_maybe_map_called_on_none_value_with_false_mapper():
    """Ensure Maybe.map can be invoked for a Maybe constructed with None and a False mapper argument."""
    # Arrange
    none_value = None
    false_value = False

    maybe_instance = maybe_module.Maybe(none_value, false_value)

    # Act: call map with the same False argument (preserve original behavior and order)
    maybe_instance.map(false_value)

def test_maybe_bind_handles_none_value_with_empty_dict():
    """Ensure Maybe.bind accepts an empty mapping when the Maybe encapsulates None."""
    # Preserve a Maybe instance created with two True values (unused but kept for parity)
    true_pair = maybe_module.Maybe(True, True)

    # Prepare an empty mapping to bind
    empty_mapping = {}

    # Create a Maybe containing None with a False flag, then bind the empty mapping to it
    maybe_none = maybe_module.Maybe(None, False)

    # Invoke bind with the empty mapping (should not raise)
    maybe_none.bind(empty_mapping)

def test_maybe_operations_box_filter_lazy_ap_and_eq():
    """Ensure Maybe objects interoperate: boxing, filtering, lazy conversion, application, and equality check."""
    # Input values (preserve exactly as in the original test)
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_value = None

    # Create a Maybe wrapping the bytes and None, then box it
    maybe_bytes = maybe_module.Maybe(raw_bytes, none_value)
    boxed_bytes = maybe_bytes.to_box()

    # Create a Maybe wrapping an int and a boolean
    zero_int = 0
    true_flag = True
    maybe_int = maybe_module.Maybe(zero_int, true_flag)

    # Apply a sequence of operations exactly as originally ordered:
    # - filter by passing the Maybe itself (preserve original behavior)
    filtered_maybe = maybe_int.filter(maybe_int)
    # - convert to lazy representation
    lazy_maybe = maybe_int.to_lazy()
    # - apply the filtered maybe to the bytes-based maybe
    applied_result = filtered_maybe.ap(maybe_bytes)
    # - filter again using the result of the previous ap
    filtered_again = filtered_maybe.filter(applied_result)
    # - construct another Maybe from lazy result and boxed bytes
    combined_maybe = maybe_module.Maybe(lazy_maybe, boxed_bytes)
    # - equality check (using __eq__ directly to preserve original call form)
    equality_check = lazy_maybe.__eq__(true_flag)

def test_maybe_ap_accepts_integer_with_none_initial_value():
    """Verify that Maybe.ap can be invoked with an integer when initialized with None and False."""
    # Input values (preserved exactly from the original test)
    integer_value = 2862
    initial_value = None
    flag = False

    # Create the Maybe instance using the provided module alias
    maybe_instance = maybe_module.Maybe(initial_value, flag)

    # Invoke the ap method with the integer; test passes if this runs without error
    maybe_instance.ap(integer_value)

def test_maybe_method_chain_executes_in_order():
    """Call a sequence of Maybe methods (filter, map, to_lazy, to_try) to ensure they execute in order."""
    initial_value = 0
    truthy_flag = True

    # Create the Maybe instance with the same constructor arguments
    maybe_instance = maybe_module.Maybe(initial_value, truthy_flag)

    # Apply filter using the maybe instance itself
    filtered = maybe_instance.filter(maybe_instance)

    # Convert the original and filtered instances to lazy representations
    lazy_original = maybe_instance.to_lazy()
    lazy_filtered = filtered.to_lazy()

    # Filter the filtered value using the lazy_filtered as the predicate
    filtered_again = filtered.filter(lazy_filtered)

    # Convert the newly filtered result to a Try-like structure
    try_result = filtered_again.to_try()

    # Repeat converting the original maybe to lazy (as in the original test)
    lazy_original_again = maybe_instance.to_lazy()

    # Map over the filtered maybe using the filtered object as the mapping function/argument
    mapped_filtered = filtered.map(filtered)

def test_maybe_filter_accepts_lazy_value_from_another_maybe():
    """Ensure Maybe.filter can accept a lazy value produced by to_lazy()."""
    negative = -283
    repeated = (negative,) * 3

    first = maybe_module.Maybe(None, True)
    filtered = first.filter(repeated)
    lazy = filtered.to_lazy()

    second = maybe_module.Maybe(None, None)
    # Should accept the lazy value without raising an exception
    second.filter(lazy)

def test_maybe_filter_with_present_value_and_absent_generic():
    """Construct present and absent Maybe values, obtain a value with get_or_else,
    box the present Maybe, and pass the obtained value to filter on the absent Maybe."""
    # A default integer to be used as fallback in get_or_else
    default_int = 2281

    # A sample string (note the escaped backslash preserved exactly)
    sample_str = "gZ(\\mOcN"

    # A small dict using the sample string as key and value
    sample_dict = {sample_str: sample_str}

    # A tuple that includes the same dict twice (preserve original structure and order)
    sample_tuple = (sample_str, sample_str, sample_dict, sample_dict)

    # Create a Maybe that is present with the tuple value
    is_present_true = True
    present_maybe = maybe_module.Maybe(sample_tuple, is_present_true)

    # Extract the value from the present Maybe (should return sample_tuple)
    gotten_value = present_maybe.get_or_else(default_int)

    # Create a Generic instance (for the absent Maybe)
    generic_instance = typing_module.Generic()

    # Create a Maybe that is absent with the generic instance
    is_present_false = False

    # Box the present maybe (result assigned but not used further, preserved from original)
    boxed_value = present_maybe.to_box()

    # Create an absent Maybe and call filter with the previously obtained value
    absent_maybe = maybe_module.Maybe(generic_instance, is_present_false)
    absent_maybe.filter(gotten_value)

def test_maybe_conversion_and_bind_operations():
    """Exercise Maybe conversions and bind to ensure methods run with given values."""
    # Create a Maybe from a boolean and None and convert it to a validation
    initial_flag = True
    none_value = None
    maybe_flag_none = maybe_module.Maybe(initial_flag, none_value)
    validation_from_flag = maybe_flag_none.to_validation()

    # Create another Maybe from an int and an empty tuple and exercise several conversions
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()
    maybe_int_tuple = maybe_module.Maybe(int_value, empty_tuple)
    validation_from_int = maybe_int_tuple.to_validation()
    default_from_int_get_or_else = maybe_int_tuple.get_or_else(int_value)
    try_from_int = maybe_int_tuple.to_try()

    # Create a Maybe from two floats (result intentionally unused here) and bind the try result
    maybe_float_pair = maybe_module.Maybe(float_value, float_value)
    maybe_int_tuple.bind(try_from_int)

def test_maybe_map_and_to_either_with_none_and_negative_int():
    """Exercise Maybe.map with a set and Maybe.to_either on an integer value."""
    # Create a Maybe containing None with a True flag.
    none_val = None
    none_flag = True
    maybe_none = maybe_module.Maybe(none_val, none_flag)

    # Call map on the Maybe, passing a set containing the flag.
    mapping_input = {none_flag}
    mapped_result = maybe_none.map(mapping_input)

    # Create a second Maybe containing the integer -1095 with a True flag.
    int_val = -1095
    int_flag = True
    maybe_int = maybe_module.Maybe(int_val, int_flag)

    # Convert the second Maybe to an Either.
    either_result = maybe_int.to_either()

def test_maybe_conversion_chain_does_not_raise():
    """Verify that calling a sequence of Maybe conversion methods does not raise exceptions."""
    # Original None literal used twice to construct a Maybe with (None, None)
    none_value = None
    maybe_none_none = maybe_module.Maybe(none_value, none_value)

    # Wrap the first Maybe instance in a tuple and use it to construct another Maybe
    maybe_tuple = (maybe_none_none,)

    # Call conversion on the first Maybe (to_lazy)
    lazy_from_first_maybe = maybe_none_none.to_lazy()

    # Use the False literal as the second argument for the second Maybe instance
    false_flag = False
    maybe_tuple_false = maybe_module.Maybe(maybe_tuple, false_flag)

    # Call several conversion methods in the same order as the original test
    either_from_first_maybe = maybe_none_none.to_either()
    try_from_second_maybe = maybe_tuple_false.to_try()
    either_from_first_maybe_again = maybe_none_none.to_either()
    either_from_second_maybe = maybe_tuple_false.to_either()

    # Finally invoke to_lazy on the Try result (preserving original call)
    try_from_second_maybe.to_lazy()

def test_maybe_to_try_then_to_box_executes():
    """Ensure Maybe.to_try() returns an object whose to_box() can be invoked."""
    has_value = True
    is_absent = False

    maybe_instance = maybe_module.Maybe(has_value, is_absent)

    try_result = maybe_instance.to_try()
    try_result.to_box()

def test_maybe_ap_and_conversion_chain():
    """Exercise a Maybe through ap and multiple conversion/filter operations."""
    # Setup input literals (unchanged)
    sample_bytes = b"C\xcf\xe7/"
    none_value = None
    flag_true = True

    # Create initial Maybe instance with the provided None and flag
    initial_maybe = maybe_module.Maybe(none_value, flag_true)

    # Apply a value (None) to the Maybe (keeps same call as original)
    applied_maybe = initial_maybe.ap(none_value)

    # Convert to lazy representation
    lazy_maybe = applied_maybe.to_lazy()

    # Convert lazy to validation type
    validation_maybe = lazy_maybe.to_validation()

    # Filter the original Maybe using the validation_maybe object (preserve call)
    filtered_maybe = initial_maybe.filter(validation_maybe)

    # Get a fallback or the value itself (original used the same object as fallback)
    fallback_maybe = filtered_maybe.get_or_else(filtered_maybe)

    # Convert filtered result to Either (preserve call)
    either_result = filtered_maybe.to_either()

    # Convert validation result to Try (preserve call)
    try_result = validation_maybe.to_try()

    # Check equality between filtered_maybe and applied_maybe (preserve call)
    equality_check = filtered_maybe.__eq__(applied_maybe)

    # Convert the fallback to a Box (preserve call)
    box_result = fallback_maybe.to_box()

    # Apply bytes to the Try result (preserve call)
    try_result.ap(sample_bytes)

def test_maybe_chain_conversion_and_bindings_no_error():
    """Exercise a chain of Maybe conversions and bindings to ensure methods interoperate without raising exceptions."""
    # Input literals (unchanged)
    sample_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    initial_flag = True

    # Create a Maybe with (None, True)
    maybe_none_bool = maybe_module.Maybe(none_value, initial_flag)

    # Apply `ap` with None, then with bytes
    after_ap_none = maybe_none_bool.ap(none_value)
    after_ap_bytes = after_ap_none.ap(sample_bytes)

    # Convert to validation after the ap chain
    validation_after_ap_bytes = after_ap_bytes.to_validation()

    # Another Maybe instance with (None, bytes)
    maybe_none_bytes = maybe_module.Maybe(none_value, sample_bytes)

    # Use get_or_else with the maybe itself as the fallback
    get_or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)

    # Convert maybe to validation
    validation_from_maybe_none_bytes = maybe_none_bytes.to_validation()

    # Bind the validation into maybe
    bind_result_from_maybe = maybe_none_bytes.bind(validation_from_maybe_none_bytes)

    # Convert maybe to either and exercise ap with itself
    either_from_maybe = maybe_none_bytes.to_either()
    ap_self_result = maybe_none_bytes.ap(maybe_none_bytes)

    # Additional integer literal used later (unchanged)
    negative_int = -3289

    # Equality checks (preserve original __eq__ calls)
    either_eq_validation = either_from_maybe.__eq__(validation_from_maybe_none_bytes)

    # Bind on either with maybe
    either_bind_result = either_from_maybe.bind(maybe_none_bytes)

    # Convert maybe to try
    try_from_maybe = maybe_none_bytes.to_try()

    # Check equality between maybe and its bind result
    maybe_eq_bind_result = maybe_none_bytes.__eq__(bind_result_from_maybe)

    # Convert the bind result to validation
    validation_from_bind = bind_result_from_maybe.to_validation()

    # Finally, apply the try with the integer (preserve call order)
    try_from_maybe.ap(negative_int)

def test_maybe_method_chain_invocations_do_not_raise():
    """Ensure a Maybe instance's equality, conversion, and mapping methods can be called in sequence without errors."""
    # Use a simple False flag as in the original test
    flag = False

    # Create a Maybe instance and call __eq__ on it (preserves original call order)
    maybe_instance = maybe_module.Maybe(flag, flag)
    _ = maybe_instance.__eq__(flag)  # result intentionally unused; call preserved for side effects if any

    # Create another Maybe instance and exercise conversion methods in sequence
    another_maybe = maybe_module.Maybe(flag, flag)
    either_value = another_maybe.to_either()
    lazy_value = another_maybe.to_lazy()
    validation_value = lazy_value.to_validation()

    # Create a third Maybe instance and call map with the validation_value
    third_maybe = maybe_module.Maybe(flag, flag)
    third_maybe.map(validation_value)

def test_maybe_equals_self_and_supports_try_to_validation():
    """Verify a Maybe constructed from boolean flags compares equal to itself and can be converted to a Try and then validated."""
    # initial boolean flag values used to construct the Maybe
    initial_flag = False

    # construct the Maybe instance with the two boolean flags
    maybe_instance = maybe_module.Maybe(initial_flag, initial_flag)

    # call __eq__ explicitly to check equality with itself (preserves original call style)
    equals_self = maybe_instance.__eq__(maybe_instance)
    assert equals_self is True

    # convert the Maybe to a Try and then invoke to_validation() on that result
    try_result = maybe_instance.to_try()
    validation_result = try_result.to_validation()
    assert validation_result is not None

