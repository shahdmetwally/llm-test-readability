import pytest
import decorators as decorators_module

def test_cached_property_get_behavior_with_none_and_self_reference():
    """Test that cached_property.__get__() handles None and self-reference arguments correctly."""
    none_instance = None
    cached_prop = decorators_module.cached_property(none_instance)
    
    # Test __get__ with None as instance and the property as owner
    result = cached_prop.__get__(none_instance, cached_prop)
    
    # Test __get__ where both instance and owner are the cached_property itself
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_get_accepts_empty_set_instance():
    """
    Verify that cached_property.__get__ can handle an
    empty set as the instance parameter without error.
    """
    empty_set_instance = set()
    cached_property_descriptor = decorators_module.cached_property(empty_set_instance)
    cached_property_descriptor.__get__(empty_set_instance, cached_property_descriptor)

def test_cached_property_wraps_empty_set_as_callable_descriptor():
    """Test that cached_property can wrap an empty set as a callable descriptor."""
    empty_set = set()
    cached_property_result = decorators_module.cached_property(empty_set)