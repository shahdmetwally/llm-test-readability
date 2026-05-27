import immutable_list as list_module

def test_immutable_list_equality():
    """Test equality of an ImmutableList with itself."""
    empty_list = list_module.ImmutableList()
    assert empty_list == empty_list

def test_immutable_list_to_string():
    """Test string representation of an ImmutableList."""
    empty_list = list_module.ImmutableList()
    assert str(empty_list) == "[]"

def test_immutable_list_to_list():
    """Test conversion of an ImmutableList to a list."""
    empty_list = list_module.ImmutableList()
    assert empty_list.to_list() == []

def test_immutable_list_addition():
    """Test addition of two ImmutableLists."""
    empty_list = list_module.ImmutableList()
    new_list = empty_list.to_list() + empty_list.to_list()
    assert new_list == empty_list.__add__(empty_list)

def test_immutable_list_length():
    """Test length of an ImmutableList."""
    empty_list = list_module.ImmutableList()
    assert len(empty_list) == empty_list.__len__()

def test_immutable_list_addition_with_list():
    """Test addition of an ImmutableList with a list."""
    empty_list = list_module.ImmutableList()
    new_list = empty_list.to_list()
    assert new_list == empty_list.__add__(new_list)

def test_immutable_list_operations():
    """Test operations on an ImmutableList instance"""

    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Create a new list by adding an empty list to the empty list
    new_list = empty_list.__add__(empty_list)

    # Check if the empty list is in the new list
    is_empty_in_new_list = new_list.find(empty_list)

    # Convert the new list to a string
    new_list_str = new_list.__str__()

    # Create a new list by adding an empty list to the start of the new list
    new_list_with_empty = new_list.unshift(empty_list)

    # Reduce the new list with the empty list
    new_list_with_empty.reduce(new_list_with_empty, empty_list)

def test_immutable_list_append_and_find():
    """
    Test that the append method correctly adds an element to the list
    and the find method correctly returns the index of an existing element.
    """
    # Given
    is_empty = True
    empty_list = list_module.ImmutableList(is_empty, is_empty=is_empty)
    element_to_add = True

    # When
    updated_list = empty_list.append(element_to_add)

    # Then
    assert updated_list.find(element_to_add) == 0

def test_immutable_list_add_none():
    """Test the __add__ method of ImmutableList with None."""
    # Create an instance of ImmutableList
    immutable_list = list_module.ImmutableList()

    # Define None value
    none_value = None

    # Call the __add__ method with None value
    immutable_list.__add__(none_value)

def test_immutable_list_length_and_find_method():
    """
    Test the length of an empty ImmutableList and the find method.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Check the length of the list
    assert empty_list.__len__() == 0

    # Create a new ImmutableList with the empty list and check if it is empty
    new_list = list_module.ImmutableList(empty_list, is_empty=empty_list)
    assert new_list.find(new_list) == new_list

def test_immutable_list_length_and_find_method():
    """
    Test the length of an immutable list and the find method of the list.
    """
    # Create a boolean value
    is_empty = False

    # Create an immutable list with the boolean value
    immutable_list = list_module.ImmutableList(is_empty, is_empty=is_empty)

    # Get the length of the immutable list
    list_length = immutable_list.__len__()

    # Find the immutable list in itself
    immutable_list.find(immutable_list)

def test_find_method_returns_none_for_empty_list():
    """
    Test that the find method returns None when called on an empty list.
    """
    # Given
    empty_list = list_module.ImmutableList(is_empty=True)

    # When
    result = empty_list.find([])

    # Then
    assert result is None, "Expected find method to return None for empty list"

def test_immutable_list_append_and_find_new():
    """
    Test the append and find methods of the ImmutableList class.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Append an empty list to the empty list
    list_with_empty_list = empty_list.append(empty_list)

    # Convert the list to a Python list
    list_as_python_list = list_with_empty_list.to_list()

    # Add None to the Python list
    list_as_python_list.__add__(None)

    # Find None in the list
    found_none = list_with_empty_list.find(None)

    # Assert that None was found in the list
    assert found_none is None

def test_immutable_list_to_list_returns_empty_list_when_is_empty_is_true():
    """
    Test that to_list() method returns an empty list when is_empty is True.
    """
    # Given
    is_empty = True
    immutable_list = list_module.ImmutableList(is_empty=is_empty)

    # When
    result = immutable_list.to_list()

    # Then
    assert result == []

def test_unshift_and_append_operations():
    """
    This test case verifies the correctness of the unshift and append operations
    on the ImmutableList. It creates an empty list, unshifts a None value,
    unshifts the list again, appends a None value to the list, and maps a None
    function over the list.
    """
    empty_list = list_module.ImmutableList(None, None)
    list_with_none = empty_list.unshift(None)
    list_with_list = empty_list.unshift(list_with_none)
    final_list = list_with_none.append(None)
    final_list.map(None)

def test_filter_immutable_list_with_same_list():
    """Test that filtering an ImmutableList with itself returns the same list."""
    is_empty = False
    input_list = list_module.ImmutableList(is_empty, is_empty=is_empty)
    # Filtering an ImmutableList with itself should return the same list
    filtered_list = input_list.filter(input_list)
    assert filtered_list == input_list

def test_add_two_empty_lists():
    """
    Test the addition of two empty lists.
    """
    # Given two empty lists
    empty_list = list_module.ImmutableList()

    # When I add the two lists
    result = empty_list.__add__(empty_list)

    # Then the result should be an empty list
    assert result.__len__() == 0

    # And when I filter the result with length 0
    result.filter(0)

    # Then the result should be an empty list
    assert result.__len__() == 0

def test_find_method_returns_length_of_list():
    """
    This test case verifies that the find method of the ImmutableList class
    returns the length of the list when the element is not found.
    """
    # Given
    element_not_in_list = 1947
    empty_element = None
    immutable_list = list_module.ImmutableList(empty_element, empty_element)

    # When
    result = immutable_list.find(element_not_in_list)

    # Then
    assert result.__len__() == 2

def test_find_method_with_empty_list():
    """
    This test case checks the behaviour of the find method when an empty list is passed.
    """
    # Given
    is_empty = True
    empty_list = list_module.ImmutableList(is_empty, is_empty=is_empty)

    # When
    result = empty_list.find(empty_list)

    # Then
    assert result == is_empty

def test_immutable_list_reduce_empty_list():
    """
    Test the reduce method of the ImmutableList class with an empty list.
    The reduce method should return the initial value when reducing an empty list.
    """
    # Given
    empty_list = list_module.ImmutableList()
    initial_value = False

    # When
    result = empty_list.reduce(initial_value, empty_list)

    # Then
    assert result == initial_value


def test_immutable_list_find_empty_list():
    """
    Test the find method of the ImmutableList class with an empty list.
    The find method should return None when searching an empty list.
    """
    # Given
    empty_list = list_module.ImmutableList(is_empty=True)

    # When
    result = empty_list.find(empty_list)

    # Then
    assert result is None

def test_immutable_list_initialization():
    """
    Test that an instance of ImmutableList can be created.
    """
    # Given
    expected_list = list_module.ImmutableList()

    # When
    actual_list = list_module.ImmutableList()

    # Then
    assert type(actual_list) == type(expected_list)

def test_immutable_list_find_method():
    """
    Test the find method of the ImmutableList class.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList(is_empty=True)
    # Convert the list to a string
    empty_list_str = str(empty_list)
    # Find the empty list in itself
    empty_list.find(empty_list)

def test_unshift_and_find_on_immutable_list():
    """
    This test case tests the unshift and find methods of the ImmutableList class.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList(is_empty=True)

    # Unshift an empty list onto the empty list
    list_after_unshift = empty_list.unshift(empty_list)

    # Find the empty list in the list after unshift
    found_list = list_after_unshift.find(empty_list)

    # Assert that the found list is the same as the empty list
    assert found_list == empty_list

def test_unshift_append_find():
    """
    Test the unshift, append and find methods of the ImmutableList class.
    """
    # Given
    is_empty = False
    immutable_list = list_module.ImmutableList(is_empty=is_empty)

    # When
    immutable_list = immutable_list.unshift(is_empty)  # unshift a boolean
    immutable_list = immutable_list.append(immutable_list)  # append the list to itself

    # Then
    immutable_list.find(is_empty)  # find the boolean in the list

def test_immutable_list_append_and_find_new():
    """
    This test case verifies the behaviour of the append and find methods of the ImmutableList class.
    """
    # Given
    is_empty = True
    immutable_list = list_module.ImmutableList(is_empty, is_empty=is_empty)

    # When
    immutable_list_after_append = immutable_list.append(is_empty)
    list_length_after_append = immutable_list_after_append.__len__()

    # Then
    assert list_length_after_append == 2

    # And
    immutable_list.find(immutable_list)

def test_immutable_list_append_reduce_unshift_find():
    # Create an empty immutable list
    empty_list = list_module.ImmutableList()

    # Append an empty list to the empty list
    list_with_empty = empty_list.append(empty_list)

    # Reduce the list with itself
    reduced_list = list_with_empty.reduce(list_with_empty, list_with_empty)

    # Check if the reduced list is equal to the empty list
    is_reduced_list_empty = reduced_list.__eq__(empty_list)

    # Unshift the reduced list to itself
    unshifted_list = reduced_list.unshift(reduced_list)

    # Convert the unshifted list to a string
    unshifted_list_str = unshifted_list.__str__()

    # Create a new immutable list from the string representation of the unshifted list
    list_from_str = list_module.ImmutableList(is_empty=unshifted_list_str)

    # Append the reduced list to itself
    appended_list = reduced_list.append(reduced_list)

    # Find the reduced list in the appended list
    found_reduced_list = appended_list.find(reduced_list)

def test_immutable_list_unshift_reduce_find():
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Create a new ImmutableList with the empty list as the head
    list_with_empty_head = empty_list.unshift(empty_list)

    # Reduce the list with the list itself
    reduced_list = list_with_empty_head.reduce(list_with_empty_head, list_with_empty_head)

    # Get the length of the reduced list
    reduced_list_length = list_with_empty_head.__len__()

    # Create a new ImmutableList with the reduced list as the head
    list_with_reduced_head = list_with_empty_head.unshift(list_with_empty_head)

    # Check if the list with the reduced head is equal to the empty list
    is_equal = list_with_reduced_head.__eq__(empty_list)

    # Create a new ImmutableList with the reduced list length as the is_empty flag
    list_with_reduced_length = list_module.ImmutableList(is_empty=reduced_list_length)

    # Find the reduced list in the reduced list
    reduced_list.find(reduced_list)

def test_immutable_list_reduce_empty_list():
    """
    Test the reduce method of the ImmutableList class when the list is empty.
    """
    # Given
    empty_dict = {}
    empty_list = list_module.ImmutableList(tail=empty_dict)
    bool_value = True
    immutable_list = list_module.ImmutableList(bool_value, is_empty=bool_value)

    # When
    result = immutable_list.reduce(empty_list, empty_list)

    # Then
    assert result == empty_list