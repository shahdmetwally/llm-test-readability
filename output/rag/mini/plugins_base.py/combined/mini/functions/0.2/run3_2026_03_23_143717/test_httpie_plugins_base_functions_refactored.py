import pytest

import httpie.plugins.base as httpie_plugins_base

def test_formatter_plugin_can_be_instantiated():
    """Ensure FormatterPlugin can be instantiated with no arguments."""
    # Instantiating should not raise an exception.
    httpie_plugins_base.FormatterPlugin()

def test_auth_plugin_get_auth_accepts_password():
    """Ensure AuthPlugin.get_auth accepts a password argument without raising an exception."""
    # Create an AuthPlugin instance.
    auth_plugin = httpie_plugins_base.AuthPlugin()
    # Use the exact password literal from the original test (preserve semantics).
    password = "xzOB\n\n.wP|P-l"
    # Call get_auth with the password; test passes if no exception is raised.
    auth_plugin.get_auth(password=password)

def test_transport_plugin_get_adapter_can_be_called():
    """Smoke test: instantiate TransportPlugin and call get_adapter() without raising."""
    transport_plugin = httpie_plugins_base.TransportPlugin()
    transport_plugin.get_adapter()

def test_transport_plugin_get_adapter_calls_successfully():
    """Ensure TransportPlugin.get_adapter() can be invoked after creating a ConverterPlugin with sample bytes."""
    # Sample bytes payload (kept identical to original test)
    sample_bytes = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"

    # Create a ConverterPlugin with the sample bytes
    converter_plugin = httpie_plugins_base.ConverterPlugin(sample_bytes)

    # Instantiate the TransportPlugin and call get_adapter()
    transport_plugin = httpie_plugins_base.TransportPlugin()
    # The original test only invokes get_adapter() — preserve that behaviour (no assertions).
    transport_plugin.get_adapter()

def test_converter_plugin_convert_accepts_none():
    """Ensure ConverterPlugin can be instantiated and invoked with None without error."""
    # Use the None literal exactly as in the original test.
    none_value = None

    # Instantiate the ConverterPlugin with None (preserve original constructor call).
    converter_plugin = httpie_plugins_base.ConverterPlugin(none_value)

    # Invoke convert with None (preserve original method call and argument).
    converter_plugin.convert(none_value)

