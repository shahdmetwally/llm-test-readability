import pytest
import immutable_list as immutable_list_module

def test_immutable_list_basic_operations_and_conversion():
    """
    Tests basic operations of an ImmutableList instance including equality,
    string representation, conversion to a regular list, and list operations.
    This ensures the class's core methods execute without errors.
    """
    # Create an ImmutableList instance
    immutable_list = immutable_list_module.ImmutableList()
    
    # Test equality with itself
    are_equal = immutable_list.__eq__(immutable_list)
    
    # Get string representation
    string_repr = immutable_list.__str__()
    
    # Convert immutable list to a regular Python list
    regular_list = immutable_list.to_list()
    
    # Concatenate the regular list with itself using list's __add__
    concatenated_list = regular_list.__add__(regular_list)
    
    # Get length of the regular list
    list_length = regular_list.__len__()
    
    # Attempt to add the regular list to the immutable list
    # (tests ImmutableList.__add__ with a regular list argument)
    immutable_list.__add__(regular_list)

def test_immutable_list_operations_with_boolean_values():
    """
    Test various ImmutableList operations including equality checks,
    concatenation, searching, string conversion, and reduction.
    This test verifies that methods can be called without errors
    when interacting with boolean values and self-referential structures.
    """
    true_value = True
    
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Check equality with a boolean value
    is_equal_to_bool = empty_list.__eq__(true_value)
    
    # Concatenate the list with itself (remains empty)
    concatenated_list = empty_list.__add__(empty_list)
    
    # Attempt to find the equality result within the empty list
    found_bool = empty_list.find(is_equal_to_bool)
    
    # Get string representation of the empty list
    string_representation = empty_list.__str__()
    
    # Create a nested structure by prepending the list to itself
    nested_list = empty_list.unshift(empty_list)
    
    # Perform reduction using the nested list as both function and initial value
    nested_list.reduce(nested_list, true_value)

def test_find_method_with_self_reference():
    """Test that ImmutableList.find() can accept the list itself as an argument."""
    # Create a boolean value to use as list element
    true_value = True
    
    # Create an ImmutableList with the boolean as head and is_empty=True
    original_list = immutable_list_module.ImmutableList(true_value, is_empty=true_value)
    
    # Append the same boolean to create a new list instance
    appended_list = original_list.append(true_value)
    
    # Attempt to find the original list within itself
    # This tests the find method's handling of self-referential arguments
    original_list.find(original_list)

def test_immutable_list_add_none():
    """Test that ImmutableList.__add__ method handles None input without crashing."""
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Test adding None to the list (should handle gracefully)
    none_value = None
    empty_list.__add__(none_value)

def test_find_on_nested_list_with_non_boolean_is_empty():
    """
    Tests the find method on an ImmutableList constructed with a non-boolean
    is_empty parameter, which creates a nested list structure.
    """
    # Create an empty list and get its length (unused in test)
    empty_list = immutable_list_module.ImmutableList()
    _ = empty_list.__len__()  # Length computation is unused but preserved
    
    # Create a nested list using another list as head and is_empty parameter
    # This creates an unusual structure where is_empty is a list, not a boolean
    nested_list = immutable_list_module.ImmutableList(
        empty_list, is_empty=empty_list
    )
    
    # Attempt to find the nested list within itself
    nested_list.find(nested_list)

def test_find_method_with_self_as_argument():
    """Test that ImmutableList.find() can accept the list itself as argument."""
    false_value = False
    
    # Create a non-empty list with False as the first element
    list_instance = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    
    # Get the list length (should be 1 for a non-empty list)
    length = list_instance.__len__()
    
    # Attempt to find the list within itself
    list_instance.find(list_instance)

def test_find_method_accepts_list_representation():
    """Test that ImmutableList.find() can accept the list representation returned by to_list()."""
    false_value = False
    # Create a non-empty ImmutableList with False as the head
    immutable_list = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    # Convert the immutable list to a standard Python list
    list_representation = immutable_list.to_list()
    # Verify find() method accepts the list representation without error
    immutable_list.find(list_representation)

def test_immutable_list_operations_with_none_values():
    """
    Tests ImmutableList operations involving None values:
    - Finding None in an empty list
    - Appending a list to itself
    - Converting to regular list
    - Calling __add__ with None
    """
    # Create empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Try to find None in empty list
    none_value = None
    find_result = empty_list.find(none_value)  # Should return -1 or None
    
    # Append the list to itself (creates nested structure)
    appended_list = empty_list.append(empty_list)
    
    # Convert to regular Python list
    regular_list = appended_list.to_list()
    
    # Try to add None to the regular list via __add__
    # This tests error handling when invalid type is passed
    regular_list.__add__(none_value)

def test_map_with_list_conversion_does_not_raise():
    """
    Tests that mapping a list representation of an ImmutableList over itself
    does not raise exceptions, verifying basic functional composition.
    """
    # Create a non-empty ImmutableList
    is_empty_flag = False
    non_empty_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)
    
    # Convert to regular list (unused in later operations)
    list_representation = non_empty_list.to_list()
    
    # Create a default ImmutableList (likely empty)
    empty_list = immutable_list_module.ImmutableList()
    
    # Get the list representation again
    same_list_again = non_empty_list.to_list()
    
    # Attempt to map the list representation over the original immutable list
    # This tests that the map method accepts a list argument without errors
    non_empty_list.map(same_list_again)

def test_immutable_list_operations_with_none_and_list_arguments():
    """
    Test ImmutableList operations (unshift, append, map) with None values
    and list arguments to ensure they execute without errors.
    """
    none_value = None
    
    # Create base list with None head and tail
    base_list = immutable_list_module.ImmutableList(none_value, none_value)
    
    # Test unshift operation with None
    unshifted_once = base_list.unshift(none_value)
    
    # Test unshift operation with another list
    unshifted_twice = base_list.unshift(unshifted_once)
    
    # Test append operation with None
    appended_list = unshifted_once.append(none_value)
    
    # Test map operation with None function (should execute without error)
    appended_list.map(none_value)

def test_filter_method_with_self_as_argument():
    """
    Test that the ImmutableList.filter() method can be called with the same
    list instance as argument without raising errors.
    """
    # Create a non-empty ImmutableList with False as both head value and is_empty flag
    is_empty_flag = False
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    
    # Call filter with the same list as argument - should not crash
    immutable_list.filter(immutable_list)

def test_filter_on_concatenated_empty_lists():
    """Test that filter can be called on an ImmutableList created by concatenating empty lists."""
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    
    # Concatenate the empty list with itself (results in another empty list)
    concatenated_list = empty_list.__add__(empty_list)
    
    # Get the length of the concatenated list (should be 0)
    length = concatenated_list.__len__()
    
    # Call filter with the length (0) as predicate - should handle empty list case
    concatenated_list.filter(length)

def test_find_on_empty_list_returns_none_and_calls_len():
    """Test that find() on an empty ImmutableList returns None, and that 
    calling __len__() on the result doesn't crash."""
    
    # Create a search value and an empty list (None head and tail)
    search_value = 1947
    none_value = None
    empty_list = immutable_list_module.ImmutableList(none_value, none_value)
    
    # Search for value in empty list (should return None)
    found_value = empty_list.find(search_value)
    
    # Verify we can call __len__ on the result without error
    found_value.__len__()

def test_find_method_with_self_reference_on_boolean_list():
    """
    Tests that the find method can be called on an ImmutableList instance
    when searching for itself, using a boolean value as the initial element.
    """
    # Create an ImmutableList with a boolean element where the element value
    # also serves as the is_empty flag (edge case scenario)
    is_empty_flag = False
    list_instance = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    
    # Attempt to find the list within itself (self-referential search)
    list_instance.find(list_instance)

def test_immutable_list_reduce_and_find_with_false_values():
    """Test ImmutableList operations with False values for reduce and find methods."""
    
    # Create an empty immutable list
    false_value = False
    empty_list = immutable_list_module.ImmutableList()
    
    # Reduce the empty list using False as the function and the list itself as initial value
    reduction_result = empty_list.reduce(false_value, empty_list)
    
    # Create a non-empty list with False as the first element
    list_with_false = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    
    # Attempt to find the list within itself
    list_with_false.find(list_with_false)

def test_create_empty_immutable_list():
    """
    Test that an empty ImmutableList can be instantiated successfully.
    This verifies the basic constructor functionality without any elements.
    """
    # Create an empty immutable list instance
    empty_list = immutable_list_module.ImmutableList()

def test_find_self_on_nonempty_list_with_false_element():
    """Test that find() can be called on a non-empty list with itself as argument."""
    # Create a non-empty list with boolean element False
    bool_element = False
    nonempty_list = immutable_list_module.ImmutableList(bool_element, is_empty=bool_element)
    
    # Get string representation (unused but preserves original behavior)
    string_repr = nonempty_list.__str__()
    
    # Attempt to find the list within itself
    nonempty_list.find(nonempty_list)

def test_unshift_and_find_self_reference():
    """Test that an ImmutableList can unshift itself and then find itself."""
    # Create an ImmutableList with False as head and is_empty=False
    is_empty_flag = False
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    
    # Unshift the list with itself (add itself to the front)
    unshifted_list = immutable_list.unshift(immutable_list)
    
    # Find the original list within itself (self-reference search)
    immutable_list.find(immutable_list)

def test_find_value_in_immutable_list_after_unshift_and_append():
    """
    Test the `find` method on an ImmutableList after performing unshift and append operations.
    Specifically, we create a non-empty list, unshift a value, append the original list,
    and then try to find the value in the resulting list.
    """
    false_value = False
    
    # Create an ImmutableList with is_empty=False (non-empty list)
    original_list = immutable_list_module.ImmutableList(is_empty=false_value)
    
    # Unshift the false value to the original list
    list_after_unshift = original_list.unshift(false_value)
    
    # Append the original list to the list after unshift
    final_list = list_after_unshift.append(original_list)
    
    # Try to find the false value in the final list
    final_list.find(false_value)

def test_find_original_list_within_self():
    """Test that an ImmutableList can find itself when used as a search element.
    
    This test creates an ImmutableList with is_empty=True, appends an element,
    checks the length of the new list, and attempts to find the original list
    within itself using the find() method.
    """
    true_value = True
    
    # Create an ImmutableList with is_empty=True (contradictory but allowed)
    original_list = immutable_list_module.ImmutableList(true_value, is_empty=true_value)
    
    # Append the same value to create a new list
    appended_list = original_list.append(true_value)
    
    # Get the length of the new list
    length_of_appended_list = appended_list.__len__()
    
    # Attempt to find the original list within itself
    original_list.find(original_list)

def test_immutable_list_complex_chain_operations():
    """
    Tests a chain of operations on ImmutableList instances including
    append, reduce, equality check, unshift, string conversion, and find.
    This ensures complex interactions between methods don't produce errors.
    """
    # Create initial empty list
    empty_list = immutable_list_module.ImmutableList()
    
    # Append list to itself (creates a list containing itself as element)
    self_appended_list = empty_list.append(empty_list)
    
    # Reduce the original list using the appended list as both function and initial value
    reduced_result = empty_list.reduce(self_appended_list, self_appended_list)
    
    # Check equality between the appended list and original empty list
    are_equal = self_appended_list.__eq__(empty_list)
    
    # Unshift the appended list onto itself
    unshifted_list = self_appended_list.unshift(self_appended_list)
    
    # Get string representation of unshifted list
    list_str = unshifted_list.__str__()
    
    # Create new list with is_empty parameter set to the string representation
    list_from_string = immutable_list_module.ImmutableList(is_empty=list_str)
    
    # Append reduced result to itself
    appended_reduced = reduced_result.append(reduced_result)
    
    # Try to find reduced result in unshifted list
    unshifted_list.find(reduced_result)

def test_immutable_list_operations_with_nested_lists():
    """
    Tests ImmutableList operations including unshift, reduce, length, 
    equality, and find methods with nested list structures.
    """
    empty_list = immutable_list_module.ImmutableList()
    list_with_empty = empty_list.unshift(empty_list)
    reduced_value = empty_list.reduce(list_with_empty, list_with_empty)
    length_of_list_with_empty = list_with_empty.__len__()
    list_with_self = list_with_empty.unshift(list_with_empty)
    equality_check = list_with_self.__eq__(empty_list)
    list_with_length_flag = immutable_list_module.ImmutableList(is_empty=length_of_list_with_empty)
    reduced_value.find(reduced_value)

def test_reduce_on_immutable_list_with_contradictory_is_empty_flag():
    """
    Tests that ImmutableList.reduce() can be called on a list instance
    created with contradictory parameters (non-empty head but is_empty=True).
    """
    # Create an empty dictionary to use as tail
    empty_dict = {}
    
    # Create first list with empty dict as tail
    list_with_dict_tail = immutable_list_module.ImmutableList(tail=empty_dict)
    
    # Create second list with contradictory state: non-empty head but is_empty=True
    is_empty_flag = True
    list_with_contradictory_state = immutable_list_module.ImmutableList(
        head=is_empty_flag, 
        is_empty=is_empty_flag
    )
    
    # Convert the contradictory list to a regular list
    converted_list = list_with_contradictory_state.to_list()
    
    # Attempt to reduce the contradictory list using its own converted list
    # as both accumulator and initial value
    list_with_contradictory_state.reduce(converted_list, converted_list)

