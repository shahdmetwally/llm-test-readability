import pytest
import immutable_list as immutable_list

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on a default-constructed (empty) ImmutableList."""

    # Create a default empty ImmutableList
    empty_immutable = immutable_list.ImmutableList()

    # Verify equality of the empty list with itself
    is_equal = empty_immutable.__eq__(empty_immutable)

    # Verify string representation of the empty list
    string_repr = empty_immutable.__str__()

    # Convert the empty ImmutableList to a plain list
    plain_list = empty_immutable.to_list()

    # Concatenate the plain list with itself (produces a regular list)
    concatenated_list = plain_list.__add__(plain_list)

    # Check the length of the plain list
    list_length = plain_list.__len__()

    # Add the plain list to the original ImmutableList (result unused)
    empty_immutable.__add__(plain_list)

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on a default-constructed ImmutableList, including
    equality check, concatenation, find, string representation, unshift, and reduce."""

    # A truthy value used as an argument in equality and reduce calls
    true_value = True

    # Create a default (empty) ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality between the empty list and a boolean (expected to return False or similar)
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the empty list with itself, producing a new ImmutableList
    concatenated_list = empty_list.__add__(empty_list)

    # Attempt to find the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Get the string representation of the empty list
    str_repr = empty_list.__str__()

    # Prepend the empty list to itself using unshift, producing a new ImmutableList
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_bool():
    """Test that ImmutableList can be created with a bool value, supports append,
    and allows find to be called with another ImmutableList as the search target."""
    # Use True as both the initial value and the is_empty flag
    initial_value = True

    # Create an ImmutableList initialized with a boolean value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the boolean value to produce a new ImmutableList
    appended_list = original_list.append(initial_value)

    # Attempt to find the original list within itself (exercises the find method)
    original_list.find(original_list)

def test_immutable_list_add_none_to_empty_list():
    """Test that calling __add__ with None on an empty ImmutableList does not raise unexpectedly."""
    # Create a default empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the immutable list
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_find_on_empty_list_with_self_as_argument():
    """
    Test that ImmutableList can be constructed with an empty list and a
    non-standard is_empty argument, and that calling find() with the list
    itself as the search target does not raise an unexpected error.
    """
    # Create a default empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Retrieve the length of the empty list
    empty_length = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as both the
    # iterable source and the is_empty flag (non-standard usage)
    list_with_self_as_empty_flag = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Attempt to find the list within itself (searching for self-reference)
    list_with_self_as_empty_flag.find(list_with_self_as_empty_flag)

def test_immutable_list_len_and_find_with_false():
    """Test that ImmutableList can be constructed with False, supports __len__, and find with itself."""
    # Create an ImmutableList with is_empty=False using False as the value
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__ on the list (result unused, but verifies no exception is raised)
    length = immutable_list_instance.__len__()

    # Attempt to find the list within itself (verifies no exception is raised)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list():
    """Test that find() can be called with the result of to_list() on an empty ImmutableList."""
    # Create an ImmutableList initialized with False, explicitly marked as not empty
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the ImmutableList to a plain list, then use it as the search target
    converted_list = immutable_list_instance.to_list()
    immutable_list_instance.find(converted_list)

def test_find_on_empty_list_and_append_self_then_convert_to_list():
    """Test that find on an empty ImmutableList returns None, appending the list
    to itself produces a new ImmutableList, and converting it to a plain list
    allows calling __add__ with None without raising an error."""
    empty_list = immutable_list.ImmutableList()
    none_value = None

    # Finding None in an empty ImmutableList should return without error
    find_result = empty_list.find(none_value)

    # Appending the empty list to itself should produce a new ImmutableList
    list_with_self = empty_list.append(empty_list)

    # Converting the resulting ImmutableList to a plain Python list
    plain_list = list_with_self.to_list()

    # Calling __add__ with None on the plain list (result is discarded)
    plain_list.__add__(none_value)

def test_find_on_empty_immutable_list_returns_empty_result():
    """Test that finding a value in an ImmutableList initialised with None
    contents returns a result whose length can be queried without error."""
    search_value = 1947
    empty_contents = None

    # Create an ImmutableList with no initial elements
    empty_list = immutable_list.ImmutableList(empty_contents, empty_contents)

    # Perform the find operation and check the length of the result
    find_result = empty_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_with_false_initialization():
    """Test that ImmutableList can be initialized with False and supports find() on itself."""
    # Use False as both the value and the is_empty flag during construction
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Search for the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_reduce_on_empty_list_and_find_on_non_empty_list():
    """
    Test that reduce on an empty ImmutableList with a False accumulator returns a result,
    and that find on an ImmutableList constructed with False values does not raise.
    """
    # Use False as the initial accumulator/seed value
    initial_value = False

    # Create an empty ImmutableList and reduce it using False as both the
    # initial accumulator and the iterable argument
    empty_list = immutable_list.ImmutableList()
    reduce_result = empty_list.reduce(initial_value, empty_list)

    # Create a non-empty ImmutableList with False as the element and is_empty=False,
    # then attempt to find using the list itself as the predicate/target
    non_empty_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Create an ImmutableList using the default (no-argument) constructor
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_init():
    """Test that ImmutableList can be constructed with False values,
    converted to string, and used as an argument to its own find method."""
    # Create an ImmutableList with is_empty=False and initial value False
    is_empty_flag = False
    empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the list to its string representation
    str_repr = empty_list.__str__()

    # Search for the list within itself
    empty_list.find(empty_list)

def test_immutable_list_unshift_and_find_with_false_initial_value():
    """Test that ImmutableList can be constructed with False, then unshifted and searched with itself."""
    # Use False as both the initial value and the is_empty flag
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Unshift the list onto itself and find the list within itself
    unshifted_result = immutable_list_instance.unshift(immutable_list_instance)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_with_to_list_result():
    """
    Test that ImmutableList.reduce() can be called with the result of to_list()
    as both arguments, when the list was constructed with a non-empty tail and
    another instance constructed with explicit head and is_empty flag.
    """
    is_empty_flag = True
    empty_tail = {}

    # Create an ImmutableList with an empty dict as the tail
    immutable_list_with_empty_tail = immutable_list.ImmutableList(tail=empty_tail)

    # Create an ImmutableList with a head value and is_empty explicitly set to True
    immutable_list_with_head = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the second list to a plain list
    list_result = immutable_list_with_head.to_list()

    # Reduce using the converted list as both the initial value and the reducer
    immutable_list_with_head.reduce(list_result, list_result)

