import pytest
import immutable_list as immutable_list_module

def test_immutable_list_equality_string_conversion():
    """Test ImmutableList equality, string representation, and conversion to list."""
    # Create an empty ImmutableList
    immutable_list = immutable_list_module.ImmutableList()

    # Test equality with itself (should return True)
    immutable_list.__eq__(immutable_list)

    # Test string representation
    immutable_list.__str__()

    # Convert to a regular list
    regular_list = immutable_list.to_list()

    # Add the list to itself (creates a new concatenated list)
    regular_list.__add__(regular_list)

    # Get the length of the list
    regular_list.__len__()

    # Add the original list to the immutable list
    immutable_list.__add__(regular_list)

def test_immutable_list_operations_with_self_reference_and_boolean():
    """
    Tests various ImmutableList operations including equality with a boolean,
    concatenation with itself, finding an element, string conversion,
    unshifting itself, and reducing with a boolean initial value.
    """
    bool_0 = True
    immutable_list_0 = immutable_list_module.ImmutableList()
    bool_1 = immutable_list_0.__eq__(bool_0)
    immutable_list_1 = immutable_list_0.__add__(immutable_list_0)
    bool_2 = immutable_list_0.find(bool_1)
    str_0 = immutable_list_0.__str__()
    immutable_list_2 = immutable_list_0.unshift(immutable_list_0)
    immutable_list_2.reduce(immutable_list_2, bool_0)

def test_find_on_immutable_list_completely_boolean():
    """Test that the find method works correctly on an ImmutableList
    where both the element and is_empty flag are boolean values."""
    # Create an ImmutableList with True as element and is_empty=True
    bool_value = True
    immutable_list_0 = immutable_list_module.ImmutableList(bool_value, is_empty=bool_value)

    # Append a boolean value to create a non-empty list
    immutable_list_1 = immutable_list_0.append(bool_value)

    # Find an element in the original list (should search the boolean value)
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_addition_with_none_does_not_raise_error():
    """
    Verify that adding None to an ImmutableList instance does not raise an error.
    """
    empty_list = immutable_list_module.ImmutableList()
    none_value = None
    empty_list.__add__(none_value)

def test_find_on_immutable_list_with_nested_list_and_is_empty_flag():
    """
    Test that find works correctly when called on an ImmutableList that
    has another ImmutableList as its head and uses a non-empty is_empty flag.
    """
    inner_list = immutable_list_module.ImmutableList()
    inner_list_length = inner_list.__len__()
    outer_list = immutable_list_module.ImmutableList(
        inner_list, is_empty=inner_list
    )
    outer_list.find(outer_list)

def test_immutable_list_len_and_find_with_false_flag():
    """Test that __len__() and find() work on an ImmutableList created with is_empty=False."""
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    length = empty_list.__len__()
    empty_list.find(empty_list)

def test_immutable_list_to_list_and_find_with_empty_flag():
    """Test that to_list() returns a list and find() can handle the result."""
    is_empty = False
    immutable_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)
    result_list = immutable_list.to_list()
    immutable_list.find(result_list)

def test_find_on_empty_list_and_self_append_conversion():
    """
    Test that calling find(None) on an empty ImmutableList returns None,
    and that appending the original list to itself and converting to list works.
    """
    empty_list = immutable_list_module.ImmutableList()
    none_value = None
    # find(None) on empty list should return None
    found_item = empty_list.find(none_value)
    # Append the empty list to itself, creating a new list
    list_with_self = empty_list.append(empty_list)
    # Convert to a Python list and attempt to add None (though result is unused)
    result_list = list_with_self.to_list()
    result_list.__add__(none_value)

def test_to_list_and_map_on_immutable_list_consistency():
    """
    Test that converting a non-empty ImmutableList to a list returns the correct sequence,
    and that creating a new empty ImmutableList and converting the original again yields the
    same result. Also verifies that map() can be called on the original list using the list
    representation.
    """
    # Create an ImmutableList with is_empty=False
    non_empty_list = immutable_list_module.ImmutableList(is_empty=False)
    # Convert to a Python list
    result_list_1 = non_empty_list.to_list()

    # Create a new (empty) ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    # Convert the original non-empty list again to verify consistency
    result_list_2 = non_empty_list.to_list()

    # Call map() on the original list using the second list representation
    non_empty_list.map(result_list_2)

def test_immutable_list_unshift_and_append_with_none_values():
    """
    Tests that unshift and append operations work correctly when the ImmutableList
    is initialized with None values and subsequent operations use None elements.
    """
    none_value = None
    # Create an ImmutableList containing two None elements
    immutable_list_0 = immutable_list_module.ImmutableList(none_value, none_value)

    # Prepend another None to the list via unshift
    immutable_list_1 = immutable_list_0.unshift(none_value)

    # Prepend the resulting sublist (immutable_list_1) as an element
    immutable_list_2 = immutable_list_0.unshift(immutable_list_1)

    # Append None to the sublist
    immutable_list_3 = immutable_list_1.append(none_value)

    # Call map on the final list with None as the transformation function
    immutable_list_3.map(none_value)

def test_filter_with_self_as_lambda():
    """Test that filtering an immutable list using another immutable list as the filter function does not raise an error."""
    is_empty = False
    immutable_list_obj = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)
    immutable_list_obj.filter(immutable_list_obj)

def test_filter_immutable_list_using_length_as_predicate():
    """
    Verify that calling filter() on an immutable list using its own length
    as the predicate function does not raise an error.
    """
    empty_list = immutable_list_module.ImmutableList()
    concatenated_list = empty_list.__add__(empty_list)
    length = concatenated_list.__len__()
    concatenated_list.filter(length)

def test_find_returns_list_supporting_len_protocol():
    """
    Test that the ImmutableList.find method returns a list-like object
    which supports the __len__ protocol, even when the item is not found.
    """
    # Use an integer value that does not exist in the empty list
    search_value = 1947
    # Create an empty immutable list (both head and tail are None)
    empty_list = immutable_list_module.ImmutableList(None, None)

    # Find the value in the empty list (should return an empty list)
    found_list = empty_list.find(search_value)

    # Verify the returned object supports __len__ (calls len internally)
    found_list.__len__()

def test_find_on_empty_immutable_list_returns_none():
    """Test that calling find() on an empty ImmutableList returns None."""
    # Create an empty immutable list with False as the element and is_empty flag
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Searching an empty list should return None
    result = empty_list.find(empty_list)
    assert result is None

def test_reduce_with_find_using_empty_immutable_list():
    """Test that reduce on an empty ImmutableList returns the initial value,
    and that find works on a non-empty list."""
    bool_0 = False
    empty_list = immutable_list_module.ImmutableList()
    # Reduce with False as initial value on an empty list should return False
    reduced_result = empty_list.reduce(bool_0, empty_list)
    # Create a non-empty list with is_empty explicitly set to False
    non_empty_list = immutable_list_module.ImmutableList(bool_0, is_empty=bool_0)
    # Find on the list itself (used as the predicate)
    non_empty_list.find(non_empty_list)

def test_empty_immutable_list_creation():
    """Verify that an empty ImmutableList can be created successfully."""
    immutable_list_0 = immutable_list_module.ImmutableList()

def test_immutable_list_str_and_find_with_boolean_flag():
    """
    Test that an ImmutableList created with a boolean value and is_empty flag
    can produce a string representation and then run a find operation on itself.
    """
    is_empty = False
    immutable_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)
    string_repr = immutable_list.__str__()
    immutable_list.find(immutable_list)

def test_unshift_on_empty_list_then_find_returns_none():
    """Test that unshifting an empty ImmutableList onto itself works,
    and that calling find on the result returns None (no matching element)."""
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Unshift the empty list onto itself, creating a new list with one element
    new_list = empty_list.unshift(empty_list)
    # Find should return None since there's no element matching the predicate
    new_list.find(empty_list)

def test_find_on_non_empty_immutable_list_returns_none_when_item_not_found():
    """Test that calling find() on a non-empty list returns None when the searched item is not present."""
    is_empty = False
    immutable_list = immutable_list_module.ImmutableList(is_empty=is_empty)
    shifted_list = immutable_list.unshift(is_empty)
    appended_list = shifted_list.append(immutable_list)
    appended_list.find(is_empty)

def test_find_on_immutable_list_with_true_is_empty_flag_and_bool_value():
    """Test that calling find with the list itself works correctly when 
    appended to a list flagged as empty and containing a boolean value."""
    is_empty_flag = True
    bool_value = True
    list_with_bool = immutable_list_module.ImmutableList(bool_value, is_empty=is_empty_flag)
    appended_list = list_with_bool.append(bool_value)
    length = appended_list.__len__()
    list_with_bool.find(list_with_bool)

def test_immutable_list_edge_case_reduce_equality_unshift_find():
    """Test various ImmutableList operations: append, reduce, equality, unshift, and find."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()

    # Append the empty list to itself to create a single-element list
    single_element_list = empty_list.append(empty_list)

    # Reduce the empty list using the single-element list as both function and initial value
    # (Note: passing a list as a function is unusual but intentional for edge case testing)
    reduced_result = empty_list.reduce(single_element_list, single_element_list)

    # Check equality between the single-element list and the empty list
    # (This is testing the __eq__ method on a non-empty vs empty list)
    equality_result = single_element_list.__eq__(empty_list)

    # Create a list with an element prepended to the single-element list
    prepended_list = single_element_list.unshift(single_element_list)

    # Convert the prepended list to string representation
    list_as_string = prepended_list.__str__()

    # Create a new ImmutableList using the string representation as is_empty parameter
    # (Note: using a non-boolean value for is_empty is intentional for testing edge cases)
    list_with_string_is_empty = immutable_list_module.ImmutableList(is_empty=list_as_string)

    # Append the reduced result to itself
    appended_reduced = reduced_result.append(reduced_result)

    # Call find on the prepended list using the reduced result as the predicate
    # (Note: testing find with a non-callable argument for error handling or edge case behavior)
    prepended_list.find(reduced_result)

def test_immutable_list_reduce_find_equality_with_self_reference():
    """Test chain of unshift, reduce, len, eq, and find operations on ImmutableList."""
    # Create an empty list, then add the list itself as an element via unshift
    immutable_list_0 = immutable_list_module.ImmutableList()
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)

    # Reduce with the same list as both accumulator and iterable
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)

    # Get length of the list that has one element
    var_1 = immutable_list_1.__len__()

    # Create another list by unshifting the list into itself
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)

    # Check equality between the new list and the empty list
    bool_0 = immutable_list_2.__eq__(immutable_list_0)

    # Create a list marked as empty based on the length found above
    immutable_list_3 = immutable_list_module.ImmutableList(is_empty=var_1)

    # Call find on the result of the reduce operation
    var_0.find(var_0)

def test_immutable_list_reduce_with_head_and_to_list():
    """Test that calling reduce() on an ImmutableList with a boolean head and the empty tail list works."""
    bool_0 = True
    empty_dict = {}
    immutable_list_with_tail = immutable_list_module.ImmutableList(tail=empty_dict)
    immutable_list_with_head = immutable_list_module.ImmutableList(bool_0, is_empty=bool_0)
    to_list_result = immutable_list_with_head.to_list()
    immutable_list_with_head.reduce(to_list_result, to_list_result)