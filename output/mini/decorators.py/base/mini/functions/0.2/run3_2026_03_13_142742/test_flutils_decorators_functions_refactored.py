import pytest

import decorators as decorators_module

def test_cached_property_descriptor_get_handles_none_and_descriptor():
    """Verify cached_property.__get__ accepts None as the instance (class-level access)
    and can be invoked with the descriptor object as both instance and owner.
    """
    # Simulate attribute access on the class (no instance)
    instance = None
    descriptor = decorators_module.cached_property(instance)

    # Call __get__ as if accessed via the class: (obj=None, owner=descriptor)
    result = descriptor.__get__(instance, descriptor)

    # Also call __get__ with the descriptor as both the instance and the owner,
    # preserving the original call pattern (no assertion; just ensure call succeeds)
    descriptor.__get__(descriptor, descriptor)

def test_cached_property_descriptor_get_with_set_instance():
    """Call the cached_property descriptor's __get__ using a set instance.

    This mirrors invoking the decorator-produced descriptor's __get__ with
    the instance and (unusually) the descriptor object as the 'owner'
    argument to ensure the call succeeds without changing behavior.
    """
    # Use a plain set instance as the object passed to the decorator/descriptor.
    instance = set()

    # Create the descriptor by calling the cached_property attribute from the
    # decorators module with the instance (keeps the original call behavior).
    descriptor = decorators_module.cached_property(instance)

    # Invoke the descriptor's __get__ exactly as in the original test:
    # pass the instance and the descriptor itself as the 'owner'.
    descriptor.__get__(instance, descriptor)

def test_cached_property_accepts_set_argument():
    """Call decorators.cached_property with a set instance to ensure it accepts that argument."""
    empty_set = set()  # an empty set used as the input value
    cached_property_result = decorators_module.cached_property(empty_set)

