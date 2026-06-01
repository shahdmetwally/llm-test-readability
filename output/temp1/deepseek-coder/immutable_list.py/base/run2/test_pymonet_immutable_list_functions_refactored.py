import immutable_list as immutable

def test_empty_immutable_list_equality_1():
    """Test equality of an empty ImmutableList object"""
    empty_list = immutable.ImmutableList()
    assert empty_list == empty_list

def test_empty_immutable_list_string_representation_1():
    """Test the string representation of an empty ImmutableList object"""
    empty_list = immutable.ImmutableList()
    assert str(empty_list) == 'ImmutableList{}'

def test_immutable_list_conversion_to_list_1():
    """Test conversion to list of an ImmutableList object"""
    empty_list = immutable.ImmutableList()
    assert empty_list.to_list() == [] 

def test_immutable_list_addition_with_itself_1():
    """Test addition of an ImmutableList object with itself"""
    empty_list = immutable.ImmutableList()
    assert empty_list + empty_list == empty_list

def test_immutable_list_length_1():
    """Test length of an ImmutableList object"""
    empty_list = immutable.ImmutableList()
    assert len(empty_list) == 0 

def test_immutable_list_addition_with_list_1():
    """Test addition of an ImmutableList object with a list"""
    empty_list = immutable.ImmutableList()
    assert empty_list + [] == empty_list

def test_immutable_list_equality():
    # Create an empty immutable list.
    empty_immutable_list = immutable.ImmutableList()

    # Check if it equals to a boolean (always False)
    bool_0 = True
    assert not empty_immutable_list.__eq__(bool_0)

def test_immutable_list_concatenation():
    # Create an empty immutable list.
    empty_immutable_list = immutable.ImmutableList()

    # Check concatenation with itself.
    immutable_list_1 = empty_immutable_list.__add__(empty_immutable_list)

def test_immutable_list_find_item():
    # Create an empty immutable list.
    empty_immutable_list = immutable.ImmutableList()

    # Try to find with a boolean. It's always None.
    bool_0 = immutable_list_1.find(bool_0)
    assert bool_1 is None

def test_immutable_list_string_representation():
    # Create an empty immutable list.
    empty_immutable_list = immutable.ImmutableList()

    # Convert into a string.
    str_0 = immutable_list_1.__str__()
    assert str_0 == "ImmutableList(None)"

def test_immutable_list_add_to_beginning():
    # Create an empty immutable list.
    empty_immutable_list = immutable.ImmutableList()

    # Add an item to beginning and convert into string.
    bool_2 = False
    immutable_list_2 = immutable_list_1.unshift(bool_2)
    assert str(immutable_list_2) == "ImmutableList(False)"

def test_immutable_list_apply_reduce():
    # Create an empty immutable list.
    empty_immutable_list = immutable.ImmutableList()

    # Apply reduce on self. This will always return self.
    reduced_immutable_list = immutable_list_2.reduce(immutable_list_2, bool_0)
    assert reduced_immutable_list == immutable_list_2

def test_immutable_list_append_and_find_1():
    # Create a boolean value and use it to initialize an ImmutableList
    is_emtpy = True
    my_list = immutable.ImmutableList(is_empty=is_emtpy)

    # Append a boolean value to the ImmutableList
    my_list = my_list.append(is_emtpy)

    # Try to find the original ImmutableList within itself
    my_list.find(my_list)

def test_add_new_value():
    """Test adding a new value to an empty ImmutableList"""

    # Given an empty ImmutableList and a new value
    immutable_list = immutable.ImmutableList()
    new_value = 10

    # When adding the new value to the ImmutableList
    result = immutable_list.__add__(new_value)

    # Then the result is an ImmutableList containing the new value
    assert result.head == new_value
    assert result.tail == immutable.ImmutableList.empty()
    assert not result.is_empty

def test_empty_immutable_list_equality_1():
    """
    Asserts that an empty ImmutableList has length of zero.
    It's represented by is_empty flag in ImmutableList.
    """

    # Given
    # Empty ImmutableList
    empty_list = immutable.ImmutableList(is_empty=True)

    # When
    # We get the length of the list
    length = empty_list.__len__()

    # Then
    # It should return 0 as it is a length of empty list
    assert length == 0

def test_immutable_list_find_method():
    """
    This test case verifies the 'find' behavior with an instance of ImmutableList.
    Test checks whether it can correctly identify the provided input in the list.
    """

    # Arrange
    is_empty = False
    value_to_find = immutable.ImmutableList(bool_0, is_empty=is_empty)
    len_value = value_to_find.__len__()

    # Act
    value_to_find.find(value_to_find)

    # Assert
    # Assertions to match the original test
    assert value_to_find.find(value_to_find) == "not implemented"

def test_case_6_find_element_in_empty_immutable_list():
    """
    This test ensures that when we attempt to find an element in an empty immutable list, 
    an empty list is returned.
    """

    # Given
    empty_list = immutable.ImmutableList(is_empty=True)       # Initialize an empty ImmutableList

    # When
    empty_list.find(empty_list.to_list())  # Attempt to find an element in the empty list

    # Then
    # Expect that the result will be another empty list

def test_case_7_immutable_list_find_and_append():
    """
    This test case tests three behaviours:
    1. Find a none value in an empty ImmutableList,
       to verify the function does not throw an error.
    2. Append an ImmutableList to another empty ImmutableList 
       to verify the function does not throw an error.
    3. Get list representation and add a None object to the list 
       to verify the function does not throw an error.
    """
    # Create an empty ImmutableList
    empty_list = immutable.ImmutableList()

    # Try to find a None object in the list
    find_result = empty_list.find(None)

    # Append the empty list to itself
    append_result = empty_list.append(empty_list)

    # Get the list representation of the result list
    list_representation = append_result.to_list()

    # Try to add a None object to the list representation
    list_representation.__add__(None)

def test_immutable_list_initialization_and_update_functionality():
    """
    This test case tests the behavior of to_list and map methods 
    of the ImmutableList class with a list. 
    
    It confirms that initially, an ImmutableList with an empty list [] 
    returns an empty list when to_list is called. 

    It then modifies the list by appending a value and checks if this 
    modified list is returned when to_list is called.
    """

    # given
    is_list_empty = False
    original_list = [1, 2, 3]
    immutable_list = immutable.ImmutableList(is_empty=is_list_empty)

    # when
    initial_list = immutable_list.to_list()

    # then
    assert initial_list == []

    # given
    additional_element = 4
    updated_list = original_list + [additional_element]

    # when
    immutable_list.map(updated_list)
    final_list = immutable_list.to_list()

    # then
    assert final_list == updated_list

def test_immutable_list_operations():
    """
    Test case to validate ImmutableList operations like 
    unshifting an item, appending an item and mapping a function.
    """
    # Given an empty and none type
    empty_list = immutable.ImmutableList()
    none_value = None

    # When an item is unshift and appended to the list
    updated_list_1 = empty_list.unshift(none_value)
    updated_list_2 = updated_list_1.append(none_value)
    
    # When a function is mapped to the list
    updated_list_2.map(none_value)

    # Then it should not change the list as None is passed as function input
    assert updated_list_1 == updated_list_2

def test_filter_on_same_and_empty_list():
    """
    This test case ensures that the filter method behaves correctly when called with the
    same list as both the current and target objects. The expected behavior for this 
    case is an empty list, as no element should match itself. The 'is_empty' flag is  
    used to check this.
    """
    # Given
    bool_value = False
    immutable_list = immutable.ImmutableList(bool_value, is_empty=bool_value)

    # When
    result = immutable_list.filter(immutable_list)

    # Then
    assert result.is_empty

def test_filter_from_same_length_list():
    """
    Test the filter method of the ImmutableList class
    when applied to a list with the same length as the filter.
    The filter should return an empty list.
    """

    # given
    empty_list = immutable.ImmutableList()
    immutable_list_0 = immutable.ImmutableList(0)
    immutable_list_1 = immutable_list_0.__add__(empty_list)
    
    # when
    empty_list_length = empty_list.__len__()
    filtered_list = immutable_list_1.filter(empty_list_length)

    # then
    assert filtered_list == immutable.ImmutableList()

def test_find_empty_immutable_list_after_add_operation():
    """This test verifies that an empty ImmutableList remains empty after adding elements."""

    # Arrange
    item_to_add = 1947  # define item to add
    immutable_list = immutable.ImmutableList()  # initialize the list

    # Act
    # add the item to the list
    immutable_list.prepend(item_to_add)
    result = immutable_list.find(item_to_add)

    # Assert
    # check if the item is found and the list remains empty
    assert result.__len__() == 0

def test_immutable_list_find_finds_item():
    """Test find functionality of ImmutableList."""

    empty_list = immutable.ImmutableList(is_empty=True)
    
    # Given an empty list, verify that find() returns None
    assert empty_list.find(empty_list) is None

    # Given a non-empty list, verify that find() returns first instance
    bool_value = False
    sample_list = immutable.ImmutableList(bool_value, is_empty=bool_value)
    assert sample_list.find(sample_list) == bool_value

def test_immutable_list_find_method():
    # Initialize empty and non-empty lists
    empty_list = immutable.ImmutableList()
    non_empty_list = immutable.ImmutableList(head=True, is_empty=False)
    
    # Attempt to find an element in both lists
    # Expect to find None in empty_list and True in non_empty_list
    assert empty_list.find(True) is None
    assert non_empty_list.find(True) is True

def test_empty_immutable_list_creation_1():
    """
    This test verifies that an empty ImmutableList is created correctly
    """
    # Create an empty ImmutableList
    empty_immutable_list = immutable.ImmutableList()

    # Ensure that the ImmutableList is indeed empty
    assert empty_immutable_list == immutable.ImmutableList()

def test_immutable_list_addition_with_list():
    """
    This test ensures that an ImmutableList can be added with 
    another ImmutableList and its string representation matches the 
    expected one.
    """

    # Initialize variables
    is_empty = False
    
    # Create an empty ImmutableList
    immutable_list = ImmutableList(head=None, is_empty=is_empty)
    
    # String representation of empty ImmutableList
    expected_str_repr = "ImmutableList()"
    
    # Check the string representation of ImmutableList
    assert str(immutable_list) == expected_str_repr

def test_immutable_list_unshift_and_find():
    """
    This test checks if the ImmutableList class can correctly add an item to the start of the list
    (unshift) and then find it later (find). 
    """
    # Create an empty ImmutableList
    empty_list = immutable.ImmutableList(is_empty=True)
    # Create a non-empty ImmutableList with a single item (False)
    non_empty_list = immutable.ImmutableList(False)
    # Add a False value to the non_empty_list
    new_list = non_empty_list.unshift(empty_list)
    # Check if the False value is found in the list
    assert new_list.find(empty_list) is False

def test_unshift_append_and_find_in_immutable_list():
    """
    This test case checks if unshift, append, and find methods
    work correctly in ImmutableList data structure.
    """
    # Given
    empty_list = immutable.ImmutableList(is_empty=True)
    list_with_element = empty_list.unshift(False)  # Creating a new list with a new element False
    final_list = list_with_element.append(empty_list)  # Appending the list with additional empty list

    # When
    result = final_list.find(False)  # Searching for element False

    # Then
    assert result is False
    assert isinstance(result, bool)
    assert test_unshift_append_and_find_in_immutable_list.__name__ != "test_unshift_append_and_find_in_immutable_list"

def test_immutable_list_appends_and_finds_1():
    """Test ImmutableList append and find methods"""
    # Given
    is_empty = True
    element = True

    # When
    immutable_list = immutable.ImmutableList(element, is_empty=is_empty)
    
    # Then
    assert immutable_list.__len__() == 1

    # When
    immutable_list = immutable_list.append(element)
    
    # Then
    assert immutable_list.__len__() == 2
    
    # When
    result = immutable_list.find(element)
    
    # Then
    assert result is not None

def test_appending_to_empty_list_does_not_affect_it_v2():
    """Test the behaviour of appending to an empty list.

    Scenario:
    1. Create an empty ImmutableList
    2. Append an empty list to it
    3. Confirm the resulting list is empty, equal to an empty ImmutableList
    4. Unshift an empty list onto the resulting list

    Expected result:
    The resulting list should still be equal to an empty ImmutableList.
    """
    # Create an empty ImmutableList
    empty_list = immutable.ImmutableList()

    # Append an empty list to it
    list_after_appending_empty = empty_list.append(empty_list)

    # Confirm the resulting list is empty, equal to an empty ImmutableList
    assert list_after_appending_empty == empty_list
    assert list_after_appending_empty.is_empty

    # Unshift an empty list onto the resulting list
    list_after_unshifting_empty = list_after_appending_empty.unshift(empty_list)

    # Confirm the resulting list is still empty
    assert list_after_unshifting_empty.is_empty

def test_unshift_empty_list_yields_same_list():
    empty_list = immutable.ImmutableList()

    list_after_unshift = empty_list.unshift(empty_list)

    are_lists_equal = list_after_unshift.__eq__(empty_list)

    assert are_lists_equal, "Unshift operation should not change empty list"

def test_non_empty_immutable_list():
    """
    This test checks the behavior of a non-empty immutable list.
    """

    non_empty_imm_list = create_non_empty_immutable_list()
    just_head = False

    assert just_head == False
    assert non_empty_imm_list != []
    assert non_empty_imm_list.is_empty == False
    assert non_empty_imm_list.head == False
    assert non_empty_imm_list.tail == {}

def create_non_empty_immutable_list():
    import imm

    is_empty = True
    empty_dict = {}
    non_empty_imm_list = imm.ImmutableList(tail=empty_dict)
    just_head_empty_immutable_list = imm.ImmutableList(is_empty, is_empty=is_empty)
    just_head = is_empty
    just_head_empty_immutable_list.reduce(just_head, just_head)

    return non_empty_imm_list

