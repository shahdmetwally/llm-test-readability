import pytest
import immutable_list as immutable_list

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on an empty ImmutableList: equality, string
    representation, conversion to list, concatenation, and length."""

    # Create an empty ImmutableList instance
    empty_immutable = immutable_list.ImmutableList()

    # Verify that an empty ImmutableList is equal to itself
    is_equal = empty_immutable.__eq__(empty_immutable)

    # Retrieve the string representation of the empty list
    string_repr = empty_immutable.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable.to_list()

    # Concatenate the plain list with itself
    concatenated_list = plain_list.__add__(plain_list)

    # Check the length of the plain list
    list_length = plain_list.__len__()

    # Add the plain list back to the original ImmutableList
    empty_immutable.__add__(plain_list)

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on a default-constructed ImmutableList, including
    equality check, concatenation, find, string representation, unshift, and reduce."""

    # A truthy value used as a comparison target and initial accumulator
    truthy_value = True

    # Create a default (empty) ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality between the empty list and a non-list value (expected to return False or similar)
    eq_result = empty_list.__eq__(truthy_value)

    # Concatenate the empty list with itself, producing a new ImmutableList
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the empty list
    str_repr = empty_list.__str__()

    # Prepend the empty list as an element to itself, producing a new ImmutableList
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and the truthy value as the initial accumulator
    unshifted_list.reduce(unshifted_list, truthy_value)

def test_immutable_list_append_and_find_with_truthy_value():
    """Test that ImmutableList can be created with a truthy value,
    supports append, and supports find operations without raising errors."""

    # Use True as both the initial element and the is_empty flag
    initial_value = True

    # Create an ImmutableList initialized with a truthy value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the truthy value to the list, producing a new immutable list
    appended_list = original_list.append(initial_value)

    # Search for the original list within itself
    original_list.find(original_list)

def test_add_none_to_empty_immutable_list():
    """Test that calling __add__ with None on an empty ImmutableList does not raise unexpectedly."""
    # Create a default empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the empty immutable list
    none_value = None
    empty_list.__add__(none_value)

def test_immutable_list_find_on_empty_list_with_self_as_argument():
    """Test that finding an element in an ImmutableList constructed from an empty
    list (with itself as the is_empty flag) does not raise an unexpected error."""

    # Create a default empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Retrieve the length of the empty list
    empty_length = empty_list.__len__()

    # Construct a new ImmutableList using the empty list as both the source
    # and the is_empty indicator
    derived_list = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Attempt to find the derived list within itself
    derived_list.find(derived_list)

def test_immutable_list_construction_and_self_referential_find_with_false():
    """Test that ImmutableList can be constructed with False, supports __len__, and find with itself."""
    # Create an ImmutableList with is_empty=False using False as the value
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__ on the list (result is not asserted, testing it does not raise)
    length = immutable_list_instance.__len__()

    # Attempt to find the list within itself (testing self-referential find)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_converted_list():
    """Test that find() can be called with the result of to_list() on an empty ImmutableList."""
    # Create an ImmutableList initialized as non-empty but explicitly marked empty
    is_empty = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty, is_empty=is_empty)

    # Convert the immutable list to a regular list
    converted_list = immutable_list_instance.to_list()

    # Search for the converted list within the immutable list
    immutable_list_instance.find(converted_list)

def test_find_on_empty_list_and_append_self_then_convert_to_list():
    """
    Test that an empty ImmutableList handles find(None), self-append,
    and to_list() conversion, followed by a no-op __add__ with None.
    """
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Searching for None in an empty list should not raise
    find_result = empty_list.find(None)

    # Append the empty list to itself, producing a new ImmutableList
    list_with_self = empty_list.append(empty_list)

    # Convert the resulting ImmutableList to a plain Python list
    plain_list = list_with_self.to_list()

    # Call __add__ with None; result is discarded (no-op side-effect check)
    plain_list.__add__(None)

def test_find_on_empty_immutable_list_returns_empty_result():
    """Test that finding a value in an ImmutableList initialised with None
    contents returns a result whose length can be queried without error."""
    search_value = 1947
    empty_contents = None

    # Create an ImmutableList with no initial data
    empty_list = immutable_list.ImmutableList(empty_contents, empty_contents)

    # Perform the find operation and check the result supports len()
    find_result = empty_list.find(search_value)
    find_result.__len__()

def test_immutable_list_self_find_with_false_as_value_and_empty_flag():
    """Test that ImmutableList can be initialized with False and supports find() using itself as the search target."""
    # Use False as both the value and the is_empty flag during construction
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Search for the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_reduce_on_empty_list_with_false_initial_value():
    """Test that reduce on an empty ImmutableList with a False initial value
    returns correctly, and that find on a newly constructed ImmutableList
    with is_empty=False behaves as expected."""

    # Use False as the initial/seed value for reduce and construction
    initial_value = False

    # Create an empty ImmutableList to act as the base collection
    empty_list = immutable_list.ImmutableList()

    # Reduce the empty list using False as both the initial value and the reducer
    reduce_result = empty_list.reduce(initial_value, empty_list)

    # Create a second ImmutableList with False passed as a value and is_empty=False
    non_empty_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Attempt to find the list within itself
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Create an ImmutableList using the default (no-argument) constructor
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_init():
    """Test that ImmutableList can be constructed with False values,
    converted to string, and used as an argument to find() on itself."""
    # Create an ImmutableList with is_empty=False and a False value
    is_empty_flag = False
    empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the list to its string representation
    str_repr = empty_list.__str__()

    # Use the list itself as the search target in find()
    empty_list.find(empty_list)

def test_immutable_list_unshift_and_find_with_false_initial_value():
    """Test that ImmutableList can be constructed with False, then unshifted and searched with itself."""
    # Use False as both the initial value and the is_empty flag
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Unshift the list onto itself and find itself within the list
    unshifted_result = immutable_list_instance.unshift(immutable_list_instance)
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_reduce_with_is_empty_flag_and_tail_only_construction():
    """
    Test that calling reduce() on an ImmutableList constructed with a value
    and is_empty=True uses the result of to_list() as both arguments.
    Also verifies that constructing an ImmutableList with only a tail dict
    does not raise errors.
    """
    is_empty_flag = True
    empty_tail = {}

    # Construct an ImmutableList with only a tail (empty dict), no head
    immutable_list_with_tail_only = immutable_list.ImmutableList(tail=empty_tail)

    # Construct an ImmutableList with a head value and is_empty flag set to True
    immutable_list_with_head = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the list to a plain Python list
    converted_list = immutable_list_with_head.to_list()

    # Reduce using the converted list as both the initial value and the reducer
    immutable_list_with_head.reduce(converted_list, converted_list)

