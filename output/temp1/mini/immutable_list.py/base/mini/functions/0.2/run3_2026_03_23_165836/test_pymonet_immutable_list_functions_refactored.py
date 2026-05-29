import pytest

import immutable_list as immutable_list_module

def test_immutable_list_basic_operations_readable():
    """Exercise basic ImmutableList methods to ensure they execute without error and return expected types."""
    # create an ImmutableList instance
    imm_list = immutable_list_module.ImmutableList()

    # equality check against itself
    assert imm_list == imm_list

    # string representation
    string_repr = imm_list.__str__()
    assert isinstance(string_repr, str)

    # convert to a plain list
    plain_list = imm_list.to_list()
    assert isinstance(plain_list, list)

    # list concatenation via __add__ on the plain list
    concatenated = plain_list.__add__(plain_list)
    assert concatenated == plain_list + plain_list

    # length retrieval via __len__ on the plain list
    length = plain_list.__len__()
    assert length == len(plain_list)

    # attempt to add the plain list to the ImmutableList (calls ImmutableList.__add__)
    added_result = imm_list.__add__(plain_list)
    # ensure the operation completed (at minimum it should not be None)
    assert added_result is not None

def test_immutable_list_sequence_operations_preserve_semantics():
    """Exercise several ImmutableList methods in sequence to verify call semantics."""
    # simple literal argument used across calls
    flag = True

    # create an empty ImmutableList instance
    lst = immutable_list_module.ImmutableList()

    # compare the list to a boolean using the dunder equality method
    eq_result = lst.__eq__(flag)

    # add the list to itself using the dunder add method
    add_result = lst.__add__(lst)

    # search for the previously computed equality result in the list
    find_result = lst.find(eq_result)

    # obtain the string representation of the list
    str_repr = lst.__str__()

    # unshift (prepend) the list onto itself
    unshifted = lst.unshift(lst)

    # reduce the unshifted list with itself and the boolean flag
    reduced = unshifted.reduce(unshifted, flag)

def test_find_self_on_empty_immutable_list():
    """Ensure calling find with the list object itself works on an (reported) empty ImmutableList."""
    is_empty_flag = True
    # Create an ImmutableList that is reported as empty via the is_empty keyword.
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Append returns a new ImmutableList instance; keep it to match original interactions.
    appended_list = immutable_list.append(is_empty_flag)
    # Invoke find with the original list instance as the search target.
    immutable_list.find(immutable_list)

def test_immutable_list_add_with_none():
    """Call ImmutableList.__add__ with None to exercise this edge-case invocation."""
    imm_list = immutable_list_module.ImmutableList()
    none_value = None
    # Invoke the special-method directly with None (preserve original call semantics)
    imm_list.__add__(none_value)

def test_construct_from_existing_and_find_self():
    """Construct an ImmutableList from an existing one and call find() on the new list with itself."""
    original_list = immutable_list_module.ImmutableList()
    # Preserve original behavior by explicitly calling the dunder length method.
    original_length = original_list.__len__()
    # Create a new ImmutableList using the original as both a positional and keyword argument.
    new_list = immutable_list_module.ImmutableList(original_list, is_empty=original_list)
    # Attempt to find the new list inside itself (preserves original call sequence).
    new_list.find(new_list)

def test_find_self_when_list_is_empty():
    """Exercise finding the list object within itself when the list is empty."""
    is_empty_flag = False  # create a non-populated/empty ImmutableList
    im_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    length = im_list.__len__()  # call __len__ explicitly to exercise that code path
    assert length == 0
    im_list.find(im_list)  # attempt to find the list object inside itself

def test_find_accepts_list_produced_by_to_list_for_non_empty_immutable_list():
    """Ensure calling find() with the list returned by to_list() does not raise for a non-empty ImmutableList."""
    # Use an explicit boolean flag for clarity
    is_empty_flag = False

    # Create an ImmutableList with the flag passed both positionally and as the is_empty keyword
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the immutable list to a regular list
    regular_list = immutable_list.to_list()

    # Call find() with the list produced by to_list(); test passes if no exception is raised
    immutable_list.find(regular_list)

def test_find_none_append_self_and_list_add_with_none():
    """
    Verify behavior when searching for None, appending the list to itself,
    and invoking list.__add__ with None (preserving original execution).
    """
    # construct an ImmutableList instance
    immutable_list = immutable_list_module.ImmutableList()

    # look up None in the immutable list
    search_value = None
    find_result = immutable_list.find(search_value)

    # append the immutable list to itself (returns a new ImmutableList)
    appended_list = immutable_list.append(immutable_list)

    # convert to a built-in Python list
    as_python_list = appended_list.to_list()

    # call list.__add__ with None (keeps the original call and order)
    as_python_list.__add__(search_value)

def test_immutable_list_map_receives_to_list_output():
    """Ensure ImmutableList.map can be called with the result of to_list().

    This test constructs an ImmutableList with the `is_empty` flag set to False,
    calls to_list() twice (to mimic repeated reads), creates a second empty
    ImmutableList instance, and finally calls map() on the first list using
    the second to_list() result. The test verifies that these operations run
    without raising exceptions.
    """
    # Explicitly set the is_empty flag to False (preserve original input value)
    is_empty_flag = False

    # Create the first ImmutableList with is_empty=False
    list_a = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # Call to_list() and store the result (first read)
    to_list_result_1 = list_a.to_list()

    # Create a second ImmutableList using default constructor
    list_b = immutable_list_module.ImmutableList()

    # Call to_list() on the first list again (second read)
    to_list_result_2 = list_a.to_list()

    # Call map() on the first list with the second to_list() result
    list_a.map(to_list_result_2)

def test_immutablelist_unshift_append_map_with_none():
    """Verify ImmutableList handles unshift, append, and map operations when given None."""
    none_value = None

    # Construct an ImmutableList with two None elements
    base_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    unshifted_once = base_list.unshift(none_value)

    # Prepend the previously created list onto the base list
    unshifted_with_list = base_list.unshift(unshifted_once)

    # Append None to the list produced by the first unshift
    appended = unshifted_once.append(none_value)

    # Invoke map with None (preserve original behaviour)
    appended.map(none_value)

def test_filter_invoked_with_self_on_empty_list():
    """Call filter with the list itself on an empty ImmutableList (should run without error)."""
    is_empty_flag = False
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Invoke filter using the same instance as the argument to exercise that code path.
    immutable_list.filter(immutable_list)

def test_immutable_list_add_self_then_filter_by_length():
    """Ensure an ImmutableList can be added to itself and then filtered using its length.

    This reproduces the original call sequence:
    - create an ImmutableList instance
    - add it to itself via __add__
    - obtain the length via __len__
    - call filter with that length value
    """
    # Create a new immutable list instance
    imm_list = immutable_list_module.ImmutableList()

    # Add the list to itself (calls __add__)
    combined_list = imm_list.__add__(imm_list)

    # Get the length of the combined list (calls __len__)
    length_value = combined_list.__len__()

    # Filter the combined list using the computed length (calls filter)
    combined_list.filter(length_value)

def test_find_returns_object_with_len_for_list_initialized_with_none():
    """Calling find(...) on an ImmutableList constructed with None values
    should return an object that supports __len__().
    """
    search_value = 1947
    none_value = None

    # ImmutableList initialized with two None elements.
    imm_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Perform lookup for the given integer value.
    result = imm_list.find(search_value)

    # Preserve original behaviour: directly call the __len__ special method.
    result.__len__()

def test_find_self_in_empty_immutable_list():
    """Verify that calling find() with the list itself on an empty ImmutableList executes."""
    is_empty_flag = False  # represent an empty list via the constructor flag
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Call find() searching for the list object itself (no assertion; just ensure call behaves)
    imm_list.find(imm_list)

def test_reduce_and_find_with_false_is_empty_flag():
    """Reduce an ImmutableList with False and then call find on a list created with is_empty=False."""
    is_false = False

    # Create an empty ImmutableList instance.
    empty_list = immutable_list_module.ImmutableList()

    # Reduce the empty list using False as the accumulator and the list itself as the iterable.
    reduced = empty_list.reduce(is_false, empty_list)

    # Create another ImmutableList with the value False and is_empty explicitly set to False.
    list_with_false = immutable_list_module.ImmutableList(is_false, is_empty=is_false)

    # Call find on the newly created list, searching for itself (preserves original call sequence).
    list_with_false.find(list_with_false)

def test_creates_immutable_list_instance():
    """Ensure ImmutableList can be instantiated without raising an exception."""
    # Instantiate using the module alias defined in the test imports.
    immutable_list = immutable_list_module.ImmutableList()

def test_find_self_on_non_dynamic_immutable_list():
    """Verify that creating an ImmutableList and calling __str__ and find(self) runs without error."""
    is_dynamic_flag = False  # use False for both the value and the is_empty keyword as in the original test
    immutable_list = immutable_list_module.ImmutableList(is_dynamic_flag, is_empty=is_dynamic_flag)

    # Exercise __str__ to get a string representation
    _ = str(immutable_list)

    # Call find with the list itself (used for side-effects in the original test); no exception expected
    immutable_list.find(immutable_list)

def test_immutable_list_unshift_and_find_self_reference():
    """Verify that an ImmutableList can be unshifted with itself and can attempt to find itself."""
    # Use a False flag for both the value and the is_empty parameter (matches original inputs)
    is_empty_flag = False
    lst = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Unshift the list onto itself and keep the returned value (behaviour preserved)
    unshift_result = lst.unshift(lst)

    # Try to find the list within itself (call is preserved; no assertion in original test)
    lst.find(lst)

def test_find_call_after_unshift_and_append():
    """Ensure that find can be called after unshift and append operations without error."""
    # Use a concrete boolean value used in the original test
    value = False

    # Create an ImmutableList instance (was module_0.ImmutableList in the generated test)
    original_list = immutable_list_module.ImmutableList(is_empty=value)

    # Prepend the same boolean value to produce a new list
    after_unshift = original_list.unshift(value)

    # Append the original list to the new list
    after_append = after_unshift.append(original_list)

    # Call find with the boolean value (no assertion in original test; just exercise the call)
    after_append.find(value)

def test_immutable_list_append_and_find_self():
    """Verify append returns a new list and find can search for the original list object."""
    # Use a simple boolean value for the list contents and the is_empty flag.
    flag = True

    # Create the original immutable list instance.
    original_list = immutable_list_module.ImmutableList(flag, is_empty=flag)

    # Append the same value to produce a new immutable list (should not mutate original).
    appended_list = original_list.append(flag)

    # Ensure append returned a different object (immutability).
    assert appended_list is not original_list

    # Obtain the length of the appended list by calling its __len__ method directly.
    appended_length = appended_list.__len__()

    # Basic sanity check on length (should be an integer >= 0).
    assert isinstance(appended_length, int) and appended_length >= 0

    # Attempt to find the original list object within the original list (exercise find call).
    original_list.find(original_list)

def test_immutable_list_chain_of_operations():
    """Exercise a sequence of ImmutableList operations to ensure consistent behavior when chaining methods."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()

    # Append the list to itself (returns a new ImmutableList)
    appended_self = empty_list.append(empty_list)

    # Reduce using the appended list as both reducer and initial value
    reduced_result = empty_list.reduce(appended_self, appended_self)

    # Check equality of the appended list against the original (keeps the call/side-effect)
    is_equal_to_empty = appended_self.__eq__(empty_list)

    # Unshift (prepend) the appended list onto itself
    unshifted = appended_self.unshift(appended_self)

    # Obtain the string representation (used below when constructing a new instance)
    string_repr = unshifted.__str__()

    # Construct a new ImmutableList using the string representation for the is_empty parameter
    constructed_with_is_empty = immutable_list_module.ImmutableList(is_empty=string_repr)

    # Append the reduced result to itself
    appended_reduced = reduced_result.append(reduced_result)

    # Find the reduced result within the unshifted list (keeps the call/side-effect)
    unshifted.find(reduced_result)

def test_immutablelist_unshift_reduce_length_equality_and_find():
    """Exercise ImmutableList unshift, reduce, length, equality and find interactions."""
    # start with an empty ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()

    # unshift the empty list onto itself (creates a new list)
    list_after_unshift = empty_list.unshift(empty_list)

    # reduce using the original empty_list as both reducer and initial value
    reduce_result = empty_list.reduce(list_after_unshift, list_after_unshift)

    # get the length of the list produced by the first unshift
    length_of_unshifted = list_after_unshift.__len__()

    # unshift the list onto itself again
    list_twice_unshifted = list_after_unshift.unshift(list_after_unshift)

    # check equality between the twice-unshifted list and the original empty list
    equality_result = list_twice_unshifted.__eq__(empty_list)

    # create a new ImmutableList using the observed length as the is_empty parameter
    constructed_with_length = immutable_list_module.ImmutableList(is_empty=length_of_unshifted)

    # call find on the reduce result, passing itself (preserve original call behavior)
    reduce_result.find(reduce_result)

def test_reduce_with_to_list_and_is_empty_flag():
    """Ensure reduce can be called using the list produced by to_list() when the list is marked empty."""
    # Use a simple boolean flag set to True (matches original test input)
    is_empty_flag = True

    # An empty mapping used as the 'tail' keyword argument in the first ImmutableList
    tail_mapping = {}

    # Create an ImmutableList using the tail mapping (keyword argument)
    list_from_tail = immutable_list_module.ImmutableList(tail=tail_mapping)

    # Create another ImmutableList using the boolean as positional and also as the is_empty keyword
    list_marked_empty = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the second list to a plain Python list (used as both accumulator and initial value)
    py_list = list_marked_empty.to_list()

    # Call reduce with the same list object as both parameters (preserves original call sequence)
    list_marked_empty.reduce(py_list, py_list)

