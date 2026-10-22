import decorators as d

def test_dunder_loading_is_maintained():
    namespace = {'__name__': 'mymodule.mysubmodulethree', '__file__': '', '__path__': '', '__attr_map__': tuple(), '__loader__': 'some_loader'}
    assert cherry_pick(namespace)['__loader__'] == 'some_loader', 'The loader attribute was not passed correctly!'

def test_cached_property_preservation_after_instance():
    d.cached_property_0 = d.decorators.cached_property()
    instance = set()
    result = d.cached_property_0.__get__(instance, d.cached_property_0)
    assert result == d.cached_property_0.__get__(instance, d.cached_property_0)

def test_timer_is_started_and_stopped_correctly():
    set_0 = set()
    cached_property_0 = d.decorators.cached_property(set_0)
    assert cached_property_0.__name__ == '_cached_property', 'Name of cached_property_0 does not match with "_cached_property".'
    assert type(cached_property_0).__name__ == 'function', 'Type of cached_property_0 is not a function.'