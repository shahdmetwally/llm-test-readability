import pytest
import decorators as decorators_module

def test_cached_property_get_with_none_instance_returns_descriptor():
    """Test that __get__ on a cached_property with None as the instance
    passes the instance through correctly (i.e., attribute lookup returns
    the descriptor itself when called on the class, not an instance)."""
    none_instance = None
    cached_property_obj = decorators_module.cached_property(none_instance)
    result = cached_property_obj.__get__(none_instance, cached_property_obj)
    cached_property_obj.__get__(cached_property_obj, cached_property_obj)

def test_cached_property_with_empty_set():
    """Test that cached_property works with an empty set as its argument."""
    empty_set = set()
    cached_property_instance = decorators_module.cached_property(empty_set)
    cached_property_instance.__get__(empty_set, cached_property_instance)

def test_cached_property_can_accept_set_instance():
    """
    Verify that cached_property can be initialized with an empty set.
    """
    # Create an empty set to pass as the function argument
    func_to_wrap = set()
    # Instantiate cached_property with the set
    wrapped = decorators_module.cached_property(func_to_wrap)

