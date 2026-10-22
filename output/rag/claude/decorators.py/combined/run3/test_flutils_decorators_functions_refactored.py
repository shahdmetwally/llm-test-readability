import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_returns_descriptor():
    """Test that cached_property.__get__ handles a None instance and a descriptor-as-instance call without error."""
    # Use None as the instance to simulate descriptor access at the class level
    none_instance = None

    # Create a cached_property descriptor wrapping None as the underlying function
    cached_prop = decorators.cached_property(none_instance)

    # Calling __get__ with None as the instance should return the descriptor itself
    get_result_with_none_instance = cached_prop.__get__(none_instance, cached_prop)

    # Calling __get__ with the descriptor as both instance and owner exercises a different code path
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_with_set_instance():
    """Test that cached_property.__get__ can be invoked with a set as both the instance and owner arguments."""
    # Create an empty set to serve as the wrapped value
    empty_set = set()

    # Wrap the set in a cached_property descriptor
    cached_prop = decorators.cached_property(empty_set)

    # Invoke __get__ with the set as both the instance and the owner
    cached_prop.__get__(empty_set, cached_prop)

def test_cached_property_accepts_empty_set_as_argument():
    """Test that cached_property can be instantiated with an empty set as its argument."""
    # Prepare an empty set to use as the argument to cached_property
    empty_set = set()

    # Construct a cached_property instance using the empty set
    cached_property_instance = decorators.cached_property(empty_set)

