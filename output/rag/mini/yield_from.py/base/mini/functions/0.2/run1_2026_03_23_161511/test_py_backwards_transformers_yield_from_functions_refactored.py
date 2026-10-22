import pytest

import yield_from as yield_from_module
import typed_ast.ast3 as typed_ast_ast3

def test_yield_from_transformer_visits_none_without_error():
    """Ensure YieldFromTransformer.visit can be invoked with a None node (no-op)."""
    # Use None to simulate absence of an AST node.
    node = None

    # Create the transformer using the aliased module import and invoke visit with None.
    transformer = yield_from_module.YieldFromTransformer(node)
    transformer.visit(node)

def test_yield_from_transformer_init_with_none():
    """Ensure YieldFromTransformer can be instantiated when no AST root is provided."""
    root_node = None  # represent missing/empty root
    transformer = yield_from_module.YieldFromTransformer(root_node)

def test_yield_from_transformer_visits_typed_ast_while_node():
    """Call YieldFromTransformer.visit on a typed_ast While node constructed with placeholder None values."""
    # Single None placeholder (mirrors the original test's usage).
    none_placeholder = None

    # Simulate node fields/children with two placeholders.
    node_children = [none_placeholder, none_placeholder]

    # Instantiate the transformer with the None placeholder.
    transformer = yield_from_module.YieldFromTransformer(none_placeholder)

    # Prepare the arguments for typed_ast.While: two identical child lists.
    while_args = [node_children, node_children]

    # Create a While node from typed_ast and invoke the transformer's visit method.
    while_node = typed_ast_ast3.While(*while_args)
    transformed = transformer.visit(while_node)

def test_yield_from_transformer_visits_typed_ast_while_node_with_repeated_keyword_keys():
    """Ensure YieldFromTransformer.visit can be invoked on a typed_ast While node with repeated keyword keys."""
    # Use an explicit None value as in the original test inputs.
    none_value = None

    # Instantiate the transformer with the same None argument as before.
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Positional arguments for constructing the While node: two None values.
    positional_args = [none_value, none_value]

    # A repeated string literal key mapping to the transformer (kept repeated to mirror original).
    string_key = "P+>W*v\nDN{M8\x0bLk"
    keyword_args = {
        string_key: transformer,
        string_key: transformer,
        string_key: transformer,
    }

    # Construct a typed_ast While node using the provided args/kwargs.
    while_node = typed_ast_ast3.While(*positional_args, **keyword_args)

    # Invoke the transformer's visit method on the constructed While node.
    result_ast = transformer.visit(while_node)

