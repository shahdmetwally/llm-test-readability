import httpie.plugins.base as base_plugins

def test_plugin_manager_registers_multiple_plugins():
    # arrange
    plugin_manager_instance = plugins.PluginManager()
    plugin1 = plugins.Plugin1()
    plugin2 = plugins.Plugin2()

    # act
    plugin_manager_instance.register(plugin1, plugin2)

    # assert
    assert len(plugin_manager_instance) == 2
    assert plugin_manager_instance == [plugin1, plugin2]

def test_auth_plugin_generates_auth_correctly():
    """
    Test if AuthPlugin generates auth correctly.
    """
    password = "xzOB\n\n.wP|P-l"
    auth_plugin = AuthPlugin()

    assert auth_plugin.get_auth(password=password) == expected_auth_value

def test_get_transport_adapter():
    transport_plugin_0 = base_plugins.TransportPlugin()
    transport_plugin_0.get_adapter()

def test_plugin_creation():
    bytes = b"\xec\xdb\xe5\\V\xe1\xbb \xfd2\x80z\xf9\x96`-\xa1y"
    converter_plugin_module = base_plugins.ConverterPlugin(bytes)
    transport_plugin_module = base_plugins.TransportPlugin()
    transport_plugin_module.get_adapter()
    assert transport_plugin_module is not None

import pytest
from httpie.plugins import AuthPlugin
from httpie.plugins.registry import plugin_manager

def test_auth_get_mapping():
    plugins = [base_plugins.AuthPluginBasicAuth(), base_plugins.AuthPluginBasicAuth(), base_plugins.AuthPluginToken()]
    plugin_manager.register(*plugins)
    mapping = plugin_manager.get_auth_plugin_mapping()
    for plugin in plugins:
        assert mapping[plugin.auth_type] == plugin


def test_auth_get_plugin():
    plugin_basic_auth = base_plugins.AuthPluginBasicAuth()
    plugin_token = base_plugins.AuthPluginToken()
    plugin_manager.register(plugin_basic_auth, plugin_token)
    assert plugin_manager.get_auth_plugin(plugin_basic_auth.auth_type) is plugin_basic_auth
    assert plugin_manager.get_auth_plugin(plugin_token.auth_type) is plugin_token