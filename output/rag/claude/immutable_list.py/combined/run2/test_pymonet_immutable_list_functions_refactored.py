import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Test that an empty ImmutableList supports equality, string conversion, list conversion, concatenation, and length operations."""

    # Create an empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Verify the list can be compared to itself for equality
    equality_result = empty_immutable_list.__eq__(empty_immutable_list)

    # Verify the list can be converted to its string representation
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a regular Python list
    converted_list = empty_immutable_list.to_list()

    # Verify the converted list supports concatenation with itself
    concatenated_list = converted_list.__add__(converted_list)

    # Verify the converted list supports length queries
    list_length = converted_list.__len__()

    # Verify the ImmutableList itself supports concatenation with the converted list
    empty_immutable_list.__add__(converted_list)

def test_empty_immutable_list_basic_operations():
    """Verify that ImmutableList supports equality, concatenation, find, str, unshift, and reduce without errors."""
    true_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality with a non-list value (bool)
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the list
    find_result = empty_list.find(eq_result)

    # Convert the list to its string representation
    str_representation = empty_list.__str__()

    # Prepend the empty list to itself
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer, with true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_with_bool_value_append_and_find():
    """Test that ImmutableList supports construction with a bool, append, and find."""

    # Use a boolean as both the list content and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with the boolean value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same boolean value, producing a new immutable list
    appended_list = original_list.append(initial_value)

    # Call find on the original list, searching for itself
    original_list.find(original_list)

def test_immutable_list_add_with_none_does_not_raise():
    """Test that calling __add__ with None on an empty ImmutableList does not raise an exception."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the empty list; should not raise
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_construction_from_empty_and_self_referential_find():
    """Test that ImmutableList can be constructed from an empty list and that find() can be called with the list as its own argument."""

    # Create an empty ImmutableList and record its length
    empty_list = immutable_list.ImmutableList()
    empty_list_length = empty_list.__len__()

    # Construct a new ImmutableList using the empty list as both the iterable
    # and the is_empty argument
    list_from_empty = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Call find on the new list using itself as the search argument
    list_from_empty.find(list_from_empty)

def test_immutable_list_construction_and_basic_methods_with_false_value():
    """Test that ImmutableList constructed with False supports __len__ and find without error."""

    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with the false value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __len__ and capture the result (no assertion; exercises the method)
    length_result = immutable_list_instance.__len__()

    # Call find with the list itself as the search target
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list():
    """Test that ImmutableList initialized with False supports to_list() and find() with the result."""

    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as content and marked as empty
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Convert the immutable list to a regular Python list
    converted_list = immutable_list_instance.to_list()

    # Search the immutable list using the converted list as the search argument
    immutable_list_instance.find(converted_list)

def test_immutable_list_find_none_append_self_and_convert_to_list():
    """Test that an empty ImmutableList can find None, append itself, convert to a plain list, and call __add__ with None."""

    # Create an empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Use None as the value to search for and to pass to __add__
    none_value = None

    # Search for None in the empty list
    find_result = empty_immutable_list.find(none_value)

    # Append the list to itself, producing a new ImmutableList containing itself as an element
    immutable_list_with_self = empty_immutable_list.append(empty_immutable_list)

    # Convert the resulting ImmutableList to a plain Python list
    converted_list = immutable_list_with_self.to_list()

    # Attempt to add None to the converted list via __add__
    converted_list.__add__(none_value)

def test_immutable_list_map_accepts_to_list_result():
    """Test that map() on an ImmutableList accepts the result of to_list() as its argument."""
    # Create a non-empty ImmutableList by explicitly setting is_empty=False
    is_empty_flag = False
    non_empty_immutable_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Convert to list (return value unused; exercises the to_list path)
    initial_list_contents = non_empty_immutable_list.to_list()

    # Create a second ImmutableList using the default constructor (return value unused)
    default_immutable_list = immutable_list.ImmutableList()

    # Obtain the list representation again to use as the argument to map()
    list_contents_for_map = non_empty_immutable_list.to_list()

    # Verify that map() accepts the list produced by to_list() without error
    non_empty_immutable_list.map(list_contents_for_map)

def test_immutable_list_none_values_across_operations():
    """Test that ImmutableList handles None across construction, unshift, append, and map."""
    none_value = None

    # Construct an ImmutableList with None as both arguments
    initial_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the initial list
    unshifted_with_none = initial_list.unshift(none_value)

    # Prepend the previously unshifted list into the initial list
    unshifted_with_list = initial_list.unshift(unshifted_with_none)

    # Append None to the unshifted list
    appended_list = unshifted_with_none.append(none_value)

    # Map None over the appended list
    appended_list.map(none_value)

def test_immutable_list_filter_with_self_as_predicate():
    """Test that ImmutableList.filter() accepts itself as a filter argument when constructed with is_empty=False."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct a non-empty ImmutableList with False as its value
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Filter the list using itself as the filter predicate
    non_empty_list.filter(non_empty_list)

def test_immutable_list_add_self_then_filter_by_length():
    """Test that an ImmutableList can be concatenated with itself, its length retrieved, and then filtered by that length without error."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Concatenate the list with itself using __add__
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    list_length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the filter argument
    concatenated_list.filter(list_length)

def test_find_on_none_initialized_immutable_list_returns_sized_result():
    """Test that find() on an ImmutableList initialized with None arguments returns a result supporting __len__."""
    # The integer value to search for within the immutable list
    search_target = 1947

    # Use None for both constructor arguments to initialize the list
    none_value = None
    immutable_list_instance = immutable_list.ImmutableList(none_value, none_value)

    # Perform the find operation and verify the result supports __len__
    find_result = immutable_list_instance.find(search_target)
    find_result.__len__()

def test_immutable_list_find_with_self_as_argument():
    """Test that ImmutableList.find() can be called with the list instance itself as the search argument."""

    # Use False both as the list value and to indicate the list is not empty
    false_value = False

    # Construct an ImmutableList with False as content and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find() using the list instance itself as the search target
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_and_find_with_bool_and_list_args():
    """Test that reduce and find can be called on ImmutableList instances constructed with boolean and list arguments without raising errors."""
    # Use False as both the reduce seed and the is_empty flag
    false_value = False

    # Create a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Call reduce with a boolean seed and the empty list as the combining value
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Create a second ImmutableList using the boolean as a value and as the is_empty flag
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find using the second list itself as the search predicate/argument
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction_succeeds():
    """Tests that ImmutableList can be instantiated with no arguments."""
    # Construct an ImmutableList using the default (no-argument) constructor
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Test that ImmutableList constructed with False supports __str__ and find operations without error."""

    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList treating False as both value and empty indicator
    empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Verify that string conversion completes without error
    string_representation = empty_list.__str__()

    # Verify that find accepts the list itself as a search argument without error
    empty_list.find(empty_list)

def test_immutable_list_unshift_and_find_with_self_as_argument():
    """Test that ImmutableList supports unshift and find operations when initialized with False and is_empty=False."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with is_empty explicitly set to False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Prepend the list to itself and capture the result
    unshifted_list = immutable_list_instance.unshift(immutable_list_instance)

    # Search for the original list within itself (using the list as the search target)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_append_and_find_operations():
    """Test that unshift, append, and find can be chained on an ImmutableList created with is_empty=False."""

    # Use False as the is_empty flag and later as the value to search/unshift
    is_empty_flag = False

    # Create a base ImmutableList that is not considered empty
    base_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Prepend the flag value to the front of the list
    list_after_unshift = base_list.unshift(is_empty_flag)

    # Append the base list to the unshifted list
    list_after_append = list_after_unshift.append(base_list)

    # Search for the flag value in the resulting list
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_len_and_find_operations():
    """Test that ImmutableList supports append, __len__, and find after construction with a boolean value."""
    # Use True as the initial element value and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with a single boolean element, marking it as non-empty
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same boolean value to produce a new immutable list
    appended_list = original_list.append(initial_value)

    # Retrieve the length of the appended list
    list_length = appended_list.__len__()

    # Perform a find operation on the original list using itself as the search target
    original_list.find(original_list)

def test_immutable_list_chained_operations_with_nested_instances():
    """Tests that ImmutableList supports chained operations (append, reduce, eq, unshift, str, find) without raising exceptions."""

    # Create an empty ImmutableList as the base instance
    empty_list = immutable_list.ImmutableList()

    # Append the list to itself, producing a new list containing itself as an element
    list_with_self_appended = empty_list.append(empty_list)

    # Reduce using the appended list as both the initial value and the reducer
    reduce_result = empty_list.reduce(list_with_self_appended, list_with_self_appended)

    # Check equality between the appended list and the original empty list
    eq_result = list_with_self_appended.__eq__(empty_list)

    # Prepend the appended list to itself via unshift
    unshifted_list = list_with_self_appended.unshift(list_with_self_appended)

    # Get the string representation of the unshifted list
    str_repr = unshifted_list.__str__()

    # Construct a new ImmutableList using the string repr as the is_empty keyword argument
    list_from_str_is_empty = immutable_list.ImmutableList(is_empty=str_repr)

    # Append the reduce result to itself
    reduced_appended = reduce_result.append(reduce_result)

    # Search for the reduce result within the unshifted list
    unshifted_list.find(reduce_result)

def test_immutable_list_chained_operations_with_reduce_and_find():
    """Tests chained ImmutableList operations including unshift, reduce, __len__, __eq__, and find."""

    # Create an empty ImmutableList as the base
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list to itself, producing a new list containing itself as an element
    list_with_self_prepended = empty_list.unshift(empty_list)

    # Reduce the prepended list using itself as both the accumulator and the reducing function
    reduced_result = empty_list.reduce(list_with_self_prepended, list_with_self_prepended)

    # Capture the length of the prepended list for use as a constructor argument later
    length_of_prepended = list_with_self_prepended.__len__()

    # Prepend the prepended list to itself, producing a further nested list
    list_with_prepended_prepended = list_with_self_prepended.unshift(list_with_self_prepended)

    # Check equality between the doubly-prepended list and the original empty list
    is_equal_to_empty = list_with_prepended_prepended.__eq__(empty_list)

    # Construct a new ImmutableList using the captured length as the is_empty flag
    list_with_is_empty_flag = immutable_list.ImmutableList(is_empty=length_of_prepended)

    # Invoke find on the reduced result, searching for itself
    reduced_result.find(reduced_result)

def test_immutable_list_reduce_with_to_list_result_as_both_args():
    """Test that reduce can be called on an ImmutableList using the to_list() result as both arguments."""

    # Basic flag and empty dict used as constructor inputs
    true_flag = True
    empty_dict = {}

    # Create an ImmutableList with an empty dict as its tail
    list_with_empty_tail = immutable_list.ImmutableList(tail=empty_dict)

    # Create a non-empty ImmutableList, explicitly marking it as non-empty
    non_empty_immutable_list = immutable_list.ImmutableList(true_flag, is_empty=true_flag)

    # Convert the ImmutableList to a plain list
    list_result = non_empty_immutable_list.to_list()

    # Call reduce using the list result as both the function and the initial value
    non_empty_immutable_list.reduce(list_result, list_result)

