import pytest

import yield_from as yield_from_module
import typed_ast.ast3 as typed_ast_ast3

def test_yield_from_transformer_visit_none_is_noop():
    """Construct a YieldFromTransformer with None and call visit(None); should be a no-op (no exceptions)."""
    ast_node = None  # Simulate absence of an AST node
    transformer = yield_from_module.YieldFromTransformer(ast_node)
    # Calling visit with None must not change behavior or raise an exception.
    transformer.visit(ast_node)

def test_yield_from_transformer_initializes_with_none():
    """Ensure YieldFromTransformer can be constructed with None as its argument."""
    # Provide None as the initialization parameter (matches original test intent).
    none_input = None
    transformer = yield_from_module.YieldFromTransformer(none_input)

def test_yield_from_transformer_visits_while_node_with_none_placeholders():
    """Exercise YieldFromTransformer.visit on a While node built from None placeholders."""
    # Use None as a placeholder value for node fields (mirrors original test input)
    none_placeholder = None

    # Create a two-element list of None placeholders (to be used as While constructor args)
    placeholder_pair = [none_placeholder, none_placeholder]

    # Instantiate the transformer with the None placeholder (preserves original constructor arg)
    transformer = yield_from_module.YieldFromTransformer(none_placeholder)

    # Duplicate the placeholder_pair to form the argument list passed to While via unpacking
    duplicated_placeholders = [placeholder_pair, placeholder_pair]

    # Construct a typed_ast While node by unpacking the duplicated placeholders
    while_node = typed_ast_ast3.While(*duplicated_placeholders)

    # Visit the constructed While node with the transformer (same call as original test)
    visited_result = transformer.visit(while_node)

def test_yield_from_transformer_visits_while_node():
    """Verify that YieldFromTransformer.visit can be invoked on a typed_ast While node."""
    # Use the None singleton as in the original test input.
    none_value = None

    # Instantiate the transformer with None (same argument as the original test).
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Positional arguments: two None values (matches the original list_0).
    positional_args = [none_value, none_value]

    # Repeated dict entries with the same string key mapping to the transformer.
    # (Duplicate keys in a literal behave the same as in the original test.)
    key = "P+>W*v\nDN{M8\x0bLk"
    keyword_args = {
        key: transformer,
        key: transformer,
        key: transformer,
    }

    # Construct a typed_ast While node using the positional and keyword arguments.
    while_node = typed_ast_ast3.While(*positional_args, **keyword_args)

    # Invoke the visitor; we only need to call it (result is kept to mirror the original).
    visit_result = transformer.visit(while_node)

