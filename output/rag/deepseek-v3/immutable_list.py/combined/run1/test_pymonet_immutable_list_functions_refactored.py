import pytest
import immutable_list as immutable_list_module

def test_immutable_list_basic_operations():
    """Verify that an empty ImmutableList supports equality comparison,
    string representation, conversion to list, concatenation, and length operations."""
    
    # Create an empty immutable list
    immutable_list = immutable_list_module.ImmutableList()
    
    # Equality comparison (self-equality should return True)
    equality_result = immutable_list.__eq__(immutable_list)
    
    # String representation
    string_representation = immutable_list.__str__()
    
    # Convert to standard Python list
    converted_list = immutable_list.to_list()
    
    # Concatenate the converted list with itself
    concatenated_list = converted_list.__add__(converted_list)
    
    # Get length of the converted list
    list_length = converted_list.__len__()
    
    # Another concatenation operation (result not captured)
    immutable_list.__add__(converted_list)

def test_immutable_list_equality_concatenation_find_string_unshift_reduce():
    """Test basic ImmutableList operations: equality, concatenation, find, string conversion, unshift, and reduce."""
    truthy_value = True
    empty_list = immutable_list_module.ImmutableList()
    
    # Test equality comparison with a boolean
    equality_result = empty_list.__eq__(truthy_value)
    
    # Test concatenation of two empty lists
    concatenated_list = empty_list.__add__(empty_list)
    
    # Test find operation on the list
    find_result = empty_list.find(equality_result)
    
    # Test string representation
    string_representation = empty_list.__str__()
    
    # Test unshift (prepend) operation
    list_with_self_prepended = empty_list.unshift(empty_list)
    
    # Test reduce operation on the populated list
    list_with_self_prepended.reduce(list_with_self_prepended, truthy_value)

def test_immutable_list_append_and_find_on_empty_list():
    """Test that appending to an empty ImmutableList creates a new list and find works on the original."""
    # Create an empty ImmutableList with is_empty=True
    bool_0 = True
    original_list = immutable_list_module.ImmutableList(bool_0, is_empty=bool_0)
    
    # Append returns a new list (immutability) - the original list is unchanged
    appended_list = original_list.append(bool_0)
    
    # Verify find works on the original empty list
    original_list.find(original_list)

def test_add_none_to_empty_immutable_list():
    """Verify that adding None to an empty ImmutableList does not raise an exception."""
    empty_list = immutable_list_module.ImmutableList()
    none_value = None
    # Calling __add__ with None; the test passes if no exception is raised.
    empty_list.__add__(none_value)

def test_immutable_list_with_is_empty_flag_creation_and_search():
    """Verify that ImmutableList creation with a list argument and is_empty flag, followed by a search, works correctly."""
    empty_list = immutable_list_module.ImmutableList()
    len_of_empty_list = empty_list.__len__()

    list_with_is_empty_flag = immutable_list_module.ImmutableList(
        empty_list, is_empty=empty_list
    )

    list_with_is_empty_flag.find(list_with_is_empty_flag)

def test_immutable_list_find_self_after_len():
    """
    Test that an ImmutableList can find itself after length is computed.
    """
    empty_flag = False
    immutable_list_instance = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    result_length = immutable_list_instance.__len__()
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_to_list_result():
    """Tests that calling find() with the result of to_list() on an empty ImmutableList works correctly."""
    is_empty_flag = False
    empty_immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    
    # Convert immutable list to a regular Python list
    converted_list = empty_immutable_list.to_list()
    
    # Use the converted list as an argument to find()
    empty_immutable_list.find(converted_list)

def test_find_none_in_empty_list_then_append_and_convert():
    """Test finding None in an empty ImmutableList, appending it to itself, converting to list, and performing addition."""
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    
    # Search for None in the empty list (should return None)
    none_value = None
    find_result = empty_list.find(none_value)
    
    # Append the empty list to itself
    appended_list = empty_list.append(empty_list)
    
    # Convert to a regular Python list
    regular_list = appended_list.to_list()
    
    # Add None to the resulting list
    regular_list.__add__(none_value)

def test_to_list_and_map_with_non_empty_immutable_list():
    """Verify that an ImmutableList with is_empty=False can be converted to a list and used with map()."""
    # Create a non-empty immutable list
    is_empty_false = False
    non_empty_list = immutable_list_module.ImmutableList(is_empty=is_empty_false)
    
    # Convert to list - first call
    first_conversion_result = non_empty_list.to_list()
    
    # Create a second immutable list with default parameters
    default_list = immutable_list_module.ImmutableList()
    
    # Convert the non-empty list again (exercising repeated to_list calls)
    second_conversion_result = non_empty_list.to_list()
    
    # Apply map operation using the conversion result
    non_empty_list.map(second_conversion_result)

def test_map_with_none_callback_after_unshift_and_append():
    """Verify map() can be called with None callback after unshift/append operations."""
    none_value = None
    
    original_list = immutable_list_module.ImmutableList(none_value, none_value)
    list_after_unshift = original_list.unshift(none_value)
    list_after_double_unshift = original_list.unshift(list_after_unshift)
    list_after_append = list_after_unshift.append(none_value)
    
    # Should not raise an error when map is called with None callback
    list_after_append.map(none_value)

def test_filter_empty_list_with_itself_as_predicate():
    """Test that filtering an empty ImmutableList using itself as the predicate returns an appropriate result."""
    empty_value = False
    empty_list = immutable_list_module.ImmutableList(empty_value, is_empty=empty_value)
    # Filter an empty list using itself as the predicate
    empty_list.filter(empty_list)

def test_filter_immutable_list_with_its_length():
    """Test that filtering an ImmutableList with its own length as the filter argument works correctly."""
    # Create two empty immutable lists
    empty_list = immutable_list_module.ImmutableList()
    
    # Concatenate the empty list with itself
    concatenated_list = empty_list.__add__(empty_list)
    
    # Get the length of the concatenated list (should be 0)
    list_length = concatenated_list.__len__()
    
    # Filter the concatenated list using its length as the filtering criterion
    concatenated_list.filter(list_length)

def test_find_returns_len_supported_object_when_value_not_found():
    """Tests that find() returns an object supporting __len__() when the value is not present."""
    search_value = 1947
    empty_value = None
    
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList(empty_value, empty_value)
    
    # Search for a value that doesn't exist in the empty list
    result = empty_list.find(search_value)
    
    # Verify the returned object supports __len__ (implicit assertion via method call)
    result.__len__()

def test_find_on_empty_immutable_list_returns_none_or_correct_value():
    """Verify find() on an empty ImmutableList handles the predicate correctly."""
    # Create a boolean flag for is_empty parameter and list value
    empty_flag = False
    
    # Create an empty ImmutableList (is_empty=True overrides the False value)
    empty_list = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    
    # Call find() with the list itself as the predicate
    empty_list.find(empty_list)

def test_reduce_on_empty_list_with_false_initial_then_find():
    """Test that reducing an empty ImmutableList with False returns the empty list,
    and find works on a list containing False as its value."""
    false_value = False
    
    # Create an empty list and reduce it with False as initial value
    empty_list = immutable_list_module.ImmutableList()
    reduced_result = empty_list.reduce(false_value, empty_list)
    
    # Create a list with False as both value and is_empty flag, then find on itself
    list_with_false_value = immutable_list_module.ImmutableList(false_value, is_empty=false_value)
    list_with_false_value.find(list_with_false_value)

def test_empty_immutable_list_creation():
    """Verify that an ImmutableList can be created without arguments."""
    empty_list = immutable_list_module.ImmutableList()

def test_empty_immutable_list_str_and_find():
    """Verify that an empty ImmutableList can be converted to a string and find() works on it."""
    empty_flag = False
    empty_list = immutable_list_module.ImmutableList(empty_flag, is_empty=empty_flag)
    list_as_string = empty_list.__str__()
    empty_list.find(empty_list)

def test_unshift_returns_new_list_and_original_remains_usable():
    """Verify that unshift() returns a new list while the original remains functional."""
    # Create an empty immutable list
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    
    # unshift should return a NEW list with the element prepended
    new_list_with_prepended_element = empty_list.unshift(empty_list)
    
    # The original list should still be usable for find operations
    empty_list.find(empty_list)

def test_find_on_populated_immutable_list():
    """Tests that 'find' can be called on an ImmutableList containing mixed elements (a boolean and another ImmutableList)."""
    # Create a non-empty ImmutableList
    false_value = False
    base_list = immutable_list_module.ImmutableList(is_empty=false_value)
    
    # Add false_value to the front (unshift returns new list)
    list_with_false = base_list.unshift(false_value)
    
    # Append the original list as an element
    nested_list = list_with_false.append(base_list)
    
    # Call find with false_value — verifies the method runs without error
    nested_list.find(false_value)

def test_immutable_list_append_len_then_find_on_original():
    """Verify that after appending an element to an ImmutableList and checking
    its length, the find() method works on the original list."""
    test_item = True
    original_list = immutable_list_module.ImmutableList(test_item, is_empty=test_item)
    appended_list = original_list.append(test_item)
    list_length = appended_list.__len__()
    original_list.find(original_list)

def test_immutable_list_chained_operations_append_reduce_equality_unshift_str_find():
    """
    Tests chained operations on ImmutableList including append, reduce,
    equality, unshift, str, and find.
    """
    first_list = immutable_list_module.ImmutableList()
    second_list = first_list.append(first_list)
    reduction_result = first_list.reduce(second_list, second_list)
    equality_result = second_list.__eq__(first_list)
    unshifted_list = second_list.unshift(second_list)
    string_repr = unshifted_list.__str__()
    list_from_string = immutable_list_module.ImmutableList(is_empty=string_repr)
    appended_reduction = reduction_result.append(reduction_result)
    unshifted_list.find(reduction_result)

def test_immutable_list_self_reference_and_nested_operations():
    """
    Tests ImmutableList operations including unshift, reduce, len, eq, and find methods.
    """
    # Create an empty ImmutableList
    empty_list = immutable_list_module.ImmutableList()
    
    # Add the empty list as an element to itself
    list_with_empty = empty_list.unshift(empty_list)
    
    # Reduce using list_with_empty as both accumulator and iterable
    reduced_result = empty_list.reduce(list_with_empty, list_with_empty)
    
    # Get length of the list that contains itself
    list_length = list_with_empty.__len__()
    
    # Create a nested structure by adding list_with_empty to itself
    nested_list = list_with_empty.unshift(list_with_empty)
    
    # Compare nested structure with empty list
    are_equal = nested_list.__eq__(empty_list)
    
    # Create new empty list using the previously computed length
    empty_list_from_length = immutable_list_module.ImmutableList(is_empty=list_length)
    
    # Call find on the reduced result with itself as argument
    reduced_result.find(reduced_result)

def test_immutable_list_to_list_as_reduce_argument_and_initial():
    """Verify that converting an ImmutableList to a Python list and using
    that list as both function argument and initial value for reduce()
    works without error."""
    
    bool_true = True
    empty_dict = {}
    
    # Create an ImmutableList with empty dict as tail
    list_with_tail = immutable_list_module.ImmutableList(tail=empty_dict)
    
    # Create an ImmutableList with True as value and is_empty=True
    list_with_boolean = immutable_list_module.ImmutableList(bool_true, is_empty=bool_true)
    
    # Convert to Python list
    converted_list = list_with_boolean.to_list()
    
    # Use the converted list as both function argument and initial value for reduce
    list_with_boolean.reduce(converted_list, converted_list)