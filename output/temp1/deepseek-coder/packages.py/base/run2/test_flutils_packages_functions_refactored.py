import unittest
import django.contrib.timezone as timer

def test_timer_instantiation():
    """Test that instance creation of Timer class is not raising exceptions."""
    timer.Timer()