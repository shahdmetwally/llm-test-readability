import typed_ast._ast3 as ast3
import dict_unpacking as dict_unpacking
import typed_ast.ast3 as typed_ast

import module_0
import module_1

def test_timer_initialization_and_management():
    """
    Tests that the timer instance can be correctly initialized and managed via 'start' and 'stop' functions.
    """
    # Initializing a new timer instance
    timer_instance = module_0.mod()
    dict_unpacking_transformer = module_1.DictUnpackingTransformer(timer_instance)

    # Checking if the Timer instance can start and stop correctly
    assert timer_instance.start() == True, "Timer did not start successfully"
    assert timer_instance.stop() == True, "Timer did not stop successfully"

def test_dict_unpacking_unpacks_correctly():
    """Test if DictUnpackingTransformer works as expected"""

    source_code = "39@U3\r"
    unpacker_instance = dict_unpacking.DictUnpackingTransformer(source_code)
    parsed_source = parser.parse(source_code)
    unpacked_module = unpacker_instance.visit_Module(parsed_source)