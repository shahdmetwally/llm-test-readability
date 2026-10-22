import yield_from as module_0
import typed_ast.ast3 as ast3

def test_visit_with_none_value():
    none_value = None
    yield_from_transformer = module_0.YieldFromTransformer(none_value)
    yield_from_transformer.visit(none_value)

def test_yield_from_transformer_none_type_behavior():
    none_type = None
    yield_from_transformer = module_0.YieldFromTransformer(none_type)
    assert yield_from_transformer.node is None
    assert yield_from_transformer.ast3 == ast3

import pytest
from helpers import (
    module_0,
)

def test_yield_from_transformer_None_input():
    input_node = None
    body_else = [input_node, input_node]
    yield_from_transformer = module_0.YieldFromTransformer(input_node)
    while_node = utils.While(*body_else)
    transformed_node = yield_from_transformer.visit(while_node)
    assert transformed_node == input_node

def test_yield_from_transformation():
    none_val = None
    none_node = ast3.NameConstant(value=none_val)
    yield_from_transformer = module_0.YieldFromTransformer(none_node)
    node_list = [none_node, none_node]
    str_key = "YieldFromTransformer"
    string_node = ast3.Str(s=str_key)
    dict_ = {string_node: yield_from_transformer}
    while_stmt = ast3.While(test=node_list[0], body=node_list[1], orelse=None, lineno=None, col_offset=None, end_lineno=None, end_col_offset=None, **dict_)
    transformed_node = yield_from_transformer.visit(while_stmt)
    assert ast3.dump(transformed_node) == ast3.dump(while_stmt)