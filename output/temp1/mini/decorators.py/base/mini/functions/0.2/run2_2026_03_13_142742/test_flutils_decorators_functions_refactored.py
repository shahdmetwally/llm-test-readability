import pytest

import decorators as decorators_module

def test_cached_property_get_with_none_instance_and_descriptor_owner():
    """Smoke test: call cached_property.__get__ with a None instance and with the
    descriptor itself as the owner to exercise descriptor lookup paths.
    """
    # Use None as the instance (mirrors original test)
    instance = None

    # Create a cached_property object using the aliased module import
    cached_prop = decorators_module.cached_property(instance)

    # Invoke __get__ with (instance=None, owner=cached_prop) and keep the result
    result = cached_prop.__get__(instance, cached_prop)

    # Invoke __get__ again with the descriptor object as both instance and owner
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_descriptor_get_with_arbitrary_object():
    """Verify that the cached_property descriptor can be created and its __get__ invoked on an arbitrary object."""
    # Use a plain set as the value passed into the decorator (keeps original behavior)
    instance = set()
    # Create the descriptor by calling the cached_property decorator with the instance
    descriptor = decorators_module.cached_property(instance)
    # Call the descriptor's __get__ with the instance and the descriptor itself as the 'owner' argument
    descriptor.__get__(instance, descriptor)

def test_cached_property_constructs_from_empty_set():
    """Verify that creating a cached_property from an empty set does not raise."""
    # Prepare an empty set to use as the wrapped value
    empty_value = set()
    # Construct the cached_property using the decorators module alias
    cached_property_obj = decorators_module.cached_property(empty_value)

