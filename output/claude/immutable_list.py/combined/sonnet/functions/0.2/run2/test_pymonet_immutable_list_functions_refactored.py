import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Tests that an empty ImmutableList supports equality, string conversion, to_list, concatenation, and length operations."""

    # Create an empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Verify the list compares equal to itself
    equality_result = empty_immutable_list.__eq__(empty_immutable_list)

    # Verify the list can be converted to a string representation
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a plain mutable list
    mutable_list = empty_immutable_list.to_list()

    # Verify mutable list supports self-concatenation via __add__
    concatenated_list = mutable_list.__add__(mutable_list)

    # Verify the mutable list reports its length
    list_length = mutable_list.__len__()

    # Verify ImmutableList supports __add__ with a mutable list (result intentionally discarded)
    empty_immutable_list.__add__(mutable_list)

def test_immutable_list_core_operations_do_not_raise():
    """Verify that ImmutableList supports eq, add, find, str, unshift, and reduce without raising errors."""

    non_list_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Test equality comparison against a non-list value
    eq_result = empty_list.__eq__(non_list_value)

    # Test concatenation of the list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Test searching for the equality result within the list
    find_result = empty_list.find(eq_result)

    # Test string representation of the list
    str_repr = empty_list.__str__()

    # Test prepending the list to itself (unshift)
    unshifted_list = empty_list.unshift(empty_list)

    # Test reduce operation on the unshifted list
    unshifted_list.reduce(unshifted_list, non_list_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList supports construction with a bool, append returns a new list, and find can be called on the original list."""
    # Use a boolean as both the initial element and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with the boolean value
    immutable_list_instance = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same boolean value; result is a new list (immutability contract)
    appended_list = immutable_list_instance.append(initial_value)

    # Call find on the original list, searching for the list itself
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_add_with_none_does_not_raise():
    """Test that calling __add__ with None on an empty ImmutableList does not raise an exception."""
    # Create a default empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the immutable list; should not raise
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_construction_and_find_with_self_reference():
    """Test that ImmutableList supports nested construction and self-referential find calls."""

    # Create a default empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Retrieve the length of the empty list
    empty_list_length = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as both
    # the data source and the is_empty indicator
    nested_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Call find on the nested list using itself as the search target
    nested_list.find(nested_list)

def test_immutable_list_operations_with_none_values():
    """Tests that ImmutableList handles None in construction and chained unshift, append, and map calls without error."""
    none_value = None

    # Construct a base ImmutableList with None as both arguments
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    list_after_unshift_none = base_list.unshift(none_value)

    # Prepend the previously unshifted list into the base list
    list_after_unshift_list = base_list.unshift(list_after_unshift_none)

    # Append None to the list that had None unshifted
    list_after_append_none = list_after_unshift_none.append(none_value)

    # Map with None as the mapping function
    list_after_append_none.map(none_value)

def test_immutable_list_filter_with_immutable_list_argument():
    """Test that ImmutableList.filter() accepts another ImmutableList as its argument without raising an error."""
    # Use False for both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList that is explicitly marked as non-empty
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Filter the list using itself as the filter argument
    immutable_list_instance.filter(immutable_list_instance)

def test_immutable_list_add_self_then_filter_by_length():
    """Test that an ImmutableList can be concatenated with itself, its length retrieved, and filter called with that length."""

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Concatenate the list with itself using __add__
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    concatenated_length = concatenated_list.__len__()

    # Call filter on the concatenated list using its own length as the argument
    concatenated_list.filter(concatenated_length)

def test_find_on_none_initialized_list_returns_sized_result():
    """Test that find() on a None-initialized ImmutableList returns a sized result."""

    # The value to search for within the list
    search_value = 1947

    # Use None for both constructor arguments to create a minimally initialized list
    none_value = None
    empty_immutable_list = immutable_list.ImmutableList(none_value, none_value)

    # Perform the find operation and verify the result supports len()
    find_result = empty_immutable_list.find(search_value)
    find_result.__len__()

def test_immutable_list_unshift_and_find_with_self_reference():
    """Test that ImmutableList supports unshift with itself and find using itself when initialized with False values."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Create an ImmutableList initialized with False, explicitly not marked as empty
    false_initialized_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Unshift the list onto itself, producing a new list
    unshifted_list = false_initialized_list.unshift(false_initialized_list)

    # Search for the list within itself
    false_initialized_list.find(false_initialized_list)

def test_immutable_list_unshift_append_and_find_with_false_value():
    """Test that an ImmutableList supports unshift, append, and find operations chained together."""
    # Use False as both the is_empty flag and the value to operate on
    false_value = False

    # Create an ImmutableList with is_empty=False
    empty_flag_list = immutable_list.ImmutableList(is_empty=false_value)

    # Unshift false_value onto the front of the list
    list_after_unshift = empty_flag_list.unshift(false_value)

    # Append the original list to the unshifted list
    list_after_append = list_after_unshift.append(empty_flag_list)

    # Search for false_value in the resulting list
    list_after_append.find(false_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that appending to an ImmutableList returns a new list with a valid length, and that find can be called on the original list."""
    # Use a boolean True as both the initial element and the is_empty flag
    initial_value = True

    # Create an ImmutableList with the boolean value, marking it as non-empty via is_empty=True
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same boolean value to produce a new immutable list
    list_after_append = original_list.append(initial_value)

    # Retrieve the length of the list after appending
    length_after_append = list_after_append.__len__()

    # Perform a find on the original list using itself as the search target
    original_list.find(original_list)

def test_immutable_list_chained_operations_append_reduce_unshift_find():
    """Tests chained ImmutableList operations: append, reduce, eq, unshift, str, construction with keyword, and find."""

    # Create an empty ImmutableList as the base structure
    empty_list = immutable_list.ImmutableList()

    # Append the empty list to itself, producing a new list
    list_with_self_appended = empty_list.append(empty_list)

    # Reduce using the appended list as both the accumulator and the reducer
    reduced_result = empty_list.reduce(list_with_self_appended, list_with_self_appended)

    # Check equality between the appended list and the original empty list
    equality_check = list_with_self_appended.__eq__(empty_list)

    # Prepend the appended list to itself via unshift
    list_after_unshift = list_with_self_appended.unshift(list_with_self_appended)

    # Obtain the string representation of the unshifted list
    string_repr = list_after_unshift.__str__()

    # Construct a new ImmutableList using the string repr as the is_empty keyword argument
    list_with_is_empty_flag = immutable_list.ImmutableList(is_empty=string_repr)

    # Append the reduced result to itself
    list_with_reduced_appended = reduced_result.append(reduced_result)

    # Search for the reduced result within the unshifted list
    list_after_unshift.find(reduced_result)

def test_immutable_list_chained_operations_unshift_reduce_find():
    """Tests chained ImmutableList operations: unshift, reduce, len, eq, and find, including construction with is_empty."""

    # Create an initial empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list to itself, producing a new list
    list_with_self_unshifted = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as both accumulator and reducer
    reduced_result = empty_list.reduce(list_with_self_unshifted, list_with_self_unshifted)

    # Get the length of the unshifted list
    length_of_unshifted = list_with_self_unshifted.__len__()

    # Prepend the unshifted list to itself again
    list_double_unshifted = list_with_self_unshifted.unshift(list_with_self_unshifted)

    # Check equality between the double-unshifted list and the original empty list
    eq_result = list_double_unshifted.__eq__(empty_list)

    # Construct a new ImmutableList using the computed length as the is_empty flag
    list_with_is_empty_flag = immutable_list.ImmutableList(is_empty=length_of_unshifted)

    # Invoke find on the reduced result using itself as the search predicate
    reduced_result.find(reduced_result)

def test_immutable_list_reduce_with_to_list_result_as_both_arguments():
    """Test that reduce can be called on an ImmutableList using the result of to_list() as both arguments."""
    flag_true = True
    empty_tail = {}

    # Construct a list with an empty dict as its tail (result unused but exercises the constructor)
    list_with_empty_tail = immutable_list.ImmutableList(tail=empty_tail)

    # Construct a non-empty list, explicitly marking it as non-empty via is_empty=True
    non_empty_list = immutable_list.ImmutableList(flag_true, is_empty=flag_true)

    # Convert the list to a plain Python list
    list_representation = non_empty_list.to_list()

    # Call reduce using the list representation as both the combining function and initial value
    non_empty_list.reduce(list_representation, list_representation)

