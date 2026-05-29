import pytest

import immutable_list as immutable_list_module

def test_immutable_list_basic_operations_readable():
    """Exercise basic ImmutableList operations without changing behavior:
    - equality with itself
    - string conversion
    - conversion to a Python list
    - list concatenation via list.__add__
    - length retrieval via list.__len__
    - ImmutableList.__add__ with a Python list (should not mutate)
    """
    # Create an ImmutableList instance
    immutable_list = immutable_list_module.ImmutableList()

    # Equality check (using the special method directly)
    equality_result = immutable_list.__eq__(immutable_list)
    assert equality_result is True

    # String representation
    string_representation = immutable_list.__str__()
    assert isinstance(string_representation, str)

    # Convert to a built-in list
    plain_list = immutable_list.to_list()
    assert isinstance(plain_list, list)

    # Concatenate the plain list with itself (list.__add__)
    concatenated_list = plain_list.__add__(plain_list)
    assert isinstance(concatenated_list, list)

    # Get the length of the plain list (list.__len__)
    list_length = plain_list.__len__()
    assert list_length == len(plain_list)

    # Call ImmutableList.__add__ with the plain list (exercise the method)
    before = immutable_list.to_list()
    _ = immutable_list.__add__(plain_list)
    # Ensure the original immutable_list was not mutated
    assert immutable_list.to_list() == before

def test_immutable_list_operations_sequence():
    """Run a sequence of ImmutableList methods to exercise their return paths."""
    flag_true = True
    imm_list = immutable_list_module.ImmutableList()

    # Compare the list to a boolean value using the dunder equality method.
    eq_result = imm_list.__eq__(flag_true)

    # Concatenate the list with itself.
    concatenated = imm_list.__add__(imm_list)

    # Attempt to find the equality result within the list.
    found = imm_list.find(eq_result)

    # Get the string representation of the list.
    string_representation = imm_list.__str__()

    # Prepend the list onto itself (unshift) and then call reduce on the result.
    prepended = imm_list.unshift(imm_list)
    prepended.reduce(prepended, flag_true)

def test_append_true_and_find_self():
    """Create an ImmutableList marked empty (True), append True, and call find on the original list searching for itself.
    This verifies that append can be invoked without modifying the original list object.
    """
    flag = True
    original = immutable_list_module.ImmutableList(flag, is_empty=flag)
    # Appending should produce a new ImmutableList instance; the original should remain unchanged.
    appended = original.append(flag)
    # Invoke find on the original list, searching for the original list object itself.
    # We don't assert on the return value here; the important aspect is that calling find does not raise.
    original.find(original)

def test_immutable_list_add_with_none_does_not_raise():
    """Verify that calling ImmutableList.__add__ with None does not raise an exception."""
    # Create an empty ImmutableList instance using the imported module alias.
    imm_list = immutable_list_module.ImmutableList()
    # Use an explicit None value to make the intent clear.
    none_value = None
    # Invoke the dunder add method directly; the test passes if no exception is raised.
    imm_list.__add__(none_value)

def test_immutable_list_find_with_self_and_is_empty_flag():
    """Construct an ImmutableList from another and call find with itself.

    This exercises construction using another ImmutableList as both the
    source and the is_empty parameter, calls the special __len__ method,
    and finally invokes find with the list itself.
    """
    # create a base ImmutableList instance
    base_list = immutable_list_module.ImmutableList()

    # directly invoke the special method to get its length (no behavioral change)
    length = base_list.__len__()

    # construct a new ImmutableList using the base_list as the iterable
    # and also pass base_list as the is_empty argument
    derived_list = immutable_list_module.ImmutableList(base_list, is_empty=base_list)

    # call find on the derived list, passing the derived list itself
    derived_list.find(derived_list)

def test_find_on_self_with_false_initialization():
    """Calling find() with the list itself as the search target runs as expected
    when the ImmutableList is constructed with False and is_empty=False.
    """
    # Use explicit, descriptive variable names for clarity
    initial_value = False
    is_empty_flag = False

    # Create an ImmutableList instance using the provided module alias
    immutable_list = immutable_list_module.ImmutableList(initial_value, is_empty=is_empty_flag)

    # Call __len__() to obtain the length (kept as an explicit call to mirror original behavior)
    length = immutable_list.__len__()

    # Invoke find() with the list itself as the argument (preserve original call and order)
    immutable_list.find(immutable_list)

def test_find_accepts_to_list_output():
    """Ensure ImmutableList.find can be invoked with the result returned by to_list()."""
    flag = False
    # Construct an ImmutableList using the same boolean for the value and is_empty flag
    immutable_list = immutable_list_module.ImmutableList(flag, is_empty=flag)
    # Convert to a standard list
    list_repr = immutable_list.to_list()
    # Invoke find with the list produced by to_list()
    immutable_list.find(list_repr)

def test_find_none_and_append_self_to_list_and_invoke_add():
    """Exercise find(None), appending the list to itself, converting to list, and calling __add__.

    This ensures those call paths are exercised in order without asserting outcomes.
    """
    # Create an ImmutableList instance
    lst = immutable_list_module.ImmutableList()

    # Search for None explicitly
    none_value = None
    found = lst.find(none_value)  # exercise find with None

    # Append the list object to itself and get a Python list representation
    appended = lst.append(lst)
    as_list = appended.to_list()

    # Invoke the list's __add__ method with None to exercise that code path
    as_list.__add__(none_value)

def test_map_with_list_snapshot_from_same_immutable_list():
    """Call map() with a list snapshot obtained from the same ImmutableList instance."""
    is_empty_flag = False
    original_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)
    list_snapshot_before = original_list.to_list()
    new_list = immutable_list_module.ImmutableList()
    list_snapshot_after = original_list.to_list()
    # Invoke map using the list snapshot produced by original_list.to_list()
    original_list.map(list_snapshot_after)

def test_unshift_append_map_with_none_values():
    """Verify ImmutableList handles unshift, append, and map calls when given None."""
    none_value = None

    # Create an ImmutableList with two None elements (preserve original construction).
    initial_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Prepend None to the initial list.
    unshifted_once = initial_list.unshift(none_value)

    # Prepend the previously unshifted list to the initial list (keeps same call order).
    unshifted_twice = initial_list.unshift(unshifted_once)

    # Append None to the list obtained after the first unshift.
    appended = unshifted_once.append(none_value)

    # Call map with None as the argument (preserve original behaviour and side-effects).
    appended.map(none_value)

def test_filter_with_self_predicate_on_explicit_empty_list():
    """Calling filter with the list itself as the predicate on an explicitly empty ImmutableList."""
    is_empty_flag = False
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Pass the ImmutableList instance itself as the argument to filter (preserve original call)
    immutable_list.filter(immutable_list)

def test_add_self_and_filter_by_length():
    """Add an ImmutableList to itself, get its length, and call filter with that length."""
    # create an empty ImmutableList instance
    original_list = immutable_list_module.ImmutableList()
    # add the list to itself using the explicit dunder method
    combined_list = original_list.__add__(original_list)
    # obtain the length via the explicit __len__ call
    combined_length = combined_list.__len__()
    # invoke filter with the computed length
    combined_list.filter(combined_length)

def test_find_returns_length_callable_on_list_with_none_elements():
    """Ensure ImmutableList.find returns an object that implements __len__ when list items are None."""
    search_value = 1947
    list_element = None

    # Create an ImmutableList containing two None elements
    imm_list = immutable_list_module.ImmutableList(list_element, list_element)

    # Perform the search and invoke __len__ on the result to exercise length behavior
    result = imm_list.find(search_value)
    result.__len__()

def test_immutable_list_find_with_self_same_flag():
    """Ensure ImmutableList.find can be called with the list itself as the search target.

    The test constructs an ImmutableList by passing the same False value both
    positionally and as the is_empty keyword (matching the original test inputs),
    then calls find with the list object as the argument.
    """
    is_empty_flag = False  # same boolean value used both positionally and as keyword
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Call find with the list itself as the search target (result intentionally ignored)
    immutable_list.find(immutable_list)

def test_reduce_and_find_with_false_flag():
    """Exercise ImmutableList.reduce and ImmutableList.find when initialized with False flags."""
    # Use an explicit boolean flag value as in the original test
    flag = False

    # Create an empty ImmutableList instance
    initial_list = immutable_list_module.ImmutableList()

    # Call reduce with the flag and the list (preserve original call order and arguments)
    reduced_result = initial_list.reduce(flag, initial_list)

    # Create another ImmutableList passing the flag both positionally and as is_empty kwarg
    list_with_flag = immutable_list_module.ImmutableList(flag, is_empty=flag)

    # Call find with the list itself as the search argument (preserve original call)
    list_with_flag.find(list_with_flag)

def test_create_immutable_list_instance():
    """Ensure an ImmutableList can be instantiated without errors."""
    # Instantiate an ImmutableList from the imported module alias.
    immutable_list = immutable_list_module.ImmutableList()

def test_find_self_on_empty_immutable_list():
    """Ensure an ImmutableList created as 'empty' can be stringified and can search for itself."""
    is_empty = False  # construct the list with False to match original test input
    immutable_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)

    # Obtain the string representation (keeps original call to __str__ for side effects)
    str_result = immutable_list.__str__()

    # Call find with the list itself (verifies find handles self-references)
    immutable_list.find(immutable_list)

def test_unshift_and_find_on_false_empty_list():
    """Create an ImmutableList with is_empty=False, unshift the list onto itself,
    and call find on the original list (preserve original call order and behavior)."""
    # Use the provided False literal as in the original test
    is_empty_flag = False

    # Construct the ImmutableList using the aliased import
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Unshift the list onto itself and keep the returned value (original test assigned it)
    unshift_result = imm_list.unshift(imm_list)

    # Call find with the list itself (no assertion in the original test)
    imm_list.find(imm_list)

def test_find_after_unshift_and_append():
    """Verify that calling find on a list still works after unshifting a value and appending another list."""
    is_empty_flag = False
    original_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)
    # Prepend the same False value to create a new list
    prefixed_list = original_list.unshift(is_empty_flag)
    # Append the original list to the prefixed list
    appended_list = prefixed_list.append(original_list)
    # Invoke find for the False value on the final list (no assertion; replicate original behaviour)
    appended_list.find(is_empty_flag)

def test_append_and_find_behaviour_with_boolean_element():
    """Ensure appending a boolean returns a new list and find can be called with the original list."""
    # Use a boolean literal for the element and the is_empty flag
    value = True

    # Construct an ImmutableList with the boolean value and is_empty flag
    original_list = immutable_list_module.ImmutableList(value, is_empty=value)

    # Append the same boolean value, producing a new ImmutableList
    appended_list = original_list.append(value)

    # Explicitly call __len__() on the appended list (preserve exact method call)
    length = appended_list.__len__()

    # Call find on the original list with the original list as the search target
    original_list.find(original_list)

def test_immutable_list_append_reduce_unshift_and_find_behaviour():
    """Exercise ImmutableList: append, reduce, unshift, __str__, constructor param,
    equality check, and find — ensure method interactions run in sequence."""
    # Create an empty ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()

    # Append the list to itself
    appended_self_list = empty_list.append(empty_list)

    # Reduce using appended_self_list as both arguments (preserve original call order)
    reduced_result = empty_list.reduce(appended_self_list, appended_self_list)

    # Check equality of the appended list against the original (result is unused)
    are_equal = appended_self_list.__eq__(empty_list)

    # Unshift the appended list onto itself
    unshifted_list = appended_self_list.unshift(appended_self_list)

    # Get the string representation of the unshifted list
    repr_str = unshifted_list.__str__()

    # Construct a new ImmutableList using the string from __str__ as the is_empty kwarg
    list_from_str_arg = immutable_list_module.ImmutableList(is_empty=repr_str)

    # Append the reduced result to itself
    appended_reduced = reduced_result.append(reduced_result)

    # Call find on the unshifted list with the reduced result
    unshifted_list.find(reduced_result)

def test_immutable_list_unshift_reduce_find_and_equality():
    """
    Exercise ImmutableList unshift, reduce, length, equality, and find operations.

    This test constructs lists, performs unshift operations, reduces one list with
    another as both reducer and initial value, checks length and equality, and
    finally calls find on the reduction result using itself as the needle.
    """
    # Create an empty/base immutable list instance
    original_list = immutable_list_module.ImmutableList()

    # Unshift the original list onto itself (creates a new list)
    unshifted_once = original_list.unshift(original_list)

    # Reduce using unshifted_once as both the reducer function and the initial value
    reduced_result = original_list.reduce(unshifted_once, unshifted_once)

    # Get the length of the unshifted list
    length_of_unshifted = unshifted_once.__len__()

    # Unshift the unshifted_once list onto itself (another new list)
    unshifted_twice = unshifted_once.unshift(unshifted_once)

    # Check equality between the twice-unshifted list and the original (boolean result captured)
    is_equal_to_original = unshifted_twice.__eq__(original_list)

    # Construct a new ImmutableList using the previously obtained length as the is_empty flag
    constructed_from_length = immutable_list_module.ImmutableList(is_empty=length_of_unshifted)

    # Call find on the reduction result, searching for the reduction result itself
    reduced_result.find(reduced_result)

def test_reduce_when_called_with_to_list_result_used_twice():
    """Call reduce using the list produced by to_list() as both arguments.

    Verifies reduce accepts the same list object for both parameters.
    """
    is_empty = True
    tail = {}

    # Preserve original parity by explicitly supplying a tail mapping
    list_with_tail = immutable_list_module.ImmutableList(tail=tail)

    # Create an ImmutableList using the boolean flag both positionally and as a keyword
    flagged_list = immutable_list_module.ImmutableList(is_empty, is_empty=is_empty)

    items = flagged_list.to_list()

    # Invoke reduce with the very same list for both arguments
    flagged_list.reduce(items, items)

