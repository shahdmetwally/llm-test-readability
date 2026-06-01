import pytest
import httpie.plugins.base as base_plugin

def test_formatter_plugin_can_be_instantiated():
    """Verify that FormatterPlugin can be instantiated without raising any errors."""
    # Instantiate FormatterPlugin to ensure no exception is raised during construction
    base_plugin.FormatterPlugin()

def test_auth_plugin_get_auth_accepts_password_kwarg():
    """Verify that AuthPlugin.get_auth can be called with a password keyword argument without raising."""
    # Use a non-trivial string including whitespace and special characters as the password
    password_value = "xzOB\n\n.wP|P-l"

    # Instantiate the base AuthPlugin directly
    auth_plugin = base_plugin.AuthPlugin()

    # Call get_auth with only the password keyword argument
    auth_plugin.get_auth(password=password_value)

def test_transport_plugin_get_adapter_does_not_raise():
    """Verify that TransportPlugin can be instantiated and get_adapter() runs without error."""

    # Instantiate the base TransportPlugin
    transport_plugin = base_plugin.TransportPlugin()

    # Call get_adapter() to confirm it executes without raising an exception
    transport_plugin.get_adapter()

def test_converter_plugin_init_with_bytes_and_transport_plugin_get_adapter_do_not_raise():
    """Verify that ConverterPlugin accepts bytes on init and TransportPlugin.get_adapter() runs without error."""

    # Arbitrary raw bytes used to initialise the ConverterPlugin
    raw_bytes_input = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"

    # Instantiate ConverterPlugin with bytes — should not raise
    converter_plugin = base_plugin.ConverterPlugin(raw_bytes_input)

    # Instantiate TransportPlugin and invoke get_adapter() — should not raise
    transport_plugin = base_plugin.TransportPlugin()
    transport_plugin.get_adapter()

def test_converter_plugin_accepts_none_argument_and_converts_none():
    """Test that ConverterPlugin can be instantiated with None and convert None without error."""
    # Use None as both the constructor argument and the value to convert
    none_value = None

    # Instantiate the plugin with a None argument
    converter_plugin = base_plugin.ConverterPlugin(none_value)

    # Verify that calling convert with None does not raise an exception
    converter_plugin.convert(none_value)

