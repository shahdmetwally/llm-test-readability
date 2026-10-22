import pytest

import yield_from as yield_from_module
import typed_ast.ast3 as ast3

def test_yield_from_transformer_accepts_none():
    """Ensure YieldFromTransformer can be instantiated with and asked to visit a None node."""
    # Use an explicit variable for the None AST node to clarify intent.
    ast_node_none = None

    # Instantiate the transformer with the None node (as in the original test).
    transformer = yield_from_module.YieldFromTransformer(ast_node_none)

    # Invoke visit on the same None node — keep the exact call/behavior from the original.
    transformer.visit(ast_node_none)

def test_yield_from_transformer_initializes_with_none():
    """Construct YieldFromTransformer with None to verify initialization accepts a missing node."""
    # Use an explicit, descriptive variable for the node value (was `none_type_0`)
    node_value = None

    # Initialize the transformer with the None node (was `yield_from_transformer_0 = module_0.YieldFromTransformer(none_type_0)`)
    transformer = yield_from_module.YieldFromTransformer(node_value)

def test_yieldfrom_transformer_visits_while_node():
    """Verify that YieldFromTransformer.visit can be invoked on a While AST node built from nested None values."""
    # A single None value used to mimic missing AST fields.
    none_value = None

    # A small list of two None values (equivalent to original list_0).
    pair_of_nones = [none_value, none_value]

    # Create the transformer with the same None argument as in the original test.
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Prepare arguments for the While node: two identical lists (equivalent to original list_1).
    while_args = [pair_of_nones, pair_of_nones]

    # Construct the While AST node using the typed_ast alias provided in imports.
    while_node = ast3.While(*while_args)

    # Invoke the transformer's visit on the While node (preserve original call and assignment).
    result_ast = transformer.visit(while_node)

def test_yield_from_transformer_visits_while_node_with_repeated_keyword():
    """Ensure YieldFromTransformer.visit handles an ast.While node constructed with the given args/kwargs."""
    none_value = None

    transformer = yield_from_module.YieldFromTransformer(none_value)

    positional_args = [none_value, none_value]

    key = "P+>W*v\nDN{M8\x0bLk"

    kwargs = {
        key: transformer,
        key: transformer,
        key: transformer,
    }

    while_node = ast3.While(*positional_args, **kwargs)

    visited = transformer.visit(while_node)

