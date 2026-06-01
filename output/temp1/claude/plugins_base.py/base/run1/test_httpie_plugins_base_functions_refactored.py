import pytest
import httpie.plugins.base as base_plugins

def test_formatter_plugin_default_instantiation():
    """Test that FormatterPlugin can be instantiated with default arguments."""
    # Verify that the base FormatterPlugin class can be constructed without error
    base_plugins.FormatterPlugin()

def test_auth_plugin_get_auth_with_password_only():
    """Test that AuthPlugin.get_auth can be called with only a password argument (no username)."""
    # Use a non-trivial password string to exercise the default get_auth implementation
    password = "xzOB\n\n.wP|P-l"

    auth_plugin = base_plugins.AuthPlugin()

    # Invoke get_auth with only the password keyword argument; username is omitted
    auth_plugin.get_auth(password=password)

def test_transport_plugin_get_adapter_returns_default():
    """Test that TransportPlugin.get_adapter() can be called and returns without error by default."""
    transport_plugin = base_plugins.TransportPlugin()
    transport_plugin.get_adapter()

def test_converter_plugin_instantiation_and_transport_plugin_default_adapter():
    """
    Verify that ConverterPlugin can be instantiated with raw bytes and that
    TransportPlugin can be instantiated and its default adapter retrieved
    without raising any exceptions.
    """
    # Raw bytes used as input to the ConverterPlugin constructor
    raw_bytes = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"

    # Instantiate a ConverterPlugin with arbitrary byte data
    converter_plugin = base_plugins.ConverterPlugin(raw_bytes)

    # Instantiate a TransportPlugin and retrieve its default adapter
    transport_plugin = base_plugins.TransportPlugin()
    transport_plugin.get_adapter()

def test_converter_plugin_convert_with_none_input():
    """Test that ConverterPlugin can be instantiated and invoked with None as both the constructor argument and convert input."""

    # Initialize the plugin with no underlying converter
    none_value = None
    converter_plugin = base_plugins.ConverterPlugin(none_value)

    # Invoke convert with None to verify it handles null input without error
    converter_plugin.convert(none_value)

