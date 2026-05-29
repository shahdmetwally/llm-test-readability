import pytest

import yield_from as yield_from_module
import typed_ast.ast3 as typed_ast_ast3

def test_yield_from_transformer_visit_with_none_module():
    """Construct a YieldFromTransformer and call visit() with None (no AST/module). Should not raise."""
    ast_module = None  # represent a missing AST/module with None
    transformer = yield_from_module.YieldFromTransformer(ast_module)
    # calling visit with None should be a no-op and not raise an exception
    transformer.visit(ast_module)

def test_initializes_yield_from_transformer_with_none():
    """Ensure YieldFromTransformer can be constructed when given None as the node argument."""
    node_arg = None  # Intentionally pass no AST node
    transformer = yield_from_module.YieldFromTransformer(node_arg)

def test_yield_from_transformer_visits_while_node():
    """Verify that YieldFromTransformer.visit can be invoked on a typed_ast While node."""
    # Use an explicit None value as in the original generated test.
    none_value = None

    # Create a simple list containing two None elements (matches original input structure).
    nodes_list = [none_value, none_value]

    # Instantiate the transformer with the same None argument as before.
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Prepare the arguments for the While constructor as two references to the same list.
    while_args = [nodes_list, nodes_list]

    # Construct the While node using the typed_ast.ast3 alias from UPDATED FILE IMPORTS.
    while_node = typed_ast_ast3.While(*while_args)

    # Invoke the transformer's visit method on the While node (preserve original call and order).
    result_node = transformer.visit(while_node)

def test_yield_from_transformer_visits_typed_ast_while():
    """Verify YieldFromTransformer.visit can be invoked on a typed_ast.While node."""
    # Prepare a sentinel None value used by the transformer and as positional args.
    none_value = None

    # Instantiate the transformer with the None parameter (as in the original test).
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Two positional None arguments (preserves the original list [None, None]).
    positional_args = [none_value, none_value]

    # The exact string literal from the original test must be preserved.
    key_string = "P+>W*v\nDN{M8\x0bLk"

    # Construct the kwargs dict using the same key repeated (last occurrence wins,
    # matching the original test's behavior).
    kwargs_mapping = {
        key_string: transformer,
        key_string: transformer,
        key_string: transformer,
    }

    # Build a typed_ast While node with the prepared positional and keyword args.
    while_node = typed_ast_ast3.While(*positional_args, **kwargs_mapping)

    # Invoke the transformer's visit method on the While node (preserves call/ordering).
    visited = transformer.visit(while_node)

