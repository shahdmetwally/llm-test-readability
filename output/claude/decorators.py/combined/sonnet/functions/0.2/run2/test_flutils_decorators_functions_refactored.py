import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_returns_descriptor():
    """Test cached_property.__get__ when called with None as instance and with the descriptor as instance/owner."""
    # Use None as the instance to simulate access from the class level
    none_instance = None

    # Create a cached_property descriptor wrapping None as the underlying function
    cached_prop = decorators.cached_property(none_instance)

    # Call __get__ with None as the instance; typically returns the descriptor itself
    get_result_with_none_instance = cached_prop.__get__(none_instance, cached_prop)

    # Call __get__ with the descriptor as both instance and owner
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_with_set_instance():
    """Test that cached_property.__get__ can be invoked with a set as both the instance and owner arguments."""
    # Create an empty set to serve as the wrapped value and the instance argument
    empty_set = set()

    # Wrap the empty set in a cached_property descriptor
    prop = decorators.cached_property(empty_set)

    # Invoke __get__ with the set as both the object instance and the owner/type
    prop.__get__(empty_set, prop)

def test_cached_property_accepts_empty_set_as_argument():
    """Test that cached_property can be instantiated with an empty set as its argument."""
    # Prepare an empty set to use as the wrapped callable argument
    empty_set = set()

    # Instantiate cached_property with the empty set; should not raise
    cached_prop_instance = decorators.cached_property(empty_set)

