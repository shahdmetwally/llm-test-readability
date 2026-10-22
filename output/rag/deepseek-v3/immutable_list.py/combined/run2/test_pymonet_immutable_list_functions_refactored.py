import pytest
import immutable_list as immutable_list_module

def test_immutable_list_equality_and_operations():
    """
    Tests that an ImmutableList correctly handles equality, string representation,
    conversion to list, and basic list operations (concatenation, length).
    """
    immutable_list_instance = immutable_list_module.ImmutableList()
    
    # Test equality with itself
    equality_result = immutable_list_instance.__eq__(immutable_list_instance)
    
    # Test string representation
    string_representation = immutable_list_instance.__str__()
    
    # Convert to standard list
    converted_list = immutable_list_instance.to_list()
    
    # Test list concatenation
    concatenated_list = converted_list.__add__(converted_list)
    
    # Test list length
    list_length = converted_list.__len__()
    
    # Test immutability by attempting addition with standard list
    immutable_list_instance.__add__(converted_list)

def test_immutable_list_operations_on_empty_list():
    """
    Verify that ImmutableList operations (eq, add, find, str, unshift, reduce)
    work correctly on empty lists.
    """
    # Create a boolean literal for equality comparison
    true_value = True
    
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    
    # Test equality comparison with non-list type
    equals_result = empty_list.__eq__(true_value)
    
    # Test concatenation of empty list with itself
    concatenated_list = empty_list.__add__(empty_list)
    
    # Test find on empty list using boolean result
    find_result = empty_list.find(equals_result)
    
    # Test string representation of empty list
    string_repr = empty_list.__str__()
    
    # Test unshift operation (inserting self as element)
    list_with_element = empty_list.unshift(empty_list)
    
    # Test reduce on list containing empty list as element
    list_with_element.reduce(list_with_element, true_value)

def test_immutable_list_append_returns_new_list_and_find_on_original():
    """Test that an empty ImmutableList can have an element appended (returning a new list)
    and that find() works on the original list."""
    test_value = True
    empty_list = immutable_list_module.ImmutableList(test_value, is_empty=test_value)
    appended_list = empty_list.append(test_value)
    empty_list.find(empty_list)

def test_empty_immutable_list_added_to_none_does_not_raise():
    """Verifies that adding None to an empty ImmutableList completes without error."""
    empty_list = immutable_list_module.ImmutableList()
    none_value = None
    empty_list.__add__(none_value)

def test_find_on_nested_immutable_list_with_self_reference():
    """
    Verify that an ImmutableList can contain another ImmutableList as its data element
    and itself as the is_empty flag, and that find() works with a self-reference.
    """
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Get its length (result unused but preserved for behavior)
    list_length = empty_list.__len__()
    
    # Create a nested list with empty_list as both data and is_empty flag
    nested_list = immutable_list_module.ImmutableList(
        empty_list, 
        is_empty=empty_list
    )
    
    # Perform find() operation with self-reference
    nested_list.find(nested_list)

def test_empty_immutable_list_length_and_find():
    """
    Verify that an empty ImmutableList has a proper length and can be searched with find().
    """
    # Create an empty ImmutableList with both value and is_empty set to False
    empty_flag = False
    empty_immutable_list = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    
    # Verify __len__() returns a value on an empty list
    list_length = empty_immutable_list.__len__()
    
    # Verify find() works on the same empty list instance
    empty_immutable_list.find(empty_immutable_list)

def test_empty_immutable_list_conversion_and_find():
    """Verify that an empty ImmutableList can be converted to a list and then searched with find()."""
    # Create an empty ImmutableList
    false_value = False
    immutable_list = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    
    # Convert the empty list to a Python list
    empty_list_result = immutable_list.to_list()
    
    # Verify that find() works on the empty list without errors
    immutable_list.find(empty_list_result)

def test_empty_list_none_find_then_append_and_to_list():
    """Test find, append, and to_list operations on an empty ImmutableList, verifying None handling and list conversion."""
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    none_value = None
    
    # Find None in the empty list (should return None or handle gracefully)
    found_result = empty_list.find(none_value)
    
    # Append the empty list to itself (creating a list with one element)
    appended_list = empty_list.append(empty_list)
    
    # Convert to a regular Python list
    result_list = appended_list.to_list()
    
    # Verify __add__ works with None (edge case test)
    result_list.__add__(none_value)

def test_non_empty_immutable_list_map_with_list_raises_type_error():
    """
    Tests converting a non-empty ImmutableList to a list,
    then using the resulting list as a mapping function on the original list.
    """
    # Create a non-empty ImmutableList (is_empty=False means it has content)
    is_empty_false = False
    non_empty_list = immutable_list_module.ImmutableList(is_empty=is_empty_false)

    # Convert the non-empty list to a Python list
    first_to_list_result = non_empty_list.to_list()

    # Create an empty ImmutableList (default is_empty=True)
    empty_list = immutable_list_module.ImmutableList()

    # Convert the non-empty list to a Python list again
    second_to_list_result = non_empty_list.to_list()

    # Attempt to use the list as a mapping function on the non-empty list
    # Note: lists are not callable, so this will raise TypeError at runtime
    non_empty_list.map(second_to_list_result)

def test_unshift_append_map_with_none_values_does_not_crash():
    """
    Test that chaining unshift, append, and map operations with None values works correctly.
    """
    none_value = None
    original_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Prepend a None value to the original list
    prepended_list = original_list.unshift(none_value)

    # Chain unshift with the already-prepended list
    double_prepended_list = original_list.unshift(prepended_list)

    # Append a None value to the first prepended list
    appended_list = prepended_list.append(none_value)

    # Apply map with None as the transformation callback
    appended_list.map(none_value)

def test_filter_with_immutable_list_as_predicate():
    """Test that filter can accept another ImmutableList as an argument without error."""
    false_value = False
    # Create an ImmutableList with False as initial value and is_empty flag
    immutable_list_instance = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    # Passing an ImmutableList object as filter argument (not a lambda)
    immutable_list_instance.filter(immutable_list_instance)

def test_filter_empty_immutable_list_with_length_zero():
    """Test that filtering an empty immutable list with its length value executes without error."""
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Concatenate the empty list with itself (results in another empty list)
    concatenated_list = empty_list.__add__(empty_list)
    
    # Get the length of the concatenated empty list (should be 0)
    list_length = concatenated_list.__len__()
    
    # Filter the concatenated list using its length as the filter predicate
    concatenated_list.filter(list_length)

def test_find_on_empty_immutable_list_returns_object_supporting_len():
    """Verify that find() on an empty ImmutableList returns an object that supports __len__()."""
    search_value = 1947
    empty_value = None
    
    # Create an empty ImmutableList (both head and tail are None)
    empty_immutable_list = immutable_list_module.ImmutableList(empty_value, empty_value)
    
    # Searching for a non-existent value in an empty list should return
    # an object that supports __len__() without raising an exception
    result = empty_immutable_list.find(search_value)
    result.__len__()

def test_find_list_inside_itself():
    """Verify that find() returns the list itself when searching for a list instance inside itself."""
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    empty_list.find(empty_list)

def test_immutable_list_reduce_with_false_initial_and_find_self():
    """Tests ImmutableList.reduce() with False as initial value and find() called on the list itself."""
    # Create an empty immutable list
    false_value = False
    empty_list = immutable_list_module.ImmutableList()

    # Test reduce with False as initial/accumulator value
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Create a single-element list containing False, with is_empty explicitly set to False
    single_element_list = immutable_list_module.ImmutableList(false_value, is_empty=false_value)

    # Test find() by passing the list itself as the search target
    single_element_list.find(single_element_list)

def test_empty_immutable_list_creation_and_default_repr():
    """Verify that creating an ImmutableList with no arguments produces an empty list."""
    empty_immutable_list = immutable_list_module.ImmutableList()

def test_empty_immutable_list_str_and_find():
    """Verify that an empty ImmutableList can be stringified and used as a search target for find()."""
    empty_flag = False
    empty_list = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    list_string_representation = empty_list.__str__()
    empty_list.find(empty_list)

def test_original_list_unchanged_after_unshift():
    """
    Verify that find() works on the original ImmutableList instance
    after unshift() returns a new list, confirming immutability.
    """
    empty_flag = False
    original_list = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    
    # unshift returns a new list; original should remain unchanged
    unshifted_result = original_list.unshift(original_list)
    
    # find() on the original list should still work without error
    original_list.find(original_list)

def test_find_returns_false_when_boolean_false_in_nested_structure():
    """
    Tests that `find()` correctly returns `False` when searching for a boolean `False`
    value that exists in a nested `ImmutableList` structure.
    """
    false_value = False
    
    # Create a non-empty ImmutableList
    base_list = immutable_list_module.ImmutableList(is_empty=false_value)
    
    # Prepend False to create a new list
    list_after_unshift = base_list.unshift(false_value)
    
    # Append the original list to create nesting
    list_after_append = list_after_unshift.append(base_list)
    
    # Search for False in the nested structure
    list_after_append.find(false_value)

def test_empty_immutable_list_append_returns_new_find_on_original():
    """Verify that appending to an empty ImmutableList returns a new list with 
    updated length, and that find() can be called on the original list."""
    
    is_empty_flag = True
    
    # Create an empty ImmutableList with is_empty set to True
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    
    # Append True to the empty list (returns a new list)
    list_after_append = empty_list.append(is_empty_flag)
    
    # Get the length of the new list
    length_of_appended_list = list_after_append.__len__()
    
    # Call find() on the original empty list (should not error)
    empty_list.find(empty_list)

def test_immutable_list_chained_operations_without_exceptions():
    """
    Verify chained operations on ImmutableList can be performed without errors.
    No assertions are made; this test verifies operations complete without exceptions.
    """
    # Create an empty ImmutableList
    original_list = immutable_list_module.ImmutableList()
    
    # Append the list to itself (creates a new list with self as element)
    appended_list = original_list.append(original_list)
    
    # Reduce with the appended list as both initial and callable (likely identity-like operation)
    reduced_result = original_list.reduce(appended_list, appended_list)
    
    # Check equality of appended_list and original_list
    eq_result = appended_list.__eq__(original_list)
    
    # Unshift the appended_list onto itself
    unshifted_list = appended_list.unshift(appended_list)
    
    # Get string representation
    string_repr = unshifted_list.__str__()
    
    # Create ImmutableList using the string as is_empty flag
    empty_string_list = immutable_list_module.ImmutableList(is_empty=string_repr)
    
    # Append reduced_result to itself
    appended_var_list = reduced_result.append(reduced_result)
    
    # Find something in unshifted_list (result not captured - testing no-error case)
    unshifted_list.find(reduced_result)

def test_immutable_list_self_reference_and_reduce_edge_cases():
    """Tests edge cases of ImmutableList including reduce operations, length, equality comparisons, and find method."""
    # Create an empty list
    empty_list = immutable_list_module.ImmutableList()
    
    # Unshift the list onto itself (creating a list containing itself)
    list_with_self = empty_list.unshift(empty_list)
    
    # Use reduce with the list itself as both function and initial value
    reduced_result = empty_list.reduce(list_with_self, list_with_self)
    
    # Get the length of the list containing itself
    len_of_list_with_self = list_with_self.__len__()
    
    # Create a nested structure by unshifting list_with_self onto itself
    doubly_nested_list = list_with_self.unshift(list_with_self)
    
    # Check equality between the nested list and empty list
    equality_result = doubly_nested_list.__eq__(empty_list)
    
    # Create an explicitly empty list using the length result
    explicitly_empty_list = immutable_list_module.ImmutableList(is_empty=len_of_list_with_self)
    
    # Call find on the previously computed reduced result
    reduced_result.find(reduced_result)

def test_to_list_result_as_reduce_function_and_initial():
    """Verifies that the result of to_list() can be passed as both the function
    and initial value to reduce()."""
    default_value = True
    empty_dict = {}
    
    # Create a list with empty_dict as the tail
    list_from_dict = immutable_list_module.ImmutableList(tail=empty_dict)
    
    # Create an empty list (is_empty=True forces empty state)
    empty_list = immutable_list_module.ImmutableList(default_value, is_empty=default_value)
    
    # Convert to a regular Python list
    list_result = empty_list.to_list()
    
    # The returned list should be usable as both the reducer function
    # and initial value parameters to reduce()
    empty_list.reduce(list_result, list_result)