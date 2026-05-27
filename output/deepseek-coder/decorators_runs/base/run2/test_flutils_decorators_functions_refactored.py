import decorators as decorators

def test_cached_property_behavior():
    """
    This test case verifies the behavior of the cached_property decorator.
    It checks if the __get__ method of the decorator is called correctly.
    """
    # Given
    none_type = None
    decorator = decorators.cached_property(none_type)

    # When
    result_none = decorator.__get__(none_type, decorator)
    result_decorator = decorator.__get__(decorator, decorator)

    # Then
    assert result_none is none_type
    assert result_decorator is decorator

def test_cached_property_returns_correct_value():
    """
    This test case verifies that the cached_property function returns the correct value.
    """
    # Given
    empty_set = set()
    cached_property_instance = decorators.cached_property(empty_set)

    # When
    result = cached_property_instance.__get__(empty_set, cached_property_instance)

    # Then
    assert result == empty_set

def test_cached_property_initialization():
    """
    This test verifies that the cached_property function correctly initializes a cached property.
    """
    # Initialize an empty set
    empty_set = set()

    # Create a cached property using the empty set
    cached_property_result = decorators.cached_property(empty_set)

    # Assert that the cached property is not None
    assert cached_property_result is not None

