import maybe as module_0
import typing as module_1

def test_maybe_class_initialization():
    """
    Test the initialization of the Maybe class.
    """
    # Given
    bytes_data = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # When
    maybe_instance = module_0.Maybe(bytes_data, bytes_data)

    # Then
    assert maybe_instance.value == bytes_data
    assert maybe_instance.default == bytes_data

def test_maybe_class_initialization_2():
    """
    This test case verifies the creation of a Maybe object.
    """
    # Given
    none_value = None

    # When
    maybe = module_0.Maybe(none_value, none_value)

    # Then
    assert maybe.value == none_value
    assert maybe.error == none_value

def test_maybe_class_functionality():
    str_input = "p4xa>bl^oP"
    maybe_obj = module_0.Maybe(str_input, str_input)
    bool_eq = maybe_obj.__eq__(str_input)
    var_ap = maybe_obj.ap(str_input)
    var_get_or_else = maybe_obj.get_or_else(str_input)
    var_map = maybe_obj.map(var_get_or_else)
    var_filter = maybe_obj.filter(var_get_or_else)
    var_map_again = var_map.map(var_get_or_else)
    var_ap_again = maybe_obj.ap(str_input)
    bool_eq_again = var_get_or_else.__eq__(var_ap_again)
    var_filter_again = var_get_or_else.filter(var_get_or_else)
    var_get_or_else_again = var_ap_again.get_or_else(str_input)
    maybe_obj_again = module_0.Maybe(str_input, str_input)
    var_to_validation = maybe_obj_again.to_validation()
    var_bind = maybe_obj_again.bind(var_to_validation)
    var_to_either = var_bind.to_either()

def test_maybe_equality_with_set():
    """
    This test checks the equality of a Maybe object with a set.
    """
    # Given
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    none_type_0 = None
    maybe_0 = module_0.Maybe(none_type_0, none_type_0)

    # When
    bool_1 = maybe_0.__eq__(set_0)

    # Then
    assert bool_1 is False

def test_maybe_bind_and_map_methods():
    """Test the Maybe class bind and map methods"""
    # Given
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)

    # When
    var_0 = maybe_0.bind(bool_0)
    var_1 = var_0.map(bool_0)

    # Then
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    maybe_1 = module_0.Maybe(tuple_0, bool_0)
    set_0 = set()
    set_0.to_box()

def test_maybe_map_method():
    """
    Test the 'map' method of the Maybe class.
    """
    # Given
    none_value = None
    bool_value = False
    maybe_instance = module_0.Maybe(none_value, bool_value)

    # When
    result = maybe_instance.map(bool_value)

    # Then
    assert result is None

def test_maybe_class_initialization_and_binding():
    """
    Test the initialization of the Maybe class and the binding of a dictionary to a Maybe instance.
    """
    # Given
    is_true = True
    is_false = False
    none_type = None
    empty_dict = {}

    # When
    maybe_true = module_0.Maybe(is_true, is_true)
    maybe_false = module_0.Maybe(none_type, is_false)
    maybe_false.bind(empty_dict)

    # Then
    assert maybe_true.value == is_true
    assert maybe_false.value == empty_dict

def test_maybe_class_behavior_2():
    """
    This test case checks the behavior of the Maybe class.
    It tests the methods: to_box, filter, to_lazy, ap, __eq__.
    """
    bytes_0 = b"\x9f\x02Gj\xbbw\xdb\x8b\xe7\xda"
    none_type_0 = None
    maybe_0 = module_0.Maybe(bytes_0, none_type_0)
    var_0 = maybe_0.to_box()
    int_0 = 0
    bool_0 = True
    maybe_1 = module_0.Maybe(int_0, bool_0)
    var_1 = maybe_1.filter(maybe_1)
    var_2 = maybe_1.to_lazy()
    var_3 = var_1.ap(maybe_0)
    var_4 = var_1.filter(var_3)
    maybe_2 = module_0.Maybe(var_2, var_0)
    bool_1 = var_2.__eq__(bool_0)

def test_maybe_ap_method():
    """
    Test the 'ap' method of the Maybe class.
    """
    # Given
    int_value = 2862
    none_type_value = None
    bool_value = False
    maybe_instance = module_0.Maybe(none_type_value, bool_value)

    # When
    maybe_instance.ap(int_value)

    # Then
    # The test case does not assert anything, so no assertions are required here.

def test_maybe_filter_and_map_methods():
    """
    Test the filter and map methods of the Maybe class.
    """
    # Given
    int_0 = 0
    bool_0 = True
    maybe_0 = module_0.Maybe(int_0, bool_0)

    # When
    var_0 = maybe_0.filter(maybe_0)
    var_1 = maybe_0.to_lazy()
    var_2 = var_0.to_lazy()
    var_3 = var_0.filter(var_2)
    var_4 = var_3.to_try()
    var_5 = maybe_0.to_lazy()
    var_6 = var_0.map(var_0)

    # Then
    assert var_0 == var_1
    assert var_2 == var_3
    assert var_4.is_success()
    assert var_5 == var_0
    assert var_6 == var_0

def test_maybe_filter_and_to_lazy():
    # Given
    int_0 = -283
    tuple_0 = (int_0, int_0, int_0)
    none_type_0 = None
    bool_0 = True
    maybe_0 = module_0.Maybe(none_type_0, bool_0)

    # When
    var_0 = maybe_0.filter(tuple_0)
    var_1 = var_0.to_lazy()

    # Then
    none_type_1 = None
    maybe_1 = module_0.Maybe(none_type_1, none_type_1)
    maybe_1.filter(var_1)

def test_maybe_get_or_else_and_filter():
    """
    This test case tests the get_or_else and filter methods of the Maybe class.
    """
    # Given
    default_value = 2281
    string_value = "gZ(\\mOcN"
    dict_value = {string_value: string_value}
    tuple_value = (string_value, string_value, dict_value, dict_value)
    bool_value = True
    maybe_instance = module_0.Maybe(tuple_value, bool_value)

    # When
    result = maybe_instance.get_or_else(default_value)

    # Then
    generic_instance = module_1.Generic()
    bool_value = False
    box_instance = maybe_instance.to_box()
    maybe_instance = module_0.Maybe(generic_instance, bool_value)
    maybe_instance.filter(result)

def test_maybe_class_and_methods():
    """
    Test the Maybe class and its methods.
    """
    # Given
    bool_0 = True
    none_type_0 = None
    maybe_0 = module_0.Maybe(bool_0, none_type_0)

    # When
    var_0 = maybe_0.to_validation()

    # Then
    float_0 = -286.64
    int_0 = -1784
    tuple_0 = ()
    maybe_1 = module_0.Maybe(int_0, tuple_0)

    # When
    var_1 = maybe_1.to_validation()

    # Then
    var_2 = maybe_1.get_or_else(int_0)

    # When
    var_3 = maybe_1.to_try()

    # Then
    maybe_2 = module_0.Maybe(float_0, float_0)

    # When
    maybe_1.bind(var_3)

def test_maybe_map_and_to_either():
    """Test the Maybe.map and Maybe.to_either methods."""

    # Create a Maybe object with None and True
    none_type = None
    bool_true = True
    maybe_none_true = module_0.Maybe(none_type, bool_true)

    # Create a set with a single element
    set_bool_true = {bool_true}

    # Apply the map method to the set
    var_map = maybe_none_true.map(set_bool_true)

    # Create a Maybe object with -1095 and True
    int_negative = -1095
    bool_true = True
    maybe_int_true = module_0.Maybe(int_negative, bool_true)

    # Convert the Maybe object to an Either object
    var_either = maybe_int_true.to_either()

    # Assert the expected values
    assert var_map == {bool_true}
    assert var_either.is_right()

def test_maybe_to_lazy_and_to_either():
    """
    Test the Maybe class methods to_lazy and to_either.
    """
    # Given
    none_type_0 = None
    maybe_0 = module_0.Maybe(none_type_0, none_type_0)  # Maybe instance with None values
    tuple_0 = (maybe_0,)
    var_0 = maybe_0.to_lazy()  # Lazy instance from Maybe instance
    bool_0 = False
    maybe_1 = module_0.Maybe(tuple_0, bool_0)  # Maybe instance with tuple and bool values
    var_1 = maybe_0.to_either()  # Either instance from Maybe instance
    var_2 = maybe_1.to_try()  # Try instance from Maybe instance
    var_3 = maybe_0.to_either()  # Either instance from Maybe instance
    var_4 = maybe_1.to_either()  # Either instance from Maybe instance
    var_2.to_lazy()  # Lazy instance from Try instance

def test_maybe_to_try_to_box():
    """Test the Maybe class to_try and to_box methods."""
    # Given
    bool_0 = True
    bool_1 = False
    maybe_0 = module_0.Maybe(bool_0, bool_1)

    # When
    var_0 = maybe_0.to_try()
    var_0.to_box()

    # Then
    # The test assertions would remain the same

def test_maybe_class_behavior_2():
    """
    This test case verifies the behavior of the Maybe class.
    """
    # Given
    bytes_0 = b"C\xcf\xe7/"
    none_type_0 = None
    bool_0 = True
    maybe_0 = module_0.Maybe(none_type_0, bool_0)  # Maybe instance
    var_0 = maybe_0.ap(none_type_0)  # Maybe instance
    var_1 = var_0.to_lazy()  # Lazy instance
    var_2 = var_1.to_validation()  # Validation instance
    var_3 = maybe_0.filter(var_2)  # Maybe instance
    var_4 = var_3.get_or_else(var_3)  # Maybe instance
    var_5 = var_3.to_either()  # Either instance
    var_6 = var_2.to_try()  # Try instance
    bool_1 = var_3.__eq__(var_0)  # Boolean
    var_7 = var_4.to_box()  # Box instance
    var_6.ap(bytes_0)  # Try instance

def test_maybe_class_behavior_2():
    """
    This test case validates the behavior of the Maybe class.
    """
    # Given
    bytes_0 = b"\xdbC\xcf\xe7/"
    none_type_0 = None
    bool_0 = True
    maybe_0 = module_0.Maybe(none_type_0, bool_0)

    # When
    var_0 = maybe_0.ap(none_type_0)
    var_1 = var_0.ap(bytes_0)
    var_2 = var_1.to_validation()
    maybe_1 = module_0.Maybe(none_type_0, bytes_0)
    var_3 = maybe_1.get_or_else(maybe_1)
    var_4 = maybe_1.to_validation()
    var_5 = maybe_1.bind(var_4)
    var_6 = maybe_1.to_either()
    var_7 = maybe_1.ap(maybe_1)
    int_0 = -3289
    bool_1 = var_6.__eq__(var_4)
    var_8 = var_6.bind(maybe_1)
    var_9 = maybe_1.to_try()
    bool_2 = maybe_1.__eq__(var_5)
    var_10 = var_5.to_validation()
    var_9.ap(int_0)

def test_maybe_equality_and_conversion():
    """
    Test equality of Maybe objects and conversion to Either, Lazy and Validation.
    """
    # Given
    bool_0 = False
    maybe_0 = module_0.Maybe(bool_0, bool_0)

    # When
    bool_1 = maybe_0.__eq__(bool_0)
    maybe_1 = module_0.Maybe(bool_0, bool_0)
    var_0 = maybe_1.to_either()
    var_1 = maybe_1.to_lazy()
    var_2 = var_1.to_validation()
    maybe_2 = module_0.Maybe(bool_0, bool_0)

    # Then
    maybe_2.map(var_2)

def test_maybe_equality_and_conversion_2():
    """Test equality of Maybe instances and conversion to Try and Validation."""
    # Given
    bool_0 = False
    maybe_0 = module_0.Maybe(bool_0, bool_0)

    # When
    bool_1 = maybe_0.__eq__(maybe_0)
    var_0 = maybe_0.to_try()
    var_0.to_validation()

    # Then
    assert bool_1 == True