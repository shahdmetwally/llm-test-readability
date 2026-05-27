import pytest
import yield_from as yield_from_module
import typed_ast.ast3 as typed_ast_module

def test_yield_from_transformer_handles_none_input():
    """Test that YieldFromTransformer can be instantiated with None and visit a None node without error."""
    none_node = None
    transformer = yield_from_module.YieldFromTransformer(none_node)
    transformer.visit(none_node)

def test_yield_from_transformer_constructor_with_none():
    """Test that YieldFromTransformer can be instantiated with None."""
    none_argument = None
    transformer_instance = yield_from_module.YieldFromTransformer(none_argument)

def test_yield_from_transformer_visits_while_node():
    """Test that YieldFromTransformer can visit a While node without error."""
    none_value = None
    none_pair = [none_value, none_value]  # Pair of None values
    
    # Create transformer with None as initial tree
    transformer = yield_from_module.YieldFromTransformer(none_value)
    
    # Arguments for While node: test and body (both using the same pair)
    while_args = [none_pair, none_pair]
    
    # Create a While AST node
    while_node = typed_ast_module.While(*while_args)
    
    # Visit the While node - this should not raise exceptions
    transformed_ast = transformer.visit(while_node)

def test_yield_from_transformer_visit_while_node_with_duplicate_keys():
    """Test that YieldFromTransformer.visit() can process a While AST node with duplicate keys in keyword arguments."""
    # Create transformer with None (empty tree)
    none_value = None
    transformer = yield_from_module.YieldFromTransformer(none_value)

    # Prepare arguments for While node construction
    positional_args = [none_value, none_value]  # test and body both None
    key = "P+>W*v\nDN{M8\x0bLk"
    # Note: duplicate keys in dict literal - last assignment wins
    keyword_args = {
        key: transformer,
        key: transformer,  # duplicate key, same value
        key: transformer,  # duplicate key, same value
    }

    # Create a While AST node with the prepared arguments
    while_node = typed_ast_module.While(*positional_args, **keyword_args)

    # Attempt to transform the While node (test that visit doesn't crash)
    result = transformer.visit(while_node)

