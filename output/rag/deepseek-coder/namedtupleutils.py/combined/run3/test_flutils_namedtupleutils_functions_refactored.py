import namedtupleutils as namedtuple_utils
import collections as module_1
import pytest

class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer_instance = Timer(label='test_function', logger=None)

    def test_timer_start_stops_correctly(self):
        # Arrange
        func_name = 'test_function'
        expected_timer_count = 1

        # Act
        self.timer_instance.start_timer()
        self.timer_instance.stop_timer()

        # Assert
        self.assertEqual(self.timer_instance.timings[func_name]['count'], expected_timer_count)

    def test_namedtupleutils_creates_namedtuple_different():
        """
        Functional test the namedtuple util method to_namedtuple
        """
        time_1 = -67.0
        set_to_convert_1 = {time_1, time_1, time_1, time_1}
        tuple_to_convert_1 = (time_1, set_to_convert_1)
    
        namedtuple_utils.to_namedtuple(tuple_to_convert_1)
        namedtuple_utils.to_namedtuple(set_to_convert_1)

def test_conversion_from_dict_to_namedtuple():
    """Test if dictionary is correctly converted to named tuple and if a named tuple is passed, it should not alter it."""
    
    str_0 = "author"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    
    dict_namedtuple = module_1.to_namedtuple(dict_0)

    var_1 = module_1.to_namedtuple(dict_namedtuple)
    
    # Check if dictionary is correctly converted to named tuple
    assert var_1 == dict_namedtuple

    # If a named tuple is passed, it should not alter it
    assert var_1 == module_1.to_namedtuple(var_1)

def test_namedtupleutils_creates_namedtuple_different():
    """
    Test that the function namedtuple_utils.to_namedtuple() creates a namedtuple from a list of tuples.
    """
    example_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    module_1.to_namedtuple(example_bytes)

def test_namedtuple_is_correctly_created_from_tuple_different_name():
    """Test that to_namedtuple correctly creates a namedtuple from a tuple."""
    test_tuple = ('Alice', 30)
    Person = namedtuple_utils.to_namedtuple(namedtuple_utils.namedtuple('Person', 'name age'), test_tuple)
    assert isinstance(Person, Person)
    assert Person.name == 'Alice'
    assert Person.age == 30

def test_timer_accuracy_stop_restart():
    """
    Test whether the timer can accurately measure the time, stops, re-starts, and throws exceptions properly
    """

def test_to_namedtuple_creates_namedtuple_from_ordered_dict():
    """
    Tests that 'to_namedtuple' correctly creates a namedtuple from an ordered dict
    """
    string_data = "wm=-g\ry#\x0b#:*"
    ordered_dict = {string_data: string_data, string_data: string_data}
    ordered_dict = collections.OrderedDict(**ordered_dict)
    namedtuple_utils.to_namedtuple(ordered_dict)
    ...

def test_timewaste_decorator():
    # Given
    timewaste = waste_time
    decorated_timewaste = Timer(text=f"{TIME_PREFIX} {{:.4f}} seconds")(waste_time)
    timewaste_decorator = functools.partial(Timer(text=f"{TIME_PREFIX} {{:.4f}} seconds"), waste_time)

    # When
    timewaste()
    decorated_timewaste()
    timewaste_decorator()

    # Then
    assert RE_TIME_MESSAGE.match(capsys.readouterr().out)