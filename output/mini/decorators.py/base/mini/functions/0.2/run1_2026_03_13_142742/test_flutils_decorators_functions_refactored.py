import pytest

import decorators as decorators_module

def test_cached_property_get_handles_none_and_self():
    """Verify cached_property.__get__ can be invoked with None and with itself."""
    # Use None as the "instance" to mirror the original test scenario.
    instance = None

    # Create the cached_property object using the decorators module.
    cached_prop = decorators_module.cached_property(instance)

    # Call __get__ with (instance=None, owner=cached_prop).
    result = cached_prop.__get__(instance, cached_prop)

    # Call __get__ again where both instance and owner are the cached_prop object.
    cached_prop.__get__(cached_prop, cached_prop)

def test_cached_property_descriptor_get_call():
    """Call cached_property.__get__ with an object and the descriptor itself as the owner arg."""
    # Use a plain set instance as the object passed to the descriptor.
    owner_obj = set()
    # Create the cached_property descriptor (preserve original call pattern).
    cached_prop = decorators_module.cached_property(owner_obj)
    # Invoke the descriptor's __get__ exactly as in the original test.
    cached_prop.__get__(owner_obj, cached_prop)

def test_cached_property_accepts_set_and_returns_wrapper():
    """Verify that calling cached_property with a set returns a result (preserve original behaviour)."""
    # Use an empty set as the original test did.
    sample_set = set()
    # Invoke the cached_property function from the decorators module (alias from updated imports).
    cached_property_result = decorators_module.cached_property(sample_set)
    assert cached_property_result is not None

