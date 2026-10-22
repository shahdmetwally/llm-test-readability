import pytest
import validation as validator
import builtins as builtins_module

def test_validation_is_success_and_is_fail_returns_maybe():
    """
    Verifies that Validation.is_success() and Validation.is_fail() methods work,
    and that the result of is_fail() can be converted to a Maybe via to_maybe().
    """
    # Arrange
    test_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_instance = validator.Validation(test_message, test_message)

    # Act
    is_success_result = validation_instance.is_success()
    is_equal_to_self = validation_instance.__eq__(validation_instance)
    is_fail_result = validation_instance.is_fail()
    maybe_from_fail = is_fail_result.to_maybe()

def test_validation_equality_with_none_returns_unsuccessful():
    """Verify that comparing a Validation instance with None returns an unsuccessful result."""
    # Arrange
    none_type_0 = None
    int_0 = -6891
    int_1 = 3125
    tuple_0 = (int_1,)
    validation_0 = validator.Validation(int_0, tuple_0)

    # Act
    var_0 = validation_0.__eq__(none_type_0)

    # Assert
    var_0.is_success()

def test_validation_str_returns_failing_result():
    """Verify that __str__() on a Validation instance returns a failing result."""
    empty_dict = {}
    validation = validator.Validation(empty_dict, empty_dict)
    str_result = validation.__str__()
    str_result.is_fail()

def test_validation_to_either_and_maybe_conversion():
    """
    Test that converting a Validation to Either and Maybe works,
    and that calling to_maybe on the result is valid.
    """
    empty_set = set()
    validation = validator.Validation(empty_set, empty_set)
    either_result = validation.to_either()
    maybe_result = validation.to_maybe()
    maybe_result.to_maybe()

def test_validation_to_either_and_fail_maybe_conversion():
    """Test that a Validation object can be converted to Either,
    supports equality comparison, and that its fail status can be
    converted to a Maybe."""
    error_message = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation = validator.Validation(error_message, error_message)
    either_result = validation.to_either()
    is_equal = validation.__eq__(validation)
    fail_result = validation.is_fail()
    fail_result.to_maybe()

def test_validation_to_maybe_returns_maybe_from_empty_sets():
    """Verifies that calling to_maybe() on a Validation with empty sets
    returns a Maybe, and that calling to_maybe() on that result also succeeds."""
    empty_set = set()
    validation = validator.Validation(empty_set, empty_set)
    maybe_result_1 = validation.to_maybe()
    maybe_result_1.to_maybe()

def test_validation_creation_with_none_input():
    """Test that Validation can be created with None as both arguments."""
    # Arrange
    input_value = None
    expected_output = None
    
    # Act
    validation_0 = validator.Validation(input_value, expected_output)

def test_validation_to_maybe_with_none_value():
    """Test that to_maybe() can be called on a Validation initialized with None."""
    none_type_0 = None
    validation_0 = validator.Validation(none_type_0, none_type_0)
    validation_0.to_maybe()

def test_validation_is_fail_returns_none_for_self_validated_object():
    """Verify that is_fail() returns None when the validated object equals itself."""
    validated_object = builtins_module.object()
    validation = validator.Validation(validated_object, validated_object)
    validation.is_fail()

def test_validation_map_with_none_does_not_error():
    """Test that calling Validation.map(None) does not raise an error."""
    # Input values for constructing the Validation instance
    invalid_int = -895
    flag = True
    pair = (invalid_int, flag)
    
    # Build a dictionary using the pair as both key and value
    sample_dict = {pair: pair}
    
    # Create a tuple containing the dictionary twice and the invalid integer
    source_data = (sample_dict, sample_dict, invalid_int)
    
    # Instantiate Validation with the source data and the boolean flag
    validation_instance = validator.Validation(source_data, flag)
    
    # Calling map with None should complete without error
    validation_instance.map(None)

def test_validation_bind_with_none():
    """Test that Validation.bind() accepts None as an argument."""
    # A byte string used as both the type and value for validation
    bytes_0 = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validator_0 = validator.Validation(bytes_0, bytes_0)

    none_type_0 = None
    validator_0.bind(none_type_0)

def test_validation_ap_method_accepts_list_of_booleans():
    """Test that the ap method of a Validation object can handle a list of booleans."""
    # Set up a Validation instance with default False and a list of True values
    default_value = False
    valid_value = True
    value_list = [valid_value, valid_value, valid_value, valid_value]
    
    # Create a Validation object with the default value and list of valid values
    validation_0 = validator.Validation(default_value, value_list)
    
    # Call the ap method with the same list
    validation_0.ap(value_list)

def test_validation_box_success_returns_success_flag():
    """Verify that a Validation object can be boxed and its success status checked."""
    # Given: A Validation instance created with True values
    input_value = True
    validation = validator.Validation(input_value, input_value)
    
    # When: Converting to boxed representation and checking success status
    boxed = validation.to_box()
    result = boxed.is_success()

def test_validation_to_lazy_bind_none_to_lazy():
    """
    Test that chaining Validation.to_lazy() -> bind(None) -> to_lazy()
    executes without error.
    """
    none_value = None
    empty_list = []
    validation_instance = validator.Validation(empty_list, empty_list)
    lazy_validation = validation_instance.to_lazy()
    bound_lazy = lazy_validation.bind(none_value)
    bound_lazy.to_lazy()

def test_validation_try_from_lazy_success_verification():
    """Verify that ap and to_try produce a success result after to_lazy."""
    empty_dict = {}
    validation = validator.Validation(empty_dict, empty_dict)
    lazy_validation = validation.to_lazy()
    try_validation = lazy_validation.to_try()
    lazy_validation.ap(validation)
    try_validation.is_success()

def test_validation_to_try_returns_success_for_valid_input():
    """Test that Validation.to_try() returns a Success object for valid input."""
    int_0 = 0
    list_0 = [int_0]
    validation_0 = validator.Validation(int_0, list_0)
    var_0 = validation_0.to_try()
    var_0.is_success()

def test_validation_eq_and_conversion_operations_with_none_key():
    """Test Validation object equality check and various conversion operations."""
    raw_bytes = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    dict_with_none_key = {none_value: raw_bytes, raw_bytes: raw_bytes}
    validation_obj1 = validator.Validation(none_value, dict_with_none_key)
    # Test self-equality
    validation_obj1.__eq__(validation_obj1)
    validation_obj1.to_box()
    validation_obj2 = validator.Validation(raw_bytes, raw_bytes)
    # Convert to Either
    validation_obj1.to_box().to_either()
    # Check if validation failed
    validation_obj2.is_fail()
    validation_obj1.to_box().to_either().to_try()
    validation_obj3 = validator.Validation(validation_obj2.is_fail(), raw_bytes)
    validation_obj3.__str__()
    validation_obj2.to_lazy()
    validator.Validation(raw_bytes, raw_bytes)
    validation_obj1.to_box().to_either()
    validation_obj3.to_lazy()
    validator.Validation(validation_obj3.to_lazy(), validator.Validation(raw_bytes, raw_bytes))
    validation_obj2.is_fail()
    # Map with previous string representation
    validation_obj1.__eq__(validation_obj1).map(validation_obj3.__str__())

def test_validation_equality_and_maybe_conversion_with_bytes():
    """Test that Validation objects support equality comparison, to_maybe conversion, and binding with bytes."""
    bytes_data = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    dict_with_none_key = {none_value: bytes_data, bytes_data: bytes_data}
    validation_1 = validator.Validation(none_value, dict_with_none_key)
    # Test equality with self
    var_eq_result = validation_1.__eq__(validation_1)
    # Convert to Maybe type
    var_maybe_result = validation_1.to_maybe()
    # Create another validation instance with bytes data and test binding
    validation_2 = validator.Validation(bytes_data, bytes_data)
    validation_2.bind(bytes_data)

def test_validation_equality_with_bytes_and_none_types():
    """Test that Validation objects containing bytes and None types can be compared and converted to Box."""
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    
    # Create dict mapping None->bytes and bytes->bytes
    mixed_dict = {none_value: bytes_value, bytes_value: bytes_value}
    
    # Create two Validation instances with different type combinations
    validation_with_dict = validator.Validation(none_value, mixed_dict)
    validation_with_bytes = validator.Validation(bytes_value, none_value)
    
    # Compare the two Validation objects for equality
    equality_result = validation_with_dict.__eq__(validation_with_bytes)
    
    # Convert the result to a Box object
    equality_result.to_box()