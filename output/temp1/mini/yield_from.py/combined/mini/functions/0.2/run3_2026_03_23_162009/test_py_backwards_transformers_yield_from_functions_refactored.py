import pytest

import yield_from as yield_from_module
import typed_ast.ast3 as typed_ast_ast3

def test_yield_from_transformer_visit_handles_none():
    """YieldFromTransformer can be instantiated and its visit method accepts None without error."""
    none_node = None

    # Instantiate the transformer with None and ensure calling visit(None) doesn't raise.
    transformer = yield_from_module.YieldFromTransformer(none_node)
    transformer.visit(none_node)

def test_yield_from_transformer_initializes_with_none():
    """Ensure YieldFromTransformer can be instantiated with None as its initial node."""
    # Use an explicit, descriptive name for the None input value.
    node_value = None

    # Construct the transformer with the None value to ensure initialization doesn't raise.
    transformer = yield_from_module.YieldFromTransformer(node_value)

def test_yield_from_transformer_visits_typed_ast_while_node():
    """Ensure YieldFromTransformer.visit can be called on a typed_ast.While node built from simple None-containing lists."""
    # Use a single placeholder None for both the transformer constructor and list elements
    placeholder_none = None

    # Create a list with two None elements to mirror the original repeated None list
    repeated_none_list = [placeholder_none, placeholder_none]

    # Instantiate the transformer (preserve original constructor call)
    transformer = yield_from_module.YieldFromTransformer(placeholder_none)

    # Prepare constructor arguments for typed_ast.While as two identical lists
    while_ctor_args = [repeated_none_list, repeated_none_list]

    # Build the While node by unpacking the two lists (preserve original call shape/order)
    while_node = typed_ast_ast3.While(*while_ctor_args)

    # Invoke the transformer's visit method on the While node and capture the result
    transformed_ast = transformer.visit(while_node)

def test_visit_on_while_node_with_duplicate_kwargs_using_yieldfrom_transformer():
    """Construct a While node with duplicate keyword keys and ensure YieldFromTransformer.visit can be invoked on it."""
    # Use the exact None value as in the original test.
    none_value = None

    # Initialize a YieldFromTransformer with None (preserve original initialization).
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Positional arguments for the While node (two None values as in original).
    args_list = [none_value, none_value]

    # Specific string literal used as the dict key in the original test (preserved exactly).
    unique_key = "P+>W*v\nDN{M8\x0bLk"

    # Keyword arguments: the original had the same key repeated three times mapping to the transformer.
    # In a dict literal duplicate keys collapse to the last, but we preserve the original construction.
    kwargs_dict = {
        unique_key: transformer,
        unique_key: transformer,
        unique_key: transformer,
    }

    # Construct the While node using the typed_ast alias provided.
    while_node = typed_ast_ast3.While(*args_list, **kwargs_dict)

    # Invoke the transformer's visit on the While node (preserve call and assignment).
    result_ast = transformer.visit(while_node)

