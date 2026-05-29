import pytest

import decorators as decorators_module

def test_cached_property___get__handles_none_owner():
    """Ensure cached_property.__get__ can be invoked with owner=None and with the descriptor itself."""
    # Use None as the "owner" (matches the original test scenario)
    owner = None

    # Instantiate the cached_property descriptor using None as the wrapped callable
    cached_prop = decorators_module.cached_property(owner)

    # Call the descriptor protocol __get__ with (None, descriptor) — preserves original call and order
    result = cached_prop.__get__(owner, cached_prop)

    # Call __get__ with the descriptor itself as both instance and owner — mirrors the original final call
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_descriptor_get_invocation_for_set_instance():
    """Call the cached_property descriptor's __get__ using a set instance."""
    # Create a simple set instance (same as the original test's set_0).
    sample_set = set()

    # Obtain the cached_property descriptor by calling the factory with the instance.
    # This mirrors the original cached_property_0 = module_0.cached_property(set_0)
    cached_prop_descriptor = decorators_module.cached_property(sample_set)

    # Invoke the descriptor's __get__ exactly as in the original test to preserve behavior.
    # Note: the original passed the descriptor itself as the 'owner' argument; we keep that.
    cached_prop_descriptor.__get__(sample_set, cached_prop_descriptor)

def test_cached_property_initializes_with_empty_set():
    """Verify that cached_property can be initialized using an empty set without raising."""
    # Create an empty set to use as the argument (same literal as in the original test).
    empty_set = set()

    # Call the cached_property factory with the empty set. This mirrors the original
    # call to module_0.cached_property(set_0) but uses the provided alias.
    cached_property_descriptor = decorators_module.cached_property(empty_set)
    assert cached_property_descriptor is not None

