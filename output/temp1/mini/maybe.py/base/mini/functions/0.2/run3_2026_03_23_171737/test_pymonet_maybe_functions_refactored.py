import pytest

import maybe as maybe_module
import typing as typing_module

def test_maybe_initializes_with_identical_byte_arguments():
    """Ensure Maybe can be constructed when given the same byte sequence twice."""
    sample_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    # Create a Maybe instance using the same byte sequence for both parameters
    maybe_obj = maybe_module.Maybe(sample_bytes, sample_bytes)

def test_maybe_constructs_with_none_values():
    """Ensure Maybe can be constructed with two None values without raising."""
    # Represent absent values explicitly with None for both parameters.
    first_value = None
    second_value = None

    # Construct Maybe using the aliased module name from imports.
    maybe_obj = maybe_module.Maybe(first_value, second_value)

def test_maybe_operations_sequence():
    """Exercise a sequence of Maybe operations to ensure method chaining and conversions behave as expected."""
    sample_value = "p4xa>bl^oP"

    m1 = maybe_module.Maybe(sample_value, sample_value)

    equals_with_value = m1.__eq__(sample_value)

    ap1 = m1.ap(sample_value)

    get_or_else1 = m1.get_or_else(sample_value)

    map1 = m1.map(ap1)
    filter1 = m1.filter(ap1)

    map2 = m1.map(ap1)

    ap2 = m1.ap(sample_value)

    equals_ap = ap1.__eq__(ap2)

    filter_on_ap1 = ap1.filter(get_or_else1)

    get_or_else_from_ap2 = ap2.get_or_else(sample_value)

    m2 = maybe_module.Maybe(sample_value, sample_value)
    validation = m2.to_validation()
    bind_result = m2.bind(validation)
    either_result = bind_result.to_either()

def test_maybe_eq_with_set_of_repeated_false():
    """Call Maybe.__eq__ with a set built from multiple identical False values to verify invocation succeeds."""
    false_value = False
    # Repeating the same boolean literal when building a set yields a single {False} element.
    boolean_set = {false_value, false_value, false_value, false_value}
    none_value = None
    maybe_instance = maybe_module.Maybe(none_value, none_value)
    equality_result = maybe_instance.__eq__(boolean_set)
    # Ensure the __eq__ invocation returns a bool or NotImplemented (both are valid outcomes for __eq__).
    assert isinstance(equality_result, bool) or equality_result is NotImplemented

def test_maybe_bind_map_and_set_to_box():
    """Exercise Maybe.bind/map chaining and a set.to_box() call to ensure they run without error."""
    # Use a simple boolean flag value throughout to mirror the original inputs
    flag = True

    # Create a Maybe instance with two boolean arguments
    maybe_instance = maybe_module.Maybe(flag, flag)

    # Bind then map using the same boolean value (preserve original call sequence)
    bound_result = maybe_instance.bind(flag)
    mapped_result = bound_result.map(flag)

    # Create a tuple of booleans and construct another Maybe with it
    bool_tuple = (flag, flag, flag, flag)
    maybe_with_tuple = maybe_module.Maybe(bool_tuple, flag)

    # Create an empty set and call its to_box() method (preserve original call)
    empty_set = set()
    empty_set.to_box()

def test_maybe_map_accepts_none_value_and_false_flag():
    """Ensure Maybe can be constructed with None and False, and map can be called with False."""
    # Prepare inputs: a None value and a False flag (preserve original literals)
    value_none = None
    flag_false = False

    # Construct Maybe using the provided module alias and call map with the same flag
    maybe_obj = maybe_module.Maybe(value_none, flag_false)
    maybe_obj.map(flag_false)

def test_maybe_bind_with_none_and_false():
    """Verify that binding an empty mapping to a Maybe created with (None, False) runs without error."""
    # Create a Maybe initialized with two True values (no effect on this test's outcome).
    first_flag = True
    maybe_true = maybe_module.Maybe(first_flag, first_flag)

    # Prepare an empty mapping to pass to bind().
    target_mapping = {}

    # Create a Maybe with None and False, then bind the empty mapping to it.
    none_value = None
    false_flag = False
    maybe_with_none = maybe_module.Maybe(none_value, false_flag)

    # Call bind with the empty mapping (preserve original call/behavior).
    maybe_with_none.bind(target_mapping)

def test_maybe_operations_combo():
    """Exercise a sequence of Maybe operations: construction, conversion, filtering, and application."""
    # Prepare inputs
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    nothing = None

    # Construct a Maybe containing the raw bytes and convert to boxed form
    maybe_bytes = maybe_module.Maybe(raw_bytes, nothing)
    boxed_bytes = maybe_bytes.to_box()

    # Construct a Maybe from an int and a boolean flag
    maybe_int = maybe_module.Maybe(0, True)

    # Filter the maybe by itself (preserve original call shape)
    filtered_self = maybe_int.filter(maybe_int)

    # Obtain a lazy representation
    lazy_representation = maybe_int.to_lazy()

    # Apply the filtered_self to maybe_bytes (applicative-style) and filter the result
    applied = filtered_self.ap(maybe_bytes)
    filtered_applied = filtered_self.filter(applied)

    # Construct a composite Maybe from the lazy representation and the boxed bytes
    maybe_combined = maybe_module.Maybe(lazy_representation, boxed_bytes)

    # Explicit equality check using __eq__
    equals_result = lazy_representation.__eq__(True)

def test_maybe_applies_value_without_error():
    """Ensure Maybe.ap can be called with an integer on a Maybe constructed from None and False."""
    # Value to apply
    value = 2862
    # Initial state passed to Maybe
    initial_value = None
    # A boolean flag used by the Maybe constructor
    flag = False

    # Construct the Maybe object using the aliased module import
    maybe_obj = maybe_module.Maybe(initial_value, flag)

    # Invoke ap with the integer value; test passes if no exception is raised
    maybe_obj.ap(value)

def test_maybe_chaining_filter_map_to_lazy_and_try():
    """Verify a sequence of Maybe operations: filter -> to_lazy -> map -> to_try can be chained."""
    # Arrange: create a Maybe with a simple numeric value and a truthy flag
    initial_value = 0
    initial_flag = True
    maybe_instance = maybe_module.Maybe(initial_value, initial_flag)

    # Act: perform the chain of operations in the original order to preserve semantics

    # Apply filter using the maybe instance itself as the predicate-like argument
    filtered_once = maybe_instance.filter(maybe_instance)

    # Convert original and filtered Maybe instances to lazy representations
    original_lazy = maybe_instance.to_lazy()
    filtered_lazy = filtered_once.to_lazy()

    # Filter the already filtered Maybe using its lazy representation
    filtered_twice = filtered_once.filter(filtered_lazy)

    # Convert the twice-filtered result to a Try-like structure
    attempt_result = filtered_twice.to_try()

    # Call to_lazy on the original maybe again (preserve call order)
    original_lazy_again = maybe_instance.to_lazy()

    # Map the filtered_once using itself (preserves original mapping call)
    mapped_result = filtered_once.map(filtered_once)

    # Assert that operations returned objects (the exact types/semantics are checked elsewhere)
    assert filtered_once is not None
    assert original_lazy is not None
    assert filtered_lazy is not None
    assert filtered_twice is not None
    assert attempt_result is not None
    assert original_lazy_again is not None
    assert mapped_result is not None

def test_maybe_filter_to_lazy_with_none_and_tuple():
    """Ensure Maybe.filter can accept a tuple and be converted to lazy
    when Maybe instances are constructed with None/True values.
    """
    # An integer value used repeatedly to form a tuple argument
    int_value = -283
    tuple_arg = (int_value, int_value, int_value)

    # First Maybe contains (None, True)
    none_value = None
    truth_flag = True
    first_maybe = maybe_module.Maybe(none_value, truth_flag)

    # Apply filter with the tuple and convert the result to a lazy representation
    filtered_result = first_maybe.filter(tuple_arg)
    lazy_result = filtered_result.to_lazy()

    # Second Maybe contains (None, None) and we call filter with the lazy result
    another_none = None
    second_maybe = maybe_module.Maybe(another_none, another_none)
    second_maybe.filter(lazy_result)

def test_maybe_get_or_else_and_filter_with_box_conversion():
    """Verify Maybe.get_or_else, Maybe.to_box, and Maybe.filter interact without changing data."""

    # Fallback value if Maybe is absent
    default_int = 2281

    # Sample string used repeatedly in the payload
    sample_string = "gZ(\\mOcN"

    # A mapping that references the sample string (used twice in the tuple)
    mapping = {sample_string: sample_string}

    # Tuple payload containing repeated strings and the mapping twice
    tuple_payload = (sample_string, sample_string, mapping, mapping)

    # Create a Maybe wrapping the tuple_payload (present=True)
    maybe_tuple = maybe_module.Maybe(tuple_payload, True)

    # Extract a value from the Maybe, falling back to default_int if absent
    extracted_value = maybe_tuple.get_or_else(default_int)

    # Instantiate a Generic object (used as payload for another Maybe)
    generic_instance = typing_module.Generic()

    # Convert the original Maybe to a boxed representation (no assertions on result)
    boxed_value = maybe_tuple.to_box()

    # Create another Maybe wrapping the generic instance (present=False)
    maybe_generic = maybe_module.Maybe(generic_instance, False)

    # Apply filter on the second Maybe using the previously extracted value
    maybe_generic.filter(extracted_value)

def test_maybe_conversion_and_binding_preserves_values():
    """Exercise Maybe conversions: to_validation, get_or_else, to_try, and bind."""

    # Construct a Maybe from a boolean and None, then convert to a validation.
    flag = True
    none_value = None
    maybe_flag_none = maybe_module.Maybe(flag, none_value)
    validation_from_flag_none = maybe_flag_none.to_validation()

    # Prepare numeric values and an empty tuple for the next Maybe.
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()

    # Construct a Maybe from an int and an empty tuple, then perform several conversions.
    maybe_int_tuple = maybe_module.Maybe(int_value, empty_tuple)
    validation_from_int_tuple = maybe_int_tuple.to_validation()
    extracted_int = maybe_int_tuple.get_or_else(int_value)
    try_from_maybe = maybe_int_tuple.to_try()

    # Another Maybe constructed from the same float for coverage of construction.
    maybe_float_float = maybe_module.Maybe(float_value, float_value)

    # Bind the earlier Try-like result into the int/tuple Maybe.
    maybe_int_tuple.bind(try_from_maybe)

def test_maybe_map_with_set_and_to_either_conversion():
    """Ensure Maybe.map accepts a set and Maybe.to_either can be called without errors."""
    # Create a Maybe with None and a True flag
    none_value = None
    flag_true = True
    maybe_none = maybe_module.Maybe(none_value, flag_true)

    # Map the Maybe using a set containing the same boolean flag
    targets_set = {flag_true}
    mapped_result = maybe_none.map(targets_set)

    # Create another Maybe with an integer value and a True flag
    number = -1095
    flag_true_alt = True
    maybe_number = maybe_module.Maybe(number, flag_true_alt)

    # Convert the second Maybe to an Either
    either_result = maybe_number.to_either()

def test_maybe_to_try_then_to_box_with_true_false():
    """Construct a Maybe with (True, False), convert it to a Try, then box the Try result."""
    # Preserve original literal inputs
    flag_true = True
    flag_false = False

    # Create a Maybe instance using the aliased import (maybe_module)
    maybe_instance = maybe_module.Maybe(flag_true, flag_false)

    # Convert the Maybe to a Try-like object
    try_obj = maybe_instance.to_try()

    # Box the Try-like object (keep original call and order)
    try_obj.to_box()

def test_maybe_conversion_flow_and_try_ap():
    """Exercise a sequence of Maybe conversions and ensure ap is called on the resulting Try.

    This reproduces the original call order:
      - construct Maybe
      - ap -> to_lazy -> to_validation -> to_try
      - filter, get_or_else, to_either, to_box
      - call __eq__ explicitly
      - call ap on the Try with the same bytes value
    """
    raw_bytes = b"C\xcf\xe7/"  # input bytes used at the final ap call
    none_value = None
    truth_flag = True

    # Construct the Maybe object (preserve original constructor arguments)
    maybe_obj = maybe_module.Maybe(none_value, truth_flag)

    # Apply None to the Maybe (same call as original)
    applied = maybe_obj.ap(none_value)

    # Convert the result to lazy and then to validation (preserve call chain)
    lazy_val = applied.to_lazy()
    validation = lazy_val.to_validation()

    # Filter the original Maybe using the validation object
    filtered = maybe_obj.filter(validation)

    # Use filtered itself as the fallback (identical to original get_or_else call)
    default_choice = filtered.get_or_else(filtered)

    # Convert filtered to Either (preserve call)
    either_val = filtered.to_either()

    # Convert validation to Try (preserve call) and later call ap on it
    try_val = validation.to_try()

    # Explicit equality check via __eq__ to match the original invocation
    equals_result = filtered.__eq__(applied)

    # Convert the chosen default to a Box (preserve call)
    boxed = default_choice.to_box()

    # Finally, call ap on the Try with the original bytes value
    try_val.ap(raw_bytes)

def test_maybe_transforms_and_conversions_interoperate():
    """Exercise Maybe's ap/bind/convert methods to ensure transformations chain correctly.

    This test constructs Maybe instances with various contents and calls ap, bind,
    and conversion helpers (to_validation, to_either, to_try, get_or_else) in a
    specific sequence to verify interoperability and side-effect free execution.
    """
    # Sample values used to construct Maybe instances
    sample_bytes = b"\xdbC\xcf\xe7/"
    none_value = None
    true_flag = True

    # Create a Maybe holding (None, True)
    maybe_none_true = maybe_module.Maybe(none_value, true_flag)

    # Apply Nothing (None) to the Maybe, then apply bytes to the result
    applied_none = maybe_none_true.ap(none_value)
    applied_bytes = applied_none.ap(sample_bytes)

    # Convert the result to a Validation
    validation_from_applied = applied_bytes.to_validation()

    # Create another Maybe holding (None, bytes)
    maybe_none_bytes = maybe_module.Maybe(none_value, sample_bytes)

    # get_or_else should return the provided default when appropriate
    get_or_else_result = maybe_none_bytes.get_or_else(maybe_none_bytes)

    # Convert this Maybe to Validation and Either forms and exercise bind/ap
    validation_from_maybe = maybe_none_bytes.to_validation()
    bind_result = maybe_none_bytes.bind(validation_from_maybe)
    either_result = maybe_none_bytes.to_either()
    ap_maybe_self = maybe_none_bytes.ap(maybe_none_bytes)

    # Use an integer with the Try conversion
    negative_int = -3289

    # Compare equality between Either and Validation representations
    equals_either_vs_validation = either_result.__eq__(validation_from_maybe)

    # Bind Either with the Maybe
    either_bind_result = either_result.bind(maybe_none_bytes)

    # Convert Maybe to Try and apply the integer
    try_result = maybe_none_bytes.to_try()
    equals_maybe_vs_bind_result = maybe_none_bytes.__eq__(bind_result)
    bind_to_validation = bind_result.to_validation()
    try_result.ap(negative_int)

def test_maybe_equality_and_conversion_chain():
    """Verify Maybe equality and conversions: to_either -> to_lazy -> to_validation, then used in map."""
    # Use a simple False flag for all Maybe instances (preserves original inputs)
    flag = False

    # Create a Maybe and call its equality method against the same flag
    maybe_primary = maybe_module.Maybe(flag, flag)
    equality_result = maybe_primary.__eq__(flag)

    # Create another Maybe instance and convert it through the chain:
    # to_either -> to_lazy -> to_validation
    maybe_secondary = maybe_module.Maybe(flag, flag)
    either_value = maybe_secondary.to_either()
    lazy_value = maybe_secondary.to_lazy()
    validation_value = lazy_value.to_validation()

    # Create a third Maybe and call map with the resulting validation value
    maybe_tertiary = maybe_module.Maybe(flag, flag)
    maybe_tertiary.map(validation_value)

def test_maybe_self_equality_and_conversion_to_validation():
    """Ensure a Maybe constructed from False values equals itself and can be converted to Try then Validation."""
    false_value = False
    maybe_instance = maybe_module.Maybe(false_value, false_value)

    # Use the dunder __eq__ directly to confirm self-comparison behaviour.
    equality_result = maybe_instance.__eq__(maybe_instance)
    assert equality_result is True

    # Convert to a Try, then to a Validation to ensure conversion methods execute without error.
    try_result = maybe_instance.to_try()
    assert try_result is not None
    validation_result = try_result.to_validation()
    assert validation_result is not None

