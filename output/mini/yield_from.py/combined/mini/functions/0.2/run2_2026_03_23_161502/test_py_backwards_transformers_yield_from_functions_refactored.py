import pytest

import yield_from as yield_from_module
import typed_ast.ast3 as typed_ast_ast3

def test_yield_from_transformer_visit_handles_none():
    """Ensure YieldFromTransformer.visit(None) can be called without raising."""
    # Use an explicit variable name to clarify that there is no AST node.
    ast_node_none = None

    # Construct the transformer with a None AST and invoke visit(None).
    # This verifies the transformer accepts None input without raising an exception.
    transformer = yield_from_module.YieldFromTransformer(ast_node_none)
    transformer.visit(ast_node_none)

def test_yield_from_transformer_initializes_with_none():
    """Ensure YieldFromTransformer can be instantiated with a None input (no AST provided)."""
    ast_root = None
    transformer = yield_from_module.YieldFromTransformer(ast_root)
    assert transformer is not None

def test_yieldfrom_transformer_visits_while_node():
    """Verify that YieldFromTransformer.visit can process a While AST node constructed from nested None-pairs."""
    # A single None value used to construct the AST node components
    none_value = None

    # Inner pair: [None, None]
    inner_pair = [none_value, none_value]

    # Create the transformer with the None value (same as original)
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Nested pairs: [inner_pair, inner_pair] -> will be unpacked into typed_ast.While(...)
    nested_pairs = [inner_pair, inner_pair]

    # Construct a While AST node by unpacking the nested_pairs (preserves original call structure)
    while_node = typed_ast_ast3.While(*nested_pairs)

    # Visit the constructed While node with the transformer (preserves original call and assignment)
    result_ast = transformer.visit(while_node)

def test_yield_from_transformer_visits_while_node():
    """Verify that YieldFromTransformer.visit can be invoked on a typed_ast While node."""
    none_value = None

    # Create the transformer with the constructor argument used in the original test
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Positional arguments for the While node (two None values as in the original)
    positional_args = [none_value, none_value]

    # Exact same string literal as in the original test
    key_str = "P+>W*v\nDN{M8\x0bLk"

    # Keyword arguments — the original had the same key repeated three times;
    # keep the literal form identical to preserve semantics.
    keyword_args = {
        key_str: transformer,
        key_str: transformer,
        key_str: transformer,
    }

    # Construct the typed_ast While node using the provided alias for typed_ast.ast3
    while_node = typed_ast_ast3.While(*positional_args, **keyword_args)

    # Invoke the transformer on the While node (preserve call and order)
    result_ast = transformer.visit(while_node)

