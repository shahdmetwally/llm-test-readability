import pytest

import maybe as maybe_module
import typing as typing_module

def test_maybe_constructs_with_identical_byte_values():
    """Ensure Maybe can be constructed when given the same byte sequence twice."""
    # A predetermined byte sequence used for both constructor arguments.
    sample_bytes = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"
    # Construct using the provided alias for the module.
    maybe_instance = maybe_module.Maybe(sample_bytes, sample_bytes)

def test_maybe_initialization_with_none_values():
    """Construct Maybe with both arguments set to None to ensure initialization succeeds."""
    # Represent absent values explicitly
    none_value = None
    # Create the Maybe instance using the aliased module name from updated imports
    maybe_instance = maybe_module.Maybe(none_value, none_value)
    # Ensure the object was created and has expected type
    assert isinstance(maybe_instance, maybe_module.Maybe)

def test_maybe_chaining_and_conversions():
    """Exercise a sequence of Maybe operations and conversions to ensure behavior remains stable."""
    # Input value used throughout the test (kept identical to original)
    input_str = "p4xa>bl^oP"

    # Create a Maybe instance with the same value for both parameters
    maybe_first = maybe_module.Maybe(input_str, input_str)

    # Equality check against the raw input string
    is_equal_to_input = maybe_first.__eq__(input_str)

    # Apply the value (ap) and reuse that result in subsequent calls
    applied_once = maybe_first.ap(input_str)

    # Retrieve a fallback value using get_or_else
    default_after_get = maybe_first.get_or_else(input_str)

    # Map and filter operations that use the previously obtained applied_once value
    mapped_from_applied = maybe_first.map(applied_once)
    filtered_from_applied = maybe_first.filter(applied_once)

    # Repeat map and ap calls exactly as in the original to preserve behavior/order
    mapped_again = maybe_first.map(applied_once)
    applied_twice = maybe_first.ap(input_str)

    # Compare the two applied results for equality
    equality_between_applied = applied_once.__eq__(applied_twice)

    # Further operations combining previous results
    filtered_on_var0 = applied_once.filter(default_after_get)
    default_from_applied_twice = applied_twice.get_or_else(input_str)

    # Create a second Maybe and exercise conversion/binding to Validation and Either
    maybe_second = maybe_module.Maybe(input_str, input_str)
    validation_of_second = maybe_second.to_validation()
    bound_with_validation = maybe_second.bind(validation_of_second)
    either_result = bound_with_validation.to_either()

def test_maybe_eq_called_with_set_of_false():
    """Call Maybe.__eq__ with a set constructed from repeated False values."""
    flag_false = False
    # Build a set from repeated False entries (duplicates will be deduplicated -> {False})
    flags_set = {flag_false, flag_false, flag_false, flag_false}
    none_val = None
    maybe_instance = maybe_module.Maybe(none_val, none_val)
    are_equal = maybe_instance.__eq__(flags_set)

def test_maybe_bind_map_then_call_to_box_on_empty_set():
    """
    Verify Maybe objects can be constructed, bound, and mapped, and that
    calling to_box on an empty set executes without error. Preserve the
    original call sequence and literal values.
    """
    # Use a simple boolean flag value (kept literal to preserve original test)
    flag = True

    # Construct a Maybe using the same boolean for both parameters
    maybe_obj = maybe_module.Maybe(flag, flag)

    # Bind and then map using the same boolean value to preserve call/argument patterns
    bound_result = maybe_obj.bind(flag)
    mapped_result = bound_result.map(flag)

    # A 4-tuple of the same boolean value to preserve literal values and order
    quad_tuple = (flag, flag, flag, flag)

    # Construct another Maybe with the tuple and the boolean flag
    maybe_with_tuple = maybe_module.Maybe(quad_tuple, flag)

    # Create an empty set and call its to_box method (preserve the call)
    empty_set = set()
    empty_set.to_box()

def test_maybe_map_with_none_and_false():
    """Verify that Maybe.map can be invoked when Maybe was constructed with None and False.

    This test preserves original call patterns: the Maybe is created with a None
    value and a False flag, and map is then called with the same False value.
    """
    none_value = None  # the wrapped value passed to Maybe
    false_flag = False  # the flag/value passed as the second constructor arg and to map()
    maybe_instance = maybe_module.Maybe(none_value, false_flag)  # construct the Maybe
    maybe_instance.map(false_flag)  # call map with the same False argument

def test_bind_when_value_is_none_and_flag_false_binds_empty_mapping():
    """Ensure a Maybe created with (None, False) can call bind() when provided an empty mapping."""
    # Create a present Maybe (True, True) — kept for parity with the original call order.
    maybe_present = maybe_module.Maybe(True, True)

    # Prepare an empty mapping to bind with.
    empty_mapping = {}

    # Create a Maybe representing an absent value (None) and a False flag.
    maybe_absent = maybe_module.Maybe(None, False)

    # Call bind on the absent Maybe with the empty mapping; should not raise.
    maybe_absent.bind(empty_mapping)

def test_maybe_chaining_and_applicative_behavior():
    """Exercise Maybe: to_box, filter (with self), to_lazy, ap, and equality check."""
    raw_bytes = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_val = None

    # Create a Maybe containing bytes and None
    maybe_bytes_none = maybe_module.Maybe(raw_bytes, none_val)
    boxed = maybe_bytes_none.to_box()

    zero = 0
    true_val = True

    # Create a Maybe containing an int and a bool
    maybe_zero_true = maybe_module.Maybe(zero, true_val)

    # Filter using the Maybe itself as the predicate/value
    filtered_self = maybe_zero_true.filter(maybe_zero_true)

    # Convert the Maybe to a lazy representation
    lazy_rep = maybe_zero_true.to_lazy()

    # Apply the filtered result to the bytes Maybe
    applied_result = filtered_self.ap(maybe_bytes_none)

    # Filter the filtered result with the outcome of the application
    filtered_with_applied = filtered_self.filter(applied_result)

    # Create a Maybe from the lazy rep and the previously boxed value
    maybe_lazy_boxed = maybe_module.Maybe(lazy_rep, boxed)

    # Check equality by calling __eq__ directly
    equality_check = lazy_rep.__eq__(true_val)

def test_maybe_ap_with_none_initial_and_false_flag():
    """Call Maybe.ap when the Maybe was created with None and a False flag."""
    value = 2862
    initial_value = None
    flag = False

    maybe_instance = maybe_module.Maybe(initial_value, flag)
    # Invoke ap with the integer value; the test passes if no exception is raised.
    maybe_instance.ap(value)

def test_maybe_filter_to_lazy_chain():
    """
    Ensure a Maybe constructed with (None, True) can be filtered by a tuple,
    converted to a lazy form, and then used as input to another Maybe.filter call.
    """
    # base integer value and a 3-tuple built from it (preserve exact literal -283)
    base_int = -283
    triple_tuple = (base_int, base_int, base_int)

    # first Maybe instance created with (None, True)
    first_maybe = maybe_module.Maybe(None, True)

    # apply filter with the tuple and convert the result to a lazy representation
    filtered_result = first_maybe.filter(triple_tuple)
    lazy_result = filtered_result.to_lazy()

    # second Maybe instance created with (None, None)
    second_maybe = maybe_module.Maybe(None, None)

    # pass the lazy result into the second Maybe's filter (preserve call and order)
    second_maybe.filter(lazy_result)

def test_maybe_filter_with_get_or_else_and_to_box():
    """Exercise Maybe.get_or_else, Maybe.to_box, and Maybe.filter with present/absent flags."""
    # Arrange: prepare inputs — keep literals identical to the original test
    default_value = 2281
    sample_text = "gZ(\\mOcN"
    sample_mapping = {sample_text: sample_text}
    sample_tuple = (sample_text, sample_text, sample_mapping, sample_mapping)

    # Create a Maybe that is present
    is_present = True
    maybe_with_tuple = maybe_module.Maybe(sample_tuple, is_present)

    # Act: get_or_else should return the contained value (or default if absent)
    result_or_default = maybe_with_tuple.get_or_else(default_value)

    # Create a Generic instance and a Maybe that is absent
    generic_instance = typing_module.Generic()
    is_absent = False

    # Call to_box on the first Maybe (preserve call / assignment even if unused)
    boxed_value = maybe_with_tuple.to_box()

    # Create a Maybe wrapping the Generic (absent) and apply filter with the obtained result
    maybe_generic = maybe_module.Maybe(generic_instance, is_absent)
    maybe_generic.filter(result_or_default)

def test_maybe_bind_and_conversion_operations():
    """Smoke test: exercise Maybe conversions and bind to ensure methods run without error."""
    # Create a Maybe wrapping a boolean and None
    bool_value = True
    none_value = None
    maybe_bool = maybe_module.Maybe(bool_value, none_value)

    # Convert the boolean-wrapped Maybe to a Validation representation
    validation_from_bool = maybe_bool.to_validation()

    # Prepare values for additional Maybe instances
    float_value = -286.64
    int_value = -1784
    empty_tuple = ()

    # Create a Maybe wrapping an int and an empty tuple
    maybe_int_tuple = maybe_module.Maybe(int_value, empty_tuple)

    # Convert to Validation, obtain a default with get_or_else, and convert to a Try
    validation_from_int_tuple = maybe_int_tuple.to_validation()
    default_int = maybe_int_tuple.get_or_else(int_value)
    try_from_maybe = maybe_int_tuple.to_try()

    # Create another Maybe instance with float values
    maybe_float = maybe_module.Maybe(float_value, float_value)

    # Bind the Try result back to the maybe_int_tuple (ensures bind accepts the Try)
    maybe_int_tuple.bind(try_from_maybe)

def test_maybe_map_and_to_either_preserves_value_and_converts_to_either():
    """Call Maybe.map and Maybe.to_either to ensure they execute without error."""

    # Create a Maybe holding None with a True presence flag
    none_value = None
    presence_flag_for_none = True
    maybe_none = maybe_module.Maybe(none_value, presence_flag_for_none)

    # Call map on the Maybe using a set containing the flag value
    mapping_arg = {presence_flag_for_none}
    mapped_result = maybe_none.map(mapping_arg)

    # Create a Maybe holding an integer and convert it to an Either
    int_value = -1095
    presence_flag_for_int = True
    maybe_int = maybe_module.Maybe(int_value, presence_flag_for_int)
    either_result = maybe_int.to_either()

def test_maybe_conversion_chain_preserves_behaviour():
    """Exercise a sequence of Maybe conversions to ensure calls succeed in order.

    This mirrors the original generated test: create Maybe instances with None
    and a single-element tuple, then call to_lazy, to_either, to_try and finally
    to_lazy on the Try result. The test intentionally has no assertions and
    exists to reproduce/validate behavior (e.g. no exceptions) from these calls.
    """
    # Base None value used to construct the first Maybe
    none_value = None
    maybe_none = maybe_module.Maybe(none_value, none_value)

    # Wrap the first Maybe in a single-element tuple for the second Maybe
    maybe_tuple = (maybe_none,)

    # Convert the first Maybe to its lazy representation
    lazy_from_none = maybe_none.to_lazy()

    # A simple boolean flag used as the second Maybe's second argument
    false_flag = False
    maybe_from_tuple = maybe_module.Maybe(maybe_tuple, false_flag)

    # Perform the sequence of conversions exactly as in the original test
    either_from_none_first = maybe_none.to_either()
    try_from_tuple = maybe_from_tuple.to_try()
    either_from_none_second = maybe_none.to_either()
    either_from_tuple = maybe_from_tuple.to_either()

    # Call to_lazy on the Try result (side-effect / final step)
    try_from_tuple.to_lazy()

def test_maybe_to_try_then_to_box_no_error():
    """Ensure a Maybe constructed with (True, False) can be converted to Try and then boxed."""
    # Setup: a Maybe indicating presence with the value False
    is_present = True
    value = False

    maybe_obj = maybe_module.Maybe(is_present, value)

    # Action: convert Maybe to a Try-like object
    try_obj = maybe_obj.to_try()

    # Finalize: invoke to_box() on the Try object (no assertion; ensure calls succeed)
    try_obj.to_box()

def test_maybe_chaining_and_conversions_preserve_behavior():
    """Exercise various Maybe conversions and chained operations to ensure
    methods like ap, to_lazy, to_validation, get_or_else, to_either, to_try,
    __eq__, and to_box are invoked in sequence without changing behavior."""
    # Sample binary input used at the end of the chain
    sample_bytes = b"C\xcf\xe7/"

    # Explicit None value and a simple truth flag used to construct the Maybe
    none_value = None
    flag_true = True

    # Create initial Maybe instance with (None, True)
    initial_maybe = maybe_module.Maybe(none_value, flag_true)

    # Apply the Maybe with None (preserves calling pattern)
    applied = initial_maybe.ap(none_value)

    # Convert the result to a lazy representation
    lazy_val = applied.to_lazy()

    # Convert the lazy value to a validation type
    validation = lazy_val.to_validation()

    # Filter the validation using itself (preserves original call)
    filtered = initial_maybe.filter(validation)

    # Use get_or_else with the fallback being the filtered object itself
    defaulted = filtered.get_or_else(filtered)

    # Convert the filtered validation to an either type
    either_val = filtered.to_either()

    # Convert the lazy value to a try type
    try_val = lazy_val.to_try()

    # Check equality between filtered and the original Maybe (retains the __eq__ call)
    equals_check = filtered.__eq__(initial_maybe)

    # Convert the defaulted result to a box
    boxed = defaulted.to_box()

    # Finally, apply the try value to the sample bytes (preserves final call)
    try_val.ap(sample_bytes)

def test_maybe_chaining_and_conversions_variants():
    """Exercise Maybe chaining, conversions (to_validation/to_either/to_try) and ap/bind usage."""
    # Sample inputs used throughout the chain (kept identical to original test)
    sample_bytes = b"\xdbC\xcf\xe7/"
    none_val = None
    bool_true = True

    # Construct a Maybe with (None, True) and apply values step by step.
    maybe_a = maybe_module.Maybe(none_val, bool_true)
    applied_none = maybe_a.ap(none_val)            # var_0 = maybe_0.ap(none_type_0)
    applied_bytes = applied_none.ap(sample_bytes)  # var_1 = var_0.ap(bytes_0)

    # Convert to validation after applications
    validation_from_applied = applied_bytes.to_validation()  # var_2 = var_1.to_validation()

    # Another Maybe constructed with (None, bytes) and various conversions
    maybe_b = maybe_module.Maybe(none_val, sample_bytes)     # maybe_1
    fallback_get = maybe_b.get_or_else(maybe_b)              # var_3 = maybe_1.get_or_else(maybe_1)
    validation_b = maybe_b.to_validation()                   # var_4 = maybe_1.to_validation()
    bound_from_validation = maybe_b.bind(validation_b)       # var_5 = maybe_1.bind(var_4)
    either_b = maybe_b.to_either()                           # var_6 = maybe_1.to_either()
    applied_self = maybe_b.ap(maybe_b)                       # var_7 = maybe_1.ap(maybe_1)

    # Additional operations mirroring original test sequence
    int_val = -3289
    eq_check = either_b.__eq__(validation_b)                 # bool_1 = var_6.__eq__(var_4)
    bound_either = either_b.bind(maybe_b)                    # var_8 = var_6.bind(maybe_1)
    try_b = maybe_b.to_try()                                 # var_9 = maybe_1.to_try()
    eq_check2 = maybe_b.__eq__(bound_from_validation)        # bool_2 = maybe_1.__eq__(var_5)
    validation_from_bound = bound_from_validation.to_validation()  # var_10 = var_5.to_validation()

    # Final application to the Try returned earlier (matches original last call)
    try_b.ap(int_val)                                        # var_9.ap(int_0)

def test_maybe_equality_and_conversion_map_chain():
    """Exercise Maybe: equality, conversions (Either, Lazy, Validation), and mapping with Validation result."""
    # Use a simple False flag for all Maybe constructions (matches the original test values)
    flag = False

    # Create a Maybe and invoke its equality special method against the raw flag
    maybe_a = maybe_module.Maybe(flag, flag)
    equality_result = maybe_a.__eq__(flag)

    # Create another Maybe and convert it through Either -> Lazy -> Validation
    maybe_b = maybe_module.Maybe(flag, flag)
    either_result = maybe_b.to_either()
    lazy_result = maybe_b.to_lazy()
    validation_result = lazy_result.to_validation()

    # Create a third Maybe and map it with the Validation obtained above
    maybe_c = maybe_module.Maybe(flag, flag)
    mapped_result = maybe_c.map(validation_result)

def test_maybe_equality_and_conversion_to_try_and_validation():
    """Ensure a Maybe compares equal to itself and can be converted to Try then Validation."""
    # Start with a simple False flag used for both Maybe parameters
    initial_flag = False
    maybe_instance = maybe_module.Maybe(initial_flag, initial_flag)

    # Call the equality dunder method explicitly (comparing the instance to itself)
    equality_result = maybe_instance.__eq__(maybe_instance)
    assert equality_result is True

    # Convert the Maybe to a Try-like object, then to a Validation-like object.
    try_obj = maybe_instance.to_try()
    try_obj.to_validation()

