import pytest
import pyutils.moduleutils.maybe as m
import typing as t

class TestSomething:
    def test_maybe_instance_can_be_created_correctly(self):
        assert m.Maybe(1) == m.Maybe(1)
        assert m.Nothing() == m.Nothing()

    def test_comparison_of_maybe_instance_and_string(self):
        assert m.Just(1) != "1"
        assert m.Nothing() == None

    def test_maybe_monad_equality(self):
        assert m.Maybe(1).is_just() == True
        assert m.Maybe().is_nothing() == True

    def test_maybe_bind_with_boolean_argument_1(self):
        assert m.Maybe(1).bind(lambda _: 'true') == 'true'

    def test_timer_starts_and_stops_unique(self):
        assert timer.start_timer() != timer.start_timer()
        assert timer.stop_timer() != timer.stop_timer()

    def test_maybe_monad_behavior(self):
        assert m.Maybe(1).map(lambda x: x + 1) == m.Just(2)
        assert m.Maybe().map(lambda x: x + 1) == m.Nothing()

    def test_timer_starts_and_stops_functionality(self):
        timer.start_timer()
        assert timer.is_timer_running() == True
        timer.stop_timer()
        assert timer.is_timer_running() == False

    def test_Maybe_filter_lazy_map(self):
        assert m.Maybe(1).filter(lambda _: True) == m.Just(1)

