import pytest
import yield_from as yield_from_module
import typed_ast.ast3 as ast_module

def test_yield_from_transformer_accepts_none_visitor():
    """
    Verify that YieldFromTransformer can be initialized with a None visitor
    and called with visit(None) without error.
    """
    visitor_instance = None
    transformer = yield_from_module.YieldFromTransformer(visitor_instance)
    transformer.visit(visitor_instance)

def test_yield_from_transformer_accepts_none_skip_annotations():
    """Verify that YieldFromTransformer can be instantiated with skip_annotations=None."""
    # Use None for skip_annotations to test default-like behavior
    skip_annotations_none = None

    # Instantiate the transformer with the None value
    transformer = yield_from_module.YieldFromTransformer(skip_annotations_none)

def test_yield_from_transformer_visit_while_with_none_values():
    """Tests that YieldFromTransformer can process a While AST node with None values."""
    # Create a None value to use as seed for test data
    none_value = None
    
    # Create a list containing two None values - this will be part of the While node's children
    none_list = [none_value, none_value]
    
    # Initialize the transformer with None as the compilation target
    transformer = yield_from_module.YieldFromTransformer(none_value)
    
    # Create the argument list for the While node (two copies of none_list)
    while_args = [none_list, none_list]
    
    # Create a While AST node with the prepared arguments
    while_node = ast_module.While(*while_args)
    
    # Visit the While node - this should handle lists containing None values without error
    result = transformer.visit(while_node)

def test_yield_from_transformer_visits_while_node_with_none_root():
    """
    Verifies that YieldFromTransformer can visit a While AST node
    when initialized with None as the root.
    """
    # Initialize transformer with None as the tree root
    tree_root = None
    transformer = yield_from_module.YieldFromTransformer(tree_root)

    # Create a list with two None values for the While node's test condition
    while_test_list = [tree_root, tree_root]

    # Create a string for the While node's body
    node_body_string = "P+>W*v\nDN{M8\x0bLk"

    # Build the attributes dictionary with repeated string keys
    # (using the same key multiple times is intentional for the AST construction)
    while_attributes = {
        node_body_string: transformer,
        node_body_string: transformer,
        node_body_string: transformer,
    }

    # Construct a While AST node with the list and dictionary
    while_node = ast_module.While(*while_test_list, **while_attributes)

    # Visit the While node with the transformer
    result_ast = transformer.visit(while_node)