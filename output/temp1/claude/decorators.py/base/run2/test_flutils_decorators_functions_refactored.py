import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_and_owner():
    """
    Test that cached_property.__get__ can be called with None as the instance,
    using the cached_property itself as the owner. Verifies that __get__ handles
    None instance gracefully and can also be called with the descriptor as both
    instance and owner.
    """
    none_value = None

    # Create a cached_property descriptor wrapping None as the underlying function
    prop = decorators.cached_property(none_value)

    # Call __get__ with None as instance and the descriptor as owner;
    # this typically returns the descriptor itself when instance is None
    result = prop.__get__(none_value, prop)

    # Call __get__ with the descriptor as both instance and owner
    prop.__get__(prop, prop)

def test_cached_property_get_with_set_as_owner():
    """Test that cached_property.__get__ can be called with a set instance
    as both the object and the owner/type argument."""
    # Use a plain set as the instance to trigger __get__ on the descriptor
    instance = set()

    # Create a cached_property descriptor wrapping the set instance
    descriptor = decorators.cached_property(instance)

    # Invoke __get__ passing the set as both the object and the owner
    descriptor.__get__(instance, descriptor)

def test_cached_property_initialized_with_empty_set():
    """Test that cached_property can be instantiated with an empty set as the wrapped value."""
    # Use an empty set as the wrapped value for cached_property
    empty_set = set()
    cached_prop = decorators.cached_property(empty_set)

