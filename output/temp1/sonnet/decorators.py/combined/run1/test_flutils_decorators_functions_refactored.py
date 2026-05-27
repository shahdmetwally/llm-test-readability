import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_returns_descriptor():
    """Test that cached_property.__get__ behaves correctly when called with None and with itself as the instance."""
    # Use None as the instance argument to simulate access from the class level
    none_instance = None

    # Create a cached_property descriptor wrapping None as the underlying function
    cached_prop = decorators.cached_property(none_instance)

    # Call __get__ with None as the instance; typically returns the descriptor itself
    get_result_with_none_instance = cached_prop.__get__(none_instance, cached_prop)

    # Call __get__ with the descriptor as both instance and owner
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_with_set_instance_and_self_as_owner():
    """Test that cached_property.__get__ can be invoked with a set instance as the object and the cached_property itself as the owner."""
    # Create an empty set to serve as the instance passed to __get__
    empty_set = set()

    # Wrap the empty set in a cached_property descriptor
    cached_prop = decorators.cached_property(empty_set)

    # Invoke __get__ with the set as the object and the cached_property as the owner
    cached_prop.__get__(empty_set, cached_prop)

def test_cached_property_accepts_empty_set():
    """Test that cached_property can be instantiated with an empty set as its argument."""
    # Provide an empty set as the wrapped value for cached_property
    empty_set = set()

    # Instantiate cached_property with the empty set; should not raise
    cached_prop = decorators.cached_property(empty_set)

