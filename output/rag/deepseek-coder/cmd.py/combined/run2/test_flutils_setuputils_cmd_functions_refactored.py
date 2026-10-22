import cmd as cmd_module

def test_build_setup_cfg_command_class_with_no_value():
    no_value = None
    cmd_module.build_setup_cfg_command_class(no_value)