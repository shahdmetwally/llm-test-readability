import validation as validation_module
import builtins as builtins_module

def test_validation_is_success_and_equality_check_and_is_fail():
    """
    Test the is_success, __eq__, and is_fail methods of the Validation class.
    """
    # Create empty maybe.
    empty_maybe = validation_module.Validation("Create empty maybe.", "Create empty maybe.")

    # Check if the validation is successful.
    is_success = empty_maybe.is_success()

    # Check if the validation is equal to itself.
    is_equal = empty_maybe.__eq__(empty_maybe)

    # Check if the validation is a failure.
    is_fail = empty_maybe.is_fail()

    # Convert the failure to a maybe.
    failure_maybe = is_fail.to_maybe()

    # Assert that the validation is successful, equal to itself, and is a failure.
    assert is_success
    assert is_equal
    assert failure_maybe.is_just()

def test_validation_eq_none_type():
    """
    This test case checks the equality of a Validation object with None.
    """
    # Given
    none_type_value = None
    int_value_1 = -6891
    int_value_2 = 3125
    tuple_value = (int_value_2,)
    validation = validation_module.Validation(int_value_1, tuple_value)

    # When
    result = validation.__eq__(none_type_value)

    # Then
    assert result.is_success()

def test_validation_str_is_fail():
    """
    Test that the __str__ method of the Validation class returns a string
    and the is_fail method returns a boolean.
    """
    # Given
    empty_dict = {}
    validation = validation_module.Validation(empty_dict, empty_dict)

    # When
    validation_str = validation.__str__()

    # Then
    assert isinstance(validation_str, str)
    assert isinstance(validation.is_fail(), bool)

def test_validation_to_either_and_to_maybe():
    """
    Test that the Validation class's to_either and to_maybe methods
    return the expected values.
    """
    # Initialize an empty set
    empty_set = set()

    # Create an instance of the Validation class
    validation = validation_module.Validation(empty_set, empty_set)

    # Call the to_either method and store the result
    either_result = validation.to_either()

    # Call the to_maybe method and store the result
    maybe_result = validation.to_maybe()

    # Call the to_maybe method again on the maybe_result
    maybe_result.to_maybe()

def test_validation_to_either_equality_and_failure_check():
    """
    Test the behavior of the Validation class.
    """
    # Given
    str_0 = "\n        Create empty maybe.\n\n        :returns: Maybe[None]\n        "
    validation_0 = validation_module.Validation(str_0, str_0)

    # When
    var_0 = validation_0.to_either()
    var_1 = validation_0.__eq__(validation_0)
    var_2 = validation_0.is_fail()

    # Then
    var_2.to_maybe()

    # Assert
    assert var_0 == builtins_module.Either.Right(None)
    assert var_1 is True
    assert var_2 is False

def test_set_to_maybe_conversion():
    """
    Test that the to_maybe() method correctly converts a set to a Maybe object.
    """
    # Initialize an empty set and a Validation object with the set
    empty_set = set()
    validation = validation_module.Validation(empty_set, empty_set)

    # Convert the Validation object to a Maybe object
    maybe_obj = validation.to_maybe()

    # Assert that the Maybe object is not None
    assert maybe_obj is not None, "Expected Maybe object, got None"

    # Convert the Maybe object to another Maybe object
    another_maybe_obj = maybe_obj.to_maybe()

    # Assert that the second Maybe object is not None
    assert another_maybe_obj is not None, "Expected Maybe object, got None"

def test_validation_module_initialization():
    """
    Test that the Validation class is correctly initialized with None values.
    """
    # Given
    none_type_value = None

    # When
    validation = validation_module.Validation(none_type_value, none_type_value)

    # Then
    assert validation.none_type_0 is None
    assert validation.none_type_1 is None

def test_validation_to_maybe():
    """
    Test that the `to_maybe` method of the Validation class correctly converts a value to a Maybe type.
    """
    # Given
    none_type_value = None
    validation = validation_module.Validation(none_type_value, none_type_value)

    # When
    validation.to_maybe()

    # Then
    assert validation.is_maybe()

def test_validation_is_fail_and_not_none():
    """
    Test that the is_fail() method of the Validation class returns False
    when the object is not None.
    """

    # Create an object
    obj = builtins_module.object()

    # Create a validation object with the object
    validation = validation_module.Validation(obj, obj)

    # Check that is_fail() returns False
    assert not validation.is_fail()

def test_validation_map_method():
    """
    This test case validates the map method of the Validation class.
    It checks if the map method correctly maps the given value to the validation object.
    """

    # Given
    none_type_value = None
    int_value = -895
    bool_value = True
    tuple_value = (int_value, bool_value)
    dict_value = {tuple_value: tuple_value}
    tuple_values = (dict_value, dict_value, int_value)
    validation_object = validation_module.Validation(tuple_values, bool_value)

    # When
    validation_object.map(none_type_value)

    # Then
    assert validation_object.map(none_type_value) == none_type_value

def test_validation_bind_none():
    """
    Test that the bind method of the Validation class correctly handles None input.
    """

    # Given
    bytes_input = b"s\x8flul\xd1p\x86\xe0<q\xd9\xb2\xf6\x17EC\xaf\xd0"
    validation = validation_module.Validation(bytes_input, bytes_input)
    none_type_input = None

    # When
    validation.bind(none_type_input)

    # Then
    assert validation.bind(none_type_input) is None

def test_validation_ap_method():
    """
    This test checks the functionality of the ap method in the Validation class.
    It verifies that the ap method correctly appends a list to an existing list.
    """

    # Given
    is_valid = False
    validation_list = [True, True, True, True]
    validation = validation_module.Validation(is_valid, validation_list)

    # When
    new_list = [True, False, True, False]
    validation.ap(new_list)

    # Then
    assert validation.validation_list == [True, True, True, True, True, False, True, False]

def test_box_is_success_method():
    # Given
    bool_value = True
    validation = validation_module.Validation(bool_value, bool_value)
    box = validation.to_box()

    # When
    result = box.is_success()

    # Then
    assert result is True

def test_lazy_validation_bind_and_to_lazy():
    """
    This test case verifies the behavior of the `to_lazy` and `bind` methods of the `Validation` class.
    """
    # Given
    none_type_value = None
    empty_list = []
    validation = validation_module.Validation(empty_list, empty_list)

    # When
    lazy_validation = validation.to_lazy()
    bound_validation = lazy_validation.bind(none_type_value)

    # Then
    bound_validation.to_lazy()

def test_validation_to_lazy_to_try_is_success():
    """
    Test the behaviour of Validation class's to_lazy, to_try and is_success methods.
    """
    # Initialize an empty dictionary
    empty_dict = {}

    # Create an instance of Validation with empty dictionaries
    validation = validation_module.Validation(empty_dict, empty_dict)

    # Use the to_lazy method to get a lazy version of the validation
    lazy_validation = validation.to_lazy()

    # Use the to_try method to get a Try version of the lazy validation
    try_validation = lazy_validation.to_try()

    # Use the ap method to apply the validation to the lazy validation
    applied_validation = lazy_validation.ap(validation)

    # Assert that the is_success method returns True
    assert try_validation.is_success(), "Expected is_success to return True"

def test_validation_success_on_successful_validation():
    """
    Test that the validation is successful when the validation is successful.
    """
    # Given
    int_0 = 0
    list_0 = [int_0]
    validation_0 = validation_module.Validation(int_0, list_0)

    # When
    var_0 = validation_0.to_try()

    # Then
    assert var_0.is_success()

def test_validation_class_behavior():
    """
    This test case validates the behavior of the Validation class.
    It covers various methods of the class like __eq__, to_box, to_either, is_fail, to_try, __str__, to_lazy.
    """

    # Given
    bytes_0 = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type_0 = None
    dict_0 = {none_type_0: bytes_0, bytes_0: bytes_0}
    validation_0 = validation_module.Validation(none_type_0, dict_0)

    # When
    var_0 = validation_0.__eq__(validation_0)  # check if validation_0 is equal to itself
    var_1 = validation_0.to_box()  # convert validation_0 to a box
    validation_1 = validation_module.Validation(bytes_0, bytes_0)  # create a new validation object
    var_2 = var_1.to_either()  # convert var_1 to an either
    var_3 = validation_1.is_fail()  # check if validation_1 is a fail
    var_4 = var_2.to_try()  # convert var_2 to a try
    validation_2 = validation_module.Validation(var_3, bytes_0)  # create a new validation object
    var_5 = validation_2.__str__()  # convert validation_2 to a string
    var_6 = validation_1.to_lazy()  # convert validation_1 to a lazy
    validation_3 = validation_module.Validation(bytes_0, bytes_0)  # create a new validation object
    var_7 = var_1.to_either()  # convert var_1 to an either
    var_8 = validation_2.to_lazy()  # convert validation_2 to a lazy
    validation_4 = validation_module.Validation(var_8, validation_3)  # create a new validation object
    var_9 = validation_1.is_fail()  # check if validation_1 is a fail

    # Then
    var_0.map(var_5)  # map var_5 to var_0

def test_validation_class_equality_and_to_maybe_method_v2():
    """
    This test case validates the equality of two instances of the Validation class
    and checks the to_maybe method.
    """

    # Define test data
    bytes_data = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type = None
    dict_data = {none_type: bytes_data, bytes_data: bytes_data}

    # Create instances of Validation class
    validation_0 = validation_module.Validation(none_type, dict_data)
    validation_1 = validation_module.Validation(bytes_data, dict_data)

    # Test equality of validation_0 and validation_0
    assert validation_0.__eq__(validation_0)

    # Test to_maybe method of validation_0
    var_1 = validation_0.to_maybe()

    # Test bind method of validation_1
    validation_1.bind(bytes_data)

def test_validation_equality_with_none_and_bytes():
    """
    Test the equality of two Validation instances.
    """
    # Given
    bytes_data = b"\xcc\xf7\x0e\x04\xc8Y\xc1 N\xbb\xa6\x85\x97\x90\x9e"
    none_type = None
    dict_data = {none_type: bytes_data, bytes_data: bytes_data}
    validation_0 = validation_module.Validation(none_type, dict_data)
    validation_1 = validation_module.Validation(bytes_data, none_type)

    # When
    result = validation_0.__eq__(validation_1)

    # Then
    result.to_box()