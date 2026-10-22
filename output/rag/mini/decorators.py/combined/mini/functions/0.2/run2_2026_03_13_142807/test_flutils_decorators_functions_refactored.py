import pytest

import decorators as decorators_module

def test_cached_property_descriptor_get_with_none_owner():
    """Ensure the cached_property descriptor's __get__ works when called with None and with the descriptor itself."""
    # Use None as the "owner" value, matching the original test input.
    owner_none = None

    # Create the descriptor by calling the cached_property factory from the module under test.
    cached_prop = decorators_module.cached_property(owner_none)

    # Invoke the descriptor's __get__ with (owner=None, type_or_owner=descriptor).
    # This call is preserved exactly from the original test to ensure identical behavior.
    result = cached_prop.__get__(owner_none, cached_prop)

    # Invoke the descriptor's __get__ again with (owner=descriptor, type_or_owner=descriptor),
    # preserving the original call sequence and arguments.
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_descriptor_get_with_set_instance():
    """Ensure cached_property descriptor's __get__ can be invoked with a set instance."""
    # Create a set instance to act as the descriptor's instance/owner parameter.
    target_set = set()

    # Call the cached_property factory with the set instance to obtain the descriptor/object.
    cached_prop_descriptor = decorators_module.cached_property(target_set)

    # Invoke the descriptor's __get__ with the original set and the descriptor itself
    # (preserving the original call pattern and order).
    cached_prop_descriptor.__get__(target_set, cached_prop_descriptor)

def test_cached_property_accepts_empty_set_and_returns_decorator():
    """Verify that cached_property can be constructed when given an empty set."""
    # Create an empty set to pass to the cached_property factory
    empty_attributes = set()
    # Call the cached_property factory with the empty set; preserve original semantics
    cached_property_decorator = decorators_module.cached_property(empty_attributes)

