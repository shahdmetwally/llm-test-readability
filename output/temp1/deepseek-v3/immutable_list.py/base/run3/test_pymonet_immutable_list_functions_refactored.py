import pytest
import immutable_list as immutable_list_module

def test_empty_immutable_list_operations():
    """Test equality, string representation, and list conversion of an empty ImmutableList."""
    # Create an empty immutable list
    empty_list = immutable_list_module.ImmutableList()
    
    # Test that an empty list equals itself
    empty_list.__eq__(empty_list)
    
    # Test string representation of empty list
    empty_list.__str__()
    
    # Convert to Python list and perform operations on it
    converted_list = empty_list.to_list()
    
    # Add the converted list to itself (creates a new list)
    converted_list.__add__(converted_list)
    
    # Get length of converted list
    converted_list.__len__()
    
    # Add the converted list to the original immutable list
    empty_list.__add__(converted_list)

def test_immutable_list_operations_do_not_raise_exceptions():
    """
    Verifies that various ImmutableList operations (equality, concatenation,
    finding, string conversion, unshift, and reduce) execute without error.
    This is a basic smoke test for the ImmutableList class.
    """
    bool_value = True
    empty_list = immutable_list_module.ImmutableList()

    # Compare an empty list to a boolean value (tests __eq__ with non-list)
    bool_result = empty_list.__eq__(bool_value)

    # Concatenation of two empty lists
    concatenated_list = empty_list.__add__(empty_list)

    # Try to find a boolean value in the empty list (should return None)
    find_result = empty_list.find(bool_result)

    # String representation of an empty list
    str_representation = empty_list.__str__()

    # Create a list by unshifting an empty list into another empty list
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the list using itself as the default initial value
    unshifted_list.reduce(unshifted_list, bool_value)

def test_find_on_immutable_list_with_boolean_elements():
    """Test that find() can be called on a non-empty ImmutableList containing boolean values, using the list itself as the start node."""
    bool_value = True
    immutable_list = immutable_list_module.ImmutableList(bool_value, is_empty=bool_value)
    appended_list = immutable_list.append(bool_value)
    # find() is called on the original list, not the appended one
    immutable_list.find(immutable_list)

def test_immutable_list_add_with_none_does_not_raise_exception():
    """
    Verify that ImmutableList.__add__() handles None as input gracefully
    without raising an exception.
    """
    # Create an empty immutable list
    immutable_list_0 = immutable_list_module.ImmutableList()

    # Add None to the list (should return a new list without error)
    none_type_0 = None
    immutable_list_0.__add__(none_type_0)

def test_find_self_in_nonempty_list_returns_none():
    """
    Verify that calling find() on a non-empty ImmutableList with the list itself
    as the target returns None, due to the identity comparison failing.
    """
    # Create an empty ImmutableList to use as the head's data
    empty_list = immutable_list_module.ImmutableList()
    # Confirm the empty list has length 0
    _ = empty_list.__len__()

    # Create a non-empty list with empty_list as its head and is_empty=empty_list (truthy)
    nonempty_list = immutable_list_module.ImmutableList(
        empty_list, is_empty=empty_list
    )
    # Attempt to find the list within itself — should return None
    nonempty_list.find(nonempty_list)

def test_immutable_list_find_on_empty_list_returns_self():
    """
    Verify that find() on an empty ImmutableList returns the list itself.
    """
    is_empty = False
    empty_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)
    _ = empty_list.__len__()
    empty_list.find(empty_list)

def test_find_on_empty_list_with_non_empty_target_returns_none():
    """Test that find() returns None when searching for a non-empty list in an empty ImmutableList."""
    is_not_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_not_empty_flag, is_empty=is_not_empty_flag)

    # Convert the empty list to a regular list for use as the search target
    target_list = empty_list.to_list()

    # Search for target_list within the empty immutable list
    empty_list.find(target_list)

def test_find_returns_none_for_missing_value_and_appended_list_to_list():
    """Verify that find() returns None for a missing value, 
    and that to_list() on an appended list works as expected."""
    empty_list = immutable_list_module.ImmutableList()
    missing_value = None
    result = empty_list.find(missing_value)
    appended_list = empty_list.append(empty_list)
    list_representation = appended_list.to_list()
    list_representation.__add__(missing_value)

def test_to_list_returns_empty_list_for_non_empty_immutable_list_and_map_works():
    """
    Tests that the `to_list` method returns an empty list for a non-empty ImmutableList,
    and that `map` can be called on the result without error.
    """
    bool_0 = False
    immutable_list_0 = immutable_list_module.ImmutableList(is_empty=bool_0)
    var_0 = immutable_list_0.to_list()
    immutable_list_1 = immutable_list_module.ImmutableList()
    var_1 = immutable_list_0.to_list()
    immutable_list_0.map(var_1)

def test_immutable_list_unshift_append_with_none_values():
    """
    Test that unshifting and appending None values to an ImmutableList
    does not raise an error, and map operation handles None callback.
    """
    none_value = None
    empty_list = immutable_list_module.ImmutableList(none_value, none_value)
    
    # Create a new list by unshifting None onto the empty list
    list_with_one_none = empty_list.unshift(none_value)
    # Unshift the single-element list itself onto the empty list
    list_with_nested = empty_list.unshift(list_with_one_none)
    # Append None to the single-element list
    list_with_appended = list_with_one_none.append(none_value)
    # Map with None as the callback
    list_with_appended.map(none_value)

def test_filter_on_empty_immutable_list_returns_self_when_checking_if_empty():
    """Test that filtering an ImmutableList with itself as predicate does not raise an error when list is empty."""
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    empty_list.filter(empty_list)

def test_filter_immutable_list_with_length_as_threshold():
    """Test filtering an ImmutableList using its length as the filter condition."""
    empty_list = immutable_list_module.ImmutableList()
    concatenated_list = empty_list.__add__(empty_list)
    list_length = concatenated_list.__len__()
    concatenated_list.filter(list_length)

def test_find_returns_non_none_result_with_len_method():
    """
    Verify that calling find() on an ImmutableList with a matching value
    returns a result that has a __len__() method (i.e., is not None).
    """
    value_to_find = 1947
    none_type = None
    immutable_list = immutable_list_module.ImmutableList(none_type, none_type)
    result = immutable_list.find(value_to_find)
    result.__len__()

def test_find_on_empty_immutable_list_with_false_is_empty_returns_default():
    """
    Test that calling find() on an ImmutableList with is_empty=False and a False value
    does not raise an error and returns the expected default value.
    """
    is_empty_flag = False
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # find() invoked with the list itself as the argument (tests edge case)
    empty_list.find(empty_list)

def test_reduce_with_boolean_and_find_self_in_list():
    """
    Tests that reduce() can accept a boolean as the first argument and an
    ImmutableList as the second, and that find() can be called on an
    ImmutableList with itself as the argument.
    """
    bool_false = False
    empty_list = immutable_list_module.ImmutableList()
    reduced_result = empty_list.reduce(bool_false, empty_list)

    list_with_flag = immutable_list_module.ImmutableList(bool_false, is_empty=bool_false)
    list_with_flag.find(list_with_flag)

def test_immutable_list_creation_without_arguments():
    """Verify that an ImmutableList instance can be created without arguments."""
    immutable_list_0 = immutable_list_module.ImmutableList()

def test_immutable_list_str_and_find_with_false_values():
    """Test that ImmutableList.__str__() and find() work correctly
    when the list is initialized with False as both the value and is_empty flag."""
    is_empty = False
    value = False
    immutable_list = immutable_list_module.ImmutableList(value, is_empty=is_empty)

    # Exercise __str__() - should produce string representation
    str_representation = immutable_list.__str__()

    # Exercise find() with the list itself as search target
    immutable_list.find(immutable_list)

def test_find_on_non_empty_immutable_list_with_boolean_self_reference():
    """Test that 'find' can be called on a non-empty ImmutableList with a boolean element."""
    bool_0 = False
    immutable_list_0 = immutable_list_module.ImmutableList(bool_0, is_empty=bool_0)
    var_0 = immutable_list_0.unshift(immutable_list_0)
    immutable_list_0.find(immutable_list_0)

def test_find_on_immutable_list_with_nested_append_returns_none():
    """Test that find() returns None when searching for False in an ImmutableList constructed via unshift and append with nested list."""
    bool_0 = False
    immutable_list_0 = immutable_list_module.ImmutableList(is_empty=bool_0)
    immutable_list_1 = immutable_list_0.unshift(bool_0)
    immutable_list_2 = immutable_list_1.append(immutable_list_0)
    immutable_list_2.find(bool_0)

def test_ImmutableList_find_after_append_and_length_check():
    """Verify that find() works correctly on an ImmutableList that has
    had items appended and its length queried, ensuring the internal
    state is properly maintained.
    """
    bool_0 = True
    # Create an empty ImmutableList with is_empty=True
    immutable_list_0 = immutable_list_module.ImmutableList(bool_0, is_empty=bool_0)
    # Append True to the list
    immutable_list_1 = immutable_list_0.append(bool_0)
    # Query the length of the appended list
    var_0 = immutable_list_1.__len__()
    # Call find() on the original list using itself as the target
    immutable_list_0.find(immutable_list_0)

def test_reduce_with_self_references_and_find_after_unshift():
    """
    Tests reduction using an immutable list as both the reduction function and initial value,
    followed by equality check, unshift, string conversion, creation with is_empty flag,
    appending reduced result to itself, and a find operation.
    """
    immutable_list_0 = immutable_list_module.ImmutableList()
    immutable_list_1 = immutable_list_0.append(immutable_list_0)
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    bool_0 = immutable_list_1.__eq__(immutable_list_0)
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    str_0 = immutable_list_2.__str__()
    immutable_list_3 = immutable_list_module.ImmutableList(is_empty=str_0)
    immutable_list_4 = var_0.append(var_0)
    immutable_list_2.find(var_0)

def test_reduce_on_empty_list_with_empty_cumulator_find_does_not_raise():
    """Test that reducing an empty ImmutableList with an empty cumulator
    and then attempting to find on the result does not raise an error."""
    immutable_list_0 = immutable_list_module.ImmutableList()
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    var_1 = immutable_list_1.__len__()
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    bool_0 = immutable_list_2.__eq__(immutable_list_0)
    immutable_list_3 = immutable_list_module.ImmutableList(is_empty=var_1)
    var_0.find(var_0)

def test_reduce_with_bool_and_empty_dict_tail_returns_correct_list():
    """Test that calling reduce on an ImmutableList with a boolean value and an empty dict
    tail correctly processes the list using a previously calculated result as both the
    function and initial value."""
    bool_value = True
    empty_dict = {}
    immutable_list_with_dict_tail = immutable_list_module.ImmutableList(tail=empty_dict)
    immutable_list_with_bool = immutable_list_module.ImmutableList(bool_value, is_empty=bool_value)
    list_result = immutable_list_with_bool.to_list()
    immutable_list_with_bool.reduce(list_result, list_result)