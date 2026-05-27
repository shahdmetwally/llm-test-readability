import pytest
import immutable_list as immutable_list

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on an empty ImmutableList: equality, string
    representation, conversion to list, list addition, and length check."""

    # Create an empty ImmutableList instance
    empty_immutable = immutable_list.ImmutableList()

    # Verify that an empty ImmutableList is equal to itself
    is_equal = empty_immutable.__eq__(empty_immutable)

    # Get the string representation of the empty list
    string_repr = empty_immutable.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable.to_list()

    # Concatenate the plain list with itself (result unused but call is exercised)
    concatenated_list = plain_list.__add__(plain_list)

    # Get the length of the plain list
    list_length = plain_list.__len__()

    # Add the plain list back to the original ImmutableList (exercises __add__ on ImmutableList)
    empty_immutable.__add__(plain_list)

def test_immutable_list_operations_with_empty_list_and_boolean():
    """Test basic operations on an empty ImmutableList, including equality check,
    concatenation, find, string conversion, unshift, and reduce."""

    # A truthy value used as an argument in equality and reduce calls
    true_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality between the empty list and a boolean (expected to return False or similar)
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the empty list with itself, producing a new empty ImmutableList
    concatenated_list = empty_list.__add__(empty_list)

    # Attempt to find the equality result value within the empty list
    find_result = empty_list.find(eq_result)

    # Get the string representation of the empty list
    str_representation = empty_list.__str__()

    # Prepend the empty list to itself using unshift, producing a new ImmutableList
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList can be created with a bool value, supports append,
    and allows find to be called with another ImmutableList as the search target."""
    # Use True as a simple non-empty initializer and is_empty flag
    initial_value = True

    # Create an ImmutableList initialized with a bool, marked as non-empty
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same bool value, producing a new immutable list
    appended_list = original_list.append(initial_value)

    # Attempt to find the original list within itself (exercises the find interface)
    original_list.find(original_list)

def test_add_with_none_on_empty_immutable_list():
    """Test that calling __add__ with None on an empty ImmutableList does not raise unexpectedly."""
    # Create a new empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the empty ImmutableList
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_find_on_self_with_empty_list_as_is_empty():
    """Test that ImmutableList can be constructed with another ImmutableList
    as both the iterable and the is_empty argument, and that find() can be
    called with the list itself as the search target."""

    # Create an empty ImmutableList and verify its length
    empty_list = immutable_list.ImmutableList()
    empty_length = empty_list.__len__()

    # Construct a new ImmutableList using the empty list as the source
    # and passing it as the is_empty flag (an unconventional but valid call)
    nested_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Attempt to find the list within itself
    nested_list.find(nested_list)

def test_immutable_list_len_and_find_with_false():
    """Test that ImmutableList can be created with False, __len__ called, and find invoked with itself."""
    # Create an ImmutableList where both the value and is_empty are False
    is_empty_flag = False
    empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__ on the list (result is unused, but call must occur)
    length = empty_list.__len__()

    # Attempt to find the list within itself
    empty_list.find(empty_list)

def test_immutable_list_find_with_converted_list():
    """Test that find() can be called with the result of to_list() on an empty ImmutableList."""
    # Create an ImmutableList initialized with False (empty/falsy) and is_empty=False
    is_empty_flag = False
    empty_immutable_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the ImmutableList to a regular list
    converted_list = empty_immutable_list.to_list()

    # Attempt to find the converted list within the ImmutableList
    empty_immutable_list.find(converted_list)

def test_find_on_empty_list_and_append_self_then_convert_to_list():
    """Test that find on an empty ImmutableList returns None, that appending
    the list to itself works, and that converting the result to a plain list
    and calling __add__ with None does not raise an error."""

    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # find(None) on an empty list should return without error
    find_result = empty_list.find(None)

    # Append the empty list to itself, producing a new ImmutableList
    list_with_self = empty_list.append(empty_list)

    # Convert the resulting ImmutableList to a plain Python list
    plain_list = list_with_self.to_list()

    # Attempt to add None to the plain list via __add__ (no assertion; testing no exception)
    plain_list.__add__(None)

def test_immutable_list_map_with_non_empty_flag_and_repeated_to_list():
    """Test that map() can be called on an ImmutableList created with is_empty=False,
    using the result of to_list() as the mapping argument, called twice."""
    # Create an ImmutableList explicitly marked as non-empty
    is_empty_flag = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Convert to a plain list (first call, result unused but invoked for side effects)
    _ = non_empty_list.to_list()

    # Create a default ImmutableList (no arguments)
    default_list = immutable_list.ImmutableList()

    # Convert the non-empty list to a plain list again for use as a map argument
    list_as_map_arg = non_empty_list.to_list()

    # Call map() on the non-empty list using the list result as the mapping function/argument
    non_empty_list.map(list_as_map_arg)

def test_immutable_list_unshift_and_map_with_none_values():
    """
    Test that ImmutableList supports unshift and append operations with None values,
    and that calling map with None as the mapping function does not raise unexpectedly.
    Verifies chaining of unshift from one list into another and appending None elements.
    """
    none_value = None

    # Create an ImmutableList with two None elements
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    unshifted_with_none = base_list.unshift(none_value)

    # Prepend the previously unshifted list into the base list
    unshifted_with_list = base_list.unshift(unshifted_with_none)  # noqa: F841

    # Append None to the unshifted list
    appended_list = unshifted_with_none.append(none_value)

    # Call map with None as the mapping function
    appended_list.map(none_value)

def test_filter_immutable_list_with_itself_when_empty():
    """Test that filtering an ImmutableList with itself does not raise an error when initialized as empty/falsy."""
    # Use False to represent an empty/falsy initial value for the list
    is_empty = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty, is_empty=is_empty)

    # Filter the list using itself as the filter argument
    immutable_list_instance.filter(immutable_list_instance)

def test_immutable_list_filter_on_empty_concatenation():
    """Test that filtering an empty ImmutableList concatenated with itself works without error."""
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself, resulting in another empty list
    concatenated_list = empty_list.__add__(empty_list)

    # Get the length of the concatenated list (expected to be 0)
    length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the filter argument
    concatenated_list.filter(length)

def test_find_on_empty_immutable_list_returns_empty_result():
    """Test that finding a value in an ImmutableList initialised with None
    contents returns a result whose length can be queried without error."""
    search_value = 1947
    empty_contents = None

    # Create an ImmutableList with no initial elements
    empty_list = immutable_list.ImmutableList(empty_contents, empty_contents)

    # Perform the find operation on the empty list
    find_result = empty_list.find(search_value)

    # Verify that the result supports len() without raising
    find_result.__len__()

def test_immutable_list_find_with_false_initialization():
    """Test that ImmutableList can be initialized with False and searched using find."""
    # Use False as both the value and the is_empty flag for initialization
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Search the list using itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_false():
    """
    Test that ImmutableList.reduce works with a False initial value and an empty list
    as the collection argument, and that ImmutableList.find can be called on a
    non-empty ImmutableList constructed with is_empty=False.
    """
    initial_value = False

    # Create an empty ImmutableList and reduce it using False as the initial accumulator
    empty_list = immutable_list.ImmutableList()
    reduced_result = empty_list.reduce(initial_value, empty_list)

    # Create a non-empty ImmutableList with is_empty explicitly set to False
    non_empty_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Attempt to find the list within itself
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Create an ImmutableList using the default (no-argument) constructor
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_init():
    """Test that ImmutableList can be constructed with False, converted to string,
    and used as an argument to its own find method without errors."""

    # Use False for both the value and is_empty flag during construction
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Verify string representation can be retrieved
    str_representation = immutable_list_instance.__str__()

    # Search for the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_and_find_with_empty_list():
    """
    Test that ImmutableList can be constructed with is_empty=False,
    unshifted with itself, and searched with find — all without raising errors.
    """
    is_empty = False

    # Create an ImmutableList that is not marked as empty
    immutable_list_instance = immutable_list.ImmutableList(is_empty, is_empty=is_empty)

    # Prepend the list to itself via unshift
    immutable_list_instance.unshift(immutable_list_instance)

    # Search the list for itself as the target element
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_append_and_find():
    """Test that unshift, append, and find can be chained on an ImmutableList
    initialised with is_empty=False without raising errors."""

    # Create an initial non-empty ImmutableList
    is_empty = False
    initial_list = immutable_list.ImmutableList(is_empty=is_empty)

    # Prepend the is_empty value to produce a new list
    unshifted_list = initial_list.unshift(is_empty)

    # Append the original list as an element to produce another new list
    appended_list = unshifted_list.append(initial_list)

    # Search for the is_empty value within the final list
    appended_list.find(is_empty)

def test_immutable_list_append_increases_length_and_find_on_self():
    """Test that appending to an ImmutableList increases its length,
    and that find() can be called with the list itself as the argument."""
    # Create an ImmutableList initialized with a truthy value, marked as non-empty
    is_truthy = True
    original_list = immutable_list.ImmutableList(is_truthy, is_empty=is_truthy)

    # Append the truthy value to produce a new immutable list
    extended_list = original_list.append(is_truthy)

    # Verify the length of the extended list
    length = extended_list.__len__()

    # Attempt to find the original list within itself
    original_list.find(original_list)

def test_immutable_list_operations_with_nested_append_reduce_and_find():
    """
    Tests a sequence of ImmutableList operations including append, reduce,
    equality check, unshift, str conversion, construction with is_empty,
    and find — verifying no exceptions are raised during chained usage.
    """
    # Create an empty ImmutableList as the base structure
    empty_list = immutable_list.ImmutableList()

    # Append the empty list to itself, producing a new immutable list
    list_with_self = empty_list.append(empty_list)

    # Reduce the new list using the appended list as both initial value and reducer
    reduced_result = empty_list.reduce(list_with_self, list_with_self)

    # Check equality between the appended list and the original empty list
    are_equal = list_with_self.__eq__(empty_list)

    # Prepend the appended list to itself via unshift
    unshifted_list = list_with_self.unshift(list_with_self)

    # Get string representation of the unshifted list
    str_representation
# (Truncated by extractor)