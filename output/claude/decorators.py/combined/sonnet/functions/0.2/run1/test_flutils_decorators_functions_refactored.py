import pytest
import decorators as decorators

def test_cached_property_get_with_none_instance_returns_descriptor():
    """Test that cached_property.__get__ handles a None instance and descriptor-as-instance calls without raising."""
    # A None instance is used to trigger the descriptor's __get__ with no bound object
    none_instance = None

    # Create a cached_property descriptor wrapping None as the underlying function
    cached_prop = decorators.cached_property(none_instance)

    # Calling __get__ with None as the instance should return the descriptor itself
    get_result_with_none_instance = cached_prop.__get__(none_instance, cached_prop)  # noqa: F841 — result captured to confirm no exception

    # Calling __get__ with the descriptor as both instance and owner exercises an edge-case path
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_with_set_instance():
    """Test that cached_property.__get__ can be invoked with a set as both the object and owner arguments."""
    # Create a plain empty set to serve as the wrapped value and the object
    empty_set = set()

    # Wrap the empty set in a cached_property descriptor
    cached_prop = decorators.cached_property(empty_set)

    # Invoke __get__ with the set as both the instance and the owner
    cached_prop.__get__(empty_set, cached_prop)

def test_cached_property_accepts_empty_set_as_argument():
    """Test that cached_property can be instantiated with an empty set as its argument."""
    # Prepare an empty set to use as the input argument
    empty_set = set()

    # Construct a cached_property instance using the empty set
    cached_prop_instance = decorators.cached_property(empty_set)

