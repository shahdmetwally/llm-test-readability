import pytest
import httpie.plugins.base as base_plugin

def test_formatter_plugin_can_be_instantiated():
    """Verify that FormatterPlugin can be instantiated with no arguments without raising an error."""
    # Instantiate FormatterPlugin using its default constructor to confirm it requires no mandatory arguments
    base_plugin.FormatterPlugin()

def test_auth_plugin_get_auth_with_password_only_does_not_raise():
    """Verify that AuthPlugin.get_auth() can be called with only a password argument without raising an error."""
    # A deliberately unusual password string, including newlines and special characters
    password_value = "xzOB\n\n.wP|P-l"

    # Instantiate the base AuthPlugin directly to test its default behaviour
    auth_plugin = base_plugin.AuthPlugin()

    # Call get_auth with only a password; no exception should be raised
    auth_plugin.get_auth(password=password_value)

def test_transport_plugin_get_adapter_does_not_raise():
    """Verify that TransportPlugin can be instantiated and get_adapter() runs without error."""
    # Instantiate the base TransportPlugin
    transport_plugin = base_plugin.TransportPlugin()

    # Call get_adapter() to confirm it completes without raising an exception
    transport_plugin.get_adapter()

def test_converter_plugin_accepts_bytes_and_transport_plugin_get_adapter():
    """Verify that ConverterPlugin accepts bytes on init and TransportPlugin.get_adapter() can be called without error."""

    # Arbitrary raw bytes used as input to ConverterPlugin constructor
    raw_bytes_data = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"

    # Instantiate ConverterPlugin with raw bytes — should not raise
    converter_plugin = base_plugin.ConverterPlugin(raw_bytes_data)

    # Instantiate TransportPlugin with no arguments — should not raise
    transport_plugin = base_plugin.TransportPlugin()

    # Call get_adapter() on the transport plugin — should not raise (smoke test: no exception == pass)
    transport_plugin.get_adapter()

def test_converter_plugin_instantiation_and_convert_with_none():
    """Test that ConverterPlugin can be instantiated with None and convert(None) can be called without error."""
    # Use None as the initialisation argument, matching the original test input
    none_value = None

    # Instantiate ConverterPlugin with None to verify it accepts a None argument
    converter_plugin_instance = base_plugin.ConverterPlugin(none_value)

    # Call convert with None to verify the method handles a None input without raising
    converter_plugin_instance.convert(none_value)

