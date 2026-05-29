import pytest

import immutable_list as immutable_list_module

def test_immutablelist_basic_api_calls_readable():
    """Exercise key ImmutableList methods: equality, string conversion, to_list, concatenation, and length retrieval."""
    # Construct an empty ImmutableList instance
    imm_list = immutable_list_module.ImmutableList()

    # Check equality of the instance with itself (calls __eq__)
    is_equal_to_self = (imm_list == imm_list)

    # Obtain string representation (calls __str__)
    string_repr = str(imm_list)

    # Convert immutable list to a mutable/list representation (calls to_list)
    as_list = imm_list.to_list()

    # Concatenate the converted list with itself (calls list.__add__)
    combined_list = as_list + as_list

    # Get the length of the converted list (calls list.__len__)
    list_length = len(as_list)

    # Attempt to add the converted list back to the immutable list (calls ImmutableList.__add__)
    imm_list + as_list

def test_immutable_list_magic_and_sequence_methods_execute_successfully():
    """Verify that core ImmutableList magic and sequence methods execute in order and return values without raising errors."""
    truth_value = True

    # Create an ImmutableList instance
    original = immutable_list_module.ImmutableList()

    # Call equality magic method with a boolean value
    equality_result = original.__eq__(truth_value)

    # Concatenate the list with itself using the addition magic method
    concatenated = original.__add__(original)

    # Use find with the previously obtained equality result
    find_result = original.find(equality_result)

    # Get the string representation of the original list
    original_str = original.__str__()

    # Unshift the original list onto itself (preserve return value)
    unshifted = original.unshift(original)

    # Basic sanity checks to catch obvious failures
    assert isinstance(original_str, str)
    assert isinstance(equality_result, bool)
    assert type(concatenated) is type(original)

    # Call reduce on the resulting list to ensure it executes without raising
    unshifted.reduce(unshifted, truth_value)

def test_immutable_list_append_and_find_self_reference():
    """Construct an ImmutableList with is_empty=True, append True, and call find with the original list."""
    # Use a clear name for the boolean flag used in construction and append
    is_empty_flag = True

    # Create the original immutable list with is_empty=True
    original_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Append a True value to the original list, capturing the returned new list
    appended_list = original_list.append(is_empty_flag)

    # Call find on the original list, passing the original list itself (preserve original call)
    original_list.find(original_list)

def test_immutable_list_add_called_with_none():
    """Ensure ImmutableList.__add__ can be called with None without raising an exception."""
    # Create an ImmutableList instance.
    immutable_list_instance = immutable_list_module.ImmutableList()

    # Explicit None value to pass into the dunder add method.
    none_value = None

    # Invoke the __add__ method with None. Test succeeds if no exception is raised.
    immutable_list_instance.__add__(none_value)

def test_immutablelist_len_and_find_with_self():
    """Instantiate an ImmutableList, call its length, wrap it in another ImmutableList, and call find with the wrapper itself."""
    # Create an initial (empty) ImmutableList instance
    empty_list = immutable_list_module.ImmutableList()
    # Call __len__() on the initial instance (result stored but not asserted to preserve original behavior)
    length = empty_list.__len__()
    # Create a second ImmutableList, passing the first as both the positional argument and the is_empty kwarg
    wrapped_list = immutable_list_module.ImmutableList(empty_list, is_empty=empty_list)
    # Call find on the second list, passing the second list itself as the search target
    wrapped_list.find(wrapped_list)

def test_immutablelist_len_and_find_self_reference():
    """Create a non-empty ImmutableList, get its length, and call find with itself."""
    # Use an explicit flag variable for clarity (matches original literal False)
    is_empty_flag = False

    # Construct the ImmutableList with is_empty=False (same as original)
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call __len__() explicitly and store the result (preserves original call)
    length_result = imm_list.__len__()

    # Call find with the list itself as argument (preserves original call and order)
    imm_list.find(imm_list)

def test_find_with_to_list_result_on_non_empty_immutable_list():
    """Ensure ImmutableList.find accepts the list produced by to_list()
    when the ImmutableList is constructed as non-empty.
    """
    # Use an explicit flag for clarity
    is_empty_flag = False

    # Construct the ImmutableList exactly as in the original test
    immutable_list_instance = immutable_list_module.ImmutableList(
        is_empty_flag, is_empty=is_empty_flag
    )

    # Obtain a plain list representation
    list_from_immutable = immutable_list_instance.to_list()

    # Invoke find with the list produced by to_list()
    immutable_list_instance.find(list_from_immutable)

def test_immutable_list_find_none_append_self_and_add_with_none():
    """Call find with None, append the list to itself, convert to a list,
    and invoke __add__ with None to exercise edge behavior."""
    original_list = immutable_list_module.ImmutableList()

    none_value = None

    # Call find with None
    found_result = original_list.find(none_value)

    # Append the list to itself
    appended_list = original_list.append(original_list)

    # Convert appended list to a Python list
    list_representation = appended_list.to_list()

    # Call the list's __add__ with None
    list_representation.__add__(none_value)

def test_immutable_list_to_list_and_map_accepts_list():
    """Ensure that to_list() returns a list and that map() accepts that list without raising an error."""
    # Create an ImmutableList explicitly marked as not empty.
    is_empty_flag = False
    original_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # Take a snapshot of the contents via to_list().
    list_snapshot_1 = original_list.to_list()

    # Create another ImmutableList using default constructor (unused beyond construction).
    default_list = immutable_list_module.ImmutableList()

    # Take another snapshot from the original list (same call order as original test).
    list_snapshot_2 = original_list.to_list()

    # Call map with the list snapshot to ensure it accepts the list (preserve original behavior).
    original_list.map(list_snapshot_2)

def test_immutablelist_methods_accept_none_and_chain():
    """Ensure ImmutableList methods accept None inputs and support chaining without error."""
    # Use a canonical None value for all None inputs
    none_value = None

    # Create the base ImmutableList with two None values
    base_list = immutable_list_module.ImmutableList(none_value, none_value)

    # Prepend None to the base list
    after_unshift_none = base_list.unshift(none_value)

    # Prepend the previously created list onto the base list
    after_unshift_list = base_list.unshift(after_unshift_none)

    # Append None to the list returned by the first unshift
    after_append_none = after_unshift_none.append(none_value)

    # Call map with None on the result of append (preserve original call; behavior-dependent)
    after_append_none.map(none_value)

def test_filter_accepts_self_without_error():
    """Ensure calling filter with the list itself does not raise an exception."""
    # Explicitly use a descriptive name for the empty flag
    is_empty_flag = False

    # Create an ImmutableList instance with the is_empty flag set to False
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call filter with the list itself to ensure this usage does not raise an exception
    immutable_list.filter(immutable_list)

def test_immutablelist_addition_then_filter_accepts_length():
    """Ensure ImmutableList can be added to itself and filter() accepts the resulting length without error."""
    # Create an ImmutableList instance (originally immutable_list_0)
    original_list = immutable_list_module.ImmutableList()

    # Add the list to itself using the explicit dunder method (originally immutable_list_1 = ...)
    combined_list = original_list.__add__(original_list)

    # Obtain the length of the combined list using the explicit dunder call (originally var_0 = ...)
    combined_length = combined_list.__len__()

    # Call filter with the obtained length — the test passes if this call executes without error
    combined_list.filter(combined_length)

def test_immutable_list_find_then_invoke_length():
    """Construct an ImmutableList with None placeholders, call find, and invoke __len__ on the result."""
    # Prepare the search value and placeholders exactly as in the original test
    search_value = 1947
    placeholder_value = None

    # Create an ImmutableList with two None placeholders (preserve original construction)
    imm_list = immutable_list_module.ImmutableList(placeholder_value, placeholder_value)

    # Call find with the same literal and then invoke __len__() on the returned object
    find_result = imm_list.find(search_value)
    find_result.__len__()

def test_immutable_list_find_accepts_self_reference():
    """Ensure ImmutableList.find can be called with the list itself as the search target without raising an error."""
    # Use an explicit descriptive name for the empty flag (original was False)
    is_empty_flag = False

    # Create an ImmutableList with the same boolean passed both positionally and as the 'is_empty' kwarg
    imm_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call find with the same list instance to verify it handles searching for itself
    imm_list.find(imm_list)

def test_reduce_with_false_seed_and_find_called_with_self():
    """Ensure reduce can be invoked with a False seed and that find accepts the list instance."""
    # Use an explicit boolean variable for clarity (originally `bool_0 = False`)
    false_flag = False

    # Create an empty ImmutableList instance (originally `immutable_list_0 = module_0.ImmutableList()`)
    empty_list = immutable_list_module.ImmutableList()

    # Call reduce with the False seed and the list itself (originally `var_0 = immutable_list_0.reduce(bool_0, immutable_list_0)`)
    reduction_result = empty_list.reduce(false_flag, empty_list)

    # Create another ImmutableList passing the boolean positionally and as the is_empty kwarg
    # (originally `immutable_list_1 = module_0.ImmutableList(bool_0, is_empty=bool_0)`)
    flagged_list = immutable_list_module.ImmutableList(false_flag, is_empty=false_flag)

    # Call find with the list instance itself (originally `immutable_list_1.find(immutable_list_1)`)
    flagged_list.find(flagged_list)

def test_immutable_list_constructs_successfully():
    """Verify that ImmutableList can be constructed without raising an exception."""
    # Construct an ImmutableList to ensure the constructor does not raise.
    immutable_list_instance = immutable_list_module.ImmutableList()
    # Basic sanity check: the constructed object should be an instance of ImmutableList.
    assert isinstance(immutable_list_instance, immutable_list_module.ImmutableList)

def test_immutable_list_str_and_find_with_false_is_empty_flag():
    """Instantiate ImmutableList with is_empty=False, call __str__, then call find with the instance itself."""
    # Setup: use False for both the positional value and the is_empty keyword
    is_empty_flag = False

    # Instantiate the ImmutableList using the provided alias for the module
    immutable_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Exercise: obtain the string representation (call preserved exactly as __str__)
    string_representation = immutable_list.__str__()

    # Exercise: call find with the instance itself as the search target (call preserved)
    immutable_list.find(immutable_list)

def test_immutable_list_unshift_self_and_find_no_error():
    """Construct an ImmutableList (not empty), unshift the list onto itself, and call find with itself (no exceptions)."""
    # Use explicit variable name for the boolean flag passed to ImmutableList
    is_empty_flag = False

    # Create the original ImmutableList instance with is_empty=False
    original_list = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Call unshift with the list itself; keep the assignment to preserve original behaviour
    unshifted_list = original_list.unshift(original_list)

    # Call find with the list itself; this is intended to run without raising
    original_list.find(original_list)

def test_immutable_list_unshift_append_find():
    """Ensure unshift followed by append leaves the structure in a state where find can be invoked for the same value."""
    # use the literal False as the original emptiness flag
    is_empty_flag = False

    # construct the original immutable list with the specified flag
    original_list = immutable_list_module.ImmutableList(is_empty=is_empty_flag)

    # unshift the same flag value to produce a new list
    list_after_unshift = original_list.unshift(is_empty_flag)

    # append the original list to the result of unshift
    list_after_append = list_after_unshift.append(original_list)

    # invoke find with the same boolean value on the final list to ensure it executes without error
    list_after_append.find(is_empty_flag)

def test_immutable_list_append_and_find_with_true_flag():
    """Ensure append and find calls execute for an ImmutableList initialized with True."""
    # Setup: create an ImmutableList initialized with True and marked as empty
    flag = True
    original_list = immutable_list_module.ImmutableList(flag, is_empty=flag)

    # Action: append the same flag value, producing a new immutable list
    appended_list = original_list.append(flag)

    # Inspect: get the length of the appended list (using explicit dunder call as in original)
    length = appended_list.__len__()

    # Verify behavior: call find on the original list with the original list as the search target
    original_list.find(original_list)

def test_immutable_list_chain_operations_interaction():
    """Exercise a chain of ImmutableList methods to verify method interactions and call sequences."""
    # Create a base empty immutable list
    base_list = immutable_list_module.ImmutableList()

    # Append the base list to itself
    appended_once = base_list.append(base_list)

    # Reduce using the appended_once as both arguments (preserve original call order)
    reduced_result = base_list.reduce(appended_once, appended_once)

    # Check equality method is callable (result is unused, preserved as in original)
    equality_check = appended_once.__eq__(base_list)

    # Unshift operation: add appended_once to the front (preserve original call)
    unshifted = appended_once.unshift(appended_once)

    # Obtain string representation (kept for use in constructing a new list)
    repr_str = unshifted.__str__()

    # Construct a new ImmutableList using the repr_str as the is_empty keyword (unchanged)
    constructed_with_is_empty = immutable_list_module.ImmutableList(is_empty=repr_str)

    # Append the reduced_result to itself (preserve original call)
    appended_reduced = reduced_result.append(reduced_result)

    # Call find on the unshifted list passing the reduced_result (preserve original call and order)
    unshifted.find(reduced_result)

def test_immutable_list_unshift_reduce_find_sequence_unique():
    """Verify a sequence of ImmutableList operations (unshift, reduce, length, equality, construction, find) executes in order."""
    # Create a base ImmutableList instance
    base_list = immutable_list_module.ImmutableList()

    # Unshift base_list onto itself (produce a new list)
    unshifted_once = base_list.unshift(base_list)

    # Reduce base_list with unshifted_once twice (same argument used twice)
    reduced_result = base_list.reduce(unshifted_once, unshifted_once)

    # Retrieve length of the unshifted_once list via __len__
    length_of_unshifted = unshifted_once.__len__()

    # Unshift unshifted_once onto itself
    unshifted_twice = unshifted_once.unshift(unshifted_once)

    # Check equality between unshifted_twice and base_list
    is_equal_to_base = unshifted_twice.__eq__(base_list)

    # Construct another ImmutableList using the length as the is_empty parameter
    constructed_with_is_empty = immutable_list_module.ImmutableList(is_empty=length_of_unshifted)

    # Call find on the reduced result, passing it itself (preserve original call sequence)
    reduced_result.find(reduced_result)

def test_immutable_list_reduce_with_self_list_arguments():
    """Construct ImmutableList instances (including one with a tail), obtain the list
    representation of one, and call reduce using that representation as both arguments.
    """
    # Use a boolean flag for the is_empty parameter
    is_empty_flag = True

    # Use an empty dict as the tail mapping
    tail_dict = {}

    # Construct an ImmutableList with an explicit tail
    list_with_tail = immutable_list_module.ImmutableList(tail=tail_dict)

    # Construct another ImmutableList using the boolean as a positional value and as is_empty
    list_with_value = immutable_list_module.ImmutableList(is_empty_flag, is_empty=is_empty_flag)

    # Convert the second ImmutableList to a Python list
    list_representation = list_with_value.to_list()

    # Call reduce on the second ImmutableList using the list representation for both arguments
    list_with_value.reduce(list_representation, list_representation)

