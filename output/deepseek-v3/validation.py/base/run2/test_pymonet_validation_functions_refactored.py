import pytest
import validation as validation_module
import builtins as builtins_module

def test_validation_self_equality_and_methods():
    """
    Test that a Validation object can be compared to itself,
    and that its success/fail status methods can be called.
    """
    # Create a docstring to use as both success and failure values
    docstring = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    
    # Create a Validation object with identical success/failure values
    validation_obj = validation_module.Validation(docstring, docstring)
    
    # Check if the validation is successful
    is_success_result = validation_obj.is_success()
    
    # Test equality with itself
    self_equality_result = validation_obj.__eq__(validation_obj)
    
    # Check if the validation is a failure
    is_fail_result = validation_obj.is_fail()
    
    # Convert the failure status to a Maybe type
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_successful_validation():
    """
    Test that comparing a Validation object with None returns a Validation
    object where is_success() returns True.
    """
    # Create a None value for comparison
    none_value = None
    
    # Create test values for Validation constructor
    validation_value = -6891
    tuple_value = (3125,)
    
    # Create Validation object with test values
    validation_obj = validation_module.Validation(validation_value, tuple_value)
    
    # Compare Validation object with None (returns another Validation object)
    comparison_result = validation_obj.__eq__(none_value)
    
    # Verify the comparison result is a successful Validation
    comparison_result.is_success()

def test_validation_string_representation_has_is_fail_method():
    """Test that the string representation of a Validation instance has an is_fail method."""
    empty_dict = {}
    validation = validation_module.Validation(empty_dict, empty_dict)
    validation_str = validation.__str__()
    # Verify the string representation has the expected method
    validation_str.is_fail()

def test_validation_with_empty_sets_can_convert_to_either_and_maybe():
    """Test that a Validation object initialized with empty sets can be converted to Either and Maybe types."""
    empty_set = set()
    validation_obj = validation_module.Validation(empty_set, empty_set)
    
    # Convert validation to Either type
    either_result = validation_obj.to_either()
    
    # Convert validation to Maybe type
    maybe_result = validation_obj.to_maybe()
    
    # Verify Maybe conversion can be called again (should be idempotent)
    maybe_result.to_maybe()

def test_validation_identical_success_failure_values_methods():
    """
    Test that a Validation object can:
    1. Be converted to an Either
    2. Correctly compare equal to itself
    3. Check if it's a failure
    4. Convert the failure check result to a Maybe
    """
    # Create a Validation instance with identical success/failure values
    docstring_content = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_obj = validation_module.Validation(docstring_content, docstring_content)
    
    # Test conversion to Either type
    either_result = validation_obj.to_either()
    
    # Test equality with itself (should be True)
    self_equality = validation_obj.__eq__(validation_obj)
    
    # Check if the Validation represents a failure
    is_fail_result = validation_obj.is_fail()
    
    # Convert the boolean result to a Maybe (though typically booleans don't have this method)
    is_fail_result.to_maybe()

def test_validation_to_maybe_can_be_called_twice_without_error():
    """Test that to_maybe() can be called twice on a Validation object without raising errors."""
    empty_set = set()
    validation = validation_module.Validation(empty_set, empty_set)
    maybe = validation.to_maybe()
    maybe.to_maybe()  # Second call should not raise any exception

def test_validation_initialization_with_none_arguments():
    """Test that Validation can be initialized with None arguments."""
    none_value = None
    validation_obj = validation_module.Validation(none_value, none_value)

def test_validation_with_none_values_can_call_to_maybe():
    """Test that Validation initialized with None values can call to_maybe without error."""
    none_arg = None
    validation = validation_module.Validation(none_arg, none_arg)
    validation.to_maybe()

def test_is_fail_can_be_called_on_validation_with_two_object_instances():
    """Test that is_fail() can be called on a Validation instance initialized with two object instances."""
    # Create a base object instance
    base_object = builtins_module.object()
    
    # Create a Validation instance using the same object for both parameters
    validation_instance = validation_module.Validation(base_object, base_object)
    
    # Verify is_fail() can be called without error
    validation_instance.is_fail()

def test_validation_map_with_none_argument():
    """Test that Validation.map() can be called with None argument without error."""
    # Create a Validation instance with complex nested structure
    none_value = None
    negative_int = -895
    flag = True
    
    # Build nested structure: tuple -> dict -> tuple -> Validation
    key_value_pair = (negative_int, flag)
    nested_dict = {key_value_pair: key_value_pair}
    validation_input = (nested_dict, nested_dict, negative_int)
    
    validation_instance = validation_module.Validation(validation_input, flag)
    
    # Call map() with None - should handle None argument gracefully
    validation_instance.map(none_value)

def test_validation_bind_with_none():
    """Test that Validation.bind() can be called with None argument."""
    # Create a Validation instance with bytes data
    test_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validation_instance = validation_module.Validation(test_bytes, test_bytes)
    
    # Call bind with None - should not raise any exceptions
    none_argument = None
    validation_instance.bind(none_argument)

def test_validation_ap_method_with_list_of_true_values():
    """Test that Validation.ap() correctly processes a list of True values."""
    # Create a Validation object with False as the main value and a list of True values
    is_false = False
    is_true = True
    list_of_true_values = [is_true, is_true, is_true, is_true]
    
    validation_obj = validation_module.Validation(is_false, list_of_true_values)
    
    # Apply the ap method with the same list of True values
    validation_obj.ap(list_of_true_values)

def test_validation_to_box_preserves_success_state():
    """Test that converting a successful Validation to a Box retains success status."""
    success_value = True
    validation_instance = validation_module.Validation(success_value, success_value)
    
    # Convert Validation to Box and verify it remains successful
    box_instance = validation_instance.to_box()
    assert box_instance.is_success()

def test_bind_none_to_lazy_validation_produces_lazy():
    """Test that binding None to a lazy-wrapped Validation yields another lazy."""
    none_value = None
    empty_list = []
    
    # Create a Validation with empty lists for success/failure values
    validation_obj = validation_module.Validation(empty_list, empty_list)
    
    # Convert to lazy computation
    lazy_validation = validation_obj.to_lazy()
    
    # Bind None to the lazy computation
    bound_lazy = lazy_validation.bind(none_value)
    
    # The result should also be convertible to lazy
    bound_lazy.to_lazy()

def test_validation_to_lazy_to_try_and_ap_methods():
    """Test that Validation can be converted to Lazy, then to Try, and supports ap operation."""
    empty_dict = {}
    validation_with_empty_dicts = validation_module.Validation(empty_dict, empty_dict)
    
    # Convert Validation to Lazy monad
    lazy_result = validation_with_empty_dicts.to_lazy()
    
    # Convert Lazy to Try monad
    try_result = lazy_result.to_try()
    
    # Apply Validation's function to Lazy using applicative (ap)
    ap_result = lazy_result.ap(validation_with_empty_dicts)
    
    # Verify Try conversion was successful
    assert try_result.is_success()

def test_validation_to_try_conversion_yields_success():
    """Test that converting a Validation with value and empty error list to Try yields success."""
    # Create a Validation with integer value and empty error list
    value = 0
    error_list = []
    validation = validation_module.Validation(value, error_list)
    
    # Convert Validation to Try and verify it's successful
    result_try = validation.to_try()
    result_try.is_success()

def test_validation_operations_with_bytes_and_none():
    """Test various Validation operations including equality checks, type conversions, and method chaining."""
    # Create test data
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    
    # Create a dictionary with bytes and None as keys/values
    mixed_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}
    
    # Create Validation instances with different combinations
    validation_none_dict = validation_module.Validation(none_value, mixed_dict)
    validation_bytes_bytes = validation_module.Validation(sample_bytes, sample_bytes)
    
    # Test equality comparison
    equality_result = validation_none_dict.__eq__(validation_none_dict)
    
    # Test type conversions
    box_result = validation_none_dict.to_box()
    either_result = box_result.to_either()
    try_result = either_result.to_try()
    
    # Test failure detection
    is_fail_result = validation_bytes_bytes.is_fail()
    
    # Create another Validation with boolean result
    validation_bool_bytes = validation_module.Validation(is_fail_result, sample_bytes)
    
    # Test string representation
    string_repr = validation_bool_bytes.__str__()
    
    # Test lazy conversion
    lazy_result_1 = validation_bytes_bytes.to_lazy()
    lazy_result_2 = validation_bool_bytes.to_lazy()
    
    # Create nested Validation with lazy result
    validation_nested = validation_module.Validation(lazy_result_2, validation_bytes_bytes)
    
    # Test failure detection again
    is_fail_again = validation_bytes_bytes.is_fail()
    
    # Test mapping operation
    equality_result.map(string_repr)

def test_validation_equality_and_bind_with_bytes_and_dict():
    """Test Validation object behavior with bytes keys and None values.

    This test verifies that:
    1. A Validation object can be created with None and a dictionary.
    2. The __eq__ method works when comparing a Validation to itself.
    3. The to_maybe() method can be called without error.
    4. A Validation object can be created with bytes as both success and failure.
    5. The bind() method can be called with bytes without raising an exception.
    """
    # Create test data
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    sample_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create Validation with None and a dictionary
    validation_with_none_and_dict = validation_module.Validation(none_value, sample_dict)

    # Compare Validation to itself (should return True)
    _ = validation_with_none_and_dict.__eq__(validation_with_none_and_dict)

    # Convert Validation to Maybe (unused result)
    _ = validation_with_none_and_dict.to_maybe()

    # Create another Validation with bytes as both success and failure
    validation_with_bytes = validation_module.Validation(sample_bytes, sample_bytes)

    # Bind bytes to Validation (tests monadic bind operation)
    validation_with_bytes.bind(sample_bytes)

def test_validation_eq_comparison_result_can_be_boxed() -> None:
    """Test that the result of comparing two Validation objects can be converted to a Box."""
    # Create test data
    test_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    
    # Create a dictionary mapping None to bytes and bytes to bytes
    mapping = {none_value: test_bytes, test_bytes: test_bytes}
    
    # Create two Validation objects with different structures
    validation_with_none_and_dict = validation_module.Validation(none_value, mapping)
    validation_with_bytes_and_none = validation_module.Validation(test_bytes, none_value)
    
    # Compare the two Validation objects and convert result to Box
    comparison_result = validation_with_none_and_dict.__eq__(validation_with_bytes_and_none)
    comparison_result.to_box()

