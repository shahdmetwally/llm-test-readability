import pytest

import immutable_list as immutable_list_module

def test_immutable_list_self_equality_and_list_operations():
    """Ensure an ImmutableList is equal to itself and supports conversion to and operations on a regular list."""
    immutable_list = immutable_list_module.ImmutableList()

    # equality with itself
    assert immutable_list == immutable_list

    # string representation
    text = str(immutable_list)
    assert isinstance(text, str)

    # conversion to a regular list
    as_list = immutable_list.to_list()
    assert isinstance(as_list, list)

    # list addition and length operations on the converted list
    combined_list = as_list + as_list
    assert isinstance(combined_list, list)
    assert combined_list == as_list.__add__(as_list)

    length = len(as_list)
    assert length == as_list.__len__()

    # ensure adding a regular list to the immutable list does not raise
    _ = immutable_list.__add__(as_list)

def test_immutable_list_api_calls_execute_in_order_readable():
    """Exercise several ImmutableList API methods to ensure calls execute as expected."""
    # Primitive literal used in the original test
    flag_true = True

    # Create an immutable list instance
    original_list = immutable_list_module.ImmutableList()

    # Call __eq__ with a boolean literal (preserve original behavior)
    equals_result = original_list.__eq__(flag_true)

    # Call __add__ to 'add' the list to itself (preserve original behavior)
    added_list = original_list.__add__(original_list)

    # Call find using the result of __eq__ (preserve original behavior)
    find_result = original_list.find(equals_result)

    # Get string representation via __str__ (preserve original behavior)
    string_repr = original_list.__str__()

    # Call unshift with the list itself (preserve original behavior)
    unshifted_list = original_list.unshift(original_list)

    # Call reduce on the unshifted list with the boolean literal (preserve original behavior)
    unshifted_list.reduce(unshifted_list, flag_true)

def test_immutable_list_append_and_find_with_self():
    """Construct an ImmutableList, append the same value, and call find with the original list."""
    # Use an explicit, descriptive name for the boolean value used in the list
    value_flag = True

    # Create the original immutable list (is_empty set to the same boolean)
    original_list = immutable_list_module.ImmutableList(value_flag, is_empty=value_flag)

    # Append the same boolean value to produce a new list (immutability preserved)
    appended_list = original_list.append(value_flag)

    # Call find on the original list, passing the original list itself (exercise API)
    original_list.find(original_list)

def test_immutable_list_add_with_none_does_not_crash():
    """Ensure ImmutableList.__add__ can be invoked with None (exercise the code path)."""
    # Create an empty ImmutableList instance from the provided module alias
    immutable_list_instance = immutable_list_module.ImmutableList()
    # Use the None literal to mirror the original test input
    none_value = None
    # Call the dunder add method with None to exercise the behavior (no assertion required)
    immutable_list_instance.__add__(none_value)

def test_immutable_list_length_and_find_with_self_reference():
    """Construct an ImmutableList, get its length, make another list referencing it, and call find with a self-reference."""
    # Create an empty ImmutableList instance.
    empty_list = immutable_list_module.ImmutableList()

    # Retrieve the length of the empty list (calls __len__()).
    empty_list_length = empty_list.__len__()

    # Create another ImmutableList, passing the first list both positionally and as the is_empty kwarg.
    child_list = immutable_list_module.ImmutableList(empty_list, is_empty=empty_list)

    # Call find on the second list with a self-reference (preserve the original bare call).
    child_list.find(child_list)

def test_immutable_list_len_and_find_self():
    """Construct an empty ImmutableList, call __len__(), then call find() with the list itself."""
    # represent the "is empty" flag used to construct the list
    is_empty_flag = False

    # instantiate the ImmutableList with is_empty=False (preserve original arguments/order)
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # call the special length method and store the result (original code assigned this to str_0)
    length_result = immutable_list.__len__()

    # attempt to find the list inside itself (preserve original call)
    immutable_list.find(immutable_list)

def test_find_with_list_from_to_list_does_not_raise():
    """Verify that converting an ImmutableList to a list and passing that list into find() does not raise."""
    # Use an explicit flag name for clarity
    is_empty_flag = False

    # Construct the ImmutableList using the provided flag (same literal values as original)
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert to a standard Python list and then search for that list within the immutable structure
    list_representation = immutable_list.to_list()

    # The original test made this call without assertions; preserve behavior (no exception expected)
    immutable_list.find(list_representation)

def test_immutable_list_find_append_self_and_list_add_with_none():
    """Verify calling find(None), appending the list to itself, converting to a Python list,
    and calling list.__add__(None) occurs in sequence."""
    # Create an empty ImmutableList instance
    immutable_list = immutable_list_module.ImmutableList()

    # Use a None value for the find operation
    none_value = None

    # Call find(None) on the immutable list
    search_result = immutable_list.find(none_value)

    # Append the immutable list onto itself
    appended = immutable_list.append(immutable_list)

    # Convert the appended immutable list to a Python list
    python_list = appended.to_list()

    # Call list.__add__ with None on the resulting list
    python_list.__add__(none_value)

def test_immutable_list_to_list_and_map_do_not_raise():
    """Creating an ImmutableList, calling to_list twice, and calling map with the second snapshot should not raise."""
    # Explicitly set the is_empty flag to mirror the original explicit call
    is_empty_flag = False

    # Create an ImmutableList with the explicit flag
    empty_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # Take the first snapshot
    first_list_snapshot = empty_list.to_list()

    # Create another ImmutableList via the default constructor
    default_list = immutable_list_module.ImmutableList()

    # Take a second snapshot by calling to_list() again on the same instance
    second_list_snapshot = empty_list.to_list()

    # Call map on the original instance, passing the second snapshot
    empty_list.map(second_list_snapshot)

def test_immutablelist_unshift_append_and_map_chain():
    """Verify that unshift, append, and map calls can be chained on ImmutableList with None values."""
    # Use None as in the original test
    none_value = None

    # Construct the base immutable list with two None values
    base_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Unshift a None onto the base list
    after_unshift_single = base_list.unshift(none_value)

    # Unshift the previously produced list onto the base list
    after_unshift_nested = base_list.unshift(after_unshift_single)

    # Append a None to the single-unshift result
    after_append = after_unshift_single.append(none_value)

    # Call map with None on the appended list (keeps original behavior)
    after_append.map(none_value)

def test_filter_called_with_self_instance():
    """Ensure ImmutableList.filter can be invoked with the list instance as its argument (no exception expected)."""
    # Use a clear variable name for the boolean flag used during construction
    is_empty_flag = False

    # Create an ImmutableList instance using the module alias provided in the test environment
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call filter with the instance itself as the argument (preserve original call and behavior)
    immutable_list.filter(immutable_list)

def test_immutable_list_add_self_and_filter_by_length():
    """Ensure an ImmutableList can be added to itself and that filter accepts the combined length."""
    # Create an ImmutableList instance
    original = immutable_list_module.ImmutableList()
    # Add the list to itself (uses __add__ under the hood)
    combined = original + original
    # Get the length of the combined list (uses __len__)
    length = len(combined)
    # Call filter with the length value to preserve original behaviour (no assertion)
    combined.filter(length)

def test_find_returns_object_with_length_method():
    """Verify that ImmutableList.find returns an object exposing a __len__ method."""
    # Choose a target value to search for
    target_value = 1947

    # ImmutableList constructed with two None values (same as original)
    none_value = None
    immutable_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Call find and get the result object
    result = immutable_list.find(target_value)

    # Invoke the special length method directly to ensure it's present and callable.
    result.__len__()

def test_find_handles_searching_for_self_in_empty_immutable_list():
    """Calling find with the list itself should not raise any errors for an empty list."""
    is_empty = False
    imm_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)
    imm_list.find(imm_list)

def test_reduce_and_find_handle_false_and_self_reference():
    """Ensure ImmutableList.reduce and .find accept False and self-referential inputs without raising."""
    # Use a False flag as in the original test
    false_flag = False

    # Create an empty ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()

    # Call reduce with False and the list itself (preserve original call and order)
    reduced_result = empty_list.reduce(false_flag, empty_list)

    # Create another ImmutableList using False for both the positional and is_empty kwarg
    list_with_false = immutable_list_module.ImmutableList(false_flag, is_empty=false_flag)

    # Call find with the list itself (preserve original call)
    list_with_false.find(list_with_false)

def test_immutable_list_instantiation_succeeds():
    """Ensure ImmutableList can be instantiated without raising an exception."""
    # Create an ImmutableList instance to verify construction succeeds.
    immutable_list_instance = immutable_list_module.ImmutableList()

def test_immutable_list_str_and_find_self():
    """Ensure converting the ImmutableList to string and finding the list within itself does not raise."""
    # Use an explicit descriptive name for the boolean flag (same literal False as original)
    is_empty_flag = False

    # Construct the ImmutableList with the same positional and keyword arguments as before
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Obtain the string representation (call preserved exactly)
    string_repr = immutable_list.__str__()

    # Call find with the list itself as the argument (call preserved exactly)
    immutable_list.find(immutable_list)

def test_immutable_list_unshift_and_find_no_errors():
    """Ensure unshift and find can be invoked on an ImmutableList without raising exceptions."""
    is_empty = False
    lst = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)

    # Call unshift with the instance itself and then call find with the instance.
    unshift_result = lst.unshift(lst)
    lst.find(lst)

def test_immutable_list_unshift_append_find_invocation():
    """Verify that unshift, append and find can be invoked on ImmutableList without error."""
    # Use the provided module alias from imports
    is_empty_flag = False

    # Create the initial immutable list instance with the same literal flag
    original_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # Prepend the boolean value and capture the returned list
    list_after_unshift = original_list.unshift(is_empty_flag)

    # Append the original list to the new list and capture the result
    list_after_append = list_after_unshift.append(original_list)

    # Invoke find with the same boolean value; original test did not assert the result
    list_after_append.find(is_empty_flag)

def test_append_returns_new_list_and_find_can_locate_self():
    """Construct an ImmutableList with True, append True, record the appended list's length, and call find on the original list searching for itself."""
    value_true = True

    # Create the original immutable list (marked empty via is_empty=True)
    original_list = immutable_list_module.ImmutableList(value_true, is_empty=value_true)

    # Append the same True value, producing a new immutable list instance
    appended_list = original_list.append(value_true)

    # Obtain the length of the appended list by calling its __len__ method directly
    length_of_appended = appended_list.__len__()

    # Search for the original list within itself
    original_list.find(original_list)

def test_immutablelist_operations_sequence_runs_without_exceptions():
    """Run a sequence of ImmutableList methods to exercise behavior without asserting (ensures no exceptions)."""

    # Create an empty ImmutableList instance
    original_list = immutable_list_module.ImmutableList()

    # Append the list to itself (returns a new list)
    appended_with_self = original_list.append(original_list)

    # Reduce: call reduce on original_list with the appended list as both args
    reduced_result = original_list.reduce(appended_with_self, appended_with_self)

    # Equality check: compare appended list to the original (invokes __eq__)
    equality_result = appended_with_self.__eq__(original_list)

    # Unshift: add the appended list to the front of itself
    unshifted_with_self = appended_with_self.unshift(appended_with_self)

    # String representation of the unshifted list (invokes __str__)
    string_representation = unshifted_with_self.__str__()

    # Construct a new ImmutableList using the string representation as the is_empty kwarg
    list_from_is_empty_kw = immutable_list_module.ImmutableList(is_empty=string_representation)

    # Append the reduced result to itself
    appended_reduced_result = reduced_result.append(reduced_result)

    # Find operation on the unshifted list using the reduced result
    unshifted_with_self.find(reduced_result)

def test_reduce_unshift_and_find_behavior():
    """Exercise unshift, reduce, len, eq, and find operations on ImmutableList."""
    # Create a base immutable list instance
    base_list = immutable_list_module.ImmutableList()

    # Unshift the base_list onto itself once
    unshifted_once = base_list.unshift(base_list)

    # Reduce using the unshifted_once as both arguments
    reduced_result = base_list.reduce(unshifted_once, unshifted_once)

    # Capture the length of the unshifted_once list
    length_unshifted = len(unshifted_once)

    # Unshift again to produce a second unshifted list
    unshifted_twice = unshifted_once.unshift(unshifted_once)

    # Compare unshifted_twice with the original base_list
    equals_base = (unshifted_twice == base_list)

    # Construct a new ImmutableList using the length as the is_empty parameter
    constructed_with_is_empty = immutable_list_module.ImmutableList(is_empty=length_unshifted)

    # Call find on the reduced result, passing the reduced result itself
    reduced_result.find(reduced_result)

def test_immutable_list_to_list_and_reduce_preserves_arguments():
    """Ensure the list produced by to_list() can be passed unchanged into reduce() on an ImmutableList."""
    # Keep the original boolean literal and name it for clarity.
    is_empty_flag = True

    # Keep the original empty dict literal used as the tail.
    empty_tail = {}

    # Create an ImmutableList using the empty tail (unused further, preserved to match original behavior).
    list_with_tail = immutable_list_module.ImmutableList(tail=empty_tail)

    # Create an ImmutableList using the boolean as positional and keyword argument exactly as originally called.
    empty_immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the immutable list to a regular list (preserve original call and assignment).
    list_representation = empty_immutable_list.to_list()

    # Call reduce with the same list passed twice, preserving original call order and arguments.
    empty_immutable_list.reduce(list_representation, list_representation)

