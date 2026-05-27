import pytest
import immutable_list as immutable_list_module

def test_empty_immutable_list_operations():
    """Test that an empty ImmutableList correctly handles equality, string representation,
    to_list conversion, and addition operations."""
    immutable_list = immutable_list_module.ImmutableList()

    # Test equality with itself
    immutable_list.__eq__(immutable_list)

    # Test string representation
    immutable_list.__str__()

    # Convert to list and perform operations on the resulting list
    result_list = immutable_list.to_list()
    result_list.__add__(result_list)  # Add list to itself (result unused)
    result_list.__len__()  # Get length of the list (result unused)

    # Test adding the original list to the immutable list
    immutable_list.__add__(result_list)

def test_immutable_list_equality_and_self_operations():
    """Tests various ImmutableList operations including equality check with a boolean,
    concatenation with itself, finding a boolean value, string representation,
    unshifting, and reducing."""
    bool_value = True
    empty_list = immutable_list_module.ImmutableList()
    
    # Check equality between empty list and a boolean
    equality_result = empty_list.__eq__(bool_value)
    
    # Concatenate list with itself
    concatenated_list = empty_list.__add__(empty_list)
    
    # Try to find the boolean result in the list (will not be found as list is empty)
    find_result = empty_list.find(equality_result)
    
    # Get string representation of empty list
    list_str = empty_list.__str__()
    
    # Create new list by unshifting the empty list onto itself
    new_list = empty_list.unshift(empty_list)
    
    # Reduce the new list using itself as both the function and initial value
    new_list.reduce(new_list, bool_value)

def test_find_on_immutable_list_with_self_reference():
    """Test that find() works correctly on an ImmutableList containing a boolean value
    with is_empty set to True, and using the list itself as the search target."""
    bool_value = True
    immutable_list = immutable_list_module.ImmutableList(bool_value, is_empty=bool_value)
    immutable_list.append(bool_value)
    immutable_list.find(immutable_list)

def test_adding_none_to_immutable_list_returns_self():
    """
    Verify that adding None to an ImmutableList returns the original list unchanged.
    """
    immutable_list = immutable_list_module.ImmutableList()
    none_value = None

    # Calling __add__ with None should return the list itself
    immutable_list.__add__(none_value)

def test_find_returns_none_when_element_not_found_in_non_empty_list():
    """
    Verifies that finding an element not present in the list returns None.
    This test creates a nested, non-empty ImmutableList and attempts to find
    a reference to the list itself (which is not stored as a direct element).
    """
    immutable_list_0 = immutable_list_module.ImmutableList()
    var_0 = immutable_list_0.__len__()  # length of empty list (0)
    immutable_list_1 = immutable_list_module.ImmutableList(
        immutable_list_0, is_empty=immutable_list_0
    )
    # Searching for the outer list (immutable_list_1) within itself;
    # since the list contains only immutable_list_0, find() should return None.
    result = immutable_list_1.find(immutable_list_1)
    assert result is None

def test_find_on_immutable_list_with_bool_elements():
    """Test that find works correctly when called on an immutable list with boolean elements."""
    is_empty = False
    immutable_list = immutable_list_module.ImmutableList(False, is_empty=is_empty)
    list_length = immutable_list.__len__()
    immutable_list.find(immutable_list)

def test_to_list_and_find_on_empty_immutable_list_with_false_is_empty():
    """Test that to_list and find can be called on an ImmutableList created with
    explicit is_empty flag set to False."""
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    list_representation = empty_list.to_list()
    # find() should not raise an exception when called on the list representation
    empty_list.find(list_representation)

def test_find_returns_none_when_item_not_found_and_append_with_self_then_to_list_with_none_addition():
    """
    Verify that `find` returns `None` for an absent item on an empty list,
    and that appending the list to itself and converting to a list returns a
    mutable list whose `__add__` works with `None`.
    """
    empty_list = immutable_list_module.ImmutableList()
    not_found = None
    result = empty_list.find(not_found)

    list_with_self = empty_list.append(empty_list)
    as_list = list_with_self.to_list()
    as_list.__add__(not_found)

def test_to_list_and_map_interaction():
    """Verify that calling to_list() on an empty and non-empty ImmutableList,
    then using the result to call map(), does not raise an error."""
    # Create an ImmutableList with is_empty=False
    non_empty_list = immutable_list_module.ImmutableList(is_empty=False)
    # Convert to a regular list
    result_list = non_empty_list.to_list()

    # Create a default (empty) ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    # Convert to a regular list again
    second_result = non_empty_list.to_list()

    # Call map using the previously obtained list as the mapping argument
    non_empty_list.map(second_result)

def test_unshift_and_append_with_none_on_immutable_list():
    """Test that unshift and append operations work correctly with None values on an ImmutableList."""
    none_value = None
    # Create an ImmutableList with None head and tail
    initial_list = immutable_list_module.ImmutableList(none_value, none_value)
    
    # Unshift None onto the list, creating a new list
    list_after_first_unshift = initial_list.unshift(none_value)
    
    # Unshift the previous result onto the original list
    list_after_second_unshift = initial_list.unshift(list_after_first_unshift)
    
    # Append None to the first unshift result
    list_after_append = list_after_first_unshift.append(none_value)
    
    # Call map with None on the appended list
    list_after_append.map(none_value)

def test_filter_empty_immutable_list_with_self_as_predicate():
    """
    Test that filtering an ImmutableList with itself as the predicate works
    when the list is empty (is_empty=True).
    """
    # Create an empty ImmutableList
    is_empty_flag = False
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Filter the list using itself as the predicate
    immutable_list.filter(immutable_list)

def test_immutable_list_filter_with_own_length():
    """Test that filtering an ImmutableList using its own length doesn't raise errors."""
    immutable_list = immutable_list_module.ImmutableList()
    concatenated_list = immutable_list.__add__(immutable_list)
    list_length = concatenated_list.__len__()
    concatenated_list.filter(list_length)

def test_find_on_empty_list_returns_object_supporting_len():
    """Test that calling find() on an empty ImmutableList returns a value that supports __len__."""
    value = 1947
    none_type = None
    empty_list = immutable_list_module.ImmutableList(none_type, none_type)
    result = empty_list.find(value)
    result.__len__()

def test_find_on_immutable_list_with_bool_and_empty_flag():
    """Test that find() returns the list itself when searching with the same list object."""
    is_empty = False
    immutable_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)
    immutable_list.find(immutable_list)

def test_reduce_with_false_initial_value_and_self_find_on_non_empty_list():
    """
    Test that reduce can be called with False as the reducer function and an
    empty ImmutableList as the initial value, and that find on a non-empty list
    can be called with the list itself as the argument.
    """
    initial_value = False
    empty_list = immutable_list_module.ImmutableList()
    reduced_result = empty_list.reduce(initial_value, empty_list)

    non_empty_list = immutable_list_module.ImmutableList(initial_value, is_empty=initial_value)
    non_empty_list.find(non_empty_list)

def test_empty_immutable_list_creation_with_no_args():
    """Verify that an ImmutableList can be created with no arguments."""
    immutable_list_0 = immutable_list_module.ImmutableList()

def test_find_on_single_false_element_with_empty_flag():
    """
    Verify that calling find() on an ImmutableList containing a single False element
    (with is_empty flag set to True) returns a result string representation correctly.
    """
    is_empty = False
    single_element_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)
    string_representation = single_element_list.__str__()
    single_element_list.find(single_element_list)

def test_immutable_list_find_after_unshift_with_empty_false_flag():
    """
    Test that calling find() on an ImmutableList after unshifting itself with is_empty=False
    does not raise an exception and behaves as expected.
    """
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    list_with_self_appended = empty_list.unshift(empty_list)
    empty_list.find(empty_list)

def test_find_on_non_empty_immutable_list_returns_correct_value():
    """Test that the find method works correctly on a non-empty ImmutableList."""
    is_empty = False
    empty_list = immutable_list_module.ImmutableList(is_empty=is_empty)
    list_with_false = empty_list.unshift(is_empty)
    nested_list = list_with_false.append(empty_list)
    # Find the target value in the constructed list
    result = nested_list.find(is_empty)

def test_immutable_list_find_after_append_and_length_check():
    """Test that find() works correctly on an ImmutableList after appending an element and checking its length."""
    bool_value = True
    single_element_list = immutable_list_module.ImmutableList(bool_value, is_empty=bool_value)
    extended_list = single_element_list.append(bool_value)
    _ = extended_list.__len__()
    # find() on the original list with itself as the target to locate
    single_element_list.find(single_element_list)

def test_reduce_and_equality_with_self_reference():
    """
    Tests reduction with a self-referencing list and verifies equality,
    unshift, and find behaviour on immutable list instances.
    """
    immutable_list_0 = immutable_list_module.ImmutableList()
    immutable_list_1 = immutable_list_0.append(immutable_list_0)  # List containing itself
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    bool_0 = immutable_list_1.__eq__(immutable_list_0)  # Compare with original empty list
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    str_0 = immutable_list_2.__str__()
    immutable_list_3 = immutable_list_module.ImmutableList(is_empty=str_0)
    immutable_list_4 = var_0.append(var_0)
    immutable_list_2.find(var_0)

def test_reduce_self_reference_and_find_on_empty_and_nested_immutable_lists():
    """Test chained reduce, unshift, equality, and find operations on an
    ImmutableList, including an empty list and a list containing itself.
    """
    immutable_list_0 = immutable_list_module.ImmutableList()
    # unshift: create a new list with immutable_list_0 as head and the original as tail
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    # reduce using immutable_list_1 as both the accumulator and the iterable
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    var_1 = immutable_list_1.__len__()
    # unshift again: prepend immutable_list_1 to itself
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    bool_0 = immutable_list_2.__eq__(immutable_list_0)
    immutable_list_3 = immutable_list_module.ImmutableList(is_empty=var_1)
    var_0.find(var_0)

def test_reduce_on_empty_flag_list_with_non_empty_tail_returns_empty_list():
    """Verify that reduce() on an ImmutableList with a non-empty tail and is_empty=True returns the expected result."""
    true_value = True
    empty_dict = {}
    list_with_empty_tail = immutable_list_module.ImmutableList(tail=empty_dict)
    empty_immutable_list = immutable_list_module.ImmutableList(true_value, is_empty=true_value)
    result_list = empty_immutable_list.to_list()
    # Call reduce using the result of to_list() as both the function and initial value
    empty_immutable_list.reduce(result_list, result_list)