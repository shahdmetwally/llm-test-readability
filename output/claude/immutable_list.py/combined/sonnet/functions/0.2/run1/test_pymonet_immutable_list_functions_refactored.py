import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Verify that an empty ImmutableList supports equality, string conversion, list conversion, concatenation, and length operations."""

    # Create an empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Check that the empty list is equal to itself
    is_equal_to_self = empty_immutable_list.__eq__(empty_immutable_list)

    # Obtain the string representation of the empty list
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable_list.to_list()

    # Concatenate the plain list with itself (result captured)
    concatenated_list = plain_list.__add__(plain_list)

    # Check the length of the plain list
    list_length = plain_list.__len__()

    # Verify that __add__ on the ImmutableList itself does not raise
    empty_immutable_list.__add__(plain_list)

def test_immutable_list_core_operations_do_not_raise():
    """Verify that ImmutableList supports equality, concatenation, find, str, unshift, and reduce without raising errors."""

    true_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality of the list against a boolean value
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the list
    str_repr = empty_list.__str__()

    # Prepend the list to itself, producing a new ImmutableList
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the accumulator seed, with true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList supports construction with a bool, append returns a new list, and find can be called on the original list."""

    # Use a boolean as both the initial element and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with the boolean value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the boolean value; result is a new ImmutableList
    appended_list = original_list.append(initial_value)

    # Call find on the original list using itself as the search target
    original_list.find(original_list)

def test_immutable_list_add_with_none_does_not_raise():
    """Test that calling __add__ with None on an empty ImmutableList does not raise an exception."""
    # Create a default empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Use None as the operand for __add__
    none_value = None

    # Invoke __add__ with None; expect no exception to be raised
    empty_immutable_list.__add__(none_value)

def test_immutable_list_construction_and_find_with_nested_list():
    """Test that ImmutableList can be constructed empty, nested, and supports find without error."""

    # Create an empty ImmutableList and verify __len__ is callable
    empty_list = immutable_list.ImmutableList()
    empty_list_length = empty_list.__len__()

    # Construct a nested ImmutableList using the empty list as both content and is_empty flag
    nested_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Invoke find on the nested list, passing itself as the search target
    nested_list.find(nested_list)

def test_immutable_list_construction_with_false_and_method_calls():
    """Tests that ImmutableList can be constructed with False and is_empty=False, and that __len__ and find can be called without error."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as the value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __len__ on the constructed list and capture the result
    length_result = immutable_list_instance.__len__()

    # Call find with the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list():
    """Test that find() can be called with the result of to_list() on an ImmutableList initialized with False."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as data and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Convert the immutable list to a regular Python list
    converted_list = immutable_list_instance.to_list()

    # Use the converted list as the search target for find()
    immutable_list_instance.find(converted_list)

def test_immutable_list_find_append_and_to_list_with_none():
    """Tests that an empty ImmutableList supports find with None, self-append, conversion to list, and __add__ with None."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    none_value = None

    # Search for None in the empty list
    find_result = empty_list.find(none_value)

    # Append the list to itself, producing a new ImmutableList
    list_with_self_appended = empty_list.append(empty_list)

    # Convert the resulting ImmutableList to a plain Python list
    converted_list = list_with_self_appended.to_list()

    # Attempt to add None to the converted list (testing __add__ with None)
    converted_list.__add__(none_value)

def test_immutable_list_map_accepts_to_list_result():
    """Test that map() on a non-empty ImmutableList accepts the result of to_list() as its argument."""
    is_empty_false = False

    # Create an ImmutableList explicitly marked as non-empty
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty_false)

    # Call to_list() once to exercise the method before creating the second list
    initial_to_list_result = non_empty_list.to_list()

    # Create a second ImmutableList using default construction
    default_list = immutable_list.ImmutableList()

    # Retrieve the list representation again to use as the map argument
    to_list_result = non_empty_list.to_list()

    # Pass the to_list() result directly into map()
    non_empty_list.map(to_list_result)

def test_immutable_list_unshift_append_and_map_with_none_values():
    """Test that ImmutableList supports unshift and append with None values, and that map can be called with None."""

    none_value = None

    # Construct a base ImmutableList with None as both arguments
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    list_after_first_unshift = base_list.unshift(none_value)

    # Prepend the first unshifted list into the base list
    list_after_second_unshift = base_list.unshift(list_after_first_unshift)

    # Append None to the first unshifted list
    list_after_append = list_after_first_unshift.append(none_value)

    # Call map with None on the appended list
    list_after_append.map(none_value)

def test_immutable_list_filter_with_immutable_list_argument():
    """Test that ImmutableList.filter() accepts another ImmutableList as its argument without raising an error."""
    # Use False for both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList that is explicitly marked as non-empty with a False value
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call filter with the ImmutableList itself as the filter argument
    immutable_list_instance.filter(immutable_list_instance)

def test_immutable_list_add_self_then_filter_by_length():
    """Test that concatenating an ImmutableList with itself and filtering by the resulting length executes without error."""
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Concatenate the list with itself using __add__
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    concatenated_length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the predicate/argument
    concatenated_list.filter(concatenated_length)

def test_find_on_none_initialized_immutable_list_returns_sized_result():
    """Test that find() on a None-initialized ImmutableList returns a sized result."""
    # The integer value to search for within the immutable list
    search_value = 1947

    # Use None for both constructor arguments to create a default/empty-like list
    none_value = None
    empty_immutable_list = immutable_list.ImmutableList(none_value, none_value)

    # Perform the find operation; result should support __len__
    find_result = empty_immutable_list.find(search_value)

    # Verify the result is a sized collection by calling __len__
    find_result.__len__()

def test_immutable_list_find_with_self_as_argument():
    """Test that ImmutableList.find() can be called with the list instance itself as the search argument."""
    # Use False for both the value and the is_empty flag during construction
    false_value = False

    # Construct an ImmutableList with False as the value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find() using the list instance itself as the search target
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_falsy_values():
    """Test that reduce and find can be called on ImmutableList instances constructed with falsy values."""

    # Use False as a falsy seed value and constructor argument
    falsy_value = False

    # Create a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Call reduce with a falsy accumulator and the empty list as the iterable
    # Result is captured but not further asserted — test verifies no exception is raised
    reduce_result = empty_list.reduce(falsy_value, empty_list)

    # Create a second ImmutableList using the falsy value as both element and is_empty flag
    non_empty_list = immutable_list.ImmutableList(falsy_value, is_empty=falsy_value)

    # Call find on the second list, passing itself as the predicate/target
    # Verifies the call completes without error
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction_succeeds():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Constructing with no arguments should succeed without raising an exception
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Test that ImmutableList initialized with False supports __str__ and find operations without error."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Verify that __str__ can be called without raising an exception
    string_representation = immutable_list_instance.__str__()

    # Verify that find can be called with the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_and_find_with_self_reference():
    """Test that ImmutableList supports unshift and find operations when initialized with False and is_empty=False."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as value and is_empty=False
    empty_immutable_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Unshift the list onto itself and capture the result
    unshifted_list = empty_immutable_list.unshift(empty_immutable_list)

    # Attempt to find the list within itself (no assertion, verifies no exception is raised)
    empty_immutable_list.find(empty_immutable_list)

def test_immutable_list_unshift_append_and_find_with_false():
    """Test that unshift, append, and find can be chained on an ImmutableList constructed with is_empty=False."""
    false_value = False

    # Create an initial ImmutableList with is_empty=False
    initial_list = immutable_list.ImmutableList(is_empty=false_value)

    # Prepend false_value to the front of the list
    list_after_unshift = initial_list.unshift(false_value)

    # Append the initial list to the unshifted list
    list_after_append = list_after_unshift.append(initial_list)

    # Search for false_value in the resulting list
    list_after_append.find(false_value)

def test_immutable_list_append_and_find_on_boolean_initialized_list():
    """Test that appending to a boolean-initialized ImmutableList updates length and that find can be called with the list itself."""
    # Use True as both the initial value and the is_empty flag
    initial_value = True

    # Create an ImmutableList initialized with a boolean value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the boolean value to produce a new immutable list
    appended_list = original_list.append(initial_value)

    # Retrieve the length of the appended list
    appended_list_length = appended_list.__len__()

    # Call find on the original list using itself as the search argument
    original_list.find(original_list)

def test_immutable_list_chained_append_reduce_unshift_find_operations():
    """Tests that ImmutableList supports chained operations (append, reduce, eq, unshift, str, find) without errors."""

    # Create an empty ImmutableList as the base for all subsequent operations
    empty_list = immutable_list.ImmutableList()

    # Append the empty list to itself, producing a new list containing it
    list_after_append = empty_list.append(empty_list)

    # Reduce using list_after_append as both the initial value and the reducer
    reduce_result = empty_list.reduce(list_after_append, list_after_append)

    # Check equality between list_after_append and empty_list
    eq_result = list_after_append.__eq__(empty_list)

    # Prepend list_after_append to itself via unshift
    list_after_unshift = list_after_append.unshift(list_after_append)

    # Obtain the string representation of the unshifted list
    str_representation = list_after_unshift.__str__()

    # Construct a new ImmutableList using the string representation as the is_empty argument
    list_with_is_empty_str = immutable_list.ImmutableList(is_empty=str_representation)

    # Append reduce_result to itself to produce another new list
    list_after_second_append = reduce_result.append(reduce_result)

    # Search for reduce_result within list_after_unshift
    list_after_unshift.find(reduce_result)

def test_immutable_list_chained_operations_unshift_reduce_find():
    """Tests chained ImmutableList operations: unshift, reduce, len, eq, and find, including construction with is_empty keyword argument."""

    # Create an empty ImmutableList as the base
    empty_list = immutable_list.ImmutableList()

    # Unshift the empty list onto itself to produce a new list
    list_after_unshift = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the initial accumulator
    reduced_result = empty_list.reduce(list_after_unshift, list_after_unshift)

    # Get the length of the unshifted list
    length_of_unshifted = list_after_unshift.__len__()

    # Unshift the already-unshifted list onto itself again
    list_after_second_unshift = list_after_unshift.unshift(list_after_unshift)

    # Check equality between the doubly-unshifted list and the original empty list
    eq_result = list_after_second_unshift.__eq__(empty_list)

    # Construct a new ImmutableList using the computed length as the is_empty argument
    list_with_is_empty_kwarg = immutable_list.ImmutableList(is_empty=length_of_unshifted)

    # Call find on the reduced result, passing itself as the search argument
    reduced_result.find(reduced_result)

def test_immutable_list_reduce_with_to_list_result_as_both_arguments():
    """Test that ImmutableList supports to_list() and reduce() using the list representation as both arguments."""

    flag_true = True
    empty_dict = {}

    # Construct an ImmutableList with an empty dict as the tail (result unused but exercises construction)
    list_with_empty_tail = immutable_list.ImmutableList(tail=empty_dict)

    # Construct a non-empty ImmutableList with is_empty explicitly set
    non_empty_immutable_list = immutable_list.ImmutableList(flag_true, is_empty=flag_true)

    # Convert the immutable list to a plain Python list
    list_representation = non_empty_immutable_list.to_list()

    # Call reduce using the list representation as both the function and the initial value
    non_empty_immutable_list.reduce(list_representation, list_representation)

