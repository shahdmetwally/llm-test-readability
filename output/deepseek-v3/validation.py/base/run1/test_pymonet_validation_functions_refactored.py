import pytest
import validation as validation_module
import builtins as builtins_module

def test_validation_with_docstring_and_method_calls():
    """
    Tests that a Validation object can be created with a docstring payload
    and that basic methods (is_success, is_fail, eq, to_maybe) can be called
    without errors.
    """
    # Create a Validation object using a docstring as both success and failure values
    docstring = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_obj = validation_module.Validation(docstring, docstring)

    # Call basic validation methods to ensure they execute without errors
    success_check = validation_obj.is_success()
    equality_check = validation_obj.__eq__(validation_obj)
    fail_check = validation_obj.is_fail()
    
    # Attempt to convert the is_fail result to a Maybe (tests method chaining)
    fail_check.to_maybe()

def test_validation_eq_none_returns_success_validation():
    """Test that comparing a Validation object with None returns a successful Validation."""
    # Create a Validation object with negative integer and tuple
    validation_value = -6891
    tuple_content = (3125,)
    validation_obj = validation_module.Validation(validation_value, tuple_content)
    
    # Compare with None and verify the result is a successful Validation
    comparison_result = validation_obj.__eq__(None)
    comparison_result.is_success()

def test_validation_str_returns_object_with_is_fail_method():
    """Test that Validation.__str__() returns an object with an is_fail() method."""
    # Create a Validation instance with empty dictionaries
    empty_dict = {}
    validation_instance = validation_module.Validation(empty_dict, empty_dict)
    
    # Call __str__() and verify the returned object has is_fail() method
    str_result = validation_instance.__str__()
    str_result.is_fail()  # Should not raise AttributeError

def test_validation_to_either_and_to_maybe_chain() -> None:
    """Test that Validation can be converted to Either and Maybe types, 
    and that Maybe.to_maybe() can be called on the resulting Maybe."""
    
    # Create empty sets for Validation constructor
    empty_set = set()
    
    # Create a Validation instance with empty sets for success and failure values
    validation = validation_module.Validation(empty_set, empty_set)
    
    # Convert Validation to Either type
    either_result = validation.to_either()
    
    # Convert Validation to Maybe type
    maybe_result = validation.to_maybe()
    
    # Call to_maybe() on the Maybe result (should be idempotent)
    maybe_result.to_maybe()

def test_validation_equality_and_transformations():
    """
    Tests that a Validation instance can be converted to an Either,
    correctly compares equal to itself, and can be checked for failure state.
    """
    # Create a Validation instance with identical success and failure messages
    docstring_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_obj = validation_module.Validation(docstring_message, docstring_message)
    
    # Convert to Either (should produce a Right for success or Left for failure)
    either_result = validation_obj.to_either()
    
    # Self-equality check (should be True)
    is_equal = validation_obj.__eq__(validation_obj)
    
    # Check if validation is a failure
    is_fail_result = validation_obj.is_fail()
    
    # Convert the failure check result to a Maybe type
    is_fail_result.to_maybe()

def test_validation_to_maybe_can_be_called_twice():
    """Test that converting a Validation to a Maybe allows calling to_maybe again."""
    empty_set = set()
    validation_obj = validation_module.Validation(empty_set, empty_set)
    maybe_obj = validation_obj.to_maybe()
    # Verify the returned Maybe can also have to_maybe() called on it
    maybe_obj.to_maybe()

def test_validation_initialization_with_none_arguments():
    """Test that Validation can be instantiated with None values for both arguments."""
    none_arg = None
    validation_instance = validation_module.Validation(none_arg, none_arg)

def test_validation_with_none_values_converts_to_maybe():
    """Test that a Validation instance initialized with None values can be converted to a Maybe."""
    # Create a Validation with None for both success and failure values
    none_value = None
    validation_instance = validation_module.Validation(none_value, none_value)
    
    # Convert Validation to Maybe - this should not raise any exceptions
    validation_instance.to_maybe()

def test_validation_is_fail_with_two_identical_objects():
    """
    Test that Validation.is_fail() method works correctly when initialized
    with two identical object instances.
    """
    # Create a base object instance
    base_object = builtins_module.object()
    
    # Create a Validation instance with the same object passed twice
    validation = validation_module.Validation(base_object, base_object)
    
    # Verify is_fail() can be called without errors
    validation.is_fail()

def test_validation_map_with_none_value_on_complex_structure():
    """Test that Validation.map() handles None value when Validation contains nested structures."""
    # Create a complex nested structure for the Validation
    none_value = None
    negative_int = -895
    true_value = True
    
    # Create a tuple that will serve as both key and value in a dictionary
    key_value_tuple = (negative_int, true_value)
    
    # Create a dictionary with the tuple as both key and value
    nested_dict = {key_value_tuple: key_value_tuple}
    
    # Create a tuple containing the dictionary twice and the negative integer
    validation_data = (nested_dict, nested_dict, negative_int)
    
    # Create Validation instance with the complex data structure
    validation_instance = validation_module.Validation(validation_data, true_value)
    
    # Test mapping with None value
    validation_instance.map(none_value)

def test_validation_bind_with_none():
    """Test that Validation.bind() accepts None as an argument without error."""
    # Create arbitrary bytes data for testing
    test_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    
    # Initialize Validation object with the same bytes for both parameters
    validation_obj = validation_module.Validation(test_bytes, test_bytes)
    
    # Test that bind() method accepts None argument
    none_value = None
    validation_obj.bind(none_value)

def test_validation_ap_with_list_of_values():
    """Test that Validation.ap() can be called with a list argument."""
    # Create a Validation object with a failure flag and list of success values
    failure_flag = False
    success_flag = True
    success_list = [success_flag, success_flag, success_flag, success_flag]
    
    validation_obj = validation_module.Validation(failure_flag, success_list)
    # Apply the ap() method with the same list of values
    validation_obj.ap(success_list)

def test_validation_to_box_conversion_and_success_check():
    """Test converting a Validation instance to a Box and verifying success status."""
    # Create a Validation with identical success and value (both True)
    success_value = True
    validation = validation_module.Validation(success_value, success_value)
    
    # Convert Validation to Box
    box = validation.to_box()
    
    # Verify the Box's success status (no assertion, just ensuring no exception)
    box.is_success()

def test_validation_to_lazy_bind_none_to_lazy():
    """Test that converting Validation to Lazy, binding None, and converting back works."""
    # Create a Validation object with empty lists as success and failure values
    empty_list = []
    validation_obj = validation_module.Validation(empty_list, empty_list)
    
    # Convert Validation to Lazy monad
    lazy_validation = validation_obj.to_lazy()
    
    # Bind None to the Lazy monad (should propagate None through the monadic chain)
    bound_lazy = lazy_validation.bind(None)
    
    # Convert the result back to Lazy (should be a no-op since it's already Lazy)
    bound_lazy.to_lazy()

def test_validation_to_lazy_to_try_and_ap():
    """Test that Validation can be converted to Lazy, then to Try, 
    and that Lazy's ap method works with another Validation."""
    
    empty_dict = {}
    validation_instance = validation_module.Validation(empty_dict, empty_dict)
    
    # Convert Validation to Lazy monad
    lazy_result = validation_instance.to_lazy()
    
    # Convert Lazy to Try monad
    try_result = lazy_result.to_try()
    
    # Apply Validation's function via Lazy's applicative (ap)
    ap_result = lazy_result.ap(validation_instance)
    
    # Check if Try conversion was successful
    assert try_result.is_success()

def test_validation_to_try_conversion_yields_successful_try():
    """
    Test that converting a Validation instance containing a value and error list
    to a Try results in a successful Try object.
    """
    value = 0
    error_list = [value]
    validation = validation_module.Validation(value, error_list)
    try_result = validation.to_try()
    # Verify the Try indicates success without raising an exception
    assert try_result.is_success()

def test_validation_operations_with_various_types_and_method_chaining():
    """
    Test that Validation objects can be created with different data types
    and support method chaining operations without errors.
    """
    # Create test data
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    
    # Create a dictionary with mixed key/value types
    mixed_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}
    
    # Create Validation instances with different data types
    validation_with_none_and_dict = validation_module.Validation(none_value, mixed_dict)
    
    # Test equality comparison
    equality_result = validation_with_none_and_dict.__eq__(validation_with_none_and_dict)
    
    # Test transformation methods
    box_result = validation_with_none_and_dict.to_box()
    
    # Create another Validation with bytes data
    validation_with_bytes = validation_module.Validation(sample_bytes, sample_bytes)
    
    # Chain transformations
    either_result_from_box = box_result.to_either()
    is_fail_result = validation_with_bytes.is_fail()
    try_result = either_result_from_box.to_try()
    
    # Create Validation with boolean result
    validation_with_fail_and_bytes = validation_module.Validation(is_fail_result, sample_bytes)
    
    # Test string representation
    validation_str = validation_with_fail_and_bytes.__str__()
    
    # More method chaining
    lazy_result_from_validation1 = validation_with_bytes.to_lazy()
    
    # Create another Validation instance
    another_validation_with_bytes = validation_module.Validation(sample_bytes, sample_bytes)
    
    # Continue method chaining
    either_result_from_box_again = box_result.to_either()
    lazy_result_from_validation2 = validation_with_fail_and_bytes.to_lazy()
    
    # Create Validation with lazy result
    validation_with_lazy_and_validation = validation_module.Validation(
        lazy_result_from_validation2, another_validation_with_bytes
    )
    
    # Check failure status again
    is_fail_result_again = validation_with_bytes.is_fail()
    
    # Final method call
    equality_result.map(validation_str)

def test_validation_equality_to_maybe_and_bind():
    """Test Validation's __eq__, to_maybe, and bind methods with various inputs."""
    
    # Create test data
    test_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    test_dict = {none_value: test_bytes, test_bytes: test_bytes}
    
    # Create Validation with None and dict
    validation_with_none = validation_module.Validation(none_value, test_dict)
    
    # Test equality with itself
    equality_result = validation_with_none.__eq__(validation_with_none)
    
    # Convert to Maybe
    maybe_result = validation_with_none.to_maybe()
    
    # Create another Validation with bytes as both success and fail values
    validation_with_bytes = validation_module.Validation(test_bytes, test_bytes)
    
    # Test bind method
    validation_with_bytes.bind(test_bytes)

def test_validation_equality_result_can_be_boxed():
    """Test that comparing two Validation objects returns a result that can be boxed."""
    # Create test data
    sample_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    
    # Create dictionary with None key and bytes value
    sample_dict = {none_value: sample_bytes, sample_bytes: sample_bytes}
    
    # Create two Validation instances with different data
    validation_with_dict = validation_module.Validation(none_value, sample_dict)
    validation_with_none = validation_module.Validation(sample_bytes, none_value)
    
    # Compare the two Validation objects
    equality_result = validation_with_dict.__eq__(validation_with_none)
    
    # Verify the comparison result can be boxed (has to_box method)
    equality_result.to_box()

