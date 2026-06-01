import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance():
    """Test that cached_property.__get__ can be called with None as the instance,
    both when the owner is the property itself and when a non-None owner is used."""
    none_value = None

    # Create a cached_property wrapping None as the underlying function
    prop = decorators.cached_property(none_value)

    # Call __get__ with None as the instance; owner is the property itself
    var_0 = prop.__get__(none_value, prop)

    # Call __get__ with the property as both the instance and the owner
    prop.__get__(prop, prop)

def test_cached_property_get_with_set_as_owner():
    """Test that cached_property.__get__ can be called with a set instance
    and the cached_property itself as the owner/type argument."""

    # Use an empty set as the instance on which the property is accessed
    instance = set()

    # Wrap the set in a cached_property descriptor
    prop = decorators.cached_property(instance)

    # Invoke __get__ with the instance and the property itself as the owner
    prop.__get__(instance, prop)

def test_cached_property_initialized_with_empty_set():
    """Test that cached_property can be instantiated with an empty set as the wrapped value."""
    wrapped_value = set()
    cached_prop = decorators.cached_property(wrapped_value)

