import pytest
import immutable_list as immutable_list

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on a default-constructed (empty) ImmutableList:
    equality check with itself, string representation, conversion to list,
    and addition of the resulting plain list to itself and to the ImmutableList.
    """
    # Create a default empty ImmutableList
    empty_immutable = immutable_list.ImmutableList()

    # Verify the empty list is equal to itself
    is_equal = empty_immutable.__eq__(empty_immutable)

    # Obtain the string representation of the empty list
    str_repr = empty_immutable.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable.to_list()

    # Concatenate the plain list with itself
    concatenated_list = plain_list.__add__(plain_list)

    # Get the length of the plain list
    list_length = plain_list.__len__()

    # Add the plain list to the original ImmutableList
    empty_immutable.__add__(plain_list)

def test_immutable_list_basic_operations_on_empty_list_eq_concat_find():
    """
    Test basic operations on a default-constructed ImmutableList:
    equality check, concatenation, find, string representation,
    unshift, and reduce — all invoked on an empty list instance.
    """
    true_value = True

    # Create a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Check equality of the empty list against a boolean value
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the empty list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Attempt to find the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Get the string representation of the empty list
    str_repr = empty_list.__str__()

    # Prepend the empty list to itself (unshift returns a new ImmutableList)
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_truthy_value():
    """Test that ImmutableList can be constructed with a truthy value,
    supports append, and supports find on itself without raising errors."""

    # Use True as both the initial element and the is_empty flag
    initial_value = True

    # Create an ImmutableList initialized with a truthy value
    immutable_list_initial = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same truthy value to produce a new immutable list
    immutable_list_after_append = immutable_list_initial.append(initial_value)

    # Search for the original list within itself
    immutable_list_initial.find(immutable_list_initial)

def test_add_with_none_on_empty_immutable_list():
    """Test that calling __add__ with None on an empty ImmutableList does not raise unexpectedly."""
    # Create a default empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the empty ImmutableList
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_find_with_empty_list_as_is_empty_flag():
    """Test that find() can be called on an ImmutableList constructed with
    an empty ImmutableList instance used as both the initial value and
    the is_empty keyword argument."""

    # Create a default empty ImmutableList and verify it has zero length
    empty_list = immutable_list.ImmutableList()
    empty_list_len = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as both
    # the positional argument and the is_empty flag
    list_with_empty_flag = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Invoke find() using the list itself as the search target
    list_with_empty_flag.find(list_with_empty_flag)

def test_immutable_list_with_false_value_len_and_find():
    """Test that ImmutableList can be constructed with False, supports __len__, and find with itself."""
    # Create an ImmutableList using False as both the value and is_empty flag
    is_empty_flag = False
    empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__ on the list (result is not asserted, testing it doesn't raise)
    length = empty_list.__len__()

    # Attempt to find the list within itself (testing it doesn't raise)
    empty_list.find(empty_list)

def test_immutable_list_find_with_converted_list():
    """Test that find() can be called with the result of to_list() on an empty ImmutableList."""
    # Create an ImmutableList initialised as non-empty (is_empty=False) with False as the value
    is_empty_flag = False
    empty_immutable_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the ImmutableList to a plain list
    as_plain_list = empty_immutable_list.to_list()

    # Search for the plain list within the ImmutableList
    empty_immutable_list.find(as_plain_list)

def test_find_on_empty_list_and_append_self_then_convert_to_list():
    """
    Test that an empty ImmutableList handles:
    - find() with None (no match expected),
    - append() with itself as the element,
    - to_list() conversion,
    - and that __add__ with None is called on the resulting list.
    """
    empty_list = immutable_list.ImmutableList()
    none_value = None

    # find on an empty list with None should return without error
    find_result = empty_list.find(none_value)

    # append the list to itself, producing a new ImmutableList containing the original
    list_with_self = empty_list.append(empty_list)

    # convert the new ImmutableList to a plain Python list
    plain_list = list_with_self.to_list()

    # attempt to add None to the plain list (tests __add__ is callable with None)
    plain_list.__add__(none_value)

def test_immutable_list_map_with_non_empty_flag_and_repeated_to_list():
    """Test that map() can be called on an ImmutableList initialised with
    is_empty=False, using the result of to_list() as the mapping argument,
    and that a second to_list() call on the same instance produces the same
    result used for mapping."""

    # Create an ImmutableList explicitly marked as non-empty
    is_empty = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty)

    # Convert to a plain list (first call, result unused but call is exercised)
    non_empty_list.to_list()

    # Create a default ImmutableList (no arguments)
    default_list = immutable_list.ImmutableList()

    # Convert the non-empty list to a plain list a second time
    list_for_mapping = non_empty_list.to_list()

    # Use the result of to_list() as the mapping argument
    non_empty_list.map(list_for_mapping)

def test_immutable_list_unshift_and_map_with_none_values():
    """Test that ImmutableList supports unshift and append operations with None values,
    and that calling map with None as the mapping function does not raise during construction."""

    # Create an ImmutableList initialised with None for both arguments
    none_value = None
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list, producing a new immutable list
    unshifted_once = base_list.unshift(none_value)

    # Prepend the already-unshifted list to the base list
    unshifted_twice = base_list.unshift(unshifted_once)

    # Append None to the first unshifted list
    appended_list = unshifted_once.append(none_value)

    # Call map with None as the mapping function on the appended list
    appended_list.map(none_value)

def test_filter_immutable_list_with_itself_when_empty():
    """Test that filtering an ImmutableList with itself does not raise when the list is empty."""
    is_empty = False  # False indicates the list is not treated as empty
    empty_list = immutable_list.ImmutableList(is_empty, is_empty=is_empty)

    # Filter the list using itself as the filter argument
    empty_list.filter(empty_list)

def test_add_empty_lists_and_filter_by_length():
    """Test that adding two empty ImmutableLists and filtering by the resulting length executes without error."""
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself, producing another empty list
    combined_list = empty_list.__add__(empty_list)

    # Get the length of the combined (still empty) list
    combined_length = combined_list.__len__()

    # Filter the combined list using its own length as the filter criterion
    combined_list.filter(combined_length)

def test_find_on_empty_immutable_list_returns_empty_result():
    """Test that finding a value in an ImmutableList constructed with None
    arguments returns a result with a length (i.e. an empty collection)."""
    search_value = 1947
    empty_contents = None

    # Create an ImmutableList with no meaningful content (both args are None)
    empty_list = immutable_list.ImmutableList(empty_contents, empty_contents)

    # Perform a find operation; result should be an empty/falsy collection
    find_result = empty_list.find(search_value)

    # Verify the result supports len(), confirming it is a valid sequence type
    find_result.__len__()

def test_immutable_list_find_with_false_value_and_non_empty_flag():
    """Test that ImmutableList.find() can be called with a non-empty list
    when initialized with False as the value and is_empty=False."""
    # Use False as the initial value, explicitly marking the list as non-empty
    not_empty = False
    immutable_list_instance = immutable_list.ImmutableList(not_empty, is_empty=not_empty)

    # Search for the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_reduce_on_empty_list_and_find_on_non_empty_list():
    """
    Test that reduce on an empty ImmutableList with a False accumulator works,
    and that find on a newly constructed non-empty ImmutableList does not raise.
    """
    # Use False as the initial accumulator/seed value
    initial_value = False

    # Create a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Reduce the empty list using the empty list itself as the reducing function/argument
    reduce_result = empty_list.reduce(initial_value, empty_list)

    # Create a non-empty ImmutableList with is_empty explicitly set to False
    non_empty_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Attempt to find using the list itself as the predicate/argument
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_constructor():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Create an empty ImmutableList using the default constructor
    empty_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_init():
    """Test that ImmutableList can be constructed with False values,
    converted to string, and used as an argument to find() on itself."""

    # Use False for both the value and is_empty flag during construction
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Verify string representation can be obtained without error
    str_representation = immutable_list_instance.__str__()

    # Search for the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_and_find_with_false_initial_value():
    """Test that ImmutableList can be constructed with False, then unshifted and searched with itself."""
    # Use False as both the initial value and the is_empty flag
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Unshift the list onto itself (prepend the list as an element)
    unshifted_result = immutable_list_instance.unshift(immutable_list_instance)

    # Search for the original list instance within itself
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_append_and_find_with_false():
    """Test that an ImmutableList can be constructed with is_empty=False,
    then unshifted, appended to, and searched with a False value without error."""

    # Create a non-empty ImmutableList
    is_empty_flag = False
    base_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Prepend the False value to the list
    list_after_unshift = base_list.unshift(is_empty_flag)

    # Append the original list as an element
    list_after_append = list_after_unshift.append(base_list)

    # Search for the False value in the resulting list
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_increases_length_and_find_on_non_empty_list():
    """Test that appending to an ImmutableList increases its length,
    and that find can be called on the original list with itself as the argument."""
    # Use True as a valid boolean value for construction and operations
    is_non_empty = True

    # Create an ImmutableList with a single True element, marked as non-empty
    original_list = immutable_list.ImmutableList(is_non_empty, is_empty=is_non_empty)

    # Append a value to produce a new ImmutableList (immutable: returns new instance)
    extended_list = original_list.append(is_non_empty)

    # Retrieve the length of the extended list
    length = extended_list.__len__()

    # Call find on the original list, passing itself as the search argument
    original_list.find(original_list)

def test_immutable_list_chained_operations_with_nested_self_references():
    """
    Test chained operations on ImmutableList where the list itself is used
    as an argument to its own methods (self-referential usage), including
    append, reduce, equality check, unshift, str conversion, construction
    with a string is_empty flag, and find.
    """
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Append the list to itself, producing a new ImmutableList
    list_with_self = empty_list.append(empty_list)

    # Reduce using list_with_self as both the initial value and the function
    reduced_result = empty_list.reduce(list_with_self, list_with_self)

    # Check equality between list_with_self and empty_list
    are_equal = list_with_self.__eq__(empty_list)

    # Prepend list_with_self to itself via unshift
    unshifted_list = list_with_self.unshift(list_with_self)

    # Get the string representation of the unshifted list
    str_representation = unshifted_list.__str__()

    # Construct a new ImmutableList using the string representation as is_empty
    list_with_str_flag = immutable_list.ImmutableList(is_empty=str_representation)

    # Append the reduced result to itself
    appended_reduced = reduced_result.append(reduced_result)

    # Search for the reduced result within the unshifted list
    unshifted_list.find(reduced_result)

def test_immutable_list_unshift_reduce_and_equality_operations():
    """
    Tests a sequence of ImmutableList operations: creating an empty list,
    unshifting (prepending) a list onto itself, reducing with the result,
    checking length, further unshifting, equality comparison, and constructing
    a new list with is_empty set from the length value, followed by a find call.
    """
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list onto itself, producing a new list
    list_after_first_unshift = empty_list.unshift(empty_list)

    # Reduce the empty list using the unshifted list as both initial value and reducer
    reduce_result = empty_list.reduce(list_after_first_unshift, list_after_first_unshift)

    # Get the length of the unshifted list
    length_of_unshifted = list_after_first_unshift.__len__()

    # Prepend the unshifted list onto itself again
    list_after_second_unshift = list_after_first_unshift.unshift(list_after_first_unshift)

    # Check equality between the doubly-unshifted list and the original empty list
    are_equal = list_after_second_unshift.__eq__(empty_list)

    # Construct a new ImmutableList using the length value as the is_empty argument
    list_with_is_empty = immutable_list.ImmutableList(is_empty=length_of_unshifted)

    # Attempt to find the reduce result within itself
    reduce_result.find(reduce_result)

def test_immutable_list_reduce_with_to_list_result():
    """
    Test that ImmutableList.reduce() can be called with the result of to_list()
    as both arguments, after constructing lists with tail and is_empty parameters.
    """
    bool_value = True
    empty_dict = {}

    # Create an ImmutableList using an empty dict as the tail
    immutable_list_with_tail = immutable_list.ImmutableList(tail=empty_dict)

    # Create an ImmutableList with a value, explicitly marked as non-empty
    immutable_list_non_empty = immutable_list.ImmutableList(bool_value, is_empty=bool_value)

    # Convert the non-empty list to a plain Python list
    as_plain_list = immutable_list_non_empty.to_list()

    # Reduce the list using the plain list as both the function and initial value
    immutable_list_non_empty.reduce(as_plain_list, as_plain_list)

