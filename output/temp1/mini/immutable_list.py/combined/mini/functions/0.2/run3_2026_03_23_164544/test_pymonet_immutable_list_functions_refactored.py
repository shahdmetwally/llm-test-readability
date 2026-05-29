import pytest

import immutable_list as immutable_list_module

def test_immutable_list_basic_methods_can_be_called():
    """Call basic ImmutableList methods (equality, str, to_list, add, len) to ensure they can be invoked."""
    # Create an ImmutableList instance
    imm_list = immutable_list_module.ImmutableList()

    # Equality check with itself
    is_equal = (imm_list == imm_list)

    # String representation
    string_repr = str(imm_list)
    assert isinstance(string_repr, str)

    # Convert to a built-in Python list
    python_list = imm_list.to_list()
    assert isinstance(python_list, list)

    # Add the python list to itself (list concatenation)
    concatenated_list = python_list + python_list
    assert isinstance(concatenated_list, list)

    # Length of the python list
    list_length = len(python_list)
    assert isinstance(list_length, int)

    # Call add on the original ImmutableList with the python list (invoke __add__)
    imm_list.__add__(python_list)

def test_immutable_list_operations_execute_in_sequence():
    """Exercise a sequence of ImmutableList operations to ensure methods execute without raising errors."""
    # A non-list value to compare against using __eq__
    non_list_value = True

    # Create an ImmutableList instance
    lst = immutable_list_module.ImmutableList()

    # Check equality against a non-list value (calls __eq__)
    equals_result = lst.__eq__(non_list_value)

    # Add/concatenate the list with itself (calls __add__)
    concatenated = lst.__add__(lst)

    # Try to find the result of the equality call within the list (calls find)
    find_result = lst.find(equals_result)

    # Get the string representation (calls __str__)
    text_repr = lst.__str__()

    # Prepend the list to itself (calls unshift)
    prepended = lst.unshift(lst)

    # Reduce the prepended list using the same values as in the original test (calls reduce)
    prepended.reduce(prepended, non_list_value)

def test_immutable_list_append_and_find_self():
    """Appending to an empty ImmutableList yields a new list and find can be called with the original as target."""
    # Use an explicit boolean value for clarity.
    value_true = True

    # Create an ImmutableList marked as empty.
    empty_list = immutable_list_module.ImmutableList(value_true, is_empty=value_true)

    # Append the same boolean value to produce a new ImmutableList instance.
    appended_list = empty_list.append(value_true)

    # Call find on the original empty list, searching for the original empty list itself.
    empty_list.find(empty_list)

def test_add_none_does_not_raise_exception():
    """Verify that calling ImmutableList.__add__ with None does not raise an exception."""
    # Create an ImmutableList instance
    immutable_list_instance = immutable_list_module.ImmutableList()
    # Use a clearly named variable for the None argument
    other_value = None
    # Invoke the dunder add method with None; test passes if no exception is raised
    immutable_list_instance.__add__(other_value)

def test_find_called_with_self_and_is_empty_flag():
    """Ensure creating an ImmutableList from another and calling find with the list itself executes without error."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()
    # Record its length (preserve explicit __len__ call from original test)
    empty_length = empty_list.__len__()
    # Create a new ImmutableList initialized from the first, passing the first as is_empty as in the original
    derived_list = immutable_list_module.ImmutableList(empty_list, is_empty=empty_list)
    # Call find on the derived list with itself (original behavior preserved)
    derived_list.find(derived_list)

def test_find_self_and_len_on_non_empty_immutable_list():
    """Ensure an ImmutableList reports length and can find itself when not empty."""
    is_empty_flag = False
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__() explicitly (preserve the original call)
    length = imm_list.__len__()

    # Attempt to find the list object within itself (preserve the original call)
    imm_list.find(imm_list)

def test_find_accepts_to_list_result_without_error():
    """Ensure ImmutableList.find accepts the result of to_list() without raising."""
    # Explicit boolean flag for clarity
    is_empty_flag = False

    # Construct an ImmutableList with the same arguments as the original test
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the immutable structure to a plain list and pass it to find
    list_result = immutable_list.to_list()
    immutable_list.find(list_result)

def test_append_self_to_list_and_call_add_with_none():
    """Exercise ImmutableList.find(None), append the list to itself, convert to list, and call __add__ with None."""
    # Create a new ImmutableList instance
    original_list = immutable_list_module.ImmutableList()

    # Search for None in the immutable list (should not raise)
    found_result = original_list.find(None)

    # Append the list to itself and ensure we still have an ImmutableList
    appended_list = original_list.append(original_list)
    assert isinstance(appended_list, immutable_list_module.ImmutableList)

    # Convert the appended list to a Python list and check the type
    list_as_pylist = appended_list.to_list()
    assert isinstance(list_as_pylist, list)

    # Invoke the list's __add__ method with None to ensure it does not raise
    _ = list_as_pylist.__add__(None)

def test_map_accepts_list_from_to_list():
    """Ensure ImmutableList.map can be called with a list produced by to_list."""
    # Create an ImmutableList that is not marked empty
    is_empty_flag = False
    original_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # Capture a snapshot of the list as a Python list
    first_snapshot = original_list.to_list()

    # Create another ImmutableList instance to mirror original test flow
    another_list = immutable_list_module.ImmutableList()

    # Capture a second snapshot from the original list and call map with it
    second_snapshot = original_list.to_list()
    original_list.map(second_snapshot)

def test_immutable_list_unshift_append_map_chain():
    """Verify that ImmutableList supports unshift, append, and map call chaining without errors."""
    none_value = None

    # Construct the base ImmutableList with two None elements
    base_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Unshift None onto the base list (creates a new list)
    first_unshifted = base_list.unshift(none_value)

    # Unshift the previously created list onto the base list
    second_unshifted = base_list.unshift(first_unshifted)

    # Append None to the first unshifted list (creates another new list)
    appended_list = first_unshifted.append(none_value)

    # Call map on the appended list with None (preserve original call; result unused)
    appended_list.map(none_value)

def test_filter_called_with_self_does_not_raise():
    """Ensure that calling filter on an ImmutableList with the list itself does not raise."""
    # Use an explicit, descriptive name for the boolean flag
    is_empty_flag = False

    # Construct the ImmutableList using the same positional and keyword arguments as before
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call filter with the list itself (preserve original call; the test ensures no exception is raised)
    immutable_list.filter(immutable_list)

def test_immutable_list_add_self_length_and_filter():
    """Combine an ImmutableList with itself, get its length, and call filter using that length."""
    # Create an empty ImmutableList instance
    original_list = immutable_list_module.ImmutableList()

    # Add the original list to itself and store the result using operator syntax for readability
    combined_list = original_list + original_list

    # Obtain the length of the combined list using len()
    length = len(combined_list)

    # Call filter on the combined list using the obtained length
    combined_list.filter(length)

def test_find_returns_sequence_with_length_accessible_on_none_elements():
    """Ensure that calling find on an ImmutableList containing None elements
    returns a result whose length can be accessed."""
    # Value to search for (not present in the list)
    search_value = 1947

    # Construct an ImmutableList with None elements
    none_value = None
    immutable_list_instance = immutable_list_module.ImmutableList(none_value, none_value)

    # Call find() with the search value and then access the length of the result.
    # This exercises find() and __len__() while preserving the original behavior.
    find_result = immutable_list_instance.find(search_value)
    _ = len(find_result)

def test_find_accepts_self_without_raising():
    """Ensure ImmutableList.find can accept the list itself as the lookup value without raising."""
    # Use an explicit False flag as in the original test to mark emptiness.
    is_empty_flag = False

    # Construct the ImmutableList instance with the is_empty flag.
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call find with the instance itself to verify no exception is raised.
    imm_list.find(imm_list)

def test_reduce_with_false_and_find_self():
    """Call reduce on an empty ImmutableList with False and call find on a list
    constructed with False/is_empty=False to ensure these operations execute.
    """
    # Use an explicit boolean variable for clarity.
    flag_false = False

    # Create an empty ImmutableList.
    empty_list = immutable_list_module.ImmutableList()

    # Call reduce on the empty list with False and the list itself.
    reduced_result = empty_list.reduce(flag_false, empty_list)

    # Construct a new ImmutableList with False and is_empty=False.
    list_with_false_is_empty = immutable_list_module.ImmutableList(flag_false, is_empty=flag_false)

    # Call find on the list, looking for itself.
    list_with_false_is_empty.find(list_with_false_is_empty)

def test_immutable_list_can_be_constructed():
    """Ensure ImmutableList can be instantiated without raising an exception."""
    # Instantiating should not raise; also assert we got an object back.
    immutable_list_instance = immutable_list_module.ImmutableList()
    assert immutable_list_instance is not None

def test_immutablelist_str_and_find_with_self_does_not_raise():
    """Construct an ImmutableList with is_empty=False, call __str__, then call find(self) to ensure these methods run without raising."""
    # Use the same boolean value for the positional argument and the is_empty keyword argument
    is_empty_flag = False
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Exercise the string conversion path (result deliberately unused)
    repr_str = imm_list.__str__()

    # Exercise the find method by searching for the list instance itself (result deliberately unused)
    imm_list.find(imm_list)

def test_unshift_and_find_with_self_reference():
    """Ensure unshift can accept the list itself as an element and find can be called with the list as target."""
    # Indicate the list is non-empty (original test used False)
    is_empty_flag = False

    # Construct the original ImmutableList instance
    original_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Prepend the list to itself; unshift should return a new ImmutableList instance
    new_list = original_list.unshift(original_list)

    # Call find on the original list with the original list as the search target
    original_list.find(original_list)

def test_find_can_be_called_after_unshift_and_append_with_false():
    """Verify that find(False) can be invoked after unshift(False) and append(original_list) without raising."""
    # Use the False literal as in the original test
    value_false = False

    # Create the initial immutable list (was immutable_list_0)
    original_list = immutable_list_module.ImmutableList(is_empty=value_false)

    # Unshift False onto the original list (was immutable_list_1)
    unshifted_list = original_list.unshift(value_false)

    # Append the original list to the unshifted list (was immutable_list_2)
    appended_list = unshifted_list.append(original_list)

    # Call find(False) on the final list to ensure the operation runs (no assertion; just ensure no exception)
    appended_list.find(value_false)

def test_immutablelist_append_and_find_behaviour():
    """Create an ImmutableList with is_empty=True, append an element, get its length, and call find on the original list."""
    # The boolean literal True is intentionally used for both the initial value and the is_empty flag.
    initial_flag = True

    # Construct the original immutable list instance.
    original_list = immutable_list_module.ImmutableList(initial_flag, is_empty=initial_flag)

    # Append the same boolean value to create a new immutable list (original should remain unchanged).
    appended_list = original_list.append(initial_flag)

    # Obtain the length of the appended list via __len__ (preserve the original explicit call).
    length_after_append = appended_list.__len__()

    # Call find on the original list, passing the original list itself as the search target.
    original_list.find(original_list)

def test_immutable_list_basic_operations_sequence():
    """Exercise a sequence of ImmutableList operations to ensure methods execute in order without error."""
    # Create an empty base list
    base_list = immutable_list_module.ImmutableList()

    # Append the base list to itself
    appended_once = base_list.append(base_list)

    # Reduce using the original base_list and the appended result
    reduced_result = base_list.reduce(appended_once, appended_once)

    # Check equality method between appended result and base list (result is unused; keeps original call)
    equals_result = appended_once.__eq__(base_list)

    # Unshift the appended result onto itself
    unshifted_list = appended_once.unshift(appended_once)

    # Obtain the string representation of the unshifted list
    string_repr = unshifted_list.__str__()

    # Construct a new ImmutableList using the string representation as the is_empty argument
    constructed_from_str = immutable_list_module.ImmutableList(is_empty=string_repr)

    # Append the reduced result to itself
    appended_reduced = reduced_result.append(reduced_result)

    # Call find on the unshifted list with the reduced result
    unshifted_list.find(reduced_result)

def test_immutablelist_unshift_reduce_find_interactions():
    """Exercise unshift, reduce, __len__, __eq__, and find interactions on ImmutableList."""
    # Create an empty ImmutableList instance
    original_list = immutable_list_module.ImmutableList()

    # Unshift the original list into itself -> produces a new ImmutableList
    unshifted_once = original_list.unshift(original_list)

    # Call reduce on the original list using the unshifted_once as both the function/accumulator args
    reduced_result = original_list.reduce(unshifted_once, unshifted_once)

    # Get the length of the unshifted_once list
    length_of_unshifted = unshifted_once.__len__()

    # Unshift the unshifted_once into itself to produce another new list
    unshifted_twice = unshifted_once.unshift(unshifted_once)

    # Check equality between the twice-unshifted list and the original list
    is_equal_to_original = unshifted_twice.__eq__(original_list)

    # Create another ImmutableList with is_empty flag set to the obtained length
    new_list_with_is_empty = immutable_list_module.ImmutableList(is_empty=length_of_unshifted)

    # Call find on the reduced result with the reduced result as the argument
    reduced_result.find(reduced_result)

def test_reduce_accepts_to_list_output_as_args():
    """Ensure that ImmutableList.reduce can be called with the list produced by to_list without raising."""
    # Setup flags and simple tail data exactly as in the original test
    is_empty_flag = True
    tail_dict = {}

    # Create an ImmutableList with an explicit tail (not used further here)
    list_with_tail = immutable_list_module.ImmutableList(tail=tail_dict)

    # Create an ImmutableList using a positional True and is_empty=True as in the original call
    empty_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Obtain a list representation from the empty_list instance
    to_list_result = empty_list.to_list()

    # Call reduce with the same list object for both arguments, preserving original call/order
    empty_list.reduce(to_list_result, to_list_result)

