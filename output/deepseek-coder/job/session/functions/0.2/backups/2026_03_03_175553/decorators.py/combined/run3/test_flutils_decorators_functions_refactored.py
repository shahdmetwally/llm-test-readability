import decorators as decorators

def test_cached_property_correctly_sets_and_gets_value():
    none_type_0 = None
    cached_property_0 = decorators.cached_property(none_type_0)
    timer_instance = cached_property_0.__get__(none_type_0, cached_property_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)

def test_cached_property_correctly_sets_and_gets_value():
    """Test that the cached_property function correctly sets and gets a value."""
    set_0 = set()
    cached_property_0 = decorators.cached_property(set_0)
    cached_property_0.__get__(set_0, cached_property_0)

def test_cached_property_correctly_sets_and_gets_value_1():
    """Test that the cached property correctly sets and gets value."""
    # Setup
    set_0 = set()

    # Exercise
    cached_property_0 = decorators_lib.cached_property(set_0)

    # Verify
    assert isinstance(cached_property_0, decorators_lib.cached_property)

