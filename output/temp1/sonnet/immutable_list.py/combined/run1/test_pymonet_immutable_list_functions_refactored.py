import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Verify that an empty ImmutableList supports equality, string conversion, list conversion, concatenation, and length operations."""

    # Create an empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Check that the empty list is equal to itself
    equality_result = empty_immutable_list.__eq__(empty_immutable_list)

    # Verify string representation can be obtained without error
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a plain mutable list
    mutable_list = empty_immutable_list.to_list()

    # Concatenate the mutable list with itself
    concatenated_list = mutable_list.__add__(mutable_list)

    # Check the length of the mutable list
    list_length = mutable_list.__len__()

    # Verify that adding a mutable list to the ImmutableList does not raise an error
    empty_immutable_list.__add__(mutable_list)

def test_immutable_list_basic_operations_on_empty_list():
    """Verify that basic ImmutableList operations (eq, add, find, str, unshift, reduce) execute without error on an empty list."""

    # A non-list value used to probe equality behaviour
    non_list_value = True

    # Create an empty ImmutableList as the base subject for all operations
    empty_list = immutable_list.ImmutableList()

    # Compare the empty list against a non-list value; result is stored for later use
    eq_result = empty_list.__eq__(non_list_value)

    # Concatenate the empty list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the empty list
    string_repr = empty_list.__str__()

    # Prepend the empty list to itself, producing a new ImmutableList
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and the original boolean as the initial value
    unshifted_list.reduce(unshifted_list, non_list_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList can be constructed with a bool, appended to, and searched via find without error."""
    # Use a boolean as both the stored element and the is_empty flag
    initial_value = True

    # Construct the immutable list with the boolean value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same boolean value; result is a new immutable list
    appended_list = original_list.append(initial_value)

    # Call find on the original list using itself as the search target
    original_list.find(original_list)

def test_immutable_list_add_with_none_does_not_raise():
    """Test that calling __add__ on an empty ImmutableList with None does not raise an exception."""
    # Create a default empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the list; verify this does not raise
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_construction_and_find_with_self_reference():
    """Test that ImmutableList can be constructed from another ImmutableList and supports find with self-reference."""

    # Create a default empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Retrieve the length of the empty list
    initial_length = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as both
    # the positional argument and the is_empty keyword argument
    derived_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Call find on the derived list using itself as the search argument
    derived_list.find(derived_list)

def test_immutable_list_construction_with_false_and_method_calls():
    """Test that ImmutableList can be constructed with False and supports __len__ and find calls."""

    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList instance with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Invoke __len__ directly and capture the result
    len_result = immutable_list_instance.__len__()

    # Call find with the list instance itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list():
    """Test that ImmutableList initialized with False can be converted to a list and passed to find."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList instance with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Convert the ImmutableList to a regular Python list
    converted_list = immutable_list_instance.to_list()

    # Pass the converted list back into find to verify no error is raised
    immutable_list_instance.find(converted_list)

def test_immutable_list_find_none_append_self_and_convert_to_list():
    """Tests that an empty ImmutableList supports find(None), self-append, to_list conversion, and __add__ with None."""
    # Create a new empty ImmutableList
    empty_immutable_list = immutable_list.ImmutableList()

    none_value = None

    # Search for None in the empty list
    find_result = empty_immutable_list.find(none_value)

    # Append the list to itself, producing a new ImmutableList containing itself as an element
    list_with_self_appended = empty_immutable_list.append(empty_immutable_list)

    # Convert the ImmutableList to a plain Python list
    converted_list = list_with_self_appended.to_list()

    # Call __add__ directly with None on the converted list (testing dunder invocation behaviour)
    converted_list.__add__(none_value)

def test_immutable_list_map_accepts_to_list_result():
    """Test that to_list() result can be passed to map() on an ImmutableList created with is_empty=False."""
    # Create a non-empty ImmutableList by explicitly setting is_empty=False
    is_empty_flag = False
    non_empty_immutable_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Call to_list() once as an initial invocation (result not further used)
    initial_to_list_result = non_empty_immutable_list.to_list()

    # Create a second, default-constructed ImmutableList (side-effect creation, not further used)
    default_immutable_list = immutable_list.ImmutableList()

    # Call to_list() again on the original list to obtain the value to pass to map()
    to_list_result = non_empty_immutable_list.to_list()

    # Pass the to_list() result into map() to verify it is accepted without error
    non_empty_immutable_list.map(to_list_result)

def test_immutable_list_operations_with_none_values():
    """Tests that ImmutableList supports construction and chained unshift, append, and map calls with None values."""

    none_value = None

    # Construct a base ImmutableList with None as both arguments
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    list_after_unshift_none = base_list.unshift(none_value)

    # Prepend the previously unshifted list onto the base list
    list_after_unshift_list = base_list.unshift(list_after_unshift_none)

    # Append None to the list that had None unshifted
    list_after_append_none = list_after_unshift_none.append(none_value)

    # Apply map with None as the mapping function
    list_after_append_none.map(none_value)

def test_immutable_list_filter_with_self_as_predicate():
    """Test that ImmutableList.filter() can be called with the list itself as the argument when constructed with a False value and is_empty=False."""
    # False is used both as the list value and to indicate the list is not empty
    is_empty_flag = False

    # Construct an ImmutableList with a boolean value, explicitly marking it as non-empty
    non_empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Filter the list using itself as the argument; should not raise an error
    non_empty_list.filter(non_empty_list)

def test_immutable_list_add_self_then_filter_by_length():
    """Test that an ImmutableList can be concatenated with itself, its length retrieved, and filter called with that length."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Concatenate the list with itself to produce a new combined list
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    list_length = concatenated_list.__len__()

    # Call filter using the length as the filter argument
    concatenated_list.filter(list_length)

def test_find_on_none_initialized_immutable_list_returns_sized_result():
    """Test that find() on an ImmutableList initialized with None returns a result that supports len()."""
    # The value to search for within the list
    search_value = 1947

    # Use None for both constructor arguments to create a minimally initialized list
    none_value = None
    empty_immutable_list = immutable_list.ImmutableList(none_value, none_value)

    # Perform the find operation and verify the result supports len()
    find_result = empty_immutable_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_with_self_as_argument():
    """Test that ImmutableList.find() can be called with the list itself as the search argument."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find() using the list instance itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_bool_and_empty_list():
    """Test that reduce and find can be called on ImmutableList instances constructed with default and boolean arguments."""

    # Use False as the seed value and is_empty flag throughout
    false_value = False

    # Create a default (empty) ImmutableList to use as the accumulator
    empty_list = immutable_list.ImmutableList()

    # Call reduce with a False seed and the empty list as the accumulator
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Create a second ImmutableList using False as the element and is_empty flag
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find on the second list, passing itself as the predicate/target
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Instantiate with no arguments; should complete without raising an exception
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Test that ImmutableList constructed with False supports __str__ and find with itself as argument."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as the value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __str__ to verify string representation can be obtained without error
    string_representation = immutable_list_instance.__str__()

    # Call find with the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_and_find_on_empty_list():
    """Test that unshift and find can be called on an ImmutableList initialized with False without raising errors."""
    # Use False for both the value argument and the is_empty keyword argument
    is_empty_flag = False

    # Construct an ImmutableList with False as content and marked as not empty
    empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Prepend the list to itself via unshift; result is captured but not further asserted
    unshifted_list = empty_list.unshift(empty_list)

    # Search for the list within itself; no assertion on the result
    empty_list.find(empty_list)

def test_immutable_list_unshift_append_then_find():
    """Test that unshift and append operations on an ImmutableList can be followed by a find call without error."""

    # Flag value passed as `is_empty` to the constructor (False = not treating list as empty)
    is_empty_flag = False

    # Create a base ImmutableList with is_empty=False
    base_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Prepend the flag value to the front of the list via unshift
    list_after_unshift = base_list.unshift(is_empty_flag)

    # Append the original base_list as an element to the unshifted list
    list_after_append = list_after_unshift.append(base_list)

    # Search for the flag value within the resulting list
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_increases_length_and_find_on_original():
    """Test that appending to an ImmutableList produces a new list with retrievable length, and that find can be called on the original list."""
    # Use True as the initial value for both the list element and the
# (Truncated by extractor)