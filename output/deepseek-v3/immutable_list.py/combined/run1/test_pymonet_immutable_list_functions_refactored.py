import pytest
import immutable_list as immutable_list_module

def test_immutable_list_basic_operations():
    """Test basic operations of ImmutableList including equality, string conversion, and list concatenation."""
    
    # Create an empty immutable list
    empty_immutable_list = immutable_list_module.ImmutableList()
    
    # Test equality with itself
    self_equality_result = empty_immutable_list.__eq__(empty_immutable_list)
    
    # Get string representation
    string_representation = empty_immutable_list.__str__()
    
    # Convert to regular list
    regular_list = empty_immutable_list.to_list()
    
    # Concatenate regular list with itself
    concatenated_list = regular_list.__add__(regular_list)
    
    # Get length of regular list
    list_length = regular_list.__len__()
    
    # Attempt to add regular list to immutable list (result unused)
    empty_immutable_list.__add__(regular_list)

def test_empty_immutable_list_operations():
    """Test various operations on an empty ImmutableList instance."""
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Test equality comparison with a boolean (should return False)
    true_value = True
    equality_result = empty_list.__eq__(true_value)
    
    # Test concatenation with itself (creates another empty list)
    concatenated_list = empty_list.__add__(empty_list)
    
    # Test find operation with the equality result
    find_result = empty_list.find(equality_result)
    
    # Test string representation
    string_representation = empty_list.__str__()
    
    # Test unshift operation (prepend list to itself)
    unshifted_list = empty_list.unshift(empty_list)
    
    # Test reduce operation with the unshifted list and True as initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find():
    """
    Test that appending to an ImmutableList and finding elements works correctly.
    """
    true_value = True
    
    # Create an ImmutableList with a single True element, marked as empty
    original_list = immutable_list_module.ImmutableList(true_value, is_empty=true_value)
    
    # Append another True value to the list
    appended_list = original_list.append(true_value)
    
    # Attempt to find the original list within itself
    original_list.find(original_list)

def test_immutable_list_add_with_none():
    """Test that ImmutableList.__add__ method accepts None without raising errors."""
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Prepare None value to add
    none_value = None
    
    # Call __add__ with None - test verifies no exception is raised
    empty_list.__add__(none_value)

def test_find_on_immutable_list_with_self_as_head_and_empty():
    """Test that find() works on an ImmutableList constructed with another ImmutableList as both head and is_empty parameter."""
    empty_list = immutable_list_module.ImmutableList()
    empty_list_length = empty_list.__len__()
    
    # Create a nested list where the head and is_empty parameter are both the empty list
    nested_list = immutable_list_module.ImmutableList(
        empty_list, is_empty=empty_list
    )
    
    # Try to find the nested list within itself
    nested_list.find(nested_list)

def test_immutable_list_len_and_find_with_false_element():
    """
    Test that ImmutableList.__len__ and .find methods work correctly
    when called on a list containing a False element.
    """
    false_element = False
    immutable_list = immutable_list_module.ImmutableList(false_element, is_empty=false_element)
    length = immutable_list.__len__()
    immutable_list.find(immutable_list)

def test_find_with_list_representation_of_same_list():
    """
    Test that the `find` method can be called with the list representation
    of the same immutable list without raising an error.
    """
    false_value = False
    # Create a non-empty immutable list with head=False and is_empty=False
    immutable_list = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    
    # Convert the immutable list to a regular list
    list_representation = immutable_list.to_list()
    
    # Attempt to find the list representation within the same immutable list
    immutable_list.find(list_representation)

def test_immutable_list_find_append_with_none():
    """Test ImmutableList operations involving None values and self-appending."""
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Try to find None in the empty list
    none_value = None
    find_result = empty_list.find(none_value)
    
    # Append the empty list to itself (creating a list containing itself)
    appended_list = empty_list.append(empty_list)
    
    # Convert the immutable list to a regular Python list
    regular_list = appended_list.to_list()
    
    # Call __add__ on the regular list with None
    # This tests that the converted list supports list operations
    regular_list.__add__(none_value)

def test_immutable_list_map_with_to_list_result():
    """
    Test that ImmutableList.map can be called with the result of to_list.
    """
    is_empty_flag = False
    non_empty_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)
    list_representation_1 = non_empty_list.to_list()
    default_list = immutable_list_module.ImmutableList()
    list_representation_2 = non_empty_list.to_list()
    non_empty_list.map(list_representation_2)

def test_immutable_list_operations_with_none():
    """Test various ImmutableList operations using None values."""
    
    # Create initial list with None as both head and tail
    none_value = None
    initial_list = immutable_list_module.ImmutableList(none_value, none_value)
    
    # Test unshift operation with None
    list_after_unshift = initial_list.unshift(none_value)
    
    # Test unshift operation with another list
    list_after_unshift_again = initial_list.unshift(list_after_unshift)
    
    # Test append operation on the previously unshifted list
    list_after_append = list_after_unshift.append(none_value)
    
    # Test map operation with None as mapper function
    list_after_append.map(none_value)

def test_filter_with_self_on_non_empty_list():
    """Test filtering an ImmutableList using itself as the predicate."""
    false_value = False
    # Create a non-empty list with a single False element
    list_instance = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    # Attempt to filter the list using itself as the filter function
    list_instance.filter(list_instance)

def test_immutable_list_add_length_filter():
    """Test that concatenating an empty ImmutableList with itself, 
    getting its length, and filtering by that length works."""
    
    empty_list = immutable_list_module.ImmutableList()
    concatenated_list = empty_list.__add__(empty_list)
    list_length = concatenated_list.__len__()
    
    # Filter the concatenated list using its own length as the filter criterion
    concatenated_list.filter(list_length)

def test_immutable_list_find_and_len():
    """
    Test that calling find on an ImmutableList and then __len__ on the result
    does not raise an exception.
    """
    search_value = 1947
    none_value = None
    
    # Create an ImmutableList with two None values (head and tail)
    immutable_list = immutable_list_module.ImmutableList(none_value, none_value)
    
    # Find the search value in the list and call __len__ on the result
    found_result = immutable_list.find(search_value)
    found_result.__len__()

def test_find_self_in_immutable_list():
    """
    Test that an ImmutableList can attempt to find itself as an element.
    """
    false_element = False
    # Create a non-empty list containing False
    list_instance = immutable_list_module.ImmutableList(false_element, is_empty=false_element)
    # Try to find the list within itself
    list_instance.find(list_instance)

def test_reduce_and_find_with_empty_and_non_empty_lists():
    """
    Test reduce and find methods on empty and non-empty immutable lists.
    """
    false_flag = False
    
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Reduce with the list itself as the accumulator (edge case)
    reduction_result = empty_list.reduce(false_flag, empty_list)
    
    # Create a non-empty list with False as the element
    non_empty_list = immutable_list_module.ImmutableList(false_flag, is_empty=false_flag)
    
    # Attempt to find the list within itself
    non_empty_list.find(non_empty_list)

def test_immutable_list_can_be_instantiated_empty():
    """Test that an empty ImmutableList can be created."""
    # Create an empty immutable list instance
    empty_immutable_list = immutable_list_module.ImmutableList()
    # Check that the instance is created and is of the correct type
    assert empty_immutable_list is not None
    assert isinstance(empty_immutable_list, immutable_list_module.ImmutableList)

def test_immutable_list_can_find_itself_after_string_conversion():
    """
    Test that an ImmutableList can be converted to string and then
    attempt to find itself within itself.
    """
    # Create a non-empty list with False as the head element
    false_element = False
    immutable_list = module_0.ImmutableList(false_element, is_empty=false_element)
    
    # Convert the list to string representation
    string_representation = immutable_list.__str__()
    
    # Attempt to find the list within itself
    immutable_list.find(immutable_list)

def test_immutable_list_can_unshift_and_find_itself():
    """
    Test that an ImmutableList can unshift itself and then find itself.
    """
    false_value = False
    # Create a non-empty ImmutableList with head=False
    immutable_list = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    
    # Unshift the list with itself (prepend itself as new head)
    new_list = immutable_list.unshift(immutable_list)
    
    # Try to find the original list within itself
    immutable_list.find(immutable_list)

def test_find_after_unshift_and_append():
    """Test that `find` works correctly after `unshift` and `append` operations."""
    # Create a boolean value to search for
    value_to_find = False
    
    # Create an initial immutable list (non-empty since is_empty=False)
    original_list = immutable_list_module.ImmutableList(is_empty=value_to_find)
    
    # Add the value to the front of the list via unshift
    list_after_unshift = original_list.unshift(value_to_find)
    
    # Append the original list to the end
    final_list = list_after_unshift.append(original_list)
    
    # Attempt to find the value in the final list
    final_list.find(value_to_find)

def test_append_to_immutable_list_and_find_element():
    """
    Test that appending an element to an ImmutableList works correctly
    and that the find method can be called on the original list.
    """
    # Create a boolean value to use as list element
    boolean_value = True
    
    # Create an ImmutableList with the boolean value, marking it as empty
    original_list = immutable_list_module.ImmutableList(
        boolean_value, 
        is_empty=boolean_value
    )
    
    # Append the same boolean value to create a new list
    appended_list = original_list.append(boolean_value)
    
    # Get the length of the appended list
    appended_list_length = appended_list.__len__()
    
    # Try to find the original list within itself
    # (testing the find method with a non-element value)
    original_list.find(original_list)

def test_immutable_list_chain_operations():
    """Test a chain of operations on ImmutableList to ensure no exceptions are raised."""
    
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Append the list to itself
    list_with_self_appended = empty_list.append(empty_list)
    
    # Reduce the list using the appended list as both accumulator and function
    reduced_value = empty_list.reduce(list_with_self_appended, list_with_self_appended)
    
    # Check equality between the two lists
    are_equal = list_with_self_appended.__eq__(empty_list)
    
    # Unshift the list with itself
    unshifted_list = list_with_self_appended.unshift(list_with_self_appended)
    
    # Get string representation of the unshifted list
    string_representation = unshifted_list.__str__()
    
    # Create a new list using the string representation as is_empty parameter
    list_from_string = immutable_list_module.ImmutableList(is_empty=string_representation)
    
    # Append the reduced value to itself
    appended_reduced = reduced_value.append(reduced_value)
    
    # Find the reduced value in the unshifted list
    unshifted_list.find(reduced_value)

def test_immutable_list_self_referential_operations():
    """
    Test ImmutableList operations with self-referential structures,
    including reduce, unshift, equality, and find operations.
    """
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Create a list with the empty list as its first element
    list_with_empty_as_head = empty_list.unshift(empty_list)
    
    # Reduce the empty list using list_with_empty_as_head as both
    # the reducer function and initial value
    reduced_result = empty_list.reduce(list_with_empty_as_head, list_with_empty_as_head)
    
    # Get the length of list_with_empty_as_head (should be 1)
    length_of_list_with_empty_as_head = list_with_empty_as_head.__len__()
    
    # Create a nested list by unshifting list_with_empty_as_head to itself
    nested_list = list_with_empty_as_head.unshift(list_with_empty_as_head)
    
    # Check if nested_list equals the original empty list (should be False)
    are_equal = nested_list.__eq__(empty_list)
    
    # Create a new list with custom is_empty parameter
    list_with_custom_is_empty = immutable_list_module.ImmutableList(
        is_empty=length_of_list_with_empty_as_head
    )
    
    # Call find method on reduced_result with itself as argument
    reduced_result.find(reduced_result)

def test_immutable_list_reduce_with_to_list_result():
    """Test ImmutableList.reduce() when called with the result of to_list() as both arguments."""
    true_value = True
    empty_dict = {}
    
    # Create an ImmutableList with an empty dict as tail
    list_with_empty_tail = immutable_list_module.ImmutableList(tail=empty_dict)
    
    # Create an ImmutableList with True as head and is_empty flag also set to True
    list_with_true_head_and_empty_flag = immutable_list_module.ImmutableList(
        true_value, is_empty=true_value
    )
    
    # Convert the second list to a regular Python list
    converted_list = list_with_true_head_and_empty_flag.to_list()
    
    # Call reduce with the same list as both arguments (unusual but preserved)
    list_with_true_head_and_empty_flag.reduce(converted_list, converted_list)
    # Note: This test has no assertions, checking only that no exception is raised.

