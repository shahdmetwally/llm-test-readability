import pytest
import codetiming.timer as timer
import colander as helpers

def test_CodetimingTimerModule_to_namedtuple():
    """Test `codetiming.Timer` .to_namedtuple() conversion method."""

    # Arrange
    arbitrary_float = -476.66
    
    # Act
    timer.to_namedtuple(arbitrary_float)

    # No assertion needed since .to_namedtuple() method does not return anything

def test_instantiating_namedtuple_from_tuple_of_floats_and_set():
    """Test instantiating namedtuple from a tuple containing a float and a set"""
    float_value = -67.0
    float_set = {float_value, float_value, float_value, float_value}
    tuple_input = (float_value, float_set)
    namedtuple = timer.to_namedtuple(tuple_input)
    assert isinstance(namedtuple, tuple)  # verify the return type as a tuple
    assert len(namedtuple) == 2, "Namedtuple length is expected to be 2"
    assert namedtuple[0] == float_value, "First element of namedtuple is expected to be the float value"
    assert namedtuple[1] == float_set, "Second element of namedtuple is expected to be the set"

    # Second assertion for function to_namedtuple
    with pytest.raises(helpers.Invalid):
        timer.to_namedtuple(float_set)

# rest of the tests ....