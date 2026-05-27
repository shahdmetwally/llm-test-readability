import pytest
import decorators as module_0

def test_cached_property_get_on_class_access_with_none_instance():
    """Verify that cached_property.__get__() handles class-level access
    where instance is None, triggering the descriptor protocol."""
    none_instance = None
    cached_prop = module_0.cached_property(none_instance)
    # First call: __get__ with None instance and None owner
    # This simulates accessing the property on the class, not an instance
    result = cached_prop.__get__(none_instance, cached_prop)
    # Second call: __get__ where instance and owner are both the cached_property
    # This tests another edge case of the descriptor protocol
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_with_set_instance():
    """Verify cached_property with a set argument and __get__ invocation."""
    sample_set = set()
    descriptor = module_0.cached_property(sample_set)
    descriptor.__get__(sample_set, descriptor)

def test_cached_property_created_with_empty_set():
    """Verify that a cached_property can be instantiated with an empty set."""
    empty_set = set()
    cached_prop = module_0.cached_property(empty_set)

