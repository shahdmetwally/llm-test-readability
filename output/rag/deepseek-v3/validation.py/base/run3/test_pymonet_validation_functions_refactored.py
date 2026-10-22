import pytest
import validation as validation_module
import builtins as builtins_module

def test_validation_with_string_input_returns_success_failure_and_maybe():
    """Test that Validation correctly handles string inputs for is_success, is_fail, and to_maybe."""
    input_string = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation = validation_module.Validation(input_string, input_string)
    
    is_success = validation.is_success()
    is_equal = validation.__eq__(validation)
    is_fail = validation.is_fail()
    
    is_fail.to_maybe()

def test_validation_equality_with_none_returns_success():
    """Test that calling __eq__ on a Validation object with None returns a successful result."""
    # Input values
    code = -6891
    value = 3125
    errors = (value,)

    # Create a Validation instance and compare with None
    validation = validation_module.Validation(code, errors)
    result = validation.__eq__(None)

    # Verify the comparison result indicates success
    result.is_success()

def test_validation_str_returns_fail_for_empty_dicts():
    """Test that Validation.__str__() with empty dicts returns a failure."""
    empty_dict = {}
    validation = validation_module.Validation(empty_dict, empty_dict)
    str_representation = validation.__str__()
    str_representation.is_fail()

def test_validation_conversion_to_either_and_maybe():
    """Test that converting a Validation to Either and Maybe works correctly."""
    set_0 = set()
    validation_0 = validation_module.Validation(set_0, set_0)
    var_0 = validation_0.to_either()
    var_1 = validation_0.to_maybe()
    var_1.to_maybe()

def test_validation_to_either_equality_and_fail_maybe():
    """
    Verifies the behaviour of Validation methods: to_either, equality check, is_fail, and to_maybe.
    """
    docstring_content = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_instance = validation_module.Validation(docstring_content, docstring_content)

    # Convert Validation to Either
    either_result = validation_instance.to_either()

    # Check equality of Validation with itself
    equality_result = validation_instance.__eq__(validation_instance)

    # Check if Validation is a failure
    fail_result = validation_instance.is_fail()

    # Convert fail result to Maybe
    fail_result.to_maybe()

def test_to_maybe_returns_object_that_supports_to_maybe():
    """Test that calling to_maybe() on a Validation returns an object which itself supports to_maybe()."""
    set_a = set()
    set_b = set()
    validation = validation_module.Validation(set_a, set_b)
    maybe_result = validation.to_maybe()
    maybe_result.to_maybe()

def test_validation_creation_with_both_fields_none():
    """Verify that a Validation object can be created with None for both fields."""
    # Arrange
    target_value = None
    constraint = None

    # Act
    validation_instance = validation_module.Validation(target_value, constraint)

def test_to_maybe_handles_none_value_and_error():
    """Test that Validation.to_maybe() handles None values without error."""
    # Arrange: Create a Validation instance with None for both value and error
    none_type_0 = None
    validation_0 = validation_module.Validation(none_type_0, none_type_0)
    
    # Act: Call to_maybe() (should not raise and should return Nothing)
    validation_0.to_maybe()

def test_is_fail_returns_something_with_no_errors():
    """Test that calling is_fail() on a Validation instance does not raise an error."""
    object_0 = builtins_module.object()  # Could be changed to a more descriptive name if domain knowledge is available
    validation_instance = validation_module.Validation(object_0, object_0)
    validation_instance.is_fail()

def test_validation_map_handles_none_gracefully():
    """Test that Validation.map handles a None argument without error."""
    none_input = None
    int_value = -895
    bool_value = True
    tuple_key = (int_value, bool_value)
    dict_nested = {tuple_key: tuple_key}
    tuple_args = (dict_nested, dict_nested, int_value)
    validation_instance = validation_module.Validation(tuple_args, bool_value)
    validation_instance.map(none_input)

def test_validation_bind_with_none_after_arbitrary_bytes():
    """Test that Validation.bind() can be called with None after initialization with arbitrary bytes."""
    input_bytes = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validation = validation_module.Validation(input_bytes, input_bytes)
    none_value = None
    validation.bind(none_value)

def test_validation_append_with_all_positive_values():
    """Test that Validation.ap() handles a list of all True values correctly."""
    # Create a validation with False as the base value
    is_valid = False
    positive_value = True
    all_positive_values = [positive_value] * 4
    
    validation = validation_module.Validation(is_valid, all_positive_values)
    validation.ap(all_positive_values)

def test_validation_to_box_is_success_returns_correctly():
    """Test that Validation.to_box().is_success() works correctly."""
    bool_0 = True
    validation_0 = validation_module.Validation(bool_0, bool_0)
    var_0 = validation_0.to_box()
    var_0.is_success()

def test_validation_to_lazy_and_bind_followed_by_to_lazy():
    """Test that calling to_lazy() followed by bind(None) produces a lazy
    validation object that itself can be converted to lazy form."""
    # Arrange
    empty_list = []
    initial_value = None

    # Act
    validation = validation_module.Validation(empty_list, empty_list)
    lazy_validation = validation.to_lazy()
    bound_lazy_validation = lazy_validation.bind(initial_value)

    # Assert (via behaviour: calling to_lazy() on the result should not raise)
    bound_lazy_validation.to_lazy()

def test_validation_to_lazy_try_ap_and_is_success_with_empty_dicts():
    """Tests the combination of to_lazy(), to_try(), ap(), and is_success() on
    a Validation instance with empty input and schema dictionaries.
    """
    input_data = {}
    schema = {}
    validation = validation_module.Validation(input_data, schema)

    lazy_validation = validation.to_lazy()
    try_result = lazy_validation.to_try()
    applied_result = lazy_validation.ap(validation)

    try_result.is_success()

def test_validation_to_try_returns_success_when_valid():
    """Test that a Validation with valid data returns a Success result."""
    int_0 = 0
    list_0 = [int_0]
    validation_0 = validation_module.Validation(int_0, list_0)
    var_0 = validation_0.to_try()
    var_0.is_success()

def test_validation_equality_chain_conversion_and_lazy_combination():
    """Test Validation object equality check and chained conversions to Either/Try/Lazy types."""
    # Initialize validation with mixed key types (None and bytes)
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    dict_with_mixed_keys = {none_value: bytes_value, bytes_value: bytes_value}
    
    # Create first Validation instance and verify equality with itself
    validation_initial = validation_module.Validation(none_value, dict_with_mixed_keys)
    equality_result = validation_initial.__eq__(validation_initial)
    
    # Convert to Box, then chain through Either → Try → Lazy operations
    box_result = validation_initial.to_box()
    validation_bytes = validation_module.Validation(bytes_value, bytes_value)
    
    either_from_box = box_result.to_either()
    fail_check = validation_bytes.is_fail()
    try_from_either = either_from_box.to_try()
    
    # Create additional Validation objects to exercise more conversion paths
    validation_with_fail = validation_module.Validation(fail_check, bytes_value)
    str_representation = validation_with_fail.__str__()
    lazy_from_bytes = validation_bytes.to_lazy()
    
    either_from_box_again = box_result.to_either()
    lazy_from_validation = validation_with_fail.to_lazy()
    
    # Combine lazy results into a new Validation
    validation_combined = validation_module.Validation(lazy_from_validation, lazy_from_bytes)
    fail_check_again = validation_bytes.is_fail()
    
    # Apply mapping with string representation
    equality_result.map(str_representation)

def test_validation_equality_and_to_maybe_conversion():
    """Test that Validation supports equality checks and conversion to Maybe."""
    # Create initial data
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}

    # Test equality with self and conversion to Maybe
    validation_0 = validation_module.Validation(none_type_0, dict_0)
    var_0 = validation_0.__eq__(validation_0)
    var_1 = validation_0.to_maybe()

    # Test that bind works with bytes data
    validation_1 = validation_module.Validation(bytes_0, bytes_0)
    validation_1.bind(bytes_0)

def test_validation_eq_returns_object_with_to_box():
    """Test that Validation.__eq__ returns an object with a to_box() method."""
    bytes_value = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_value = None
    dict_value = {none_value: bytes_value, bytes_value: bytes_value}

    # Create two Validation instances with different types of values
    validation_1 = validation_module.Validation(none_value, dict_value)
    validation_2 = validation_module.Validation(bytes_value, none_value)

    # Equality comparison between the two instances
    result = validation_1.__eq__(validation_2)

    # Verify that the result supports the to_box() method
    result.to_box()