import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_and_owner():
    """
    Test that cached_property.__get__ behaves correctly when called with
    None as the instance, using the property itself as the owner.
    This exercises the descriptor protocol edge case where no instance is bound.
    """
    none_value = None

    # Create a cached_property wrapping None as the underlying function
    prop = decorators.cached_property(none_value)

    # Call __get__ with None instance and the property as owner (returns the descriptor itself)
    var_0 = prop.__get__(none_value, prop)

    # Call __get__ with the property as both instance and owner
    prop.__get__(prop, prop)

def test_cached_property_get_with_set_instance_and_prop_as_owner():
    """Test that cached_property.__get__ can be called with a set instance
    and the cached_property itself as the owner type."""
    # Use an empty set as both the instance and the owner argument
    instance = set()
    prop = decorators.cached_property(instance)

    # Invoke the descriptor protocol: __get__(instance, owner)
    prop.__get__(instance, prop)

def test_cached_property_initialized_with_empty_set():
    """Test that cached_property can be instantiated with an empty set as the wrapped value."""
    empty_set = set()
    cached_prop = decorators.cached_property(empty_set)

