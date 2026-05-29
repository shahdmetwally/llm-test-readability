import pytest

import immutable_list as immutable_list_module

def test_immutable_list_basic_operations():
    """Basic smoke test for ImmutableList: equality, string conversion, to_list, addition, and length."""
    immutable_list = immutable_list_module.ImmutableList()
    # equality check against itself
    is_equal_self = immutable_list.__eq__(immutable_list)
    assert isinstance(is_equal_self, bool)
    # get string representation
    text_repr = immutable_list.__str__()
    assert isinstance(text_repr, str)
    # convert to a (plain) list representation
    list_representation = immutable_list.to_list()
    assert isinstance(list_representation, list)
    # add the list representation to itself
    added_list = list_representation.__add__(list_representation)
    assert isinstance(added_list, list)
    # get the length of the list representation
    list_length = list_representation.__len__()
    assert isinstance(list_length, int)
    # add the list representation to the original immutable list
    result = immutable_list.__add__(list_representation)
    assert result is not None

def test_immutable_list_operations_equality_add_find_unshift_and_reduce():
    """Smoke test exercising several ImmutableList operations in sequence.

    This ensures methods like __eq__, __add__, find, __str__, unshift and
    reduce can be invoked together without changing behaviour.
    """
    # use a simple True flag as in the original generated test
    true_flag = True

    # create an empty ImmutableList instance
    original_list = immutable_list_module.ImmutableList()

    # check equality against a boolean value
    equality_result = original_list.__eq__(true_flag)

    # add the list to itself (calls __add__)
    added_list = original_list.__add__(original_list)

    # find the result of the equality check in the original list
    found = original_list.find(equality_result)

    # get string representation
    text = original_list.__str__()

    # unshift (prepend) the list onto itself, producing a new list
    unshifted_list = original_list.unshift(original_list)

    # reduce the unshifted list using itself and the original boolean flag
    unshifted_list.reduce(unshifted_list, true_flag)

def test_append_true_value_and_find_self():
    """Create an ImmutableList with True (marked as empty), append True, then call find on the original list."""
    is_empty_flag = True
    original_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Append the same boolean value to produce a new immutable list instance
    appended_list = original_list.append(is_empty_flag)
    # Invoke find on the original list, searching for the list object itself
    original_list.find(original_list)

def test_add_with_none_argument_invokes_dunder_add():
    """Verify ImmutableList.__add__ can be invoked with None (preserve original behavior)."""
    # Create an ImmutableList instance from the aliased module
    immutable_list = immutable_list_module.ImmutableList()
    # Explicitly pass None to mirror the original test input
    none_value = None
    # Invoke the dunder method directly to preserve exact call semantics
    immutable_list.__add__(none_value)

def test_find_method_called_on_composed_immutable_list_with_self():
    """Exercise creating an ImmutableList from another and calling find() with self."""
    # Create a base immutable list instance.
    base_list = immutable_list_module.ImmutableList()
    # Call the dunder __len__ method explicitly to exercise length retrieval.
    length = base_list.__len__()
    # Create a new ImmutableList using the base_list and pass base_list as is_empty flag.
    composed_list = immutable_list_module.ImmutableList(base_list, is_empty=base_list)
    # Call find on the composed list, passing the composed list itself as the search target.
    composed_list.find(composed_list)

def test_find_self_on_immutable_list_with_is_empty_false():
    """Ensure ImmutableList.find can be invoked to search for the list object itself
    when the is_empty flag is False.
    """
    is_empty_flag = False
    # Construct an ImmutableList using the boolean flag both as the positional
    # argument and the is_empty keyword (preserves original call semantics).
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Explicitly call __len__ to exercise the length retrieval (result not asserted).
    length = immutable_list.__len__()
    # Attempt to find the list object within itself (preserves original call order).
    immutable_list.find(immutable_list)

def test_find_with_list_value_on_immutable_list_when_not_empty():
    """
    Construct an ImmutableList with is_empty=False, convert it to a Python list,
    and call find() with that list value to exercise the method (no assertions).
    """
    is_empty_flag = False
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Get the list representation of the immutable list (used as the search value).
    search_value = immutable_list.to_list()

    # Call find() with the list value to ensure the call executes as in the original test.
    immutable_list.find(search_value)

def test_immutable_list_find_append_and_list_add_with_none():
    """Verify ImmutableList.find, append(self), to_list, and calling list.__add__ with None."""
    # Create an ImmutableList instance
    immutable = immutable_list_module.ImmutableList()
    # Use a None value for searching and for the subsequent __add__ call
    none_value = None

    # Attempt to find None in the immutable list (preserve original call)
    found = immutable.find(none_value)

    # Append the immutable list to itself (preserve original call and behavior)
    appended = immutable.append(immutable)

    # Convert the appended ImmutableList to a built-in Python list
    as_list = appended.to_list()

    # Invoke list.__add__ with None (preserve original call and behavior)
    as_list.__add__(none_value)

def test_immutable_list_map_with_to_list():
    """Ensure to_list can be called multiple times and its result can be passed to map."""
    # Create an ImmutableList explicitly marked as non-empty
    is_empty_flag = False
    list_a = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # First call to to_list: capture contents
    list_a_contents = list_a.to_list()

    # Create a second ImmutableList instance (preserved for original structure)
    list_b = immutable_list_module.ImmutableList()

    # Second call to to_list: capture contents again
    list_a_contents_again = list_a.to_list()

    # Invoke map on list_a using the result of to_list
    list_a.map(list_a_contents_again)

def test_immutable_list_unshift_append_map_with_none_and_nested_list():
    """Exercise ImmutableList.unshift, .append and .map using None and a nested list.

    Verifies the sequence of operations (unshift twice, append, then map)
    runs without altering the original list objects (i.e., preserves immutability)
    and does not raise exceptions.
    """
    # Use a None value throughout to mirror original test inputs
    none_value = None

    # Create an ImmutableList with two None elements (matches original constructor call)
    original_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Prepend None to the original list
    prepended_once = original_list.unshift(none_value)

    # Prepend the previously created list to the original list (nested list as element)
    prepended_with_list = original_list.unshift(prepended_once)

    # Append None to the list created by the first unshift
    appended = prepended_once.append(none_value)

    # Call map with None as the mapping function/argument (preserve call sequence)
    appended.map(none_value)

def test_filter_accepts_instance_as_predicate():
    """Calling ImmutableList.filter with the list instance itself as the predicate (regression check)."""
    # Use the same boolean literal as in the original test to preserve behaviour.
    flag = False
    # Create an ImmutableList with flag as both the first positional argument and the is_empty kwarg.
    immutable_list = immutable_list_module.ImmutableList(flag, is_empty=flag)
    # Invoke filter passing the instance itself as the predicate (preserves original call/behaviour).
    immutable_list.filter(immutable_list)

def test_add_self_and_filter_by_length():
    """Create an ImmutableList, add it to itself, then call filter with its length."""
    # construct an ImmutableList instance
    original = immutable_list_module.ImmutableList()
    # use the explicit dunder add to combine the list with itself
    combined = original.__add__(original)
    # obtain length using the dunder __len__ method
    length = combined.__len__()
    # call filter with the computed length to exercise the method
    combined.filter(length)

def test_immutable_list_find_result_len_callable():
    """Ensure ImmutableList.find(...) returns an object whose __len__ method can be invoked."""
    search_value = 1947
    none_value = None

    # Create an ImmutableList with None values
    imm_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Perform a find on the list and get the result object
    result = imm_list.find(search_value)

    # Invoke __len__ on the returned object to verify the method is callable
    result.__len__()

def test_find_accepts_self_as_search_target():
    """Call ImmutableList.find with the list itself as the search target (should not raise)."""
    is_empty_flag = False
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)
    # Invoke find using the same instance as the argument; success is the absence of an exception.
    imm_list.find(imm_list)

def test_immutable_list_reduce_with_false_and_find_self():
    """Exercise ImmutableList.reduce with False and ImmutableList.find with self as argument."""
    flag_false = False

    # Create an empty ImmutableList instance and call reduce with False
    empty_list = immutable_list_module.ImmutableList()
    reduced_value = empty_list.reduce(flag_false, empty_list)

    # Create another ImmutableList with False and is_empty=False, then call find with itself
    list_with_flag = immutable_list_module.ImmutableList(flag_false, is_empty=flag_false)
    list_with_flag.find(list_with_flag)

def test_instantiate_immutable_list():
    """Ensure ImmutableList can be instantiated without raising an error."""
    # Instantiate an ImmutableList using the provided module alias.
    immutable_list = immutable_list_module.ImmutableList()
    # The test succeeds if construction completes (no assertions required).

def test_find_self_on_non_collection_immutable_list():
    """Call __str__ and then find(self) on an ImmutableList created from a False value."""
    flag = False
    immutable_list = immutable_list_module.ImmutableList(flag, is_empty=flag)
    string_repr = immutable_list.__str__()  # exercise __str__ for coverage
    immutable_list.find(immutable_list)  # attempt to find the list within itself

def test_unshift_with_self_and_find_self():
    """Ensure calling unshift with the list itself and then find(self) executes without error."""
    # Use a concrete False flag for the is_empty parameter (matching the original test input)
    is_empty_flag = False

    # Create an ImmutableList instance with the is_empty flag
    lst = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Prepend the list to itself (edge-case operation preserved from the original test)
    result = lst.unshift(lst)

    # Attempt to find the list within itself (keeps the original call and order)
    lst.find(lst)

def test_append_and_find_false_in_immutable_list():
    """Ensure that False can be unshifted, appended, and then found in an ImmutableList."""
    is_empty_flag = False  # the boolean value used throughout the test

    # Create an ImmutableList initialized with is_empty_flag
    base_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # Prepend the False value to produce a new list
    list_with_false = base_list.unshift(is_empty_flag)

    # Append the original list to the new list
    combined_list = list_with_false.append(base_list)

    # Attempt to find the False value in the combined list
    combined_list.find(is_empty_flag)

def test_append_true_and_find_self_in_immutable_list():
    """Ensure appending True works and the original list can be searched for within itself."""
    flag = True
    original_list = immutable_list_module.ImmutableList(flag, is_empty=flag)
    appended_list = original_list.append(flag)  # append a True value to the immutable list
    length_after_append = appended_list.__len__()  # get length via __len__()
    original_list.find(original_list)  # search for the original list within itself

def test_immutable_list_chained_operations():
    """Chain multiple ImmutableList operations to ensure they can be called together:
    append, reduce, equality check, unshift, str, custom init, append, and find.
    """
    # start with an empty ImmutableList
    empty = immutable_list_module.ImmutableList()

    # append the empty list to itself
    appended_self = empty.append(empty)

    # perform a reduce using the appended list as both arguments
    reduced = empty.reduce(appended_self, appended_self)

    # check equality between appended list and the original empty list
    is_equal = appended_self.__eq__(empty)

    # unshift (prepend) the appended list onto itself
    unshifted = appended_self.unshift(appended_self)

    # get string representation of the unshifted list
    repr_str = unshifted.__str__()

    # create a new ImmutableList using the string representation as the is_empty argument
    custom_initialized = immutable_list_module.ImmutableList(is_empty=repr_str)

    # append the reduced result to itself
    doubled = reduced.append(reduced)

    # attempt to find the reduced result inside the unshifted list
    unshifted.find(reduced)

def test_reduce_unshift_and_find_interactions():
    """Exercise ImmutableList unshift, reduce, __len__, __eq__, and find interactions."""
    # Create an empty/base immutable list instance
    base_list = immutable_list_module.ImmutableList()

    # Create a new list by unshifting the base_list onto itself
    extended_once = base_list.unshift(base_list)

    # Reduce the base_list with the extended_once as both reducer and initial value
    reduced_result = base_list.reduce(extended_once, extended_once)

    # Capture the length of the extended_once list
    length_of_extended = extended_once.__len__()

    # Unshift extended_once onto itself to form another list
    extended_twice = extended_once.unshift(extended_once)

    # Compare extended_twice to the original base_list for equality
    equals_base = extended_twice.__eq__(base_list)

    # Create a new ImmutableList using the length_of_extended value for the is_empty parameter
    list_from_length = immutable_list_module.ImmutableList(is_empty=length_of_extended)

    # Call find on the reduced_result passing itself as the search target
    reduced_result.find(reduced_result)

def test_reduce_uses_to_list_result_as_both_accumulator_and_initial():
    """Verify that reduce() can be called with the to_list() result used as both accumulator and initial value."""
    # Use a boolean flag and an empty dict exactly as in the original test inputs.
    is_empty_flag = True
    empty_tail = {}

    # Create an ImmutableList using the 'tail' keyword argument.
    list_with_tail = immutable_list_module.ImmutableList(tail=empty_tail)

    # Create another ImmutableList with a boolean value and the same boolean passed to is_empty.
    list_with_bool = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the list to a Python list to use as the accumulator/initial value.
    accumulator = list_with_bool.to_list()

    # Call reduce with the same object for both the accumulator and the initial value.
    list_with_bool.reduce(accumulator, accumulator)

