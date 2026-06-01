import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_and_owner():
    """
    Test that cached_property.__get__ behaves correctly when called with
    None as the instance argument, both with None and with the descriptor
    itself as the owner.
    """
    none_value = None

    # Create a cached_property descriptor wrapping None as the function
    prop = decorators.cached_property(none_value)

    # Call __get__ with None as instance and the descriptor as owner;
    # when instance is None, __get__ should return the descriptor itself
    result = prop.__get__(none_value, prop)

    # Call __get__ again with the descriptor as both instance and owner
    prop.__get__(prop, prop)

def test_cached_property_get_with_set_as_owner():
    """Test that cached_property.__get__ can be called with a set instance
    as both the instance and the owner/type argument."""
    # Create an empty set to use as the instance
    empty_set = set()

    # Wrap the set in a cached_property descriptor
    prop = decorators.cached_property(empty_set)

    # Invoke __get__ with the set as both instance and owner
    prop.__get__(empty_set, prop)

def test_cached_property_initialized_with_empty_set():
    """Test that cached_property can be instantiated with an empty set as the wrapped value."""
    empty_set = set()
    # Create a cached_property instance wrapping an empty set
    cached_prop = decorators.cached_property(empty_set)

