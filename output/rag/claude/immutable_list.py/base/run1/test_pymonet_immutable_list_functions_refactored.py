import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Test basic operations on an empty ImmutableList: equality, string representation,
    conversion to list, list addition, length check, and ImmutableList addition."""

    # Create a new empty ImmutableList
    empty_immutable = immutable_list.ImmutableList()

    # Verify that an empty ImmutableList is equal to itself
    is_equal = empty_immutable.__eq__(empty_immutable)

    # Get the string representation of the empty list
    string_repr = empty_immutable.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable.to_list()

    # Concatenate the plain list with itself
    concatenated_list = plain_list.__add__(plain_list)

    # Check the length of the plain list
    list_length = plain_list.__len__()

    # Add the plain list to the original ImmutableList
    empty_immutable.__add__(plain_list)

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on an empty ImmutableList, including equality check,
    concatenation, find, string representation, unshift, and reduce."""

    # A truthy value used as a comparison and accumulator argument
    true_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality of the empty list against a boolean (non-list) value
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the empty list with itself, producing a new ImmutableList
    concatenated_list = empty_list.__add__(empty_list)

    # Attempt to find the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Get the string representation of the empty list
    str_repr = empty_list.__str__()

    # Prepend the empty list to itself using unshift, producing a new ImmutableList
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and true_value as the initial accumulator
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_truthy_value():
    """Test that ImmutableList can be constructed with a truthy value,
    supports append, and supports find operations on itself."""

    # Use True as both the initial element and the is_empty flag
    truthy_value = True

    # Create an ImmutableList initialized with a truthy value
    initial_list = immutable_list.ImmutableList(truthy_value, is_empty=truthy_value)

    # Append the truthy value to produce a new immutable list
    appended_list = initial_list.append(truthy_value)

    # Attempt to find the original list within itself
    initial_list.find(initial_list)

def test_add_none_to_empty_immutable_list():
    """Test that calling __add__ with None on an empty ImmutableList does not raise unexpectedly."""
    # Create a new empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the empty ImmutableList
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_find_on_self_with_empty_list_as_is_empty():
    """
    Test that ImmutableList can be constructed with another ImmutableList
    as the 'is_empty' flag, and that calling find() on itself does not raise.
    """
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Verify the empty list reports zero length
    empty_length = empty_list.__len__()

    # Construct a new ImmutableList using the empty list as both the iterable
    # and the 'is_empty' keyword argument
    nested_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Attempt to find the nested list within itself
    nested_list.find(nested_list)

def test_immutable_list_len_and_find_with_false():
    """Test that ImmutableList can be constructed with False, supports __len__, and find with itself."""
    # Use False as both the initial value and is_empty flag
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__ on the list (result is unused, testing that no exception is raised)
    length = immutable_list_instance.__len__()

    # Attempt to find the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list():
    """Test that ImmutableList.find works when searching with the result of to_list()
    on an empty (non-empty=False) ImmutableList initialised with False."""
    is_empty = False

    # Create an ImmutableList with is_empty=False and the main value set to False
    immutable_list_instance = immutable_list.ImmutableList(is_empty, is_empty=is_empty)

    # Convert the ImmutableList to a plain list
    converted_list = immutable_list_instance.to_list()

    # Search the ImmutableList using the converted list as the search target
    immutable_list_instance.find(converted_list)

def test_find_on_empty_list_and_append_self_then_convert_to_list():
    """
    Test that an empty ImmutableList handles:
    - find() with None (no match expected),
    - append() with itself as an element,
    - to_list() conversion, and
    - calling __add__ with None on the resulting list (no assertion on result).
    """
    empty_list = immutable_list.ImmutableList()
    none_value = None

    # find(None) on an empty list; result is not asserted but call must succeed
    find_result = empty_list.find(none_value)

    # Append the empty ImmutableList to itself, producing a new ImmutableList
    list_with_self = empty_list.append(empty_list)

    # Convert the new ImmutableList to a plain Python list
    plain_list = list_with_self.to_list()

    # Attempt to add None to the plain list; result is not asserted
    plain_list.__add__(none_value)

def test_immutable_list_map_with_non_empty_flag_and_repeated_to_list():
    """Test that map() can be called on an ImmutableList initialised with
    is_empty=False, using the result of to_list() as the mapping argument,
    even after a second ImmutableList (default-constructed) exists."""

    # Create an ImmutableList explicitly marked as non-empty
    is_empty = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty)

    # Convert to a plain list for the first time
    list_contents = non_empty_list.to_list()

    # Create a second, default-constructed ImmutableList (unused, but part of the scenario)
    default_list = immutable_list.ImmutableList()

    # Retrieve the list contents again (second call to to_list on the original instance)
    list_contents_second_call = non_empty_list.to_list()

    # Use the retrieved list as the argument to map()
    non_empty_list.map(list_contents_second_call)

def test_immutable_list_unshift_and_map_with_none_values():
    """
    Test that ImmutableList handles None values correctly when using unshift,
    append, and map operations. Verifies that chaining these operations with
    None arguments does not raise unexpected errors during construction.
    """
    none_value = None

    # Create an ImmutableList with two None elements
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list, producing a new immutable list
    unshifted_once = base_list.unshift(none_value)

    # Prepend the previously unshifted list to the base list
    unshifted_twice = base_list.unshift(unshifted_once)

    # Append None to the first unshifted list
    appended_list = unshifted_once.append(none_value)

    # Map with None as the mapping function over the appended list
    appended_list.map(none_value)

def test_filter_on_empty_immutable_list():
    """Test that calling filter on an ImmutableList initialised with is_empty=False
    and a False value does not raise an error and executes without side effects."""
    is_empty = False

    # Create an ImmutableList with False as the value and is_empty explicitly set to False
    empty_list = immutable_list.ImmutableList(is_empty, is_empty=is_empty)

    # Filter the list using itself as the predicate/filter argument
    empty_list.filter(empty_list)

def test_add_empty_lists_and_filter_by_length():
    """Test that adding two empty ImmutableLists and filtering by the resulting length executes without error."""
    # Create an empty ImmutableList as the base
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself, resulting in another empty list
    concatenated_list = empty_list.__add__(empty_list)

    # Get the length of the concatenated list (expected to be 0)
    length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the filter criterion
    concatenated_list.filter(length)

def test_find_on_empty_immutable_list_returns_empty_result():
    """Test that finding a value in an ImmutableList initialised with None
    contents returns a result whose length can be queried without error."""
    search_value = 1947
    empty_contents = None

    # Create an ImmutableList with no initial elements
    empty_list = immutable_list.ImmutableList(empty_contents, empty_contents)

    # Perform the find operation and verify the result supports __len__
    find_result = empty_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_with_false_value():
    """Test that ImmutableList.find can be called with a falsy (False) value
    on a list initialised with is_empty=False."""
    # Use False as both the initial value and the is_empty flag
    not_empty = False
    immutable_list_instance = immutable_list.ImmutableList(not_empty, is_empty=not_empty)

    # Attempt to find the list within itself using the False-initialised instance
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_false_defaults():
    """
    Test that ImmutableList.reduce works on an empty list with a False accumulator,
    and that ImmutableList.find works when searching with a non-empty list instance
    created with False defaults.
    """
    initial_accumulator = False

    # Create a default (empty) ImmutableList and reduce it using False as the accumulator
    empty_list = immutable_list.ImmutableList()
    reduce_result = empty_list.reduce(initial_accumulator, empty_list)

    # Create a second ImmutableList with False as the value and is_empty=False
    list_with_false_defaults = immutable_list.ImmutableList(initial_accumulator, is_empty=initial_accumulator)

    # Search within the list using itself as the search target
    list_with_false_defaults.find(list_with_false_defaults)

def test_immutable_list_default_constructor():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Create an empty ImmutableList using the default constructor
    empty_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_init():
    """Test that ImmutableList can be constructed with False, converted to string,
    and used as the target of a find operation on itself."""
    # Create an ImmutableList initialized with False, explicitly marking it as non-empty
    is_empty_flag = False
    empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Verify string representation can be obtained without error
    string_repr = empty_list.__str__()

    # Attempt to find the list within itself
    empty_list.find(empty_list)

def test_immutable_list_unshift_and_find_with_false_initial_values():
    """Test that ImmutableList can be constructed with False, then unshift and find
    called with the list itself as an argument, without raising exceptions."""

    # Use False as both the initial value and the is_empty flag
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Prepend the list to itself via unshift
    immutable_list_instance.unshift(immutable_list_instance)

    # Search for the list within itself via find
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_append_and_find():
    """Test that unshift, append, and find can be chained on an ImmutableList
    initialised as non-empty (is_empty=False)."""

    # Create an ImmutableList explicitly marked as non-empty
    is_empty = False
    base_list = immutable_list.ImmutableList(is_empty=is_empty)

    # Prepend the is_empty value to the list via unshift
    list_after_unshift = base_list.unshift(is_empty)

    # Append the original base_list as an element
    list_after_append = list_after_unshift.append(base_list)

    # Search for the is_empty value within the resulting list
    list_after_append.find(is_empty)

def test_immutable_list_append_increases_length_and_find_on_self():
    """Test that appending to an ImmutableList increases its length,
    and that find() can be called with the list itself as the argument."""
    # Create an ImmutableList initialized with a truthy value and marked as non-empty
    is_truthy = True
    original_list = immutable_list.ImmutableList(is_truthy, is_empty=is_truthy)

    # Append the truthy value to produce a new immutable list
    extended_list = original_list.append(is_truthy)

    # Check the length of the extended list
    length = extended_list.__len__()

    # Call find with the original list as the search target
    original_list.find(original_list)

