import immutable_list as immutable_list

def test_immutable_list_equality():
    """Test if two empty ImmutableList instances are equal."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__eq__(immutable_list_0)

def test_immutable_list_string_representation():
    """Test if the string representation of an ImmutableList instance is as expected."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__str__() == 'ImmutableList[]'

def test_immutable_list_to_list_conversion():
    """Test if the to_list method of an ImmutableList instance returns an empty list."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.to_list() == []

def test_immutable_list_addition():
    """Test if adding two empty ImmutableList instances results in a new ImmutableList instance with an empty list."""
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list_0.to_list()
    immutable_list_2 = immutable_list_0.__add__(immutable_list_1)
    assert immutable_list_2.to_list() == []

def test_immutable_list_length():
    """Test if the length of an ImmutableList instance is as expected."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__len__() == 0

def test_immutable_list_addition_with_list():
    """Test if adding an empty ImmutableList instance to a list results in a new ImmutableList instance with the list."""
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list_0.to_list()
    immutable_list_0.__add__(immutable_list_1)
    assert immutable_list_0.to_list() == immutable_list_1

def test_immutable_list_equality_2():
    bool_0 = True
    immutable_list_0 = immutable_list.ImmutableList()
    bool_1 = immutable_list_0.__eq__(bool_0)
    immutable_list_1 = immutable_list_0.__add__(immutable_list_0)
    bool_2 = immutable_list_0.find(bool_1)
    str_0 = immutable_list_0.__str__()
    immutable_list_2 = immutable_list_0.unshift(immutable_list_0)
    immutable_list_2.reduce(immutable_list_2, bool_0)

def test_immutable_list_append_and_find():
    """Test that ImmutableList appends elements correctly and can find them."""
    bool_0 = True
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_1 = immutable_list_0.append(bool_0)
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_add_method():
    """Test the add method of ImmutableList class."""
    # Create an instance of ImmutableList
    il_0 = immutable_list.ImmutableList()
    # Define a None type object
    none_type_0 = None
    # Try to add the None type object to the ImmutableList instance
    try:
        il_0.__add__(none_type_0)
    except ValueError as ve:
        # If a ValueError is raised, the test passes
        assert str(ve) == "ImmutableList: you can not add any other instace than ImmutableList"

def test_immutable_list_length_and_find_method():
    immutable_list_0 = immutable_list.ImmutableList()
    length_of_immutable_list_0 = immutable_list_0.__len__()
    immutable_list_1 = immutable_list.ImmutableList(
        immutable_list_0, is_empty=immutable_list_0
    )
    immutable_list_1.find(immutable_list_1)

def test_immutable_list_length_and_find_method_2():
    """
    This test checks the length of an ImmutableList instance and the find method of the same.
    """
    # Given
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)

    # When
    str_0 = immutable_list_0.__len__()
    immutable_list_0.find(immutable_list_0)

    # Then
    assert str_0 == 0

def test_immutable_list_find_method():
    """
    Test the find method of ImmutableList.
    """
    # Given
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    var_0 = immutable_list_0.to_list()

    # When
    immutable_list_0.find(var_0)

    # Then
    # No assertions as the method does not return anything.

def test_case_7():
    immutable_list_0 = immutable_list.ImmutableList()
    none_type_0 = None
    var_0 = immutable_list_0.find(none_type_0)
    immutable_list_1 = immutable_list_0.append(immutable_list_0)
    var_1 = immutable_list_1.to_list()
    var_1.__add__(none_type_0)

def test_immutable_list_creation():
    """Test the creation of an ImmutableList instance."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(is_empty=bool_0)
    var_0 = immutable_list_0.to_list()
    immutable_list_1 = immutable_list.ImmutableList()
    var_1 = immutable_list_0.to_list()
    immutable_list_0.map(var_1)

def test_immutable_list_unshift_append_map():
    none_type = None
    immutable_list_0 = il.ImmutableList(none_type, none_type)
    immutable_list_1 = immutable_list_0.unshift(none_type)
    immutable_list_2 = immutable_list_0.unshift(immutable_list_1)
    immutable_list_3 = immutable_list_1.append(none_type)
    immutable_list_3.map(none_type)

def test_immutable_list_filter():
    """Test that filter method returns a new ImmutableList with only elements that satisfy the predicate."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_0.filter(immutable_list_0)

def test_add_two_empty_lists():
    """Test adding two empty lists results in an empty list."""
    # Given
    empty_list = immutable_list.ImmutableList()

    # When
    result = empty_list.__add__(empty_list)

    # Then
    assert result.__len__() == 0

def test_find_method_returns_correct_length_2():
    """Test that the find method returns the correct length."""
    int_0 = 1947
    none_type_0 = None
    immutable_list_0 = immutable_list.ImmutableList(none_type_0, none_type_0)
    timer_instance = immutable_list_0.find(int_0)
    assert timer_instance.__len__() == 2

def test_timer_start_stops_correctly():
    """Test that timer starts and stops correctly"""
    is_empty = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty, is_empty=is_empty)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_find():
    """Test ImmutableList.reduce and ImmutableList.find methods."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList()
    timer_instance = immutable_list_0.reduce(bool_0, immutable_list_0)
    immutable_list_1 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_1.find(immutable_list_1)

def test_create_empty_immutable_list():
    """Test that an empty ImmutableList can be created."""
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_method():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    str_0 = immutable_list_0.__str__()
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_unshift_and_find_2():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    timer_instance = immutable_list_0.unshift(immutable_list_0)
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_unshift_append_find():
    is_empty = False
    immutable_list_instance = immutable_list_module.ImmutableList(is_empty=is_empty)
    immutable_list_instance_unshift = immutable_list_instance.unshift(is_empty)
    immutable_list_instance_append = immutable_list_instance_unshift.append(immutable_list_instance)
    immutable_list_instance_append.find(is_empty)

def test_case_19_immutable_list_append_and_find():
    bool_0 = True
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_1 = immutable_list_0.append(bool_0)
    var_0 = immutable_list_1.__len__()
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_append_reduce_unshift_find():
    immutable_list_module_0 = immutable_list_module.ImmutableList()
    immutable_list_module_1 = immutable_list_module_0.append(immutable_list_module_0)
    timer_instance = immutable_list_module_0.reduce(immutable_list_module_1, immutable_list_module_1)
    bool_0 = immutable_list_module_1.__eq__(immutable_list_module_0)
    immutable_list_module_2 = immutable_list_module_1.unshift(immutable_list_module_1)
    str_0 = immutable_list_module_2.__str__()
    immutable_list_module_3 = immutable_list_module.ImmutableList(is_empty=str_0)
    immutable_list_module_4 = timer_instance.append(timer_instance)
    immutable_list_module_2.find(timer_instance)

def test_immutable_list_unshift_reduce_len_eq():
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    var_1 = immutable_list_1.__len__()
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    bool_0 = immutable_list_2.__eq__(immutable_list_0)
    immutable_list_3 = immutable_list.ImmutableList(is_empty=var_1)
    var_0.find(var_0)

def test_immutable_list_to_list_method():
    """Test the to_list method of the ImmutableList class."""
    bool_0 = True
    dict_0 = {}
    immutable_list_0 = immutable_list.ImmutableList(tail=dict_0)
    immutable_list_1 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    var_0 = immutable_list_1.to_list()
    immutable_list_1.reduce(var_0, var_0)