import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as its tree argument."""
    # Pass None as the AST tree argument to simulate an empty/missing tree
    none_argument = None

    # Instantiate the transformer; this should not raise any errors
    transformer_instance = base.BaseNodeTransformer(none_argument)

def test_visit_import_from_with_mat_mult_and_rewrite_args():
    """Test that visit_ImportFrom handles an ImportFrom node built with MatMult and BaseImportRewrite args."""

    # Create a MatMult AST node to serve as a component of the ImportFrom node
    mat_mult_node = module_1.MatMult()

    # Create a BaseImportRewrite visitor using the MatMult node
    import_rewriter = module_0.BaseImportRewrite(mat_mult_node)

    # Build the argument list for ImportFrom: rewriter, mat_mult, rewriter
    import_from_args = [import_rewriter, mat_mult_node, import_rewriter]

    # Construct the ImportFrom AST node by unpacking the argument list
    import_from_node = module_1.ImportFrom(*import_from_args)

    # Invoke the visitor method under test
    import_rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_none_module_and_mat_mult_name():
    """Test that visit_ImportFrom handles an ImportFrom node with a None module and a MatMult in names."""

    # Create a MatMult AST node to serve as an unusual/degenerate name entry
    mat_mult_node = module_1.MatMult()

    # Use None as the module argument to simulate a missing/degenerate module reference
    none_value = None

    # Instantiate the rewriter with None as its initialisation argument
    rewriter = module_0.BaseImportRewrite(none_value)

    # Build positional args: module=None, names=[None, mat_mult_node]
    import_from_args = [none_value, mat_mult_node]

    # No keyword arguments supplied
    import_from_kwargs = {}

    # Construct the ImportFrom AST node using the degenerate arguments
    import_from_node = module_1.ImportFrom(*import_from_args, **import_from_kwargs)

    # Invoke the visitor method — verifies it does not raise on edge-case input
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_dict_unpacked_args():
    """Test that visit_ImportFrom handles an ImportFrom node constructed via dict unpacking without error."""

    # Source path string used as the rewriter's module identifier
    source_path = "\x0bQHzaZ?\tpM/wFtV"
    rewriter = base.BaseImportRewrite(source_path)

    # Target path string used as rewrite destination
    target_path = "%WE}A)"

    # Dict with duplicate keys (last value wins); used for both positional and keyword unpacking
    import_args_dict = {source_path: target_path, target_path: target_path, target_path: target_path, source_path: target_path}

    # Construct an ImportFrom AST node using dict unpacking for both args and kwargs
    import_from_node = ast3.ImportFrom(*import_args_dict, **import_args_dict)

    # Exercise the visitor method under test
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_edge_case_string_arguments():
    """Test that visit_ImportFrom handles an ImportFrom node built with edge-case string arguments (empty and non-printable) without error."""

    # Edge-case strings: one contains non-printable/whitespace characters, one is empty
    non_printable_str = "\x0bQbHzaZ?\tpM/wFtV"
    empty_str = ""

    # Dict with intentional duplicate keys, used as both positional and keyword args
    import_from_kwargs = {
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
    }

    # Construct an ImportFrom AST node using the edge-case arguments
    import_from_node = ast3.ImportFrom(*import_from_kwargs, **import_from_kwargs)

    # Construct the rewrite visitor with the ImportFrom node
    rewrite_visitor = base.BaseImportRewrite(import_from_node)

    # Invoke the visitor method under test
    visit_result = rewrite_visitor.visit_ImportFrom(import_from_node)

