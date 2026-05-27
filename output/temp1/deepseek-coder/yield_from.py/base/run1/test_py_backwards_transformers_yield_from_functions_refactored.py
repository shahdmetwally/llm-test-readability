import pytest
import yield_from as sleep
import typed_ast.ast3 as typed_node

def test_count_divisible_digits_when_divisor_is_2():
    number_finder = NumberFinder(24)
    assert number_finder.count_divisible_digits(2) == 3

def test_yield_from_transformer_applies_yield_from_transformation_correctly():
    none_type = None
    yield_from_transformer = yield_from_module.YieldFromTransformer(none_type)
    assert isinstance(yield_from_transformer, yield_from_module.YieldFromTransformer)

def test_yield_from_transformer_visit_while():
    none_value = None
    none_list = [none_value, none_value]
    yft_transformer = yield_from.YieldFromTransformer(none_value)
    none_list_of_list = [none_list, none_list]
    while_node = typed_node.While(*none_list_of_list)
    final_node_after_transformation = yft_transformer.visit(while_node)
    assert final_node_after_transformation is not None

def test_pyopenssl_inject_success():
    http_request_success_fixture = conftest.pyopenssl_inject()
    while_yield_from_transform = yield_from.visit(http_request_success_fixture)
    assert while_yield_from_transform == http_request_success_fixture