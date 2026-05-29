import pytest

import builtins as builtins_module
import validation as validation_module

def test_validation_self_equality_and_maybe_conversion():
    """Create a Validation with identical input strings and exercise is_success, self-equality, is_fail, and to_maybe calls."""
    # The original multi-line literal is preserved exactly.
    docstring_text = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct the Validation object using the provided alias for the module.
    validation_obj = validation_module.Validation(docstring_text, docstring_text)

    # Call is_success() and keep the result (no assertion in original test).
    is_success_result = validation_obj.is_success()

    # Explicitly call __eq__ to check self-equality (result retained as in original).
    equals_self_result = validation_obj.__eq__(validation_obj)

    # Call is_fail(), then invoke to_maybe() on that result, preserving call order.
    is_fail_result = validation_obj.is_fail()
    is_fail_result.to_maybe()

def test_validation_eq_with_none_exposes_is_success():
    """Ensure that comparing a Validation instance to None via __eq__ returns an object with an is_success() method."""
    # Prepare the exact literal inputs used by the original test
    none_value = None
    primary_value = -6891
    tuple_element = 3125

    # Construct the tuple exactly as before
    elements_tuple = (tuple_element,)

    # Instantiate the Validation object using the provided alias for the validation module
    validation_instance = validation_module.Validation(primary_value, elements_tuple)

    # Call __eq__ with None (preserve explicit magic-method call) and then invoke is_success()
    comparison_result = validation_instance.__eq__(none_value)
    comparison_result.is_success()

def test_validation_str_allows_is_fail_call():
    """Call Validation.__str__() and then invoke is_fail() on its result."""
    # Use an empty mapping for both constructor arguments (preserve original literals)
    empty_mapping = {}
    # Construct the Validation object using the provided module alias
    validation_obj = validation_module.Validation(empty_mapping, empty_mapping)
    # Explicitly call the dunder __str__ method (preserve original call form)
    result = validation_obj.__str__()
    # Invoke is_fail() on the returned object (preserve original behavior)
    result.is_fail()

def test_validation_to_either_and_maybe_callable_sequence():
    """Construct a Validation with empty inputs and exercise to_either and to_maybe conversions."""
    # Create the empty input used for the Validation instance (matches original test)
    empty_set = set()

    # Instantiate Validation with the same empty set for both parameters
    validator = validation_module.Validation(empty_set, empty_set)

    # Call to_either and store the result (preserve original call)
    either_result = validator.to_either()

    # Call to_maybe and store the result (preserve original call)
    maybe_result = validator.to_maybe()

    # Call to_maybe again on the returned object (preserve original call/order)
    maybe_result.to_maybe()

def test_validation_to_either_eq_self_and_is_fail_to_maybe():
    """Verify Validation can be converted to an Either, compared to itself,
    and that its is_fail result can be converted to a Maybe."""
    # The original multi-line docstring literal is kept exactly as-is.
    validation_doc = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "

    # Construct Validation with the same docstring for both parameters.
    validation_instance = validation_module.Validation(validation_doc, validation_doc)

    # Convert the Validation to an Either (call preserved).
    either_result = validation_instance.to_either()

    # Explicitly call equality with itself (calls __eq__ as in the original).
    equals_self_result = validation_instance.__eq__(validation_instance)

    # Call is_fail() and then convert that result to a Maybe (preserve call chain).
    is_fail_result = validation_instance.is_fail()
    is_fail_result.to_maybe()

def test_validation_to_maybe_chainable():
    """Ensure Validation.to_maybe() returns an object that supports subsequent to_maybe() calls."""
    # Create an empty set used for both constructor arguments
    empty_values = set()

    # Instantiate Validation with the same empty set for both parameters
    validator = validation_module.Validation(empty_values, empty_values)

    # Call to_maybe() and capture the returned object
    maybe_obj = validator.to_maybe()

    # Call to_maybe() again on the returned object to verify it can be invoked a second time
    maybe_obj.to_maybe()

def test_validation_allows_none_arguments():
    """Ensure Validation can be constructed when both parameters are None (no exception raised)."""
    none_arg = None
    validation_instance = validation_module.Validation(none_arg, none_arg)
    assert isinstance(validation_instance, validation_module.Validation)

def test_validation_to_maybe_accepts_none_inputs():
    """Ensure that Validation.to_maybe() can be called on a Validation constructed with None values."""
    # Prepare None inputs (same as the original test)
    none_value = None

    # Create a Validation instance with None inputs and call to_maybe()
    validation_instance = validation_module.Validation(none_value, none_value)

    # Calling to_maybe() on a Validation created with None inputs should not raise.
    validation_instance.to_maybe()

def test_validation_is_fail_reports_failure_for_same_object_arguments():
    """Ensure Validation.is_fail() is exercised when constructed with the same object twice."""
    # Create a plain object instance to pass to Validation
    sample_object = builtins_module.object()

    # Instantiate Validation with the same object for both parameters
    validation_instance = validation_module.Validation(sample_object, sample_object)

    # Invoke the method under test; maintain original call order and semantics
    validation_instance.is_fail()

def test_validation_map_accepts_none_and_preserves_state():
    """Ensure Validation.map can be called with None for a Validation created from a complex initial state."""
    # Input value to pass to map()
    none_value = None

    # Preserve original literal values
    negative_value = -895
    flag = True

    # Build a key/value pair matching the original structure
    key_pair = (negative_value, flag)

    # Create a mapping where the tuple maps to itself
    mapping = {key_pair: key_pair}

    # Construct the initial state tuple (mapping, mapping, negative_value)
    initial_state = (mapping, mapping, negative_value)

    # Instantiate Validation with the complex initial state and the boolean flag
    validator = validation_module.Validation(initial_state, flag)

    # Call map with None — the test passes if no exception is raised
    validator.map(none_value)

def test_validation_bind_accepts_none():
    """Construct a Validation with a fixed bytes payload and call bind(None)."""
    # fixed bytes payload used for both Validation constructor arguments
    payload_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    # create the Validation instance using the provided validation_module alias
    validator = validation_module.Validation(payload_bytes, payload_bytes)
    # explicit None value passed to bind (preserve original literal and call)
    none_value = None
    # call bind with None — test passes if no exception is raised
    validator.bind(none_value)

def test_validation_applies_list_items_without_error():
    """Ensure Validation.ap accepts a list of booleans and completes without error."""
    # Arrange: initial flag and a list of four identical boolean values
    initial_flag = False
    element_value = True
    values = [element_value, element_value, element_value, element_value]

    # Create Validation instance with the same inputs as the original test
    validator = validation_module.Validation(initial_flag, values)

    # Act: call .ap with the list (the test passes if no exception is raised)
    validator.ap(values)

def test_validation_to_box_is_success_callable():
    """Ensure Validation(...).to_box().is_success() can be called when initialized with True values."""
    # Prepare boolean inputs (same as original)
    flag = True

    # Create a Validation instance using the provided validation module alias
    validation = validation_module.Validation(flag, flag)

    # Convert the validation to a box and invoke is_success() to ensure the call succeeds
    box = validation.to_box()
    box.is_success()

def test_validation_to_lazy_and_bind_accepts_none():
    """Ensure Validation.to_lazy(), bind(None), and to_lazy() on the bound result succeed."""
    # Use a None value to bind to the lazy object (preserve original None literal).
    none_value = None

    # Use empty lists as in the original test input.
    empty_items = []
    # Instantiate the Validation object with the same arguments as the original test.
    validation_obj = validation_module.Validation(empty_items, empty_items)

    # Convert to a lazy representation (same call as original).
    lazy_validation = validation_obj.to_lazy()

    # Bind the lazy object to None (same call and literal).
    bound_lazy = lazy_validation.bind(none_value)

    # Call to_lazy() again on the bound result (same call as original).
    bound_lazy.to_lazy()

def test_validation_lazy_to_try_and_ap_does_not_error():
    """Exercise to_lazy(), to_try(), and ap() on a Validation and call is_success()."""
    # Use the same empty mapping for both Validation constructor parameters
    empty_mapping = {}

    # Construct the Validation instance from the mapping
    validation_instance = validation_module.Validation(empty_mapping, empty_mapping)

    # Convert to a lazy representation
    lazy_validation = validation_instance.to_lazy()

    # Convert the lazy representation to a try representation
    try_validation = lazy_validation.to_try()

    # Apply the lazy value back to the original Validation instance
    ap_result = lazy_validation.ap(validation_instance)

    # Call is_success() on the try result (no assertion; preserve original behavior)
    try_validation.is_success()

def test_validation_to_try_returns_result_with_is_success_callable() -> None:
    """Ensure Validation.to_try() returns an object with an is_success method that can be called."""
    value_zero = 0
    values = [value_zero]

    validation = validation_module.Validation(value_zero, values)

    result = validation.to_try()
    assert callable(getattr(result, "is_success", None))
    # Call to ensure the method can be invoked without raising.
    result.is_success()

def test_validation_equality_and_transformations():
    """Exercise a variety of Validation constructors and transformation methods with bytes and None."""
    # Sample binary data used throughout the test (unchanged literal)
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"

    # Explicit None value used as a key in the mapping
    none_value = None

    # Mapping that uses None and the sample bytes as keys/values (preserve original structure)
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create a Validation with None as the first argument and the mapping as second
    validation_none = validation_module.Validation(none_value, mapping)

    # Call __eq__ comparing the object to itself (preserve original call and result)
    equals_result = validation_none.__eq__(validation_none)

    # Convert the validation to a boxed form (preserve original call)
    boxed_result = validation_none.to_box()

    # Create another Validation initialized with the sample bytes for both params
    validation_bytes = validation_module.Validation(sample_bytes, sample_bytes)

    # Convert the boxed result to an Either (preserve original call)
    either_result = boxed_result.to_either()

    # Check if validation_bytes represents a failure (preserve original call)
    is_fail_result = validation_bytes.is_fail()

    # Convert the either result to a Try (preserve original call)
    try_result = either_result.to_try()

    # Create a Validation using the earlier is_fail result and the sample bytes
    validation_from_isfail = validation_module.Validation(is_fail_result, sample_bytes)

    # Obtain string representation of validation_from_isfail (preserve original call)
    validation2_str = validation_from_isfail.__str__()

    # Convert validation_bytes to a lazy representation (preserve original call)
    lazy_result = validation_bytes.to_lazy()

    # Create an additional Validation with bytes/bytes (preserve original call)
    validation3 = validation_module.Validation(sample_bytes, sample_bytes)

    # Repeat converting the boxed result to an Either (same as earlier call)
    either_result_again = boxed_result.to_either()

    # Convert validation_from_isfail to a lazy representation (preserve original call)
    validation2_lazy = validation_from_isfail.to_lazy()

    # Create a Validation combining the lazy form of validation_from_isfail and validation3
    validation4 = validation_module.Validation(validation2_lazy, validation3)

    # Re-check failure status on validation_bytes (preserve original call)
    is_fail_again = validation_bytes.is_fail()

    # Map the string form of validation_from_isfail over the equals_result (preserve original call)
    equals_result.map(validation2_str)

def test_validation_equality_to_maybe_and_bind_calls():
    """Exercise Validation equality, to_maybe, and bind with byte and None inputs."""
    # A sample byte sequence used as both key and value
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None

    # Mapping that uses None as a key and the byte sequence as both a key and a value
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create a Validation instance with None and the mapping
    validation_obj = validation_module.Validation(none_value, mapping)

    # Compare the Validation instance to itself via __eq__ (preserve original call)
    eq_result = validation_obj.__eq__(validation_obj)

    # Call to_maybe() on the validation instance (preserve original call)
    maybe_result = validation_obj.to_maybe()

    # Create a second Validation instance with bytes for both parameters and bind bytes to it
    validation_second = validation_module.Validation(sample_bytes, sample_bytes)
    validation_second.bind(sample_bytes)

def test_validation_eq_returns_boxable_result():
    """Validation.__eq__ should return a value that exposes to_box()."""
    # sample bytes used both as a key and a value in the mapping
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None  # explicit None kept for clarity

    # mapping mirrors the original: {None: bytes, bytes: bytes}
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # construct two Validation instances with the original arguments/order
    left_validation = validation_module.Validation(none_value, mapping)
    right_validation = validation_module.Validation(sample_bytes, none_value)

    # invoke equality and then call to_box() on the result (preserves original calls/order)
    eq_result = left_validation.__eq__(right_validation)
    eq_result.to_box()

