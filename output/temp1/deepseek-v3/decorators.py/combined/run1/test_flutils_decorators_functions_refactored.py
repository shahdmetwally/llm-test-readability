import pytest
import decorators as module_0

def test_cached_property_get_with_none_instance():
    """Test that cached_property.__get__ handles None instance gracefully."""
    none_instance = None
    cached_prop = module_0.cached_property(none_instance)

    # First call: __get__ with None instance and valid owner
    result = cached_prop.__get__(none_instance, cached_prop)

    # Second call: __get__ with cached_prop as both instance and owner
    # This tests a different code path where instance is not None
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_with_set_instance():
    """Verify that cached_property's __get__ method works when called with a set instance."""
    sample_set = set()
    cached_prop = module_0.cached_property(sample_set)
    # Call __get__ with the set instance as the object and cached_prop as the type
    cached_prop.__get__(sample_set, cached_prop)

def test_cached_property_initialized_with_empty_set():
    """Verify that cached_property can be instantiated with an empty set."""
    empty_set = set()
    cached_property_instance = module_0.cached_property(empty_set)

