import pytest

import cmd as cmd_module

def test_build_setup_cfg_command_class_with_none():
    """Ensure build_setup_cfg_command_class accepts a None setup config."""
    setup_cfg = None  # simulate absence of a setup config; function should accept None without raising
    cmd_module.build_setup_cfg_command_class(setup_cfg)

