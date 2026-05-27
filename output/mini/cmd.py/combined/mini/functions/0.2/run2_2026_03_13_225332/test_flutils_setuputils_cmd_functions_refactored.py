import pytest

import cmd as cmd_module

def test_build_setup_cfg_command_class_accepts_none():
    """Call build_setup_cfg_command_class with None to verify it accepts a None argument without error."""
    # Prepare the input exactly as in the original test (None).
    none_input = None

    # Call the function under test using the provided module alias.
    cmd_module.build_setup_cfg_command_class(none_input)

