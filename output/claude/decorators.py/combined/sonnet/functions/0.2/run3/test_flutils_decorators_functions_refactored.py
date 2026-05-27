import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_returns_descriptor():
    """Test cached_property.__get__ when called with None and with the descriptor as instance/owner."""
    # Use None as the instance to simulate access from the class rather than an instance
    none_instance = None

    # Create a cached_property descriptor wrapping None as the underlying function
    cached_prop = decorators.cached_property(none_instance)

    # Call __get__ with None as the instance; typically returns the descriptor itself
    get_result_with_none_instance = cached_prop.__get__(none_instance, cached_prop)

    # Call __get__ with the descriptor as both instance and owner
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_with_set_instance():
    """Test that cached_property.__get__ can be invoked with a set instance as both obj and type arguments."""
    # Create a plain empty set to serve as the target object
    empty_set = set()

    # Wrap the empty set in a cached_property descriptor
    cached_prop = decorators.cached_property(empty_set)

    # Invoke __get__ with the set as both the instance and the owner
    cached_prop.__get__(empty_set, cached_prop)

def test_cached_property_accepts_empty_set_as_argument():
    """Test that cached_property can be instantiated with an empty set as its argument."""
    # Prepare an empty set to use as the input argument
    empty_set = set()

    # Instantiate cached_property with the empty set; should not raise
    cached_prop_instance = decorators.cached_property(empty_set)

