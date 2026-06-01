import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as its argument."""

    # Pass None as the constructor argument to verify it is accepted without error
    none_argument = None
    transformer_instance = base.BaseNodeTransformer(none_argument)

def test_visit_import_from_with_mat_mult_node_does_not_raise():
    """Test that visit_ImportFrom handles an ImportFrom node built with a MatMult node as its first argument."""

    # Use a MatMult node as an unconventional first argument to stress-test the visitor
    mat_mult_node = ast3.MatMult()

    # Construct the transformer under test using the MatMult node
    import_rewrite_transformer = base.BaseImportRewrite(mat_mult_node)

    # Build the argument list: transformer appears at positions 0 and 2, node at position 1
    import_from_args = [import_rewrite_transformer, mat_mult_node, import_rewrite_transformer]

    # Construct the ImportFrom AST node by unpacking the argument list
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Invoke the visitor method — the call itself is the behaviour under test
    import_rewrite_transformer.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_none_module_and_mat_mult_arg():
    """Tests that visit_ImportFrom handles an ImportFrom node built with a None module and a MatMult node in its args without error."""

    # Create a MatMult AST node to use as one of the ImportFrom arguments
    mat_mult_node = ast3.MatMult()

    # Use None as the module value for the ImportFrom node
    none_value = None

    # Instantiate the rewriter with None as its initialisation argument
    rewriter = base.BaseImportRewrite(none_value)

    # Build positional and keyword argument collections for the ImportFrom constructor
    import_from_args = [none_value, mat_mult_node]
    import_from_kwargs = {}

    # Construct the ImportFrom AST node using the prepared arguments
    import_from_node = ast3.ImportFrom(*import_from_args, **import_from_kwargs)

    # Invoke the visitor method under test
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_dict_args_does_not_raise():
    """Verify that visit_ImportFrom does not raise when called with an ImportFrom node constructed from dict-based positional and keyword arguments."""

    # Source pattern string used to initialise the rewriter
    rewrite_source = "\x0bQHzaZ?\tpM/wFtV"
    import_rewriter = base.BaseImportRewrite(rewrite_source)

    # Target string used as the replacement value in all dict entries
    rewrite_target = "%WE}A)"

    # Build a dict with duplicate keys (intentional: reflects auto-generated input)
    # used as both positional (*) and keyword (**) arguments for ImportFrom
    import_args_dict = {
        rewrite_source: rewrite_target,
        rewrite_target: rewrite_target,
        rewrite_target: rewrite_target,
        rewrite_source: rewrite_target,
    }

    # Construct an AST ImportFrom node using the dict for both args and kwargs
    import_from_node = ast3.ImportFrom(*import_args_dict, **import_args_dict)

    # Invoke the visitor method under test
    import_rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_edge_case_string_args():
    """Tests that visit_ImportFrom handles an ImportFrom node built from edge-case strings (non-printable and empty) without error."""

    # Edge-case strings: one containing non-printable characters, one empty
    non_printable_str = "\x0bQbHzaZ?\tpM/wFtV"
    empty_str = ""

    # Dict with intentional duplicate keys — mirrors the original generated input exactly
    import_from_kwargs = {
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
    }

    # Construct an ImportFrom AST node using the edge-case dict as both args and kwargs
    import_from_node = ast3.ImportFrom(*import_from_kwargs, **import_from_kwargs)

    # Instantiate the rewrite visitor with the constructed node
    rewrite_visitor = base.BaseImportRewrite(import_from_node)

    # Invoke the visitor method under test
    visit_result = rewrite_visitor.visit_ImportFrom(import_from_node)