import immutable_list as immutable_list

def test_immutable_list_equality():
    """Test if two empty ImmutableList instances are equal."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__eq__(immutable_list_0)

def test_immutable_list_string_representation():
    """Test if the string representation of an ImmutableList instance is correct."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__str__() == 'ImmutableList[]'

def test_immutable_list_to_list_conversion():
    """Test if the to_list method of an ImmutableList instance returns the correct list."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.to_list() == []

def test_immutable_list_addition():
    """Test if adding two ImmutableList instances results in a new ImmutableList instance."""
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list.ImmutableList()
    assert immutable_list_0.__add__(immutable_list_1).__eq__(immutable_list_0)

def test_immutable_list_length():
    """Test if the length of an ImmutableList instance is correct."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__len__() == 0

def test_immutable_list_addition_to_list():
    """Test if adding a list to an ImmutableList instance results in a new ImmutableList instance."""
    immutable_list_0 = immutable_list.ImmutableList()
    assert immutable_list_0.__add__([1, 2, 3]).__eq__(immutable_list_0)

def test_immutable_list_equality_2():
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list.ImmutableList()
    assert immutable_list_0.__eq__(immutable_list_1)

def test_immutable_list_append_and_find_2():
    bool_0 = True
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_1 = immutable_list_0.append(bool_0)
    immutable_list_0.find(immutable_list_0)

def test_add_method_with_empty_list():
    # Given
    immutable_list_0 = immutable_list.ImmutableList()
    none_type_0 = None

    # When
    result = immutable_list_0.__add__(none_type_0)

    # Then
    assert result is None, "The result should be None"

def test_case_4_modified():
    immutable_list_0 = immutable_list.ImmutableList()
    var_0 = immutable_list_0.__len__()
    immutable_list_1 = immutable_list.ImmutableList(
        immutable_list_0, is_empty=immutable_list_0
    )
    immutable_list_1.find(immutable_list_1)

def test_immutable_list_length_and_find_method():
    """Test the length of the ImmutableList and find method."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    str_0 = immutable_list_0.__len__()
    immutable_list_0.find(immutable_list_0)

def test_timer_start_stops_correctly_2():
    """Test if the timer starts and stops correctly."""
    # Create a new instance of Timer
    timer_instance = Timer(name="class")

    # Start the timer
    timer_instance.start()

    # Do something
    waste_time()

    # Stop the timer
    timer_instance.stop()

    # Check if the timer is stopped
    assert not timer_instance.is_running

def test_case_7_modified():
    immutable_list_0 = immutable_list.ImmutableList()
    none_type_0 = None
    var_0 = immutable_list_0.find(none_type_0)
    immutable_list_1 = immutable_list_0.append(immutable_list_0)
    var_1 = immutable_list_1.to_list()
    var_1.__add__(none_type_0)

def test_immutable_list_creation():
    """Test the creation of an ImmutableList instance."""
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(is_empty=bool_0)
    var_0 = immutable_list_0.to_list()
    immutable_list_1 = immutable_list.ImmutableList()
    var_1 = immutable_list_0.to_list()
    immutable_list_0.map(var_1)

def test_immutable_list_unshift_append_map():
    none_type = None
    immutable_list_empty = immutable_list.ImmutableList(none_type, none_type)
    immutable_list_unshift = immutable_list_empty.unshift(none_type)
    immutable_list_unshift_unshift = immutable_list_unshift.unshift(immutable_list_unshift)
    immutable_list_unshift_append = immutable_list_unshift.append(none_type)
    immutable_list_unshift_append.map(none_type)

def test_filter_method_with_empty_list_and_immutable_list():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_0.filter(immutable_list_0)

def test_add_two_empty_lists():
    """Test adding two empty lists results in an empty list."""
    # Given
    empty_list_1 = immutable_list.ImmutableList()
    empty_list_2 = immutable_list.ImmutableList()

    # When
    result = empty_list_1.__add__(empty_list_2)

    # Then
    assert result.__len__() == 0

def test_find_method_returns_correct_length_2():
    int_0 = 1947
    none_type_0 = None
    immutable_list_0 = immutable_list.ImmutableList(none_type_0, none_type_0)
    timer_instance = immutable_list_0.find(int_0)
    assert timer_instance.__len__() == 2

def test_immutable_list_find_method():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_reduce_find():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList()
    timer_instance = immutable_list_0.reduce(bool_0, immutable_list_0)
    immutable_list_1 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    immutable_list_1.find(immutable_list_1)

def test_immutable_list_creation_1():
    immutable_list_0 = immutable_list.ImmutableList()

def test_immutable_list_str_representation():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    str_0 = immutable_list_0.__str__()
    immutable_list_0.find(immutable_list_0)

def test_unshift_and_find_modified():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    var_0 = immutable_list_0.unshift(immutable_list_0)
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_unshift_append_find_modified():
    bool_0 = False
    immutable_list_0 = immutable_list.ImmutableList(is_empty=bool_0)
    immutable_list_1 = immutable_list_0.unshift(bool_0)
    immutable_list_2 = immutable_list_1.append(immutable_list_0)
    immutable_list_2.find(bool_0)

def test_immutable_list_append_and_find():
    """Test that ImmutableList appends elements correctly and returns correct length."""
    is_empty = True
    immutable_list_0 = immutable_list.ImmutableList(is_empty, is_empty=is_empty)
    immutable_list_1 = immutable_list_0.append(is_empty)
    len_after_append = len(immutable_list_1)
    assert len_after_append == 2
    immutable_list_0.find(immutable_list_0)

def test_immutable_list_append_reduce_unshift_find():
    # Create an empty ImmutableList
    empty_list = immutable_list.ImmutableList()

    # Append the empty list to itself
    list_with_self = empty_list.append(empty_list)

    # Reduce the list with itself
    reduced_list = list_with_self.reduce(list_with_self, list_with_self)

    # Check if the reduced list is equal to the empty list
    assert reduced_list.__eq__(empty_list)

    # Unshift the reduced list to itself
    unshifted_list = reduced_list.unshift(reduced_list)

    # Convert the unshifted list to a string
    str_list = unshifted_list.__str__()

    # Create a new ImmutableList with the string representation of the unshifted list
    new_list = immutable_list.ImmutableList(is_empty=str_list)

    # Append the reduced list to itself
    appended_list = reduced_list.append(reduced_list)

    # Find the reduced list in the appended list
    found = appended_list.find(reduced_list)

def test_immutable_list_unshift_reduce_len_eq():
    immutable_list_0 = immutable_list.ImmutableList()
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    var_0 = immutable_list_0.reduce(immutable_list_1, immutable_list_1)
    var_1 = immutable_list_1.__len__()
    immutable_list_2 = immutable_list_1.unshift(immutable_list_1)
    bool_0 = immutable_list_2.__eq__(immutable_list_0)
    immutable_list_3 = immutable_list.ImmutableList(is_empty=var_1)
    var_0.find(var_0)

def test_immutable_list_reduce_returns_correct_result():
    bool_0 = True
    dict_0 = {}
    immutable_list_0 = immutable_list.ImmutableList(tail=dict_0)
    immutable_list_1 = immutable_list.ImmutableList(bool_0, is_empty=bool_0)
    var_0 = immutable_list_1.to_list()
    immutable_list_1.reduce(var_0, var_0)