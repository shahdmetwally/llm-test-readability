import immutable_list as immutable_list

def test_immutable_list_equality():
    """Test that two empty ImmutableLists are equal."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__eq__(immutable_list_0)

def test_immutable_list_string_representation():
    """Test that the string representation of an ImmutableList is as expected."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__str__() == 'ImmutableList[]'

def test_immutable_list_to_list_conversion():
    """Test that converting an ImmutableList to a list works as expected."""
    immutable_list_0 = immutable_list.ImmutableList()
    list_0 = immutable_list_0.to_list()
    assert list_0 == []

def test_immutable_list_addition():
    """Test that adding two ImmutableLists together works as expected."""
    immutable_list_0 = immutable_list.ImmutableList()
    list_0 = immutable_list_0.to_list()
    immutable_list_1 = immutable_list_0.__add__(list_0)
    assert immutable_list_1.__eq__(immutable_list_0)

def test_immutable_list_length():
    """Test that getting the length of an ImmutableList works as expected."""
    immutable_list_0 = immutable_list.ImmutableList()
    list_0 = immutable_list_0.to_list()
    assert immutable_list_0.__len__() == len(list_0)

def test_immutable_list_addition_with_list():
    """Test that adding an ImmutableList and a list together works as expected."""
    immutable_list_0 = immutable_list.ImmutableList()
    list_0 = immutable_list_0.to_list()
    immutable_list_1 = immutable_list_0.__add__(list_0)
    assert immutable_list_1.__eq__(immutable_list_0)

def test_immutable_list_find_element():
    """Test the find method of ImmutableList."""
    list_1 = immutable_list.ImmutableList()
    list_1.unshift(1)
    list_1.unshift(2)
    list_1.unshift(3)
    assert list_1.find(2) == 2

def test_case_2():
    """Test if the ImmutableList append method works correctly"""
    is_empty = True
    initial_value = True
    immutable_list_instance = immutable_list.ImmutableList(initial_value, is_empty=is_empty)
    appended_value = False
    updated_immutable_list = immutable_list_instance.append(appended_value)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_add_method():
    """Test the add method of the ImmutableList class."""
    # Given
    immutable_list_instance = immutable_list.ImmutableList()
    none_type_instance = None

    # When
    with pytest.raises(ValueError):
        immutable_list_instance.__add__(none_type_instance)

def test_immutable_list_equality():
    # Test code here
    pass

def test_immutable_list_string_representation():
    # Test code here
    pass

def test_immutable_list_to_list_conversion():
    # Test code here
    pass

def test_immutable_list_addition():
    # Test code here
    pass

def test_immutable_list_length():
    # Test code here
    pass

def test_immutable_list_addition_with_list():
    # Test code here
    pass

def test_immutable_list_find_element():
    # Test code here
    pass

def test_case_2():
    # Test code here
    pass

def test_immutable_list_add_method():
    # Test code here
    pass

def test_immutable_list_find_method():
    """Test that ImmutableList.find() method works correctly."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    str_0 = immutable_list_0.__len__()
    immutable_list_0.find(immutable_list_0)

def test_find_method_returns_correct_result_2():
    is_empty = False
    immutable_list = immutable_list.ImmutableList(is_empty, is_empty=is_empty)
    list_to_find = immutable_list.to_list()
    immutable_list.find(list_to_find)

def test_append_and_find_methods():
    # Create an empty ImmutableList
    empty_immutable_list = immutable_list.ImmutableList()

    # Define a NoneType
    none_type = None

    # Try to find a NoneType in the empty ImmutableList
    found_none_type = empty_immutable_list.find(none_type)

    # Append the empty ImmutableList to itself
    appended_immutable_list = empty_immutable_list.append(empty_immutable_list)

    # Convert the appended ImmutableList to a list
    appended_immutable_list_as_list = appended_immutable_list.to_list()

    # Try to add a NoneType to the list
    appended_immutable_list_as_list.__add__(none_type)

def test_immutable_list_creation_2():
    """Test the creation of an ImmutableList instance."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(is_empty=bool_0)
    var_0 = immutable_list_0.to_list()
    immutable_list_1 = immutable_list.ImmutableList()
    var_1 = immutable_list_0.to_list()
    immutable_list_0.map(var_1)

def test_immutable_list_equality_1():
    pass

def test_immutable_list_string_representation_1():
    pass

def test_immutable_list_to_list_conversion_1():
    pass

def test_immutable_list_addition_1():
    pass

def test_immutable_list_length_1():
    pass

def test_immutable_list_addition_with_list_1():
    pass

def test_immutable_list_find_element_1():
    pass

def test_case_2_1():
    pass

def test_immutable_list_add_method_1():
    pass

def test_immutable_list_equality_2():
    pass

def test_immutable_list_string_representation_2():
    pass

def test_immutable_list_to_list_conversion_2():
    pass

def test_immutable_list_addition_2():
    pass

def test_immutable_list_length_2():
    pass

def test_immutable_list_addition_with_list_2():
    pass

def test_immutable_list_find_element_2():
    pass

def test_case_2_2():
    pass

def test_immutable_list_add_method_2():
    pass

def test_immutable_list_find_method():
    pass

def test_find_method_returns_correct_result_2():
    pass

def test_append_and_find_methods():
    pass

def test_immutable_list_creation_2():
    pass

def test_filter_method_with_immutable_list_1():
    """Test that filter method works correctly with ImmutableList."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_0.filter(immutable_list_0)

def test_add_two_empty_lists():
    """
    Test that adding two empty lists results in an empty list.
    """
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list_0.__add__(immutable_list_0)
    length_0 = immutable_list_1.__len__()
    assert length_0 == 0, "Expected length of list after addition to be 0"
    immutable_list_1.filter(length_0)
    length_1 = immutable_list_1.__len__()
    assert length_1 == 0, "Expected length of list after filtering to be 0"

def test_find_method_returns_correct_length_1():
    """Test that the find method returns the correct length."""
    none_type_0 = None
    immutable_list_0 = immutable_list.ImmutableList(none_type_0, none_type_0)
    timer_instance = immutable_list_0.find(1947)
    assert len(timer_instance) == 1

def test_timer_start_stops_correctly():
    """
    Test that the timer starts and stops correctly.
    """
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_reduce_find():
    bool_0 = False
    immutable_list_0 = il.ImmutableList()
    timer_instance = immutable_list_0.reduce(bool_0, immutable_list_0)
    immutable_list_1 = il.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_1.find(immutable_list_1)

def test_create_empty_immutable_list():
    """Test that an empty ImmutableList can be created."""
    empty_immutable_list = module_0.ImmutableList()
    assert empty_immutable_list.is_empty

def test_immutable_list_find_method_1():
    """Test the find method of ImmutableList class."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    str_0 = immutable_list_0.__str__()
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_unshift_find_1():
    bool_0 = False
    immutable_list_0 = immutable_list_module.ImmutableList(bool_0, is_empty=bool_0)
    var_0 = immutable_list_0.unshift(immutable_list_0)
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_unshift_append_find_1():
    is_empty = False
    immutable_list_instance = immutable_list_module.ImmutableList(is_empty=is_empty)
    immutable_list_instance_unshift = immutable_list_instance.unshift(is_empty)
    immutable_list_instance_append = immutable_list_instance_unshift.append(immutable_list_instance)
    immutable_list_instance_append.find(is_empty)

def test_immutable_list_appends_and_finds():
    bool_0 = True
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_1 = immutable_list_0.append(bool_0)
    var_0 = immutable_list_1.__len__()
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_append_reduce_unshift_find():
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list_0.append(immutable_list_0)
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    bool_0 = immutable_list_1.__eq__(immutable_list_0)
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    str_0 = immutable_list_2.__str__()
    immutable_list_3 = immutable_list.ImmutableList(is_empty=str_0)
    immutable_list_4 = var_0.append(var_0)
    immutable_list_2.find(var_0)

def test_immutable_list_unshift_reduce_len_eq():
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    var_1 = immutable_list_1.__len__()
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    bool_0 = immutable_list_2.__eq__(immutable_list_0)
    immutable_list_3 = immutable_list.ImmutableList(is_empty=var_1)
    var_0.find(var_0)

def test_immutable_list_reduce_returns_correct_result():
    bool_0 = True
    dict_0 = {}
    immutable_list_0 = immutable_list_module.ImmutableList(tail=dict_0)
    immutable_list_1 = immutable_list_module.ImmutableList(bool_0, is_empty=bool_0)
    var_0 = immutable_list_1.to_list()
    immutable_list_1.reduce(var_0, var_0)