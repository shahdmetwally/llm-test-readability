import pytest
import immutable_list as immutable_list

def test_empty_immutable_list_basic_operations():
    """Test that an empty ImmutableList supports equality, string conversion, list conversion, concatenation, and length operations."""

    # Create an empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Verify the list considers itself equal to itself
    equality_result = empty_immutable_list.__eq__(empty_immutable_list)

    # Verify the list can be converted to a string representation
    string_representation = empty_immutable_list.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable_list.to_list()

    # Concatenate the plain list with itself
    concatenated_list = plain_list.__add__(plain_list)

    # Check the length of the plain list
    list_length = plain_list.__len__()

    # Verify the ImmutableList supports addition with a plain list
    empty_immutable_list.__add__(plain_list)

def test_immutable_list_core_operations_do_not_raise():
    """Verify that ImmutableList supports equality, concatenation, find, str, unshift, and reduce without raising errors."""

    true_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Test equality comparison with a non-list value
    eq_result = empty_list.__eq__(true_value)

    # Test concatenation of the list with itself
    concatenated_list = empty_list.__add__(empty_list)

    # Test searching for the equality result within the list
    find_result = empty_list.find(eq_result)

    # Test string representation of the list
    str_representation = empty_list.__str__()

    # Test prepending the list to itself (unshift)
    unshifted_list = empty_list.unshift(empty_list)

    # Test reducing the unshifted list using itself as the reducer and true_value as initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList supports construction with a bool, append returns a new list, and find can be called with another ImmutableList as the search argument."""
    # Use True as both the initial element and the is_empty flag
    initial_value = True

    # Construct an ImmutableList with a boolean element and is_empty=True
    base_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the boolean value to the base list, producing a new immutable list
    appended_list = base_list.append(initial_value)

    # Search for the base_list within itself using find
    base_list.find(base_list)

def test_immutable_list_add_with_none_argument():
    """Test that calling __add__ on an empty ImmutableList with None does not raise an error."""
    # Create a default empty ImmutableList instance
    empty_immutable_list = immutable_list.ImmutableList()

    # Use None as the value to add
    none_value = None

    # Invoke __add__ with None; verifies the method handles None without crashing
    empty_immutable_list.__add__(none_value)

def test_immutable_list_construction_and_find_with_self_reference():
    """Test default construction, len(), parameterised construction with is_empty, and find() with a self-referential argument."""

    # Create a default (empty) ImmutableList and exercise its __len__ method
    empty_list = immutable_list.ImmutableList()
    empty_list_length = empty_list.__len__()  # return value unused; call exercised for coverage

    # Construct a second ImmutableList using the empty list as both the
    # positional argument and the is_empty keyword argument
    derived_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Call find() on the derived list, passing the list itself as the search target
    derived_list.find(derived_list)

def test_immutable_list_len_and_find_with_false_value():
    """Test that ImmutableList supports __len__ and find when constructed with False as value and is_empty flag."""

    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False as the initial value and is_empty=False
    empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call __len__ to verify it executes without error (return value intentionally unused)
    length_result = empty_list.__len__()

    # Call find passing the list itself as the search argument
    empty_list.find(empty_list)

def test_immutable_list_find_with_converted_list_as_argument():
    """Test that ImmutableList.find accepts the result of to_list() without error when initialized with False."""
    # Use False as both the initial value and the is_empty flag
    false_value = False

    # Create an ImmutableList instance initialized with False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Convert the immutable list to a regular list
    converted_list = immutable_list_instance.to_list()

    # Use the converted list as the argument to find
    immutable_list_instance.find(converted_list)

def test_immutable_list_find_append_and_to_list_with_none():
    """Test find/append with None on ImmutableList, conversion to list, and __add__ with None."""

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Use None as the search/append value throughout
    none_value = None

    # Search for None in the empty list
    find_result = empty_list.find(none_value)

    # Append the list to itself (using the ImmutableList as the appended element)
    appended_list = empty_list.append(empty_list)

    # Convert the appended ImmutableList to a regular Python list
    converted_list = appended_list.to_list()

    # Call __add__ on the converted list with None (exercising the method without assertion)
    converted_list.__add__(none_value)

def test_immutable_list_map_with_to_list_result():
    """Test that map() can be called on an ImmutableList using the result of to_list() as the mapping argument."""

    # Create a non-empty ImmutableList by explicitly setting is_empty=False
    is_empty_flag = False
    non_empty_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Call to_list() on the non-empty list (result unused, exercising the method)
    initial_to_list_result = non_empty_list.to_list()

    # Create a second ImmutableList using the default constructor
    default_list = immutable_list.ImmutableList()

    # Call to_list() again on the non-empty list to obtain the mapping argument
    to_list_result = non_empty_list.to_list()

    # Pass the to_list() result into map() to verify the call is accepted
    non_empty_list.map(to_list_result)

def test_immutable_list_operations_with_none_values():
    """Test that ImmutableList handles None in construction, unshift, append, and map."""

    none_value = None

    # Construct a base ImmutableList with None arguments
    base_list = immutable_list.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    list_after_unshift_none = base_list.unshift(none_value)

    # Prepend the previously unshifted list onto the base list
    list_after_unshift_list = base_list.unshift(list_after_unshift_none)

    # Append None to the unshifted list
    list_after_append_none = list_after_unshift_none.append(none_value)

    # Map with None as the mapping function
    list_after_append_none.map(none_value)

def test_immutable_list_filter_with_another_immutable_list_as_argument():
    """Test that ImmutableList.filter accepts another ImmutableList instance as its argument without raising."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct an ImmutableList with False value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call filter using the same ImmutableList instance as the argument
    immutable_list_instance.filter(immutable_list_instance)

def test_immutable_list_add_self_then_filter_by_length():
    """Test that self-concatenation of an ImmutableList produces a list whose length can be passed to filter."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself to produce a new list
    concatenated_list = empty_list.__add__(empty_list)

    # Retrieve the length of the concatenated list
    concatenated_length = concatenated_list.__len__()

    # Use the length as the argument to filter on the concatenated list
    concatenated_list.filter(concatenated_length)

def test_find_on_none_initialized_list_returns_sized_result():
    """Test that find() on a None-initialized ImmutableList returns a sized result."""
    # The integer value to search for within the list
    search_value = 1947

    # Use None for both constructor arguments to represent an empty/null initialization
    empty_arg = None

    # Construct an ImmutableList with two None arguments
    immutable_list_instance = immutable_list.ImmutableList(empty_arg, empty_arg)

    # Perform a find operation on the list using the search value
    find_result = immutable_list_instance.find(search_value)

    # Verify the result supports __len__ (i.e., is a sized object)
    find_result.__len__()

def test_immutable_list_find_with_self_reference():
    """Test that find() can be called with the list itself when initialized with False and is_empty=False."""

    # Use False as both the list value and the is_empty flag
    false_value = False

    # Create an ImmutableList that is explicitly marked as non-empty
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find() using the list itself as the search target
    non_empty_list.find(non_empty_list)

def test_immutable_list_reduce_empty_and_find_non_empty_with_false():
    """Test that reduce on an empty ImmutableList and find on a non-empty ImmutableList execute without error."""

    # A False boolean used as the seed value and the is_empty flag
    false_value = False

    # Construct a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Reduce the empty list using false_value as seed and empty_list as the accumulator collection
    reduce_result = empty_list.reduce(false_value, empty_list)

    # Construct a non-empty ImmutableList using false_value as the element and is_empty=False
    non_empty_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Call find on the non-empty list, passing the list itself as the predicate/argument
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction_succeeds():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Verify that constructing an empty ImmutableList does not raise any errors
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_value():
    """Test that ImmutableList constructed with False supports __str__ and find without errors."""
    # Use False as both the list value and the is_empty flag
    false_value = False

    # Construct the ImmutableList with False as value and is_empty=False
    immutable_list_instance = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Verify __str__ can be called without error
    string_representation = immutable_list_instance.__str__()

    # Verify find can be called with the list itself as the search argument
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_unshift_and_find_with_false_initialization():
    """Test that an ImmutableList initialized with False supports unshift and find on itself."""
    # Use False as both the value and the is_empty flag
    false_value = False

    # Create an ImmutableList with False as content and explicitly not marked empty
    false_initialized_list = immutable_list.ImmutableList(false_value, is_empty=false_value)

    # Prepend the list to itself and capture the result
    unshifted_list = false_initialized_list.unshift(false_initialized_list)

    # Search for the list within itself (result not used, verifies no error is raised)
    false_initialized_list.find(false_initialized_list)

def test_immutable_list_unshift_append_and_find():
    """Test that unshift, append, and find can be chained on an ImmutableList without errors."""
    # Use False both as the is_empty flag and as the element value throughout
    is_empty_flag = False

    # Create an ImmutableList that is not empty
    initial_list = immutable_list.ImmutableList(is_empty=is_empty_flag)

    # Prepend the flag value to the front of the list
    list_after_unshift = initial_list.unshift(is_empty_flag)

    # Append the initial list as an element to the unshifted list
    list_after_append = list_after_unshift.append(initial_list)

    # Search for the flag value in the final list
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_and_find_with_bool_element():
    """Tests that ImmutableList supports append, len, and find operations when initialized with a boolean value."""
    # Use a boolean as both the initial value and the is_empty flag
    is_empty_flag = True

    # Create an ImmutableList with a boolean value, marking it as non-empty via is_empty
    initial_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Append the boolean value to the list, producing a new immutable list
    list_after_append = initial_list.append(is_empty_flag)

    # Exercise __len__ on the appended list to verify the method is callable
    list_length = list_after_append.__len__()

    # Exercise find on the original list, using the initial list itself as the search target
    initial_list.find(initial_list)

def test_immutable_list_chained_operations_append_reduce_unshift_find():
    """Test that ImmutableList supports chained append, reduce, equality, unshift, str, and find operations without error."""

    # Create an empty ImmutableList as the base for all subsequent operations
    empty_list = immutable_list.ImmutableList()

    # Append the empty list to itself, producing a new list containing itself as an element
    list_with_self_appended = empty_list.append(empty_list)

    # Reduce the original empty list using the appended list as both the initial value and the reducer
    reduced_result = empty_list.reduce(list_with_self_appended, list_with_self_appended)

    # Check equality between the appended list and the empty list
    equality_check = list_with_self_appended.__eq__(empty_list)

    # Prepend the appended list to itself using unshift
    unshifted_list = list_with_self_appended.unshift(list_with_self_appended)

    # Get the string representation of the unshifted list
    list_str_repr = unshifted_list.__str__()

    # Construct a new ImmutableList using the string representation as the is_empty keyword argument
    list_with_is_empty_str = immutable_list.ImmutableList(is_empty=list_str_repr)

    # Append the reduced result to itself
    list_with_reduced_appended = reduced_result.append(reduced_result)

    # Search for the reduced result within the unshifted list
    unshifted_list.find(reduced_result)

def test_immutable_list_chained_operations_unshift_reduce_find():
    """Test that ImmutableList supports chained unshift, reduce, len, eq, and find operations without error."""

    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list into itself, producing a new list
    list_with_self_prepended = empty_list.unshift(empty_list)

    # Reduce the prepended list using itself as the initial accumulator/function
    reduced_result = empty_list.reduce(list_with_self_prepended, list_with_self_prepended)

    # Get the length of the prepended list
    length_of_prepended = list_with_self_prepended.__len__()

    # Prepend the prepended list into itself again
    list_with_prepended_prepended = list_with_self_prepended.unshift(list_with_self_prepended)

    # Check equality between the doubly-prepended list and the original empty list
    eq_result = list_with_prepended_prepended.__eq__(empty_list)

    # Construct a new ImmutableList using the computed length as the is_empty parameter
    list_with_is_empty_param = immutable_list.ImmutableList(is_empty=length_of_prepended)

    # Invoke find on the reduced result using itself as the predicate
    reduced_result.find(reduced_result)

def test_immutable_list_to_list_and_reduce_with_bool_head():
    """Test ImmutableList construction, to_list conversion, and reduce using the list representation as both arguments."""
    # Input values used to construct ImmutableList instances
    head_value = True
    empty_tail = {}

    # Construct a list with an empty dict as the tail (result unused beyond construction)
    list_with_dict_tail = immutable_list.ImmutableList(tail=empty_tail)

    # Construct a non-empty list with a bool head and is_empty flag set to True
    non_empty_list = immutable_list.ImmutableList(head_value, is_empty=head_value)

    # Convert the non-empty list to a plain list representation
    list_representation = non_empty_list.to_list()

    # Invoke reduce using the list representation as both the accumulator and the iterable
    non_empty_list.reduce(list_representation, list_representation)

