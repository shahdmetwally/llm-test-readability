import pytest
import httpie.plugins.base as plugins_base

def test_formatter_plugin_can_be_instantiated():
    """Test that a FormatterPlugin instance can be created without arguments."""
    # Ensure the FormatterPlugin class can be instantiated successfully
    plugins_base.FormatterPlugin()

