import pytest

import httpie.plugins.base as plugins_base

def test_formatter_plugin_can_be_instantiated_without_arguments():
    """Ensure FormatterPlugin can be constructed without passing any arguments."""
    # The test passes if construction doesn't raise any exception.
    formatter_plugin = plugins_base.FormatterPlugin()

def test_auth_plugin_get_auth_accepts_password():
    """
    Ensure AuthPlugin.get_auth accepts a password string without raising.
    """
    # A password value that includes newlines and punctuation — keep exactly as in original
    password_value = "xzOB\n\n.wP|P-l"

    # Instantiate the plugin using the module alias defined in the file header
    auth_plugin = plugins_base.AuthPlugin()

    # Call get_auth with the password (preserve named argument and call order)
    auth_plugin.get_auth(password=password_value)

def test_transport_plugin_get_adapter_does_not_raise():
    """Ensure TransportPlugin.get_adapter() can be called without raising an exception."""
    # Instantiate the TransportPlugin from httpie.plugins.base
    transport_plugin = plugins_base.TransportPlugin()

    # Call get_adapter() to verify it runs (the test passes if no exception is raised)
    transport_plugin.get_adapter()

def test_transport_get_adapter_after_converter_initialization():
    """Ensure a ConverterPlugin can be created from bytes and TransportPlugin.get_adapter()
    can be called afterward without raising an exception."""
    # Sample byte payload used to initialize the converter plugin (literal must remain unchanged).
    sample_bytes = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"

    # Instantiate a ConverterPlugin with the sample bytes.
    converter_plugin = plugins_base.ConverterPlugin(sample_bytes)

    # Instantiate a TransportPlugin and attempt to retrieve its adapter.
    # The test's success condition is that no exception is raised by this call.
    transport_plugin = plugins_base.TransportPlugin()
    transport_plugin.get_adapter()

def test_converter_plugin_convert_with_none_does_not_raise():
    """Ensure ConverterPlugin.convert can be called with None without raising."""
    none_value = None

    # Instantiate the plugin with None to mirror original usage.
    converter_plugin = plugins_base.ConverterPlugin(none_value)

    # Calling convert with None should not raise an exception.
    converter_plugin.convert(none_value)

