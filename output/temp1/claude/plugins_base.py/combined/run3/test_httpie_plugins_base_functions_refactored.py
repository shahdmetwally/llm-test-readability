import pytest
import httpie.plugins.base as base_plugin

def test_formatter_plugin_can_be_instantiated():
    """Verify that FormatterPlugin can be instantiated with no arguments without raising an error."""
    # Instantiate the plugin using its default constructor; no exception should be raised
    base_plugin.FormatterPlugin()

def test_auth_plugin_get_auth_called_with_password():
    """Verify that AuthPlugin.get_auth can be invoked with a password keyword argument without raising."""
    # An arbitrary password string, including special characters and newlines
    password = "xzOB\n\n.wP|P-l"

    # Instantiate the base AuthPlugin directly to exercise its default get_auth behaviour
    auth_plugin = base_plugin.AuthPlugin()

    # Invoke get_auth with the password; no exception should be raised
    auth_plugin.get_auth(password=password)

def test_transport_plugin_get_adapter_does_not_raise():
    """Verify that TransportPlugin can be instantiated and get_adapter() runs without error."""
    # Instantiate the default TransportPlugin from the base plugin module
    transport_plugin = base_plugin.TransportPlugin()

    # Calling get_adapter() should complete without raising an exception
    transport_plugin.get_adapter()

def test_converter_plugin_accepts_bytes_and_transport_plugin_returns_adapter():
    """Verify ConverterPlugin accepts bytes on init and TransportPlugin.get_adapter() runs without error."""

    # Arbitrary raw bytes used as input to the ConverterPlugin constructor
    raw_bytes_input = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"

    # Instantiate ConverterPlugin with a bytes argument
    converter_plugin = base_plugin.ConverterPlugin(raw_bytes_input)

    # Instantiate TransportPlugin and invoke get_adapter() to confirm it runs without error
    transport_plugin = base_plugin.TransportPlugin()
    transport_plugin.get_adapter()

def test_converter_plugin_convert_with_none_does_not_raise():
    """Test that ConverterPlugin can be instantiated and convert() called with None without raising."""

    # Use None as the input to exercise null-handling in the plugin
    none_input = None

    # Instantiate the ConverterPlugin with a None argument
    converter_plugin = base_plugin.ConverterPlugin(none_input)

    # Invoke convert() with None to verify it does not raise
    converter_plugin.convert(none_input)

