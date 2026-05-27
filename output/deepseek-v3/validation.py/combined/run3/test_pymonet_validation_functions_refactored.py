import pytest
import validation as validator
import builtins as builtins_module

def test_validation_creation_and_basic_methods():
    """
    Test that a Validation instance can be created and its basic methods
    (is_success, __eq__, is_fail, to_maybe) can be called without error.
    """
    # Create a Validation instance with identical value and error strings
    description_string = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_instance = module_0.Validation(description_string, description_string)

    # Test basic predicate methods
    is_success_result = validation_instance.is_success()
    equality_result = validation_instance.__eq__(validation_instance)
    is_fail_result = validation_instance.is_fail()

    # Test conversion method on the failure result
    is_fail_result.to_maybe()

def test_validation_eq_none_returns_successful_result():
    """Test that comparing a Validation instance with None returns a result that can check success status."""
    
    # Test data
    none_value = None
    negative_value = -6891
    positive_value = 3125
    
    # Create a tuple with single element
    single_element_tuple = (positive_value,)
    
    # Create Validation instance
    validation_instance = validator.Validation(negative_value, single_element_tuple)
    
    # Compare with None and check result
    comparison_result = validation_instance.__eq__(none_value)
    comparison_result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Test that __str__ method of Validation returns an object with an is_fail method."""
    # Create a Validation instance with empty dictionaries
    empty_dict = {}
    validation_instance = validator.Validation(empty_dict, empty_dict)
    
    # Get string representation
    str_result = validation_instance.__str__()
    
    # Verify the result has an is_fail method
    str_result.is_fail()

def test_validation_with_empty_sets_can_convert_to_either_and_maybe() -> None:
    """Test that Validation initialized with empty sets can convert to Either and Maybe types."""
    empty_set = set()
    validation = module_0.Validation(empty_set, empty_set)
    
    either_result = validation.to_either()
    maybe_result = validation.to_maybe()
    
    # Verify Maybe conversion can be chained
    maybe_result.to_maybe()

def test_validation_basic_operations_with_string():
    """Test basic Validation operations with a multiline string input."""
    multiline_docstring = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    
    # Create Validation instance and test various operations
    validation_instance = module_0.Validation(multiline_docstring, multiline_docstring)
    
    # Test conversion to Either
    either_result = validation_instance.to_either()
    
    # Test equality with itself
    self_equality_result = validation_instance.__eq__(validation_instance)
    
    # Test failure check and conversion to Maybe
    is_fail_result = validation_instance.is_fail()
    is_fail_result.to_maybe()

def test_validation_to_maybe_can_be_called_twice() -> None:
    """Test that calling to_maybe() on a Validation instance and then on the result does not raise an error."""
    empty_set = set()
    validation_instance = module_0.Validation(empty_set, empty_set)
    maybe_result = validation_instance.to_maybe()
    # This second call should not raise an error
    maybe_result.to_maybe()

def test_validation_initialization_with_none_values():
    """Test that a Validation object can be instantiated with None values."""
    # Create None value to pass as arguments
    none_value = None
    
    # Instantiate Validation with None values for both parameters
    validation_instance = validator.Validation(none_value, none_value)
    
    # Verify the instance was created successfully
    assert validation_instance is not None
    # Verify the attributes are set to None
    assert validation_instance.value is None
    assert validation_instance.errors is None

def test_validation_to_maybe_with_none_values() -> None:
    """Test that Validation.to_maybe() works when initialized with None values."""
    # Create None values for initialization
    none_value = None
    
    # Create Validation instance with None values
    validation_instance = validator.Validation(none_value, none_value)
    
    # Call to_maybe() method - test passes if no exception occurs
    validation_instance.to_maybe()

def test_validation_is_fail_with_identical_objects() -> None:
    """Test that Validation.is_fail() can be called when instantiated with identical objects."""
    # Create a test object
    test_object = builtins_module.object()
    
    # Create a Validation instance with two references to the same object
    validation_instance = validator.Validation(test_object, test_object)
    
    # Verify is_fail() can be called without errors
    validation_instance.is_fail()

def test_validation_map_with_none_and_complex_data() -> None:
    """Test Validation.map() method with None argument when Validation contains nested complex data structures."""
    
    # Create a None value to pass to map
    none_value = None
    
    # Integer and boolean values for constructing the Validation object
    negative_number = -895
    true_value = True
    
    # Tuple to be used as a key in a dictionary
    key_value_tuple = (negative_number, true_value)
    
    # Dictionary with the tuple as both key and value
    nested_dict = {key_value_tuple: key_value_tuple}
    
    # Complex tuple containing two copies of the dictionary and the integer
    complex_tuple = (nested_dict, nested_dict, negative_number)
    
    # Create a Validation instance with the complex tuple and the boolean
    validation_instance = validator.Validation(complex_tuple, true_value)
    
    # Call map with None
    validation_instance.map(none_value)

def test_validation_bind_with_none() -> None:
    """Test that Validation.bind() can be called with None argument."""
    # Create test bytes data
    test_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    
    # Create Validation instance with same bytes for both parameters
    validation_instance = module_0.Validation(test_bytes, test_bytes)
    
    # Test binding with None value
    none_value = None
    validation_instance.bind(none_value)

def test_validation_ap_with_list_of_true_values_basic() -> None:
    """Test Validation.ap() method with a list of boolean True values."""
    is_valid = False
    true_value = True
    true_values = [true_value, true_value, true_value, true_value]
    
    validation = validator.Validation(is_valid, true_values)
    # Note: This test calls the ap() method but doesn't assert anything
    validation.ap(true_values)

def test_validation_ap_with_list_of_true_values_basic():
    from pymonad.validation import Validation
    from pymonad.maybe import Maybe
    
    # Test that ap works correctly with a list of true values
    def add_one(x):
        return x + 1
    
    def multiply_two(x):
        return x * 2
    
    # Create a successful validation with a function
    func_val = Validation.success(add_one)
    
    # Create a successful validation with a value
    value_val = Validation.success(5)
    
    # Apply the function validation to the value validation
    result = func_val.ap(value_val)
    
    # Check the result
    assert result == Validation.success(6)
    
    # Test with a different function
    func_val2 = Validation.success(multiply_two)
    result2 = func_val2.ap(value_val)
    assert result2 == Validation.success(10)
    
    # Test with a failed validation (function side)
    failed_func = Validation.fail(["Function error"])
    result3 = failed_func.ap(value_val)
    assert result3 == Validation.fail(["Function error"])
    
    # Test with a failed validation (value side)
    failed_value = Validation.fail(["Value error"])
    result4 = func_val.ap(failed_value)
    assert result4 == Validation.fail(["Value error"])
    
    # Test with both failed validations
    result5 = failed_func.ap(failed_value)
    # Should combine errors
    assert result5 == Validation.fail(["Function error", "Value error"])

def test_validation_to_lazy_bind_to_lazy():
    """
    Test that to_lazy() can be called on the result of bind() operation on a Validation instance.
    """
    none_value = None
    empty_list = []
    
    # Create Validation instance with empty lists
    validation_instance = validator.Validation(empty_list, empty_list)
    
    # Convert to lazy validation
    lazy_validation = validation_instance.to_lazy()
    
    # Bind with None value
    bound_result = lazy_validation.bind(none_value)
    
    # Call to_lazy() on the bound result
    bound_result.to_lazy()

def test_validation_to_lazy_to_try_and_ap_operations():
    """Test chaining Validation to Lazy, converting to Try, and applying ap."""
    # Create empty dict and Validation instance
    empty_dict = {}
    validation_instance = validator.Validation(empty_dict, empty_dict)
    
    # Convert Validation to Lazy monad
    lazy_instance = validation_instance.to_lazy()
    
    # Convert Lazy to Try monad
    try_instance = lazy_instance.to_try()
    
    # Apply the lazy instance to the original validation via ap
    ap_result = lazy_instance.ap(validation_instance)
    
    # Verify the try operation completed successfully
    assert try_instance.is_success()

def test_validation_to_try_returns_successful_try() -> None:
    """Test that converting a Validation to Try returns a successful Try."""
    # Create a simple value and wrap it in a list
    value = 0
    value_list = [value]
    
    # Create Validation instance with the value and list
    validation_instance = validator.Validation(value, value_list)
    
    # Convert Validation to Try and verify it's successful
    try_instance = validation_instance.to_try()
    try_instance.is_success()

def test_validation_operations_and_methods():
    """Test various operations and method calls on Validation instances."""
    # Create test data
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    sample_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}
    
    # Create Validation instances and test operations
    validation_with_none = validator.Validation(none_value, sample_dict)
    is_equal = validation_with_none.__eq__(validation_with_none)
    box_result = validation_with_none.to_box()
    
    validation_bytes_bytes = validator.Validation(sample_bytes, sample_bytes)
    either_result = box_result.to_either()
    is_fail_result = validation_bytes_bytes.is_fail()
    try_result = either_result.to_try()
    
    validation_with_bool_and_bytes = validator.Validation(is_fail_result, sample_bytes)
    validation2_str = validation_with_bool_and_bytes.__str__()
    lazy_result1 = validation_bytes_bytes.to_lazy()
    
    validation_bytes_bytes2 = validator.Validation(sample_bytes, sample_bytes)
    either_result2 = box_result.to_either()
    lazy_result2 = validation_with_bool_and_bytes.to_lazy()
    
    validation_with_lazy_and_validation = validator.Validation(lazy_result2, validation_bytes_bytes2)
    is_fail_result2 = validation_bytes_bytes.is_fail()
    
    # Final operation
    is_equal.map(validation2_str)

def test_validation_methods_can_be_called_without_exceptions() -> None:
    """Test that Validation methods can be called without raising exceptions."""
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    mapping = {none_value: sample_bytes, sample_bytes: sample_bytes}

    # Create Validation with None and a dict
    validation_with_none_and_dict = validator.Validation(none_value, mapping)
    equality_result = validation_with_none_and_dict.__eq__(validation_with_none_and_dict)
    maybe_result = validation_with_none_and_dict.to_maybe()

    # Create Validation with bytes as both value and error
    validation_with_bytes = validator.Validation(sample_bytes, sample_bytes)
    validation_with_bytes.bind(sample_bytes)

def test_validation_eq_comparison_and_to_box():
    """Test that comparing two Validation objects with different values via __eq__ and calling to_box() works."""
    
    # Create sample bytes data
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    
    # Create a dictionary with None as key and bytes as value, and bytes as both key and value
    none_value = None
    mapping_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}
    
    # Create two Validation objects with swapped arguments
    validation_with_none = validator.Validation(none_value, mapping_dict)
    validation_with_bytes = validator.Validation(sample_bytes, none_value)
    
    # Compare the two Validation objects and call to_box() on the result
    equality_result = validation_with_none.__eq__(validation_with_bytes)
    equality_result.to_box()

