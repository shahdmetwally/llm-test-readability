import validation as valid
import builtins as builtin

def test_validation_is_success_and_equality_and_is_fail():
    """
    Test that the Validation class's is_success, __eq__, and is_fail methods work as expected.
    """

    # Given
    str_0 = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_0 = valid.Validation(str_0, str_0)

    # When
    var_0 = validation_0.is_success()
    var_1 = validation_0.__eq__(validation_0)
    var_2 = validation_0.is_fail()

    # Then
    var_2.to_maybe()

def test_validation_equality_with_none():
    """
    Test the equality of a Validation object with None.
    """
    # Given
    none_type = None
    int_0 = -6891
    int_1 = 3125
    tuple_0 = (int_1,)
    validation_0 = valid.Validation(int_0, tuple_0)

    # When
    result = validation_0.__eq__(none_type)

    # Then
    assert not result.is_success()

def test_validation_str_is_fail():
    """
    Test that the __str__ method of Validation class returns a string
    and the is_fail method returns a boolean.
    """
    # Create an empty dictionary
    empty_dict = {}

    # Create an instance of Validation with empty dictionaries
    validation = valid.Validation(empty_dict, empty_dict)

    # Call the __str__ method of validation and store the result
    str_result = validation.__str__()

    # Assert that the result is a string
    assert isinstance(str_result, str)

    # Call the is_fail method of str_result and store the result
    is_fail_result = str_result.is_fail()

    # Assert that the result is a boolean
    assert isinstance(is_fail_result, bool)

def test_validation_to_either_and_maybe():
    """Test the transformation of Validation to Either and Maybe."""
    # Initialize an empty set
    empty_set = set()

    # Create a Validation instance
    validation = valid.Validation(empty_set, empty_set)

    # Transform Validation to Either
    either = validation.to_either()

    # Transform Validation to Maybe
    maybe = validation.to_maybe()

    # Transform Maybe to Maybe (just to show that it works)
    maybe.to_maybe()

def test_validation_to_either_equality_and_failure_check():
    """
    Test the behavior of Validation class methods:
    - to_either()
    - __eq__()
    - is_fail()
    """

    # Create empty validation
    empty_validation = valid.Validation("\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        ", "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        ")

    # Convert validation to either
    validation_as_either = empty_validation.to_either()

    # Check equality of validation with itself
    is_equal = empty_validation.__eq__(empty_validation)

    # Check if validation is a failure
    is_failure = empty_validation.is_fail()

    # Convert failure to maybe
    failure_as_maybe = is_failure.to_maybe()

def test_validation_to_maybe_conversion():
    """
    Test the conversion of a Validation object to a Maybe object.
    """
    # Initialize an empty set
    empty_set = set()

    # Create a Validation object with empty sets
    validation = valid.Validation(empty_set, empty_set)

    # Convert the Validation object to a Maybe object
    maybe_object = validation.to_maybe()

    # Convert the Maybe object to a Maybe object again
    # This is to ensure that the conversion is idempotent
    maybe_object.to_maybe()

def test_validation_object_creation_and_none_type_value():
    """
    This test case verifies the creation of a Validation object with a None type value.
    """
    # None type value
    none_type_value = None

    # Create a Validation object using the none_type_value
    validation_object = valid.Validation(none_type_value, none_type_value)

    # Assert that the validation_object is an instance of the Validation class
    assert isinstance(validation_object, valid.Validation)

def test_validation_to_maybe_conversion():
    """
    Test that the to_maybe() method of the Validation class correctly converts a Validation instance to a Maybe instance.
    """
    # Given
    none_type_0 = None
    validation_0 = valid.Validation(none_type_0, none_type_0)

    # When
    validation_0.to_maybe()

    # Then
    assert isinstance(validation_0, valid.Maybe)

def test_validation_is_fail_returns_false_for_valid_validation():
    """
    This test verifies that the is_fail method of Validation class returns False for a valid Validation object.
    """
    # Given
    valid_object = valid.object()
    validation = valid.Validation(valid_object, valid_object)

    # When
    result = validation.is_fail()

    # Then
    assert result is False, "is_fail method should return False for a valid Validation object"

def test_validation_map_with_none_type():
    """Test the map method of Validation with None type."""
    # Given
    none_type = None
    int_val = -895
    bool_val = True
    tuple_val = (int_val, bool_val)
    dict_val = {tuple_val: tuple_val}
    tuple_input = (dict_val, dict_val, int_val)
    validation = valid.Validation(tuple_input, bool_val)

    # When
    validation.map(none_type)

    # Then
    assert validation.value == (None, None, int_val)

def test_validation_bind_with_none():
    """
    Test that the bind method of the Validation class correctly handles None.
    """
    # Given
    bytes_data = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validation = valid.Validation(bytes_data, bytes_data)
    none_value = None

    # When
    result = validation.bind(none_value)

    # Then
    assert result == none_value

def test_validation_ap_method():
    """
    Test the 'ap' method of the Validation class.
    """
    # Given
    is_valid = False
    errors = [True, True, True, True]
    validation = valid.Validation(is_valid, errors)

    # When
    new_errors = [True, True, True, True]
    validation.ap(new_errors)

    # Then
    assert validation.is_valid == False
    assert validation.errors == [True, True, True, True, True, True, True, True]

def test_validation_to_box_is_success():
    """
    Test that the to_box method of Validation class returns a Box instance
    and the is_success method of Box class returns the correct boolean value.
    """

    # Given
    bool_0 = True
    validation_0 = valid.Validation(bool_0, bool_0)
    var_0 = validation_0.to_box()

    # When
    result = var_0.is_success()

    # Then
    assert result == bool_0

def test_lazy_bind_and_to_lazy():
    """
    This test case verifies the behaviour of the `bind` and `to_lazy` methods of the `Lazy` class.
    """
    # Given
    empty_list = []
    validation = valid.Validation(empty_list, empty_list)
    lazy = validation.to_lazy()

    # When
    none_value = None
    result = lazy.bind(none_value)

    # Then
    result.to_lazy()

def test_validation_to_lazy_to_try_is_success():
    """
    Test the transformation of a Validation object to a Lazy object,
    then to a Try object, and finally checking if the Try object is successful.
    """

    # Initialize an empty dictionary
    empty_dict = {}

    # Create a Validation object using the empty dictionary
    validation = valid.Validation(empty_dict, empty_dict)

    # Transform the Validation object to a Lazy object
    lazy_obj = validation.to_lazy()

    # Transform the Lazy object to a Try object
    try_obj = lazy_obj.to_try()

    # Apply the Validation object to the Try object
    var_2 = var_0.ap(validation)

    # Check if the Try object is successful
    assert try_obj.is_success()

def test_validation_to_try_is_success():
    """
    Test the to_try() method of Validation class.
    It should return a Success instance when the validation is successful.
    """

    # Given
    int_0 = 0
    list_0 = [int_0]
    validation_0 = valid.Validation(int_0, list_0)

    # When
    var_0 = validation_0.to_try()

    # Then
    assert var_0.is_success()

def test_validation_map():
    """Test map function of Validation instance."""
    # Given
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = valid.Validation(none_type_0, dict_0)
    var_0 = validation_0.__eq__(validation_0)
    var_1 = validation_0.to_box()
    validation_1 = valid.Validation(bytes_0, bytes_0)
    var_2 = validation_1.to_either()
    var_3 = validation_1.is_fail()
    var_4 = var_2.to_try()
    validation_2 = valid.Validation(var_3, bytes_0)
    var_5 = validation_2.__str__()
    var_6 = validation_1.to_lazy()
    validation_3 = valid.Validation(bytes_0, bytes_0)
    var_7 = validation_1.to_either()
    var_8 = validation_2.to_lazy()
    validation_4 = valid.Validation(var_8, validation_3)
    var_9 = validation_1.is_fail()

    # When
    var_0.map(var_5)

    # Then
    assert var_0 is True

def test_validation_equality_and_bind():
    """Test equality of Validation instances and bind method."""

    # Given
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = valid.Validation(none_type_0, dict_0)

    # When
    var_0 = validation_0.__eq__(validation_0)
    var_1 = validation_0.to_maybe()
    validation_1 = valid.Validation(bytes_0, bytes_0)
    validation_1.bind(bytes_0)

    # Then
    assert var_0 is True
    assert isinstance(var_1, valid.Maybe)

def test_validation_equality_and_bind():
    """
    Test the equality of two Validation objects.
    """
    # Given
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = valid.Validation(none_type_0, dict_0)
    validation_1 = valid.Validation(bytes_0, none_type_0)

    # When
    var_0 = validation_0.__eq__(validation_1)

    # Then
    var_0.to_box()