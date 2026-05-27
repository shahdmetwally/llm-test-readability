import pytest

import cmd as cmd_module

def test_build_setup_cfg_command_accepts_none_no_exception():
    """Calling build_setup_cfg_command_class with None should not raise an exception."""
    none_value = None

    # Act: invoking the function is a success if no exception is raised.
    cmd_module.build_setup_cfg_command_class(none_value)

