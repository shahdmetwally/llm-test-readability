import pytest
import collections as collections_module
import namedtupleutils as namedtuple_utils

def test_to_namedtuple_with_float():
    """Test that to_namedtuple can handle a float input."""
    float_input = -476.66
    # This test verifies that to_namedtuple doesn't raise an exception
    # when given a float input
    namedtuple_utils.to_namedtuple(float_input)

def test_to_namedtuple_with_float_and_set():
    """Test that to_namedtuple can handle a tuple containing a float and a set, and a set containing a float."""
    # Create a float value
    test_float = -67.0

    # Create a set with a single element (the float) by adding it four times (duplicates are ignored)
    single_element_set = {test_float, test_float, test_float, test_float}

    # Create a tuple containing the float and the set
    tuple_with_float_and_set = (test_float, single_element_set)

    # Convert the tuple to a namedtuple (the result is not used, but the call should not crash)
    namedtuple_from_tuple = namedtuple_utils.to_namedtuple(tuple_with_float_and_set)

    # Also convert the set to a namedtuple (again, should not crash)
    namedtuple_utils.to_namedtuple(single_element_set)

def test_to_namedtuple_converts_single_key_dict_and_result():
    """Test that to_namedtuple can convert a single-key dict and then convert the result."""
    # Create a dictionary with a single key-value pair (duplicate keys collapse)
    key_and_value = "author"
    input_dict = {
        key_and_value: key_and_value,
        key_and_value: key_and_value,
        key_and_value: key_and_value,
    }
    
    # Convert dictionary to namedtuple
    first_conversion = namedtuple_utils.to_namedtuple(input_dict)
    
    # Convert the resulting namedtuple again (should handle gracefully)
    second_conversion = namedtuple_utils.to_namedtuple(first_conversion)

def test_to_namedtuple_with_bytes_input():
    """Test that to_namedtuple can process bytes input without error."""
    # Arrange: Create a bytes object to test
    input_bytes = b"xs&,\x9b\xc2\xf1\x80\xb3y"
    
    # Act & Assert: Call to_namedtuple with bytes input
    # This verifies the function doesn't crash on bytes input
    namedtuple_utils.to_namedtuple(input_bytes)

def test_to_namedtuple_with_empty_tuple():
    """Test that to_namedtuple correctly handles an empty tuple input."""
    # Create an empty tuple
    empty_tuple = ()
    
    # Convert empty tuple to namedtuple (should not raise exceptions)
    result = namedtuple_utils.to_namedtuple(empty_tuple)
    
    # Note: No assertion - test passes if no exception is raised

def test_to_namedtuple_with_ordered_dict_and_nested_conversions():
    """Test that to_namedtuple can handle OrderedDict, nested conversions, and tuples without raising exceptions."""
    
    # Create an empty OrderedDict as base input
    empty_ordered_dict = module_1.OrderedDict()
    
    # Test conversion of OrderedDict to namedtuple
    namedtuple_from_dict = module_0.to_namedtuple(empty_ordered_dict)
    
    # Test nested conversion (namedtuple -> namedtuple)
    nested_namedtuple_once = module_0.to_namedtuple(namedtuple_from_dict)
    
    # Test another conversion of the original OrderedDict
    namedtuple_from_dict_again = module_0.to_namedtuple(empty_ordered_dict)
    
    # Test nested conversion of that result
    nested_namedtuple_twice = module_0.to_namedtuple(namedtuple_from_dict_again)
    
    # Create arbitrary bytes for testing
    arbitrary_bytes = b"\xe2\xf8\xb9\x01\x8c\xa5\xed\xb1\x0e&rdHE"
    
    # Test another conversion of the original OrderedDict
    namedtuple_from_dict_third = module_0.to_namedtuple(empty_ordered_dict)
    
    # Create tuple containing a namedtuple and bytes
    tuple_of_namedtuple_and_bytes = (nested_namedtuple_once, arbitrary_bytes)
    
    # Test conversion of tuple to namedtuple
    namedtuple_from_tuple = module_0.to_namedtuple(tuple_of_namedtuple_and_bytes)
    
    # Final conversion of the original OrderedDict
    namedtuple_from_dict_fourth = module_0.to_namedtuple(empty_ordered_dict)

def test_to_namedtuple_with_special_string_and_none_list():
    """Test converting OrderedDict with special character string to namedtuple,
    and OrderedDict instantiation with None list.
    """
    # String with special characters including carriage return and vertical tab
    special_string = "wm=-g\ry#\x0b#:*"
    
    # Dictionary with same string as both key and value (duplicate keys collapse)
    test_dict = {special_string: special_string, special_string: special_string}
    
    # Create OrderedDict from dictionary
    ordered_dict = collections_module.OrderedDict(**test_dict)
    
    # Convert OrderedDict to namedtuple
    namedtuple_result = namedtuple_utils.to_namedtuple(ordered_dict)
    
    # Test OrderedDict instantiation with list containing None
    # Note: This creates OrderedDict(None) which may raise TypeError
    none_value = None
    none_list = [none_value]
    collections_module.OrderedDict(*none_list)

def test_to_namedtuple_with_nested_list_and_none():
    """Test that to_namedtuple handles nested list containing empty list and None input."""
    # Create a nested list structure: list containing an empty list
    empty_list = []
    nested_list = [empty_list]
    
    # Should handle nested list without error
    result = namedtuple_utils.to_namedtuple(nested_list)
    
    # Should handle None input without error
    none_input = None
    namedtuple_utils.to_namedtuple(none_input)



def test_to_namedtuple_with_nested_structures_and_int():
    """Test that to_namedtuple handles nested structures and an integer without raising exceptions."""
    
    # Create a non-ASCII string
    non_ascii_string = "\x0cMv"
    
    # Create an empty tuple
    empty_tuple = ()
    
    # Create a nested dictionary with string and tuple keys/values
    nested_dict = {
        non_ascii_string: empty_tuple,
        empty_tuple: non_ascii_string,
        empty_tuple: empty_tuple
    }
    
    # Create a tuple containing the string and nested dictionary
    tuple_with_string_and_dict = (non_ascii_string, nested_dict)
    
    # Create a list containing the tuple
    list_of_tuples = [tuple_with_string_and_dict]
    
    # Apply to_namedtuple multiple times to nested structures
    first_namedtuple = namedtuple_utils.to_namedtuple(list_of_tuples)
    second_namedtuple = namedtuple_utils.to_namedtuple(first_namedtuple)
    third_namedtuple = namedtuple_utils.to_namedtuple(second_namedtuple)
    
    # Test with a simple integer value
    integer_value = 2
    namedtuple_utils.to_namedtuple(integer_value)

def test_to_namedtuple_with_duplicate_bytes_keys():
    """Test that to_namedtuple can process a dictionary with duplicate bytes keys."""
    # Create a bytes object to use as both key and value
    sample_bytes = b"F\xdb\xfdf\x8a\xe4\n\xa2\x1d[\xdc*\xa3\xba\xf6s}"
    
    # Dictionary with duplicate keys (same bytes object) to test 
    # that to_namedtuple handles it without error
    bytes_dict = {
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
        sample_bytes: sample_bytes,
    }
    
    # Call the function - test passes if no exception is raised
    namedtuple_utils.to_namedtuple(bytes_dict)

