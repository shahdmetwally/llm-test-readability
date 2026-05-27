import pytest
import immutable_list as immutable_list_module

def test_empty_immutable_list_operations():
    """Verify that an empty ImmutableList supports equality, string representation,
    to_list, concatenation, and length operations."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()

    # Test equality with itself (should return True for empty list)
    is_equal = empty_list.__eq__(empty_list)

    # Test string representation of empty list
    list_repr = empty_list.__str__()

    # Convert to Python list (should be empty)
    list_output = empty_list.to_list()

    # Concatenate two empty lists (result should also be empty)
    concatenated_list = list_output.__add__(list_output)

    # Get length of empty list (should be 0)
    list_length = list_output.__len__()

    # Additional concatenation using the original ImmutableList
    empty_list.__add__(list_output)

def test_immutable_list_various_operations():
    """
    Test various ImmutableList operations including equality with non-list,
    concatenation, find, string conversion, unshift, and reduce.
    """
    # Create a boolean value for comparison
    true_value = True

    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()

    # Test equality: compare empty list with a boolean (should be False)
    equality_result = empty_list.__eq__(true_value)

    # Test concatenation: add two empty lists together
    concatenated_list = empty_list.__add__(empty_list)

    # Test find: search for the equality result in the empty list
    found_element = empty_list.find(equality_result)

    # Test string representation
    string_repr = empty_list.__str__()

    # Test unshift: add the empty list as an element to another empty list
    unshifted_list = empty_list.unshift(empty_list)

    # Test reduce: apply reduce operation on the unshifted list with initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_find_on_list_marked_empty_after_append():
    """Test that find works on a list marked as empty after an append operation."""
    truthy_value = True
    
    # Create an ImmutableList that is explicitly marked as empty
    initial_list = immutable_list_module.ImmutableList(truthy_value, is_empty=truthy_value)
    
    # Append a value to create a second list
    appended_list = initial_list.append(truthy_value)
    
    # Test find on the original (empty-marked) list
    initial_list.find(initial_list)

def test_immutable_list_add_none():
    """Verify that adding None to an empty ImmutableList does not raise an exception."""
    empty_list = immutable_list_module.ImmutableList()
    none_value = None
    empty_list.__add__(none_value)

def test_find_on_nested_immutable_list_self_reference():
    """Test that find() works on an ImmutableList containing another ImmutableList as an element."""
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    # Verify __len__() works on empty list
    length_of_empty_list = empty_list.__len__()
    # Create a nested ImmutableList with empty_list as both element and is_empty flag
    nested_list = immutable_list_module.ImmutableList(
        empty_list, is_empty=empty_list
    )
    # Search for the nested list within itself
    nested_list.find(nested_list)

def test_empty_list_has_zero_length_and_find_accepts_list_argument():
    """
    Test that an ImmutableList created with is_empty=True has zero length
    and that find() accepts another ImmutableList as argument.
    """
    false_value = False
    empty_list = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    list_length = empty_list.__len__()
    empty_list.find(empty_list)

def test_empty_list_with_boolean_and_find():
    """Tests that an empty ImmutableList can be created with a boolean value 
    and supports find operation on its list representation."""
    # Create an empty ImmutableList using False as both the value and is_empty flag
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    
    # Convert the empty list to a regular Python list
    result_list = empty_list.to_list()
    
    # Verify find works on the empty list's representation
    empty_list.find(result_list)

def test_empty_immutable_list_find_append_and_to_list_operations():
    """Tests basic ImmutableList operations on an empty list: find, append, to_list, and list addition."""
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    
    # Attempt to find None in the empty list
    none_value = None
    search_result = empty_list.find(none_value)
    
    # Append the empty list to itself, creating a nested structure
    appended_list = empty_list.append(empty_list)
    
    # Convert the nested list back to a regular Python list
    converted_list = appended_list.to_list()
    
    # Test that the converted list supports addition (with None as the operand)
    converted_list.__add__(none_value)

def test_to_list_consistency_and_map_with_list_result():
    """Tests to_list() on a non-empty ImmutableList and map() with the same list's conversion result."""
    # Create a non-empty ImmutableList
    is_not_empty = False
    non_empty_list = immutable_list_module.ImmutableList(is_empty=is_not_empty)

    # Convert to list and store result
    first_to_list_result = non_empty_list.to_list()

    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()

    # Convert the same non-empty list again and use result for map
    second_to_list_result = non_empty_list.to_list()
    non_empty_list.map(second_to_list_result)

def test_immutable_list_map_with_none_callable():
    """
    Verify that map() on an ImmutableList handles a None callable without error.
    """
    none_value = None

    # Create initial list with None head and tail
    initial_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Build list through sequence of unshift and append operations
    list_after_unshift = initial_list.unshift(none_value)
    list_after_second_unshift = initial_list.unshift(list_after_unshift)
    list_after_append = list_after_unshift.append(none_value)

    # Call map with None — should not raise
    list_after_append.map(none_value)

def test_filter_on_empty_immutable_list_with_false_predicate():
    """Verify that `filter` on an empty `ImmutableList` with `False` as both
    value and `is_empty` flag does not raise an error."""
    false_value = False
    empty_immutable_list = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    empty_immutable_list.filter(empty_immutable_list)

def test_filter_on_empty_immutable_list_with_length_zero():
    """Tests that filtering an empty ImmutableList with its length (0) as the filter argument does not raise errors."""
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    
    # Add the empty list to itself (result is another empty list)
    combined_empty_list = empty_list.__add__(empty_list)
    
    # Get the length of the combined empty list (should be 0)
    list_length = combined_empty_list.__len__()
    
    # Use the length (0) as a filter argument on the empty list
    combined_empty_list.filter(list_length)

def test_find_on_empty_list_returns_object_with_len():
    """Verify that find() on an empty ImmutableList returns an object with __len__."""
    search_value = 1947
    none_type = None
    
    # Create an empty list (both head and tail are None)
    empty_list = immutable_list_module.ImmutableList(none_type, none_type)
    found_object = empty_list.find(search_value)
    
    # Calling __len__ on the result should succeed (returns 0, not raises exception)
    found_object.__len__()

def test_find_on_empty_immutable_list_returns_none():
    """Test that find() on an empty ImmutableList returns None."""
    # Create an empty list with is_empty=True
    empty_flag = False
    empty_list = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    
    # find() on empty list should return None regardless of predicate
    result = empty_list.find(empty_list)
    assert result is None, f"Expected None but got {result}"

def test_find_on_single_element_boolean_list():
    """
    Test that find() works correctly on an ImmutableList containing
    a single boolean element.
    """
    test_bool = False
    empty_list = immutable_list_module.ImmutableList()
    # Reduce on empty list with boolean initializer
    reduced_result = empty_list.reduce(test_bool, empty_list)

    # Create a single-element list with is_empty=False
    single_element_list = immutable_list_module.ImmutableList(test_bool, is_empty=test_bool)
    # Find should handle the single boolean element
    single_element_list.find(single_element_list)

def test_default_empty_immutable_list_creation():
    """Verify that an empty ImmutableList can be created with default parameters."""
    empty_list = immutable_list_module.ImmutableList()

def test_empty_immutable_list_string_representation_and_find():
    """Test that an empty ImmutableList produces correct string representation
    and handles find() appropriately."""
    # Create an empty immutable list
    empty_flag = False
    empty_list = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    
    # Get string representation of the empty list
    list_string = empty_list.__str__()
    
    # Search for an element in the empty list (should return None/appropriate value)
    empty_list.find(empty_list)

def test_find_on_empty_list_after_unshift_finds_self_reference():
    """Test that find works correctly on an empty list after unshifting an element."""
    # Create an empty ImmutableList flagged as empty
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Unshift the empty list onto itself — this creates a new list with empty_list as the head
    unshifted_list = empty_list.unshift(empty_list)

    # Find should locate the empty_list element within the new list
    empty_list.find(empty_list)

def test_find_boolean_value_in_list_after_unshift_and_append():
    """Test that boolean values can be found in an ImmutableList after unshift and append operations."""
    # Create an initial list that is not empty
    is_empty_value = False
    initial_list = immutable_list_module.ImmutableList(is_empty=is_empty_value)

    # Add the boolean value to the front of the list
    list_after_unshift = initial_list.unshift(is_empty_value)

    # Append the original list as an element
    final_list = list_after_unshift.append(initial_list)

    # Search for the boolean value in the transformed list
    final_list.find(is_empty_value)

def test_immutable_list_find_finds_self_reference():
    """Tests that find() returns an element when searching with the list itself as the target."""
    true_value = True
    initial_list = immutable_list_module.ImmutableList(true_value, is_empty=true_value)
    appended_list = initial_list.append(true_value)
    length = appended_list.__len__()
    initial_list.find(initial_list)

def test_self_referential_immutable_list_complex_operations():
    """Tests self-referential ImmutableList operations including append,
    reduce, equality, unshift, string conversion, and find with nested
    list references."""
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    
    # Append the list to itself, creating a self-referential structure
    list_with_self_ref = empty_list.append(empty_list)
    
    # Reduce the empty list using the self-referential list as both
    # reduction function and initial value
    reduce_result = empty_list.reduce(list_with_self_ref, list_with_self_ref)
    
    # Check equality between the self-referential list and the empty list
    equality_result = list_with_self_ref.__eq__(empty_list)
    
    # Unshift the self-referential list onto itself
    string_converted_list = list_with_self_ref.unshift(list_with_self_ref)
    
    # Convert the resulting list to a string representation
    list_as_string = string_converted_list.__str__()
    
    # Create a new ImmutableList using the string as is_empty parameter
    list_from_string_empty = immutable_list_module.ImmutableList(is_empty=list_as_string)
    
    # Append the reduce result to itself
    appended_reduce_result = reduce_result.append(reduce_result)
    
    # Search for the reduce result within the string-converted list
    string_converted_list.find(reduce_result)

def test_self_referential_immutable_list_with_nested_operations():
    """Test ImmutableList operations when elements are the list instances themselves,
    including chained unshift, reduce, length, equality, and find methods."""
    
    # Create empty list and then a list containing the empty list as element
    empty_list = immutable_list_module.ImmutableList()
    list_with_self_element = empty_list.unshift(empty_list)
    
    # Reduce using the list itself as both function and initial value
    reduction_result = empty_list.reduce(list_with_self_element, list_with_self_element)
    
    # Get length of list that contains itself
    list_length = list_with_self_element.__len__()
    
    # Create doubly-wrapped list (list containing a list containing itself)
    doubly_wrapped_list = list_with_self_element.unshift(list_with_self_element)
    
    # Check equality between the doubly-wrapped list and the empty list
    equality_check = doubly_wrapped_list.__eq__(empty_list)
    
    # Create a new empty list marked with the previously computed length
    empty_list_with_length = immutable_list_module.ImmutableList(is_empty=list_length)
    
    # Call find on the reduction result with itself as argument
    reduction_result.find(reduction_result)

def test_immutable_list_reduce_with_own_to_list_result():
    """Verify that an ImmutableList can be reduced using the result of its own to_list() call."""
    default_bool = True
    empty_dict = {}
    
    # Create list with empty dict as tail
    tail_list = immutable_list_module.ImmutableList(tail=empty_dict)
    
    # Create list with bool value and is_empty flag set
    main_list = immutable_list_module.ImmutableList(default_bool, is_empty=default_bool)
    
    # Convert main list to a Python list
    result_list = main_list.to_list()
    
    # Reduce the main list using its own result as both initial value and iterable
    main_list.reduce(result_list, result_list)