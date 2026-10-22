import pytest

import decorators as decorators_module

def test_cached_property_descriptor_get_called_with_none_then_descriptor():
    """Call the cached_property descriptor's __get__ first with None, then with the descriptor itself."""
    # Preserve the original literal input (None) used to create the descriptor.
    none_value = None

    # Create the cached_property descriptor from the decorators module.
    descriptor = decorators_module.cached_property(none_value)

    # First call: __get__(None, descriptor)
    result = descriptor.__get__(none_value, descriptor)

    # Second call: __get__(descriptor, descriptor)
    descriptor.__get__(descriptor, descriptor)

def test_cached_property_descriptor_get_called_with_instance_and_owner():
    """Verify that cached_property returns a descriptor whose __get__ can be invoked with an instance and an owner."""
    # Create an object to act as the instance argument for the descriptor.
    instance = set()

    # Obtain the cached_property descriptor by calling the factory with the instance.
    descriptor = decorators_module.cached_property(instance)

    # Invoke the descriptor's __get__ with the same instance and the descriptor as the owner.
    # This mirrors the original call pattern and ensures no exceptions occur during invocation.
    descriptor.__get__(instance, descriptor)

def test_cached_property_initializes_with_set():
    """Ensure decorators.cached_property can be initialized with an empty set without raising."""
    # Create an empty set to use as the argument for cached_property
    empty_set = set()

    # Call the cached_property factory/function with the empty set.
    # This preserves the original behaviour (no assertions); the test ensures
    # that initialization completes without raising an exception.
    cached_property_result = decorators_module.cached_property(empty_set)

