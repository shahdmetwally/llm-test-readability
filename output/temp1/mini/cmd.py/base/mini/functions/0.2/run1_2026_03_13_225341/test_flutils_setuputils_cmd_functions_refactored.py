import pytest

import cmd as cmd_module

def test_build_setup_cfg_command_class_handles_none():
    """Ensure build_setup_cfg_command_class accepts None without raising an exception."""
    empty_cfg = None  # simulate missing/empty configuration input
    # Call should complete without raising
    cmd_module.build_setup_cfg_command_class(empty_cfg)

