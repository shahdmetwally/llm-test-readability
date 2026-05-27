import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Tests that an empty ImmutableList supports equality, string conversion, list conversion, concatenation, and length operations."""

    # Create an empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Verify the list considers itself equal to itself
    equality_result = empty_immutable_list.__eq__(empty_immutable_list)

    # Verify the list can be converted to a string representation
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a plain Python list
    converted_list = empty_immutable_list.to_list()

    # Concatenate the converted list with itself using list's __add__
    concatenated_list = converted_list.__add__(converted_list)

    # Retrieve the length of the converted list
    list_length = converted_list.__len__()

    # Verify ImmutableList's __add__ works with a plain list
    empty_immutable_list.__add__(converted_list)

def test_immutable_list_core_operations_on_empty_list():
    """Verify core ImmutableList operations (eq, add, find, str, unshift, reduce) execute without error on an empty list."""

    # A non-list value used to probe equality behaviour
    non_list_value = True

    # Construct an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Check equality against a non-list value
    eq_result = empty_list.__eq__(non_list_value)

    # Concatenate the empty list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the empty list
    string_repr = empty_list.__str__()

    # Prepend the empty list to itself via unshift
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as reducer and non_list_value as initial value
    unshifted_list.reduce(unshifted_list, non_list_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Tests that ImmutableList can be constructed with a bool, appended to, and searched via find."""
    # Use a boolean as both the initial value and the is_empty flag
    bool_value = True

    # Construct the initial immutable list with the boolean value
    initial_list = immutable_list.ImmutableList(bool_value, is_empty=bool_value)

    # Append the boolean value to produce a new immutable list
    appended_list = initial_list.append(bool_value)

    # Search for the original list within itself using find
    initial_list.find(initial_list)

def test_immutable_list_add_with_none_does_not_raise():
    """Test that calling __add__ with None on an empty ImmutableList does not raise an error."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the empty list; should not raise
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_construction_and_find_with_empty_list():
    """Test that ImmutableList can be constructed from an empty list, reports its length, and supports find() calls."""

    # Create a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Call __len__ to confirm it executes without error on an empty list
    empty_list_length = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as both the source
    # and the is_empty indicator
    list_with_empty_source = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Call find on the new list, passing itself as the search target
    list_with_empty_source.find(list_with_empty_source)

def test_immutable_list_construction_and_basic_method_calls():
    """Tests that ImmutableList can be constructed with False values and supports __len__ and find method calls."""

    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct the ImmutableList with False as content and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __len__ to verify it executes without error (result is not further asserted)
    length_result = immutable_list_instance.__len__()

    # Call find with the list itself as the search target to verify it executes without error
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_list_representation():
    """Test that ImmutableList constructed with False supports to_list() and find() using the resulting list."""
    # Use False as both the initial value and the is_empty flag
    initial_value = False

    # Construct the ImmutableList with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Convert the ImmutableList to a standard Python list
    list_representation = immutable_list_instance.to_list()

    # Use the list representation as the argument to find()
    immutable_list_instance.find(list_representation)

def test_immutable_list_find_append_and_convert_to_list():
    """Tests that ImmutableList supports find with None, self-append, to_list conversion, and __add__ with None."""

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Use None as a search/operand value throughout the test
    none_value = None

    # Search for None in the empty list
    find_result = empty_list.find(none_value)

    # Append the list to itself, producing a new ImmutableList
    list_with_self_appended = empty_list.append(empty_list)

    # Convert the new ImmutableList to a plain Python list
    plain_list = list_with_self_appended.to_list()

    # Attempt to add None to the plain list (result is not captured, testing no exception is raised)
    plain_list.__add__(none_value)

def test_immutable_list_to_list_and_map_with_non_empty_flag():
    """Test that to_list() and map() can be called on an ImmutableList initialized with is_empty=False."""

    # Create an ImmutableList explicitly marked as non-empty
    is_empty_false = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty_false)

    # Call to_list() on the non-empty list (result unused, exercising the call path)
    initial_to_list_result = non_empty_list.to_list()

    # Create a second ImmutableList using default constructor arguments
    default_list = immutable_list.ImmutableList()

    # Call to_list() again on the original non-empty list to use as input for map()
    to_list_result = non_empty_list.to_list()

    # Call map() on the non-empty list, passing the to_list() result as the mapping argument
    non_empty_list.map(to_list_result)

def test_immutable_list_unshift_append_and_map_with_none():
    """Test that ImmutableList supports chained unshift/append with None values and accepts None as a map argument."""

    none_value = None

    # Create an initial ImmutableList using None for both constructor arguments
    initial_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the initial list
    list_after_first_unshift = initial_list.unshift(none_value)

    # Prepend the already-unshifted list into the initial list (result intentionally unused)
    list_after_second_unshift = initial_list.unshift(list_after_first_unshift)

    # Append None to the first unshifted list
    list_after_append = list_after_first_unshift.append(none_value)

    # Call map with None on the appended list to verify it is accepted without error
    list_after_append.map(none_value)

def test_immutable_list_filter_with_self_as_predicate():
    """Test that ImmutableList constructed with False supports filtering with itself as the argument."""
    # False is used both as the list value and the is_empty flag
    is_empty_flag = False

    # Construct an ImmutableList with is_empty explicitly set to False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Filter the list using itself as the predicate/argument
    immutable_list_instance.filter(immutable_list_instance)

def test_immutable_list_add_self_then_filter_by_length():
    """Test that an empty ImmutableList can be added to itself, and its resulting length can be used as a filter argument without error."""

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself using __add__
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    concatenated_length = concatenated_list.__len__()

    # Use the computed length as the filter argument
    concatenated_list.filter(concatenated_length)

def test_find_on_none_initialized_immutable_list_returns_sized_result():
    """Test that find() on a None-initialized ImmutableList returns a sized result."""
    # The value to search for within the list
    search_value = 1947

    # Use None for both constructor arguments to create a minimally initialized list
    none_value = None
    empty_immutable_list = immutable_list.ImmutableList(none_value, none_value)

    # Perform the find operation and verify the result supports __len__
    find_result = empty_immutable_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_with_self_reference():
    """Test that ImmutableList initialized with False supports find() called with itself as the argument."""
    # Use False both as the list value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as its content and marked as not empty
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find() passing the list itself as the search target
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_false_seed():
    """Test that ImmutableList supports reduce with a False seed and find on a list constructed with is_empty=False."""

    # Use False as both the seed value and the is_empty flag throughout this test
    false_value = False

    # Construct a default (empty) ImmutableList to serve as the accumulator in reduce
    empty_list = immutable_list.ImmutableList()

    # Call reduce using False as the initial seed and the empty list as the accumulator argument
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Construct a second ImmutableList with False as a positional arg and is_empty=False
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find on the non-empty list, passing the list itself as the search target
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_constructor_creates_instance():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Verify that constructing an empty ImmutableList does not raise an error
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Verify that ImmutableList constructed with False supports __str__ and find with a list argument."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as content and is_empty=False
    false_valued_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Invoke __str__ to ensure string conversion does not raise
    string_representation = false_valued_list.__str__()

    # Call find with the list itself as the search target
    false_valued_list.find(false_valued_list)

def test_immutable_list_unshift_and_find_with_self_reference():
    """Test that ImmutableList supports unshift and find operations using itself as the argument."""
    # Use False as both the initial value and the is_empty flag
    initial_value = False

    # Construct an ImmutableList with False value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Unshift the list onto itself and capture the result
    unshift_result = immutable_list_instance.unshift(immutable_list_instance)

    # Find the list within itself (self-referential lookup)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_append_and_find_do_not_raise():
    """Test that unshift, append, and find operations on an ImmutableList complete without raising exceptions."""
    # Use False as both the is_empty flag and the value to search for later
    is_empty_flag = False

    # Create an initial non-empty ImmutableList
    initial_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Prepend the flag value to produce a new list
    list_after_unshift = initial_list.unshift(is_empty_flag)

    # Append the original list as an element to produce another new list
    list_after_append = list_after_unshift.append(initial_list)

    # Search for the flag value in the final list (result intentionally discarded)
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_increases_length_and_supports_find():
    """Test that appending to an ImmutableList returns a new list with correct length, and that find can be called on the original list."""
    # Use True as both the initial element value and
# (Truncated by extractor)