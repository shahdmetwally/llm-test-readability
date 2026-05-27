import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_and_owner():
    """
    Test that cached_property.__get__ behaves correctly when called with
    None as the instance argument, both with None and with the descriptor
    itself as the owner argument.
    """
    none_value = None

    # Create a cached_property descriptor wrapping None as the function
    prop = decorators.cached_property(none_value)

    # Call __get__ with None as instance and the descriptor as owner;
    # this typically returns the descriptor itself when instance is None
    result = prop.__get__(none_value, prop)

    # Call __get__ again with the descriptor as both instance and owner
    prop.__get__(prop, prop)

def test_cached_property_get_with_set_as_owner():
    """Test that cached_property.__get__ can be called with a set instance
    and the cached_property itself as the owner type."""
    # Use an empty set as both the instance and the owner argument
    instance = set()
    prop = decorators.cached_property(instance)

    # Invoke __get__ to trigger the descriptor protocol
    prop.__get__(instance, prop)

def test_cached_property_initialized_with_empty_set():
    """Test that cached_property can be instantiated with an empty set as the wrapped value."""
    empty_set = set()
    cached_prop = decorators.cached_property(empty_set)

