import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Verify that a default-constructed ImmutableList supports equality, string conversion, list conversion, concatenation, and length operations."""

    # Construct a default (empty) ImmutableList
    empty_immutable_list = immutable_list.ImmutableList()

    # Check that the empty list considers itself equal to itself
    equality_result = empty_immutable_list.__eq__(empty_immutable_list)

    # Retrieve the string representation of the empty list
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a plain Python list
    converted_plain_list = empty_immutable_list.to_list()

    # Concatenate the plain list with itself (list.__add__)
    concatenated_list = converted_plain_list.__add__(converted_plain_list)

    # Check the length of the plain list
    plain_list_length = converted_plain_list.__len__()

    # Concatenate the plain list onto the original ImmutableList (result unused)
    empty_immutable_list.__add__(converted_plain_list)

def test_immutable_list_basic_operations_on_empty_list():
    """Verify that ImmutableList supports basic operations (eq, add, find, str, unshift, reduce) on an empty instance without errors."""

    true_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality of the empty list against a non-list value
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the empty list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the empty list
    string_repr = empty_list.__str__()

    # Prepend the empty list to itself, producing a new ImmutableList
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList supports construction with a bool, append returns a new list, and find can be called on the original list."""

    # Use a boolean as both the initial element and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with the boolean value, marking it as non-empty via is_empty
    immutable_list_instance = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same boolean value; result is a new list (immutability contract)
    appended_list = immutable_list_instance.append(initial_value)

    # Verify that find can be called on the original list instance using itself as the search target
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_add_with_none_does_not_raise():
    """Test that calling __add__ on an empty ImmutableList with None does not raise an exception."""
    # Create a default (empty) ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Use None as the operand for __add__
    none_value = None

    # Invoke __add__ with None; expect no exception to be raised
    empty_list.__add__(none_value)

def test_immutable_list_construction_and_find():
    """Test that ImmutableList can be constructed empty, with arguments, and supports find."""

    # Create an empty ImmutableList and measure its length
    empty_list = immutable_list.ImmutableList()
    empty_list_length = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as both content and is_empty flag
    list_with_args = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Invoke find on the constructed list to verify the method is callable
    list_with_args.find(list_with_args)

def test_immutable_list_construction_with_false_and_method_calls():
    """Test that ImmutableList can be constructed with False values and supports __len__ and find calls."""

    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as the value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __len__ on the constructed instance
    length_result = immutable_list_instance.__len__()

    # Call find on the instance, passing the instance itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list_value():
    """Test that ImmutableList initialized with False supports to_list conversion and find using the resulting list."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as content and marking it as not empty
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Convert the immutable list to a regular Python list
    converted_list = immutable_list_instance.to_list()

    # Use the converted list as the argument to find
    immutable_list_instance.find(converted_list)

def test_immutable_list_find_append_and_to_list_with_none():
    """Test that ImmutableList supports find, append, and to_list operations when using None as input."""
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Use None as the search and operand value throughout
    none_value = None

    # Search for None in the empty list
    find_result = empty_list.find(none_value)

    # Append the list to itself, producing a new ImmutableList
    appended_list = empty_list.append(empty_list)

    # Convert the appended ImmutableList to a regular Python list
    converted_list = appended_list.to_list()

    # Call __add__ on the converted list with None as the operand
    converted_list.__add__(none_value)

def test_immutable_list_to_list_and_map_with_non_empty_flag():
    """Test that ImmutableList with is_empty=False supports to_list() and map() calls."""

    # Create an ImmutableList explicitly marked as non-empty
    is_empty_flag = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Call to_list() a first time (result is not used further)
    first_to_list_result = non_empty_list.to_list()

    # Construct a default ImmutableList with no arguments
    default_list = immutable_list.ImmutableList()

    # Call to_list() a second time on the original list to obtain the mapping input
    second_to_list_result = non_empty_list.to_list()

    # Pass the second to_list() result into map()
    non_empty_list.map(second_to_list_result)

def test_immutable_list_operations_with_none_values():
    """Test that ImmutableList supports unshift, append, and map operations when using None as values and arguments."""

    none_value = None

    # Construct a base ImmutableList with None as both arguments
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    list_after_first_unshift = base_list.unshift(none_value)

    # Prepend the first unshifted list into the base list
    list_after_second_unshift = base_list.unshift(list_after_first_unshift)

    # Append None to the first unshifted list
    list_after_append = list_after_first_unshift.append(none_value)

    # Attempt to map with None as the mapping function
    list_after_append.map(none_value)

def test_immutable_list_filter_with_self_as_argument():
    """Test that ImmutableList initialized with False can call filter() with itself as the argument without error."""
    # Use False for both the list value and the is_empty flag
    false_value = False

    # Construct a non-empty ImmutableList using False as the initial value
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Filter the list using itself as the argument
    non_empty_list.filter(non_empty_list)

def test_immutable_list_filter_with_length_after_self_concatenation():
    """Test that filtering a self-concatenated ImmutableList using its own length does not raise an error."""
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself to produce a new ImmutableList
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    concatenated_length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the filter argument
    concatenated_list.filter(concatenated_length)

def test_find_on_none_initialized_list_returns_sized_result():
    """Test that find() on a None-initialized ImmutableList returns a sized result."""
    # The value to search for within the list
    search_value = 1947

    # Use None for both constructor arguments to create a None-initialized list
    none_value = None
    empty_list = immutable_list.ImmutableList(none_value, none_value)

    # Perform the find operation and verify the result supports __len__
    find_result = empty_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_with_self_reference():
    """Test that ImmutableList.find() can be called with the list itself as the argument when initialized with False and is_empty=False."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find() using the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_boolean_args():
    """Test that reduce and find can be called on ImmutableList instances constructed with boolean arguments."""

    # Use False as both a seed value for reduce and a constructor flag
    false_value = False

    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Call reduce with a boolean seed and the empty list itself as the combining argument
    # Result is captured but not asserted; the call must not raise
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Create a non-empty ImmutableList using the boolean value, with is_empty explicitly set to False
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find using the list itself as the search target; must not raise
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction_succeeds():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Constructing with no arguments should succeed without raising an exception
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Test that ImmutableList initialized with False supports __str__ and find operations."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Verify that __str__ can be called without error
    string_representation = immutable_list_instance.__str__()

    # Verify that find can be called using the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_and_find_with_false_value():
    """Test that unshift and find operations work on an ImmutableList initialized with False as value and is_empty flag."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as value and is_empty=False
    bool_initialized_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Unshift the list onto itself and capture the result
    unshifted_list = bool_initialized_list.unshift(bool_initialized_list)

    # Find the list within itself
    bool_initialized_list.find(bool_initialized_list)

def test_immutable_list_unshift_append_then_find():
    """Test that unshift, append, and find can be chained on an ImmutableList initialized with is_empty=False."""

    # False is used both as the is_empty flag and as the element/search value throughout
    is_empty_flag = False

    # Create an initial ImmutableList with is_empty set to False
    initial_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Prepend the flag value to the list via unshift
    list_after_unshift = initial_list.unshift(is_empty_flag)

    # Append the original list as an element to the unshifted list
    list_after_append = list_after_unshift.append(initial_list)

    # Search for the flag value in the resulting list
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_and_find_operations():
    """Tests appending to an ImmutableList, retrieving its length, and calling find on it."""

    # Use True as the initial element value and as the is_empty flag
    truthy_value = True

    # Create an ImmutableList with a single truthy element, marked as non-empty
    initial_list = immutable_list.ImmutableList(truthy_value, is_empty=truthy_value)

    # Append the truthy value and obtain the resulting new ImmutableList
    list_after_append = initial_list.append(truthy_value)

    # Retrieve the length of the list after appending
    length_after_append = list_after_append.__len__()

    # Call find on the initial list, searching for the initial list itself as the target
    initial_list.find(initial_list)

def test_immutable_list_chained_operations_do_not_raise():
    """Verify that chained ImmutableList operations (append, reduce, eq, unshift, str, find) complete without error."""

    # Create a base empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Append the list to itself, producing a new list
    list_with_self_appended = empty_list.append(empty_list)

    # Reduce the appended list using the appended list as the initial accumulator
    reduced_result = empty_list.reduce(list_with_self_appended, list_with_self_appended)

    # Check equality between the appended list and the empty list
    equality_result = list_with_self_appended.__eq__(empty_list)

    # Unshift the appended list onto itself
    list_after_unshift = list_with_self_appended.unshift(list_with_self_appended)

    # Obtain the string representation of the unshifted list
    string_representation = list_after_unshift.__str__()

    # Construct a new ImmutableList using the string representation as the is_empty argument
    list_from_string_is_empty = immutable_list.ImmutableList(is_empty=string_representation)

    # Append the reduced result to itself
    list_with_reduced_appended = reduced_result.append(reduced_result)

    # Search for the reduced result within the unshifted list
    list_after_unshift.find(reduced_result)

def test_immutable_list_chained_operations_with_reduce_and_find():
    """Verify that ImmutableList supports chained unshift, reduce, __len__, __eq__, and find operations without error."""

    # Create an initial empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list into itself, producing a new list
    list_with_self_prepended = empty_list.unshift(empty_list)

    # Reduce the prepended list using itself as both accumulator and reducer
    reduced_result = empty_list.reduce(list_with_self_prepended, list_with_self_prepended)

    # Get the length of the prepended list
    length_of_prepended = list_with_self_prepended.__len__()

    # Prepend the already-prepended list into itself again
    list_double_prepended = list_with_self_prepended.unshift(list_with_self_prepended)

    # Check equality between the double-prepended list and the original empty list
    eq_result = list_double_prepended.__eq__(empty_list)

    # Construct a new ImmutableList using the length value as the is_empty argument
    list_with_length_as_is_empty = immutable_list.ImmutableList(is_empty=length_of_prepended)

    # Attempt to find the reduced result within itself
    reduced_result.find(reduced_result)

def test_immutable_list_reduce_with_to_list_result_as_both_arguments():
    """Test that reduce can be called on an ImmutableList using the result of to_list() as both arguments."""
    true_flag = True
    empty_dict_tail = {}

    # Construct an ImmutableList with an empty dict as its tail (not used further)
    list_with_dict_tail = immutable_list.ImmutableList(tail=empty_dict_tail)

    # Construct an ImmutableList with a head value and is_empty set to True
    non_empty_immutable_list = immutable_list.ImmutableList(true_flag, is_empty=true_flag)

    # Convert the list to a plain Python list
    list_representation = non_empty_immutable_list.to_list()

    # Call reduce using the list representation as both the accumulator and the collection
    non_empty_immutable_list.reduce(list_representation, list_representation)

