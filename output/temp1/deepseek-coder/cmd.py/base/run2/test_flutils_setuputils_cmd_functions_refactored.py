import cmd as pytest_cmd

import pytest_cmd

def test_build_setup_cfg_command_class():
    no_input = None
    test_class_instance = pytest_cmd.build_setup_cfg_command_class(no_input)
    assert isinstance(test_class_instance, pytest_cmd.SetupCfgCommand)

