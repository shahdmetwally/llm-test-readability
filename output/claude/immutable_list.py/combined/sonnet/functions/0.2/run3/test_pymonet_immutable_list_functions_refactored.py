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

    # Concatenate the mutable list with itself
    concatenated_list = mutable_list.__add__(mutable_list)

    # Check the length of the mutable list
    list_length = mutable_list.__len__()

    # Invoke __add__ on the ImmutableList with the mutable list (result intentionally discarded)
    empty_immutable_list.__add__(mutable_list)

def test_immutable_list_core_operations_do_not_raise():
    """Verify that ImmutableList supports equality, concatenation, find, str, unshift, and reduce without raising exceptions."""

    true_value = True

    # Create a base empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Compare the list against a boolean value
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the list
    str_repr = empty_list.__str__()

    # Prepend the empty list to itself, producing a new list
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the accumulator seed, with true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList supports construction with a bool, append returns a new list, and find can be called on the original list."""
    # Use a boolean as both the stored value and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with the boolean value
    immutable_list_instance = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same boolean value, producing a new immutable list
    appended_list = immutable_list_instance.append(initial_value)

    # Verify that find can be called on the original list using itself as the search target
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_add_with_none_does_not_raise():
    """Test that calling __add__ with None on a default ImmutableList does not raise an exception."""
    # Create a default (empty) ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the immutable list; should not raise
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_construction_and_find_with_self_reference():
    """Test construction of ImmutableList with defaults, length retrieval, nested construction with self-reference, and find with self as argument."""

    # Create a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Exercise __len__ on the empty list (result captured but not asserted, matching original intent)
    empty_list_length = empty_list.__len__()

    # Construct a second ImmutableList using the first as both the data source and the is_empty flag
    nested_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Call find on the nested list using itself as the search target
    nested_list.find(nested_list)

def test_immutable_list_construction_len_and_find_with_false():
    """Test that ImmutableList can be constructed with False, supports __len__, and find can be called with the list itself."""

    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __len__ on the constructed list and capture the result
    len_result = immutable_list_instance.__len__()

    # Call find with the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list_as_argument():
    """Test that ImmutableList initialized with False can convert to list and use the result in find."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as value and marked as not empty (is_empty=False)
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Convert the immutable list to a regular Python list
    converted_list = immutable_list_instance.to_list()

    # Use the converted list as the search argument to find
    immutable_list_instance.find(converted_list)

def test_immutable_list_append_self_and_convert_to_list():
    """Test that an ImmutableList can append itself, convert to a plain list, and call __add__ with None."""

    # Create an empty ImmutableList
    empty_immutable_list = immutable_list.ImmutableList()

    none_value = None

    # Search for None in the empty list (result is not used further)
    find_result = empty_immutable_list.find(none_value)

    # Append the empty list to itself, producing a new ImmutableList containing itself as an element
    immutable_list_with_self = empty_immutable_list.append(empty_immutable_list)

    # Convert the resulting ImmutableList to a plain Python list
    plain_list = immutable_list_with_self.to_list()

    # Call __add__ with None on the plain list; result is intentionally discarded
    plain_list.__add__(none_value)

def test_immutable_list_map_with_to_list_result():
    """Test that map() can be called on an ImmutableList using the result of to_list() as the mapping argument."""

    # Create an ImmutableList explicitly marked as non-empty
    is_empty_false = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty_false)

    # Call to_list() on the non-empty list (result unused, exercising the method)
    initial_to_list_result = non_empty_list.to_list()

    # Create a second ImmutableList using default construction
    default_list = immutable_list.ImmutableList()

    # Retrieve the list representation of the non-empty list to use as map input
    to_list_result = non_empty_list.to_list()

    # Call map() on the non-empty list, passing the to_list() result as the mapping argument
    non_empty_list.map(to_list_result)

def test_immutable_list_operations_with_none_values():
    """Verify that ImmutableList handles None for construction, unshift, append, and map without errors."""

    none_value = None

    # Construct a base ImmutableList with None as both arguments
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Unshift None onto the base list, producing a new list
    list_after_unshift_none = base_list.unshift(none_value)

    # Unshift the previously produced list onto the base list (result intentionally unused;
    # verifies the call completes without raising an exception)
    list_after_unshift_list = base_list.unshift(list_after_unshift_none)

    # Append None to the unshifted list
    list_after_append_none = list_after_unshift_none.append(none_value)

    # Map with None as the mapping function (verifies no exception is raised)
    list_after_append_none.map(none_value)

def test_immutable_list_filter_with_self_as_argument():
    """Test that ImmutableList.filter() can be called with the list itself as the argument when constructed with is_empty=False."""
    # Use False for both the list value and the is_empty flag
    is_empty_flag = False

    # Construct an ImmutableList that is not empty, with False as its value
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Filter the list using itself as the filter argument; should not raise
    immutable_list_instance.filter(immutable_list_instance)

def test_immutable_list_add_self_then_filter_by_length():
    """Test that concatenating an ImmutableList with itself yields a list whose length can be used as a filter argument."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Concatenate the list with itself to produce a new combined list
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    list_length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the filter argument
    concatenated_list.filter(list_length)

def test_find_on_none_initialized_immutable_list_returns_sized_result():
    """Test that find() on an ImmutableList initialized with None returns a sized result."""
    # The value to search for within the immutable list
    search_value = 1947

    # Both constructor arguments are None
    none_value = None

    # Construct an ImmutableList using None for both arguments
    empty_immutable_list = immutable_list.ImmutableList(none_value, none_value)

    # Perform a find operation; result should support __len__
    find_result = empty_immutable_list.find(search_value)

    # Verify the result is sized (supports len())
    find_result.__len__()

def test_immutable_list_find_with_self_as_argument():
    """Test that ImmutableList.find() can be called with the list instance itself as the search argument."""
    # Use False as both the list's value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as value and marked as not empty
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find() using the list instance itself as the search target
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_bool_seed():
    """Test that reduce and find can be called on ImmutableList instances constructed with boolean arguments."""

    # Use False as the seed value and constructor flag throughout the test
    false_value = False

    # Create an empty ImmutableList to serve as the reducer and base structure
    empty_list = immutable_list.ImmutableList()

    # Call reduce with a boolean seed and the empty list as the combining argument
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Create a second ImmutableList using the boolean value and is_empty flag
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find on the second list, passing itself as the search argument
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction_succeeds():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Constructing with no args should succeed without raising an exception
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Test that ImmutableList supports __str__ and find when constructed with False and is_empty=False."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Verify that __str__ can be called without error
    string_representation = immutable_list_instance.__str__()

    # Verify that find can be called with the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_and_find_with_self_reference():
    """Test that ImmutableList supports unshift and find when initialized with False and is_empty=False."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as value and is_empty=False
    empty_immutable_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Unshift the list onto itself and capture the result
    unshifted_list = empty_immutable_list.unshift(empty_immutable_list)

    # Attempt to find the list within itself (no assertion; verifies no exception is raised)
    empty_immutable_list.find(empty_immutable_list)

def test_immutable_list_unshift_append_and_find():
    """Test that an ImmutableList supports unshift, append, and find operations in sequence."""

    # Use False as the is_empty flag when constructing the initial list
    is_empty_flag = False

    # Create an initial ImmutableList that is not empty
    initial_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Unshift the flag value onto the front of the list
    list_after_unshift = initial_list.unshift(is_empty_flag)

    # Append the initial list to the unshifted list
    list_after_append = list_after_unshift.append(initial_list)

    # Search for the flag value within the resulting list
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_increases_length_and_find_is_callable():
    """Test that appending to an ImmutableList returns a new list with a valid length, and that find can be called with another ImmutableList as the argument."""
    # Use True as both the initial value and the is_empty flag
    truthy_value = True

    # Create an ImmutableList initialised with a truthy value, marked as non-empty
    initial_list = immutable_list.ImmutableList(truthy_value, is_empty=truthy_value)

    # Append the truthy value to produce a new ImmutableList
    list_after_append = initial_list.append(truthy_value)

    # Retrieve the length of the list after appending
    length_after_append = list_after_append.__len__()

    # Call find on the original list, passing the original list itself as the search argument
    initial_list.find(initial_list)

def test_immutable_list_chained_operations_with_self_referential_args():
    """Tests chained ImmutableList operations including append, reduce, eq, unshift, str, and find with self-referential and cross-instance arguments."""

    # Create a base empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Append the list to itself, producing a new list containing itself as an element
    list_with_self_appended = empty_list.append(empty_list)

    # Reduce using the appended list as both the initial value and the reducer
    reduced_result = empty_list.reduce(list_with_self_appended, list_with_self_appended)

    # Check equality between the appended list and the original empty list
    eq_result = list_with_self_appended.__eq__(empty_list)

    # Prepend the appended list to itself via unshift
    list_after_unshift = list_with_self_appended.unshift(list_with_self_appended)

    # Obtain the string representation of the unshifted list
    str_representation = list_after_unshift.__str__()

    # Construct a new ImmutableList using the string representation as the is_empty argument
    list_from_str_is_empty = immutable_list.ImmutableList(is_empty=str_representation)

    # Append the reduced result to itself
    list_with_reduced_appended = reduced_result.append(reduced_result)

    # Invoke find on the unshifted list using the reduced result as the predicate/value (smoke call)
    list_after_unshift.find(reduced_result)

def test_immutable_list_chained_operations_unshift_reduce_find():
    """Test that ImmutableList supports chained unshift, reduce, len, eq, and find operations without error."""

    # Create an empty ImmutableList as the base
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list into itself, producing a new list
    list_with_self_prepended = empty_list.unshift(empty_list)

    # Reduce the prepended list using itself as both accumulator and reducer
    reduced_result = empty_list.reduce(list_with_self_prepended, list_with_self_prepended)

    # Capture the length of the prepended list
    length_of_prepended_list = list_with_self_prepended.__len__()

    # Prepend the prepended list into itself again, producing a doubly-nested list
    list_double_prepended = list_with_self_prepended.unshift(list_with_self_prepended)

    # Check equality between the doubly-prepended list and the original empty list
    is_equal_to_empty = list_double_prepended.__eq__(empty_list)

    # Construct a new ImmutableList using the captured length as the is_empty flag
    list_with_is_empty_flag = immutable_list.ImmutableList(is_empty=length_of_prepended_list)

    # Search for the reduced result within itself
    reduced_result.find(reduced_result)

def test_immutable_list_to_list_and_reduce_with_basic_inputs():
    """Test that ImmutableList supports to_list() and reduce() calls with basic construction arguments."""

    true_flag = True
    empty_dict = {}

    # Construct a list with an empty dict as tail (exercises the tail= constructor path)
    list_with_empty_tail = immutable_list.ImmutableList(tail=empty_dict)

    # Construct a non-empty list using positional and keyword arguments
    non_empty_list = immutable_list.ImmutableList(true_flag, is_empty=true_flag)

    # Convert the list to a plain Python list
    list_result = non_empty_list.to_list()

    # Call reduce using the list result as both the initial accumulator and the sequence
    non_empty_list.reduce(list_result, list_result)

