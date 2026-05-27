import pytest
import immutable_list as immutable_list

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on a default-constructed (empty) ImmutableList:
    equality check with itself, string representation, conversion to list,
    list concatenation, and length query."""

    # Create a default empty ImmutableList
    empty_immutable = immutable_list.ImmutableList()

    # An empty ImmutableList should be equal to itself
    is_equal = empty_immutable.__eq__(empty_immutable)

    # String representation of the empty list
    string_repr = empty_immutable.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable.to_list()

    # Concatenate the plain list with itself (produces a new list)
    concatenated_list = plain_list.__add__(plain_list)

    # Check the length of the plain list
    list_length = plain_list.__len__()

    # Add the plain list back to the original ImmutableList (result unused)
    empty_immutable.__add__(plain_list)

def test_empty_immutable_list_basic_operations():
    """Test basic operations on an empty ImmutableList: equality, string
    representation, conversion to list, concatenation, and length."""

    # Create an empty ImmutableList and verify self-equality
    empty_immutable = immutable_list.ImmutableList()
    bool_result = empty_immutable.__eq__(empty_immutable)

    # Get the string representation of the empty list
    str_result = empty_immutable.__str__()

    # Convert the ImmutableList to a plain Python list
    plain_list = empty_immutable.to_list()

    # Concatenate the plain list with itself (produces a new list)
    concatenated_list = plain_list.__add__(plain_list)

    # Check the length of the plain list
    list_length = plain_list.__len__()

    # Concatenate the plain list back onto the original ImmutableList
    empty_immutable.__add__(plain_list)

def test_immutable_list_basic_operations_on_empty_list():
    """Test basic operations on an empty ImmutableList, including equality check,
    addition, find, string representation, unshift, and reduce."""

    # A truthy value used as an argument in equality and reduce operations
    truthy_value = True

    # Create an empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Check equality of the empty list against a non-list value (bool)
    eq_result = empty_list.__eq__(truthy_value)

    # Add the empty list to itself, producing a new (still empty) list
    concatenated_list = empty_list.__add__(empty_list)

    # Attempt to find the result of the equality check within the empty list
    find_result = empty_list.find(eq_result)

    # Get the string representation of the empty list
    str_repr = empty_list.__str__()

    # Prepend the empty list to itself using unshift
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and truthy_value as initial value
    unshifted_list.reduce(unshifted_list, truthy_value)

def test_immutable_list_chained_operations_with_reduce_on_empty_list():
    """Test basic operations on a default-constructed ImmutableList with no elements."""

    # A truthy value used as an argument in equality and reduce calls
    true_value = True

    # Create a default (empty) ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Compare the empty list against a boolean; result is expected to be falsy
    eq_result = empty_list.__eq__(true_value)

    # Concatenate the empty list with itself; result should also be empty
    concatenated_list = empty_list.__add__(empty_list)

    # Search for the equality result within the empty list
    find_result = empty_list.find(eq_result)

    # Obtain the string representation of the empty list
    str_representation = empty_list.__str__()

    # Prepend the empty list itself as an element (unshift), producing a new list
    unshifted_list = empty_list.unshift(empty_list)

    # Reduce the unshifted list using itself as the reducer and true_value as the initial value
    unshifted_list.reduce(unshifted_list, true_value)

def test_immutable_list_append_and_find_with_truthy_value():
    """Test that ImmutableList can be constructed with a truthy value,
    supports append, and supports find operations without raising errors."""

    # Use True as both the initial element and the is_empty flag
    initial_value = True

    # Create an ImmutableList with a truthy element, marking it as non-empty
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the same truthy value to produce a new immutable list
    appended_list = original_list.append(initial_value)

    # Attempt to find the original list within itself
    original_list.find(original_list)

def test_immutable_list_append_and_find_with_bool_value():
    """Test that ImmutableList can be created with a bool value, supports append,
    and allows find to be called with another ImmutableList as the search target."""
    # Use True as both the initial value and the is_empty flag
    initial_value = True

    # Create an ImmutableList initialised with a boolean value
    original_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Append the boolean value to produce a new ImmutableList
    appended_list = original_list.append(initial_value)

    # Attempt to find the original list within itself
    original_list.find(original_list)

def test_immutable_list_add_with_none_returns_no_error():
    """Test that calling __add__ with None on an empty ImmutableList does not raise unexpectedly."""
    # Create a default empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    # Attempt to add None to the immutable list
    none_value = None
    empty_list.__add__(none_value)

def test_add_with_none_on_empty_immutable_list():
    """Test that calling __add__ with None on an empty ImmutableList does not raise unexpectedly."""
    # Create a new empty ImmutableList instance
    empty_list = immutable_list.ImmutableList()

    none_value = None

    # Attempt to add None to the empty ImmutableList
    empty_list.__add__(none_value)

def test_immutable_list_find_on_empty_list_with_self_as_argument():
    """
    Test that ImmutableList can be constructed with another ImmutableList
    as both the iterable and the is_empty flag, and that find() can be
    called with the list itself as the search argument without raising.
    """
    # Create an empty ImmutableList and verify its length is zero
    empty_list = immutable_list.ImmutableList()
    empty_length = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as both
    # the source iterable and the is_empty indicator
    list_with_self_reference = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Attempt to find the list within itself (exercises find() with a
    # self-referential argument on a list built from an empty source)
    list_with_self_reference.find(list_with_self_reference)

def test_immutable_list_find_with_self_referential_empty_flag():
    """
    Test that ImmutableList can be constructed with an empty list and a
    non-standard is_empty flag, and that calling find() with the list
    itself as the search target does not raise an unexpected error.
    """
    # Create a default empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Retrieve the length of the empty list (expected to be 0)
    empty_list_length = empty_list.__len__()

    # Construct a second ImmutableList using the empty list as the iterable
    # and passing the empty list itself as the is_empty flag
    list_with_self_as_empty_flag = immutable_list.ImmutableList(
        empty_list, is_empty=empty_list
    )

    # Attempt to find the list itself within the newly constructed list
    list_with_self_as_empty_flag.find(list_with_self_as_empty_flag)

def test_immutable_list_len_and_find_with_false():
    """Test that ImmutableList can be constructed with False, supports __len__, and find with itself."""
    # Create an ImmutableList with is_empty=False using False as the value
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__ on the list (result is not asserted, testing it does not raise)
    length = immutable_list_instance.__len__()

    # Attempt to find the list within itself (testing self-referential find does not raise)
    immutable_list_instance.find(immutable_list_instance)

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
    """Test that find() can be called with the result of to_list() on a non-empty ImmutableList."""
    # Create an ImmutableList initialized as non-empty (False signals not empty) but with is_empty=False
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the immutable list to a plain list
    converted_list = immutable_list_instance.to_list()

    # Search for the converted list within the immutable list
    immutable_list_instance.find(converted_list)

def test_immutable_list_find_with_converted_list():
    """Test that find() can be called with the result of to_list() on an ImmutableList initialized with False."""
    # Create an ImmutableList initialized as non-empty (is_empty=False) with False as value
    is_empty_flag = False
    empty_immutable_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the ImmutableList to a plain list
    converted_list = empty_immutable_list.to_list()

    # Search for the converted list within the ImmutableList
    empty_immutable_list.find(converted_list)

def test_filter_on_empty_concatenated_list():
    """Test that filtering an empty ImmutableList concatenated with itself
    using its own length as the filter argument executes without error."""

    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Concatenate the empty list with itself, resulting in another empty list
    concatenated_list = empty_list.__add__(empty_list)

    # Get the length of the concatenated list (expected to be 0)
    length = concatenated_list.__len__()

    # Filter the concatenated list using its own length as the filter argument
    concatenated_list.filter(length)

def test_filter_on_empty_concatenated_list():
    """Test that filtering an empty ImmutableList concatenated with itself
    using its own length as the filter argument executes without error."""

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

    # Create an ImmutableList with no initial data
    empty_list = immutable_list.ImmutableList(empty_contents, empty_contents)

    # Perform the find operation and verify the result supports len()
    find_result = empty_list.find(search_value)
    find_result.__len__()

def test_find_on_empty_immutable_list_returns_empty_result():
    """Test that finding a value in an ImmutableList initialised with None
    contents returns a result whose length can be queried without error."""
    search_value = 1947
    empty_contents = None

    # Create an ImmutableList with no initial elements
    empty_list = immutable_list.ImmutableList(empty_contents, empty_contents)

    # Perform the find operation and check the result supports len()
    find_result = empty_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_with_false_initialization():
    """Test that ImmutableList can be initialized with False and supports find() using itself as the search target."""
    # Use False as both the value and the is_empty flag during construction
    is_empty_flag = False
    immutable_list_instance = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Search for the list within itself
    immutable_list_instance.find(immutable_list_instance)

def test_immutable_list_find_with_false_as_value_and_empty_flag():
    """Test that ImmutableList can be initialized with False and supports find() on itself."""
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

    # Create a default empty ImmutableList to act as the reducer argument
    empty_list = immutable_list.ImmutableList()

    # Reduce the empty list using False as both the initial value and the reducer
    reduce_result = empty_list.reduce(initial_value, empty_list)

    # Construct a new ImmutableList with False as a value and is_empty=False
    non_empty_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Attempt to find the list within itself
    non_empty_list.find(non_empty_list)

def test_reduce_with_false_seed_and_find_on_non_empty_list():
    """Test that reduce on an empty ImmutableList with a False initial value
    returns correctly, and that find on a newly constructed ImmutableList
    with is_empty=False behaves as expected."""

    # Use False as the initial/seed value for reduce and construction flags
    initial_value = False

    # Create a default empty ImmutableList to act as the collection and accumulator argument
    empty_list = immutable_list.ImmutableList()

    # Reduce the empty list using False as the initial value and the list itself as the reducer
    reduce_result = empty_list.reduce(initial_value, empty_list)

    # Construct a new ImmutableList with False as a value and is_empty explicitly set to False
    non_empty_list = immutable_list.ImmutableList(initial_value, is_empty=initial_value)

    # Attempt to find the list within itself
    non_empty_list.find(non_empty_list)

def test_immutable_list_default_construction():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Create an ImmutableList using the default (no-argument) constructor
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_default_construction():
    """Test that ImmutableList can be instantiated with no arguments."""
    # Create an ImmutableList using the default (no-argument) constructor
    empty_immutable_list = immutable_list.ImmutableList()

def test_immutable_list_str_and_find_with_false_init():
    """Test that ImmutableList can be constructed with False values,
    converted to string, and used as an argument to find() on itself."""

    # Construct an ImmutableList with False as the value and is_empty=False
    is_empty_flag = False
    empty_list = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Verify string representation can be obtained without error
    string_repr = empty_list.__str__()

    # Attempt to find the list within itself
    empty_list.find(empty_list)

def test_immutable_list_str_and_find_with_false_init_and_self_reference():
    """Test that ImmutableList can be constructed with False values,
    converted to string, and used as an argument to find() on itself."""
    # Create an ImmutableList with is_empty=False and a falsy initial value
    is_empty_false = False
    empty_list = immutable_list.ImmutableList(is_empty_false, is_empty=is_empty_false)

    # Verify string representation can be obtained without error
    str_repr = empty_list.__str__()

    # Verify find() can be called with the list itself as the search target
    empty_list.find(empty_list)

def test_immutable_list_unshift_reduce_and_equality_operations():
    """
    Test a sequence of ImmutableList operations: creating empty lists,
    prepending elements via unshift, reducing with another list as the
    accumulator/function, checking length, equality comparison, and
    constructing a list with an explicit is_empty flag. Verifies that
    find can be called on the result of reduce without raising.
    """
    # Create an empty ImmutableList as the base
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list into itself, producing a new list
    list_with_self = empty_list.unshift(empty_list)

    # Reduce the new list using list_with_self as both accumulator and function
    reduced_result = empty_list.reduce(list_with_self, list_with_self)

    # Get the length of the unshifted list
    length = list_with_self.__len__()

    # Prepend list_with_self into itself to produce a deeper nested list
    nested_list = list_with_self.unshift(list_with_self)

    # Check equality between the nested list and the original empty list
    are_equal = nested_list.__eq__(empty_list)

    # Construct a new ImmutableList using the computed length as is_empty flag
    list_with_is_empty_flag = immutable_list.ImmutableList(is_empty=length)

    # Call find on the reduced result using itself as the predicate/value
    reduced_result.find(reduced_result)

def test_immutable_list_unshift_reduce_and_equality_operations():
    """
    Test a sequence of ImmutableList operations: creating empty lists,
    prepending elements via unshift, reducing with a list as the initial
    accumulator, checking length, and verifying equality between instances.
    Also exercises constructing an ImmutableList with an explicit is_empty flag
    and calling find on the result of reduce.
    """
    # Create an empty ImmutableList as the base
    empty_list = immutable_list.ImmutableList()

    # Prepend the empty list to itself, producing a new ImmutableList
    list_with_self = empty_list.unshift(empty_list)

    # Reduce the original empty list using list_with_self as both
    # the initial accumulator and the combining function
    reduced = empty_list.reduce(list_with_self, list_with_self)

    # Get the length of the unshifted list (used later as is_empty flag)
    length = list_with_self.__len__()

    # Prepend list_with_self to itself, producing a deeper nested list
    nested_list = list_with_self.unshift(list_with_self)

    # Check equality between the nested list and the original empty list
    are_equal = nested_list.__eq__(empty_list)

    # Construct a new ImmutableList using the computed length as the is_empty flag
    list_from_length = immutable_list.ImmutableList(is_empty=length)

    # Attempt to find the reduced value within itself
    reduced.find(reduced)

def test_immutable_list_reduce_with_converted_list():
    """
    Test that ImmutableList.to_list() result can be passed to reduce()
    on a non-empty ImmutableList constructed with is_empty=True.
    Also verifies that ImmutableList can be constructed with an empty dict as tail.
    """
    is_empty_flag = True
    empty_tail = {}

    # Create an ImmutableList with an empty dict as the tail argument
    immutable_list_with_dict_tail = immutable_list.ImmutableList(tail=empty_tail)

    # Create a non-empty ImmutableList using is_empty flag set to True
    immutable_list_non_empty = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the list to a plain Python list
    converted_list = immutable_list_non_empty.to_list()

    # Reduce using the converted list as both the iterable and the initial value
    immutable_list_non_empty.reduce(converted_list, converted_list)

def test_immutable_list_reduce_with_converted_list():
    """
    Test that ImmutableList.to_list() and reduce() can be called on a non-empty
    ImmutableList constructed with is_empty=True, using the converted list as
    both arguments to reduce.
    """
    is_empty_flag = True
    empty_tail = {}

    # Create an ImmutableList with an empty dict as tail (no head)
    immutable_list_with_tail = immutable_list.ImmutableList(tail=empty_tail)

    # Create a non-empty ImmutableList marked explicitly as empty
    immutable_list_marked_empty = immutable_list.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the list to a plain Python list
    converted_list = immutable_list_marked_empty.to_list()

    # Reduce using the converted list as both the initial value and the iterable
    immutable_list_marked_empty.reduce(converted_list, converted_list)

