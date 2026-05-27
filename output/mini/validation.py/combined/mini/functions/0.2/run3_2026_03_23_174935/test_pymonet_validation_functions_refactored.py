import pytest

import builtins as builtins_module
import validation as validation_module

def test_validation_is_success_equals_and_is_fail_to_maybe_sequence():
    """Construct a Validation and exercise is_success, __eq__, is_fail and to_maybe in sequence."""
    # The exact descriptive string used for both constructor arguments (unchanged)
    description_text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Create a Validation instance using the provided module alias
    validation_obj = validation_module.Validation(description_text, description_text)

    # Call and store is_success result (preserve call)
    is_success_result = validation_obj.is_success()

    # Call and store equality check against itself (preserve call)
    equality_result = validation_obj.__eq__(validation_obj)

    # Call and store is_fail result (preserve call), then call to_maybe() on that result
    is_fail_result = validation_obj.is_fail()
    is_fail_result.to_maybe()

def test_validation_eq_with_none_is_successful():
    """Ensure that comparing a Validation instance to None produces a successful result."""
    # Prepare input values (preserve original literals)
    none_value = None
    primary_value = -6891
    secondary_value = 3125

    # Pack the secondary value into the same tuple structure as the original test
    secondary_tuple = (secondary_value,)

    # Instantiate Validation using the provided validation module alias
    validation_instance = validation_module.Validation(primary_value, secondary_tuple)

    # Call the explicit equality method with None (preserve original method call)
    result = validation_instance.__eq__(none_value)

    # Preserve the original verification step: call is_success() on the result
    result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Ensure that Validation.__str__ returns an object supporting is_fail()."""
    # Use an empty mapping for both parameters (preserves original inputs)
    input_data = {}
    # Instantiate Validation with the same mapping for both constructor args
    validation_instance = validation_module.Validation(input_data, input_data)
    # Call __str__ explicitly (preserve original call) and capture its result
    result = validation_instance.__str__()
    # Invoke is_fail() on the result to exercise that API (no assertion; preserve original behavior)
    result.is_fail()

def test_validation_to_either_and_repeated_to_maybe():
    """Ensure Validation produces an either and a maybe, and that calling to_maybe twice is supported."""
    # Create an empty set to pass into Validation (same object passed twice, as in original)
    empty_set = set()

    # Construct the Validation instance with the two empty sets
    validator = validation_module.Validation(empty_set, empty_set)

    # Produce an "either" representation (original call preserved)
    either_result = validator.to_either()

    # Produce a "maybe" representation (original call preserved)
    maybe_result = validator.to_maybe()

    # Call to_maybe again on the maybe result to ensure repeated calls are allowed (original call preserved)
    maybe_result.to_maybe()

def test_validation_conversion_and_self_equality():
    """
    Ensure a Validation built from a docstring converts to either, equals itself,
    and that its is_fail result can be converted to a maybe.
    """
    # Original docstring literal preserved exactly
    docstring_text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct Validation instance using provided validation module alias
    validation_instance = validation_module.Validation(docstring_text, docstring_text)

    # Convert to Either (call preserved)
    either_result = validation_instance.to_either()

    # Explicitly call equality with itself (original used __eq__ directly)
    equals_self = validation_instance.__eq__(validation_instance)

    # Call is_fail() and then convert that result to maybe (calls preserved)
    is_fail_result = validation_instance.is_fail()
    is_fail_result.to_maybe()

def test_validation_to_maybe_returns_object_with_to_maybe_method():
    """Create a Validation with two identical empty sets, call to_maybe()
    and verify the returned object exposes a callable to_maybe() method."""
    empty_set = set()
    validation_instance = validation_module.Validation(empty_set, empty_set)
    maybe_result = validation_instance.to_maybe()
    # The returned object should have a callable to_maybe attribute and it should be invocable
    assert hasattr(maybe_result, "to_maybe") and callable(maybe_result.to_maybe)
    maybe_result.to_maybe()

def test_validation_initializes_with_none_parameters():
    """Ensure Validation can be instantiated when given None for both constructor arguments."""
    # Use explicit None values for both parameters to match the original test
    none_value = None

    # Instantiate Validation with two None arguments (preserves original behavior)
    validation_instance = validation_module.Validation(none_value, none_value)

def test_validation_to_maybe_accepts_none_inputs():
    """Ensure Validation.to_maybe() can be called when Validation is initialized with None values."""
    # Use explicit None variables for clarity
    none_value = None

    # Initialize Validation with None parameters
    validation_instance = validation_module.Validation(none_value, none_value)

    # Call to_maybe() and verify it does not raise
    validation_instance.to_maybe()

def test_validation_is_fail_with_identical_inputs():
    """Call Validation.is_fail() for a Validation initialized with identical inputs."""
    # Create a simple object instance to use as both constructor arguments.
    obj = builtins_module.object()

    # Initialize Validation with the same object for both parameters.
    validation_instance = validation_module.Validation(obj, obj)

    # Invoke the is_fail method (preserve original behavior).
    validation_instance.is_fail()

def test_validation_map_handles_none_input_with_complex_initial_structure():
    """Ensure Validation.map can be invoked with None when initialized with complex nested structures."""
    # Input value passed to .map()
    none_input = None

    # Primitive values used to build the nested structures (preserve original literals)
    negative_int = -895
    true_flag = True

    # A tuple used as a key and value in the mapping
    key_tuple = (negative_int, true_flag)

    # A dict that maps the tuple to itself (preserve original structure)
    mapping = {key_tuple: key_tuple}

    # A tuple that contains the dict twice and the original integer (preserve original ordering)
    init_sequence = (mapping, mapping, negative_int)

    # Instantiate the Validation class with the complex initial data and the boolean flag
    validator = validation_module.Validation(init_sequence, true_flag)

    # Call map with None to ensure it accepts this input (no assertion; test passes if no exception is raised)
    validator.map(none_input)

def test_validation_bind_accepts_none():
    """Ensure Validation.bind can be called with None without raising an exception."""
    # Sample input bytes (unchanged literal from the original test)
    sample_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"

    # Instantiate the Validation object with two identical byte inputs
    validator = validation_module.Validation(sample_bytes, sample_bytes)

    # Bind None to the validator; the test passes if this does not raise
    none_value = None
    validator.bind(none_value)

def test_validation_ap_accepts_list_of_booleans():
    """Validation.ap should accept a list of booleans without raising errors."""
    # initial flag passed to the Validation constructor
    initial_flag = False

    # build a list of True values
    true_value = True
    boolean_list = [true_value, true_value, true_value, true_value]

    # construct the Validation instance and invoke .ap with the list
    validator = validation_module.Validation(initial_flag, boolean_list)
    validator.ap(boolean_list)

def test_validation_to_box_calls_is_success():
    """Construct a Validation, convert it to a box, and call is_success()."""
    # Use a simple True flag for both constructor parameters (same as original).
    initial_flag = True

    # Create the Validation object using the provided validation_module alias.
    validation_obj = validation_module.Validation(initial_flag, initial_flag)

    # Convert to a boxed result and call is_success() to exercise that path.
    boxed_result = validation_obj.to_box()
    boxed_result.is_success()

def test_validation_to_lazy_and_bind_with_none():
    """Ensure Validation.to_lazy() and bind(None) can be called in sequence without error."""
    # Prepare inputs: an explicit None and an empty list for both Validation parameters.
    none_value = None
    empty_list = []

    # Create a Validation instance with two empty lists.
    validator = validation_module.Validation(empty_list, empty_list)

    # Convert to a lazy representation and then bind None to it.
    lazy_validator = validator.to_lazy()
    bound_lazy = lazy_validator.bind(none_value)

    # Final call mirrors the original sequence; no assertion needed — test passes if no exception is raised.
    bound_lazy.to_lazy()

def test_validation_lazy_to_try_and_ap_invocations():
    """Exercise Validation -> to_lazy -> to_try -> ap -> is_success call sequence."""
    # Use an empty dict as input (preserve original literal)
    empty_dict = {}

    # Instantiate Validation with the same dict for both arguments
    validation = validation_module.Validation(empty_dict, empty_dict)

    # Convert to lazy representation
    lazy_validation = validation.to_lazy()

    # Convert lazy representation to a "try" representation
    try_result = lazy_validation.to_try()

    # Apply the original Validation to the lazy representation
    applied_result = lazy_validation.ap(validation)

    # Call is_success on the try result (no assertion in original test)
    try_result.is_success()

def test_validation_to_try_exposes_is_success_method():
    """Ensure Validation.to_try() returns an object that exposes is_success()."""
    value = 0
    values_list = [value]

    # Create a Validation instance with the integer and the list
    validation_instance = validation_module.Validation(value, values_list)

    # Call to_try() and obtain the result object
    result = validation_instance.to_try()

    # Ensure the result exposes is_success and that it is callable; invoking it should not raise
    assert hasattr(result, "is_success")
    assert callable(getattr(result, "is_success"))
    result.is_success()

def test_validation_chained_transformations_and_mappings():
    """Ensure various Validation transformations (box/either/try/lazy/str/is_fail/eq/map)
    can be invoked and composed without error."""
    # Sample byte payload used throughout the test (unchanged literal).
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Dictionary mixing None and bytes as keys/values.
    sample_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Validation where the key is None and the value is the dict.
    validation_with_none_key = validation_module.Validation(none_value, sample_dict)

    # Self-equality check.
    eq_result = validation_with_none_key.__eq__(validation_with_none_key)

    # Convert to boxed representation.
    boxed_result = validation_with_none_key.to_box()

    # Validation with bytes used for both key and value.
    validation_bytes = validation_module.Validation(sample_bytes, sample_bytes)

    # Convert boxed result to Either-like representation.
    either_result = boxed_result.to_either()

    # Check failure flag on validation_bytes.
    is_fail_flag = validation_bytes.is_fail()

    # Convert either_result to a Try-like representation.
    try_result = either_result.to_try()

    # Create a Validation from the failure flag and bytes.
    validation_from_flag = validation_module.Validation(is_fail_flag, sample_bytes)

    # String representation of the validation created from the flag.
    str_representation = validation_from_flag.__str__()

    # Convert validation_bytes to a lazy representation.
    lazy_from_validation_bytes = validation_bytes.to_lazy()

    # Another Validation with bytes (used to compose nested validation).
    validation_bytes_second = validation_module.Validation(sample_bytes, sample_bytes)

    # Repeat conversion of boxed_result to either (mirrors original sequence).
    either_result_again = boxed_result.to_either()

    # Convert the validation_from_flag to a lazy representation.
    lazy_from_validation_from_flag = validation_from_flag.to_lazy()

    # Compose a nested Validation using the lazy result and another Validation.
    nested_validation = validation_module.Validation(lazy_from_validation_from_flag, validation_bytes_second)

    # Re-check failure flag on validation_bytes (preserve duplicated call).
    is_fail_flag_again = validation_bytes.is_fail()

    # Finally, map the earlier equality result with the string representation.
    eq_result.map(str_representation)

def test_validation_self_equality_to_maybe_and_bind_execute_without_error():
    """Verify Validation instances handle None/bytes inputs: self-equality, to_maybe, and bind run without error."""

    # A sample bytes literal used as key/value (identical to original test)
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    # Explicit None value used as a key in the mapping
    none_value = None

    # Mapping with None as a key and the bytes value mapping to itself
    sample_mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create a Validation instance where the first argument is None and the second is the mapping
    validation_with_none_key = validation_module.Validation(none_value, sample_mapping)

    # Call __eq__ comparing the instance to itself (preserve explicit __eq__ call)
    equals_self_result = validation_with_none_key.__eq__(validation_with_none_key)

    # Call to_maybe on the instance (preserve original method call)
    maybe_result = validation_with_none_key.to_maybe()

    # Create another Validation instance with bytes as both parameters
    validation_with_bytes_key = validation_module.Validation(sample_bytes, sample_bytes)

    # Call bind on the second Validation instance with the bytes value (preserve original call)
    validation_with_bytes_key.bind(sample_bytes)

def test_validation_equality_result_supports_to_box():
    """Verify that Validation.__eq__ returns a result object that exposes to_box()."""
    # Sample bytes used as both a key and a value in the mapping
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    # Explicit None value used as a distinct mapping key
    none_value = None

    # Create a mapping with None and the bytes literal as keys (preserve original structure)
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Construct two Validation instances with the same kinds of inputs as the original test
    left_validation = validation_module.Validation(none_value, mapping)
    right_validation = validation_module.Validation(sample_bytes, none_value)

    # Invoke the __eq__ method explicitly (preserve original call form) and call to_box() on the result
    equality_result = left_validation.__eq__(right_validation)
    equality_result.to_box()

