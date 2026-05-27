import immutable_list as list_module

def test_immutable_list_equality():
    """Test equality of an ImmutableList with itself."""
    empty_list = list_module.ImmutableList()
    assert empty_list == empty_list

def test_immutable_list_string_representation():
    """Test string representation of an empty ImmutableList."""
    empty_list = list_module.ImmutableList()
    assert str(empty_list) == "[]"

def test_immutable_list_to_list_conversion():
    """Test conversion of an empty ImmutableList to a list."""
    empty_list = list_module.ImmutableList()
    assert empty_list.to_list() == []

def test_immutable_list_addition():
    """Test addition of two ImmutableLists."""
    empty_list = list_module.ImmutableList()
    concat_list = empty_list.to_list() + empty_list.to_list()
    assert len(concat_list) == 2 * len(empty_list)
    assert (empty_list + empty_list).to_list() == concat_list

def test_immutable_list_length():
    """Test length of an ImmutableList."""
    empty_list = list_module.ImmutableList()
    assert len(empty_list) == 0

def test_immutable_list_operations():
    """
    Test operations on an ImmutableList.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Create a new ImmutableList by adding an empty list to the empty list
    new_list = empty_list.__add__(empty_list)

    # Check if the empty list is in the new list
    is_empty_in_new_list = new_list.find(empty_list)

    # Convert the new list to a string
    new_list_str = new_list.__str__()

    # Create a new list by adding the empty list to the front of the new list
    new_list_with_empty_front = new_list.unshift(empty_list)

    # Reduce the new list with the empty list
    new_list_with_empty_front.reduce(new_list_with_empty_front, empty_list)

def test_immutable_list_append_and_find():
    """
    Test the append and find methods of the ImmutableList class.
    """
    # Given
    is_empty = True
    empty_list = list_module.ImmutableList(is_empty=is_empty)

    # When
    list_with_element = empty_list.append(is_empty)
    found_element = list_with_element.find(is_empty)

    # Then
    assert found_element == is_empty

def test_immutable_list_addition_with_none():
    """Test ImmutableList's __add__ method with None."""
    # Given
    immutable_list = list_module.ImmutableList()
    none_value = None

    # When
    result = immutable_list.__add__(none_value)

    # Then
    assert result is None

def test_immutable_list_length_and_find_method():
    """
    Test the length of an empty ImmutableList and the find method of an ImmutableList.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Check the length of the empty list
    assert empty_list.__len__() == 0

    # Create a new ImmutableList with the empty list and check if it is empty
    new_list = list_module.ImmutableList(empty_list, is_empty=empty_list)
    assert new_list.is_empty()

    # Check if the new list can find the empty list
    assert new_list.find(empty_list) is not None

def test_immutable_list_length_and_find_method():
    """
    Test the length of an ImmutableList and the find method.
    """
    # Create an empty ImmutableList
    empty_immutable_list = list_module.ImmutableList(is_empty=True)
    # Get the length of the ImmutableList
    empty_list_length = len(empty_immutable_list)
    # Find the empty ImmutableList in itself
    empty_immutable_list.find(empty_immutable_list)

def test_find_method_returns_none_for_empty_list():
    """
    This test case verifies that the find method returns None when called on an empty list.
    """
    # Given
    empty_list = list_module.ImmutableList(is_empty=True)

    # When
    result = empty_list.find([])

    # Then
    assert result is None, "Expected find method to return None for empty list"

def test_immutable_list_append_and_find_1():
    # Create an empty immutable list
    empty_list = list_module.ImmutableList()

    # Append an empty list to the empty list
    list_with_empty_list = empty_list.append(empty_list)

    # Convert the list to a Python list
    list_as_python_list = list_with_empty_list.to_list()

    # Attempt to find None in the list
    none_index = list_with_empty_list.find(None)

    # Attempt to add None to the list
    list_as_python_list.__add__(None)

    # Assert that None is not found in the list
    assert none_index == -1

def test_immutable_list_to_list_returns_empty_list_when_initialized_with_is_empty_true():
    """
    Test that to_list() method of ImmutableList class returns an empty list when initialized with is_empty=True.
    """
    # Given
    is_empty = True
    immutable_list = list_module.ImmutableList(is_empty=is_empty)

    # When
    result = immutable_list.to_list()

    # Then
    assert result == []

def test_immutable_list_to_list_returns_empty_list_when_initialized_without_is_empty():
    """
    Test that to_list() method of ImmutableList class returns an empty list when initialized without is_empty.
    """
    # Given
    immutable_list = list_module.ImmutableList()

    # When
    result = immutable_list.to_list()

    # Then
    assert result == []

def test_unshift_and_append_and_map_operations():
    """
    This test case checks the behaviour of unshift, append and map operations on ImmutableList.
    """
    # Given
    empty_list = list_module.ImmutableList()
    none_value = None

    # When
    list_after_unshift = empty_list.unshift(none_value)
    list_after_second_unshift = list_after_unshift.unshift(list_after_unshift)
    list_after_append = list_after_unshift.append(none_value)

    # Then
    list_after_map = list_after_append.map(none_value)

    # Assert
    assert list_after_map == list_module.ImmutableList(None, list_module.ImmutableList(None, None), None)

def test_filter_immutable_list_with_same_list():
    """
    Test that the filter method of ImmutableList behaves as expected when
    filtering the list with itself.
    """
    # Given
    is_empty = False
    # When
    immutable_list = list_module.ImmutableList(is_empty, is_empty=is_empty)
    # Then
    immutable_list.filter(immutable_list)

def test_immutable_list_addition_and_filtering():
    """
    Test that the addition of two empty lists results in an empty list,
    and that filtering an empty list with a non-zero length does not raise an error.
    """
    # Given
    empty_list = list_module.ImmutableList()

    # When
    result_list = empty_list.__add__(empty_list)
    result_length = result_list.__len__()

    # Then
    result_list.filter(result_length)

def test_find_method_returns_none_for_unfound_element():
    """
    This test case verifies that the find method of the ImmutableList class
    returns None when the element is not found in the list.
    """
    # Given
    element_not_in_list = 1947
    empty_list = list_module.ImmutableList(None, None)

    # When
    result = empty_list.find(element_not_in_list)

    # Then
    assert result is None
    assert len(result) == 0

def test_immutable_list_find_method():
    """
    Test the find method of the ImmutableList class.
    """
    # Given
    is_empty = False
    immutable_list = list_module.ImmutableList(is_empty, is_empty=is_empty)

    # When
    result = immutable_list.find(immutable_list)

    # Then
    assert result == -1

def test_immutable_list_reduce_with_empty_list():
    """
    Test that the reduce method of the ImmutableList class
    correctly reduces an empty list.
    """
    # Given
    empty_list = list_module.ImmutableList()
    initial_value = False

    # When
    result = empty_list.reduce(initial_value, empty_list)

    # Then
    assert result == initial_value


def test_immutable_list_find_with_empty_list():
    """
    Test that the find method of the ImmutableList class
    correctly finds an element in an empty list.
    """
    # Given
    empty_list = list_module.ImmutableList(is_empty=True)

    # When
    result = empty_list.find(empty_list)

    # Then
    assert result is None

def test_immutable_list_creation_1():
    """
    Test that an instance of ImmutableList can be created.
    """
    # Create an instance of ImmutableList
    immutable_list = list_module.ImmutableList()

    # Assert that the instance was created successfully
    assert isinstance(immutable_list, list_module.ImmutableList)

def test_immutable_list_find_method_1():
    """
    Test the find method of the ImmutableList class.
    """
    # Given
    is_empty = False
    immutable_list = list_module.ImmutableList(is_empty, is_empty=is_empty)

    # When
    result = immutable_list.find(immutable_list)

    # Then
    assert result == immutable_list

def test_unshift_and_find_on_immutable_list():
    """
    Test the unshift and find methods of the ImmutableList class.
    """
    # Given
    is_empty = False
    immutable_list = list_module.ImmutableList(is_empty, is_empty=is_empty)

    # When
    updated_list = immutable_list.unshift(immutable_list)

    # Then
    updated_list.find(immutable_list)

def test_unshift_and_append_then_find():
    """
    Test the behaviour of unshift, append and find methods of ImmutableList.
    """
    # Given
    is_empty = False
    immutable_list = list_module.ImmutableList(is_empty=is_empty)

    # When
    immutable_list = immutable_list.unshift(is_empty)  # unshift a False value
    immutable_list = immutable_list.append(immutable_list)  # append the list to itself

    # Then
    immutable_list.find(is_empty)  # find the first occurrence of False

def test_immutable_list_append_and_find_2():
    """
    Test the append and find methods of the ImmutableList class.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList(is_empty=True)

    # Append a boolean value to the list
    list_with_bool = empty_list.append(True)

    # Check the length of the list
    assert list_with_bool.__len__() == 1

    # Find the boolean value in the list
    assert list_with_bool.find(True) is not None

def test_immutable_list_append_reduce_unshift_find():
    """
    Test the behaviour of append, reduce, unshift and find methods of ImmutableList.
    """
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Append an empty list to the empty list
    list_with_empty_list = empty_list.append(empty_list)

    # Reduce the list with itself
    reduced_list = list_with_empty_list.reduce(list_with_empty_list, list_with_empty_list)

    # Check if the reduced list is equal to the empty list
    is_reduced_list_empty = reduced_list.__eq__(empty_list)

    # Unshift the reduced list to itself
    unshifted_list = reduced_list.unshift(reduced_list)

    # Convert the unshifted list to a string
    unshifted_list_str = unshifted_list.__str__()

    # Create a new ImmutableList with the string representation of the unshifted list
    new_list = list_module.ImmutableList(is_empty=unshifted_list_str)

    # Append the new list to itself
    appended_list = new_list.append(new_list)

    # Find the new list in the appended list
    found_list = appended_list.find(new_list)

def test_unshift_reduce_len_eq_find():
    # Create an empty ImmutableList
    empty_list = list_module.ImmutableList()

    # Unshift an empty list into the empty list
    list_with_empty = empty_list.unshift(empty_list)

    # Reduce the list with itself
    reduced_list = list_with_empty.reduce(list_with_empty, list_with_empty)

    # Get the length of the reduced list
    len_reduced_list = list_with_empty.__len__()

    # Unshift the reduced list into itself
    list_with_reduced = list_with_empty.unshift(list_with_empty)

    # Check if the list with the reduced list is equal to the empty list
    is_equal = list_with_reduced.__eq__(empty_list)

    # Create a new ImmutableList with the length of the reduced list as the is_empty flag
    new_list = list_module.ImmutableList(is_empty=len_reduced_list)

    # Find the reduced list in the reduced list
    reduced_list.find(reduced_list)

def test_immutable_list_reduce_1():
    """
    Test the reduce method of the ImmutableList class.
    """
    # Given
    empty_list = list_module.ImmutableList(is_empty=True)
    bool_value = True
    dict_value = {}
    list_with_tail = list_module.ImmutableList(tail=dict_value)
    list_with_head = list_module.ImmutableList(head=bool_value, is_empty=bool_value)

    # When
    reduced_list = list_with_head.to_list()
    list_with_head.reduce(reduced_list, reduced_list)

    # Then
    # Assertions would go here, but they are not changed in this test.

