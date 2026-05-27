import typing as module_1
import maybe as module_2

def test_maybe_creation_with_bytes():
    import module_2
    bytes_value = b"\xf4\xaf\xe2\xc9\xee\xc8\xd67n\x9eK\x0b\x97Y\xb5"

    # Create a Maybe with bytes.
    maybe_with_bytes = module_2.Maybe(bytes_value, bytes_value)

    # Assert the values of both values.
    assert maybe_with_bytes.yes == bytes_value
    assert maybe_with_bytes.no == bytes_value

def test_maybe_creation_with_none():
    """Test the creation of Maybe instance with None."""
    # Assume that Maybe.value and None are the same.
    none_value = None
    expected_value = module_1.Maybe(none_value, none_value)

    none_type = None
    maybe = module_2.Maybe(none_type, none_type)

    assert maybe == expected_value

def test_maybe_monad_laws():
    # Given
    str_0 = "p4xa>bl^oP"
    maybe_0 = module_2.Just(str_0)

    # When
    bool_0 = maybe_0 == module_2.Just(str_0)
    var_0 = maybe_0.apply(str_0)
    var_1 = maybe_0.get_or_else(str_0)
    var_2 = maybe_0.map(var_0)
    var_3 = maybe_0.filter(var_0)
    var_4 = maybe_0.map(var_0)
    var_5 = maybe_0.apply(str_0)
    bool_1 = var_0 == var_5
    var_6 = var_0.filter(var_1)
    var_7 = var_5.get_or_else(str_0)
    maybe_1 = module_2.Just(str_0)

    # Then
    assert bool_0 == True
    assert var_0 == str_0
    assert var_1 == str_0
    assert var_2 == module_2.Just(str_0)
    assert var_3 == maybe_0
    assert var_4 == module_2.Just(str_0)
    assert var_5 == module_2.Just(str_0)
    assert bool_1 == True
    assert var_6 == module_2.Just(str_0)
    assert var_7 == str_0
    assert var_8 == module_2.Just(str_0)
    assert var_9 == module_2.Just(str_0)
    assert var_10 == module_2.Just(str_0)