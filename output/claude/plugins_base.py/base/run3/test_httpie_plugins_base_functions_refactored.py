import pytest
import httpie.plugins.base as base_plugin

def test_formatter_plugin_default_instantiation():
    """Test that FormatterPlugin can be instantiated with default arguments."""
    # Verify that the base FormatterPlugin class can be constructed without errors
    base_plugin.FormatterPlugin()

def test_auth_plugin_get_auth_with_password_only():
    """Test that AuthPlugin.get_auth can be called with only a password argument (no username)."""
    # Use a non-trivial string to ensure the method handles arbitrary password values
    password_value = "xzOB\n\n.wP|P-l"

    auth_plugin = base_plugin.AuthPlugin()

    # Invoke get_auth with only the password keyword argument
    auth_plugin.get_auth(password=password_value)

def test_transport_plugin_get_adapter_returns_default():
    """Test that TransportPlugin.get_adapter() can be called on a default instance without error."""
    transport_plugin = base_plugin.TransportPlugin()
    transport_plugin.get_adapter()

def test_converter_plugin_init_and_transport_plugin_get_adapter():
    """
    Verify that ConverterPlugin can be instantiated with raw bytes,
    and that TransportPlugin can be instantiated and its get_adapter()
    method can be called without raising an error.
    """
    # Raw bytes used to initialise the converter plugin
    raw_bytes = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"

    # Instantiate a ConverterPlugin with the raw bytes payload
    converter_plugin = base_plugin.ConverterPlugin(raw_bytes)

    # Instantiate a TransportPlugin and invoke get_adapter()
    transport_plugin = base_plugin.TransportPlugin()
    transport_plugin.get_adapter()

def test_converter_plugin_convert_with_none_input():
    """Test that ConverterPlugin.convert can be called with None as both the
    plugin argument and the value to convert, without raising an error."""

    # Instantiate ConverterPlugin with None as the initialisation argument
    none_value = None
    converter_plugin = base_plugin.ConverterPlugin(none_value)

    # Invoke convert with None to verify it handles a null input gracefully
    converter_plugin.convert(none_value)

