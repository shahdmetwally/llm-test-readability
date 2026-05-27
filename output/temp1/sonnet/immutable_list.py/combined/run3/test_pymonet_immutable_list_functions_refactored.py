import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Tests that an empty ImmutableList supports equality, string conversion, list conversion, concatenation, and length operations."""

    # Create a default empty ImmutableList
    empty_immutable_list = immutable_list.ImmutableList()

    # Verify the list reports equality when compared to itself
    is_equal_to_itself = empty_immutable_list.__eq__(empty_immutable_list)

    # Verify the list can produce a string representation
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a plain Python list
    converted_list = empty_immutable_list.to_list()

    # Verify the plain list supports concatenation with itself
    concatenated_list = converted_list.__add__(converted_list)

    # Verify the plain list reports its length
    list_length = converted_list.__len__()

    # Verify the ImmutableList supports addition with a plain list (return value intentionally discarded)
    empty_immutable_list.__add__(converted_list)

def test_immutable_list_basic_operations_on_empty_list():
    """Tests that basic ImmutableList operations execute without error on an empty list."""

    # A non-list value used to probe equality behaviour
    non_list_value = True

    # Create an empty ImmutableList as the primary subject under test
    empty_list = immutable_list.ImmutableList()

    # Check equality between the empty list and a non-list value
    eq_result = empty_list.__eq__(non_list_value)

    # Concatenate the empty list with itself via __add__
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the empty list
    string_repr = empty_list.__str__()

    # Prepend the empty list as an element to itself (unshift)
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and the non-list value as the initial accumulator
    unshifted_list.reduce(unshifted_list, non_list_value)

def test_immutable_list_append_and_find_do_not_raise():
    """Verify that ImmutableList supports construction, append, and find without raising exceptions."""
    # Use a boolean True as both the stored element and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with the initial value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the value to produce a new immutable list (original remains unchanged)
    list_after_append = original_list.append(initial_value)

    # Search for the original list within itself; result is not asserted — tests no exception is raised
    original_list.find(original_list)

def test_immutable_list_add_with_none_argument():
    """Test that __add__ can be called on an empty ImmutableList with None without error."""
    # Create a default empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Use None as the operand for the addition
    none_value = None

    # Invoke __add__ with None; verifies the call does not raise unexpectedly
    empty_immutable_list.__add__(none_value)

def test_immutable_list_construction_and_find_with_self_reference():
    """Test that ImmutableList can be constructed with itself as is_empty, and find can be called with itself as the search target."""

    # Create a default empty ImmutableList and verify length is retrievable
    empty_list = immutable_list.ImmutableList()
    empty_list_length = empty_list.__len__()

    # Construct a new ImmutableList using the empty list as both the data source and is_empty flag
    list_with_self_as_empty_flag = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Call find on the list using itself as the search target
    list_with_self_as_empty_flag.find(list_with_self_as_empty_flag)

def test_immutable_list_construction_with_false_and_basic_methods():
    """Test that ImmutableList can be constructed with False, and that __len__ and find are callable."""

    # Use False as both the value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False for both positional and keyword arguments
    empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __len__ directly to verify it is accessible
    length_result = empty_list.__len__()

    # Call find with the list itself as the search target
    empty_list.find(empty_list)

def test_immutable_list_find_with_converted_list():
    """Test that ImmutableList.find() accepts a list produced by to_list() when constructed with False and is_empty=False."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as the value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Convert the ImmutableList to a plain list
    converted_list = immutable_list_instance.to_list()

    # Call find() with the converted list — verifies no error is raised
    immutable_list_instance.find(converted_list)

def test_immutable_list_find_none_append_self_and_convert_to_list():
    """Test that an empty ImmutableList supports find(None), self-append, to_list conversion, and list __add__ with None."""

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    none_value = None

    # Find None within the empty list (smoke-tests the find method with None input)
    find_result = empty_list.find(none_value)

    # Append the empty list to itself, producing a new ImmutableList
    list_with_self_appended = empty_list.append(empty_list)

    # Convert the resulting ImmutableList to a plain Python list
    converted_list = list_with_self_appended.to_list()

    # Call __add__ with None on the converted list (smoke-tests list __add__ with None)
    converted_list.__add__(none_value)

def test_immutable_list_map_accepts_to_list_output():
    """Verify that to_list() output from a non-empty ImmutableList can be passed to map() without error."""
    # Create an ImmutableList explicitly marked as non-empty
    is_empty_flag = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Retrieve the list representation (intermediate call, result not used further)
    initial_to_list_result = non_empty_list.to_list()

    # Instantiate a second, default ImmutableList alongside the first
    default_list = immutable_list.ImmutableList()

    # Retrieve the list representation again to use as input for map()
    to_list_result_for_map = non_empty_list.to_list()

    # Pass the to_list() output into map() to verify it is accepted without error
    non_empty_list.map(to_list_result_for_map)

def test_immutable_list_operations_with_none_values():
    """Test that ImmutableList handles None values through unshift, append, and map operations."""

    none_value = None

    # Construct a base ImmutableList with None arguments
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    list_after_unshift_none = base_list.unshift(none_value)

    # Prepend the previously unshifted list onto the base list
    list_after_unshift_list = base_list.unshift(list_after_unshift_none)

    # Append None to the unshifted list
    list_after_append_none = list_after_unshift_none.append(none_value)

    # Map with None over the appended list
    list_after_append_none.map(none_value)

def test_immutable_list_filter_with_another_immutable_list_instance():
    """Test that ImmutableList.filter() accepts another ImmutableList instance as its argument without error."""
    # Use False for both the list value and the is_empty flag
    boolean_false = False

    # Create an ImmutableList with is_empty=False
    empty_immutable_list = immutable_list.ImmutableList(boolean_false, is_empty=boolean_false)

    # Filter the list using itself as the argument; should not raise
    empty_immutable_list.filter(empty_immutable_list)

def test_immutable_list_filter_with_length_after_self_concatenation():
    """Test that filtering a self-concatenated ImmutableList using its own length executes without error."""

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself to produce a (still-empty) combined list
    concatenated_list = empty_list.__add__(empty_list)

    # Capture the length of the concatenated list
    list_length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the filter argument
    concatenated_list.filter(list_length)

def test_find_on_none_initialized_list_returns_sized_result():
    """Test that find() on an ImmutableList constructed with None returns a sized result."""
    # The value to search for within the list
    search_value = 1947

    # Use None for both constructor arguments to create a minimally initialized list
    none_value = None
    empty_immutable_list = immutable_list.ImmutableList(none_value, none_value)

    # Perform the search and verify the result supports __len__
    find_result = empty_immutable_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_with_self_as_argument():
    """Test that ImmutableList.find() can be called with the list itself when constructed with False and is_empty=False."""
    # Use False as both the initial value and the is_empty flag
    is_empty_flag = False

    # Construct an ImmutableList with is_empty explicitly set to False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call find() using the list itself as the search argument (self-referential lookup)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_operations():
    """Tests reduce on an empty ImmutableList and find on a non-empty ImmutableList with boolean arguments."""

    # Use False as the seed value and the is_empty flag throughout
    false_value = False

    # Create an empty ImmutableList to act as the base for reduce
    empty_list = immutable_list.ImmutableList()

    # Reduce the empty list using false_value as the seed and empty_list as the reducer
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Create a non-empty ImmutableList using false_value as an element, with is_empty explicitly set to False
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find on the non-empty list, passing the list itself as the search predicate/target
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction_succeeds():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Constructing with no arguments should succeed without raising an exception
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Test that ImmutableList supports __str__ and find when constructed with False as value and is_empty flag."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False value and is_empty=False
    empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Verify that string representation can be retrieved without error
    string_representation = empty_list.__str__()

    # Verify that find can be called with the list itself as the search target
    empty_list.find(empty_list)

def test_immutable_list_unshift_and_find_with_false_value():
    """Test that an ImmutableList initialized with False supports unshift and find operations on itself."""

    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Unshift the list onto itself and capture the result
    unshifted_result = immutable_list_instance.unshift(immutable_list_instance)

    # Find the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_append_and_find():
    """Test that ImmutableList supports unshift, append, and find operations in sequence."""
    # Value used as the initial is_empty flag and later as the search target
    search_value = False

    # Create an ImmutableList that is not considered empty
    initial_list = immutable_list.ImmutableList(is_empty=search_value)

    # Prepend search_value to the front of the list
    list_after_unshift = initial_list.unshift(search_value)

    # Append the initial list to the unshifted list
    list_after_append = list_after_unshift.append(initial_list)

    # Search for search_value in the resulting list
    list_after_append.find(search_value)

def test_immutable_list_append_and_find_operations():
    """Tests that appending to an ImmutableList updates its length and that find can be called on the original list."""

    # Use True as both the initial element value and the is_empty flag
    initial_value = True

    # Create an ImmutableList seeded with initial_value, marking it as empty per the flag
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same value and capture the resulting new immutable list
    list_after_append = original_list.append(initial_value)

    # Retrieve the length of the list after appending
    length_after_append = list_after_append.__len
# (Truncated by extractor)