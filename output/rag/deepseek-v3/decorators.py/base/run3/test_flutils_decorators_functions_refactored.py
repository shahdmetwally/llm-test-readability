import pytest
import decorators as module_0

def test_cached_property_descriptor_protocol_with_none_func():
    """Test that invoking __get__ on a cached_property with None as the function
    and with various argument combinations does not raise an exception."""
    none_func = None
    cached_property_instance = module_0.cached_property(none_func)

    # Simulate the descriptor protocol: accessing the property on an instance with its type
    result = cached_property_instance.__get__(none_func, cached_property_instance)

    # Access the property from the class perspective (obj is the descriptor itself)
    cached_property_instance.__get__(cached_property_instance, cached_property_instance)

def test_cached_property_get_with_empty_set():
    """Test that cached_property's __get__ method can handle an empty set as the instance."""
    instance = set()
    cached_property = module_0.cached_property(instance)
    cached_property.__get__(instance, cached_property)

def test_cached_property_init_with_empty_set():
    """Verify that cached_property can be initialized with an empty set."""
    empty_set = set()
    cached_property_instance = module_0.cached_property(empty_set)

