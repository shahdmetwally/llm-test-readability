import cmd as shell_command_processing

import unittest

class TestModule0(unittest.TestCase):
    def test_none_argument_support_for_build_setup_cfg_command_class(self):
        none_type_value = None
        shell_command_processing.build_setup_cfg_command_class(none_type_value)