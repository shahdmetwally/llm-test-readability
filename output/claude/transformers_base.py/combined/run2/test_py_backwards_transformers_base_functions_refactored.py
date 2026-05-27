import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as its tree argument."""
    # Pass None as the AST tree argument to verify the constructor handles it
    none_argument = None
    transformer_instance = base.BaseNodeTransformer(none_argument)

def test_visit_import_from_with_mat_mult_and_rewrite_args():
    """Test that visit_ImportFrom handles an ImportFrom node built with MatMult and BaseImportRewrite arguments without error."""

    # Create a MatMult AST node to serve as a component in the ImportFrom node
    mat_mult_node = module_1.MatMult()

    # Create the import rewriter under test, initialised with the MatMult node
    import_rewriter = module_0.BaseImportRewrite(mat_mult_node)

    # Build the positional arguments list for the ImportFrom constructor
    import_from_args = [import_rewriter, mat_mult_node, import_rewriter]

    # Construct an ImportFrom AST node using the mixed argument list
    import_from_node = module_1.ImportFrom(*import_from_args)

    # Invoke the visitor method — the core behaviour under test
    import_rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_none_module_and_mat_mult_name():
    """Test that visit_ImportFrom handles an ImportFrom node with a None module and a MatMult object as a name without error."""

    # Create a MatMult AST node to serve as an entry in the names list
    mat_mult_node = ast3.MatMult()

    # Use None as the module name to represent a degenerate/missing module
    none_module = None

    # Instantiate the rewriter with a None configuration
    rewriter = base.BaseImportRewrite(none_module)

    # Build positional and keyword arguments for the ImportFrom node
    import_from_args = [none_module, mat_mult_node]
    import_from_kwargs = {}

    # Construct the ImportFrom AST node using the prepared arguments
    import_from_node = ast3.ImportFrom(*import_from_args, **import_from_kwargs)

    # Invoke the visitor method under test with the constructed node
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_dict_unpacked_args_does_not_raise():
    """Test that visit_ImportFrom handles an ImportFrom node constructed via dict unpacking without raising."""

    # Create a rewriter instance using a raw string as the rewrite rule
    rewrite_rule = "\x0bQHzaZ?\tpM/wFtV"
    rewriter = base.BaseImportRewrite(rewrite_rule)

    # Define a second string used as the value throughout the args dict
    target_module = "%WE}A)"

    # Build the args dict using both strings as keys/values (duplicate keys are intentional)
    import_args_dict = {
        rewrite_rule: target_module,
        target_module: target_module,
        target_module: target_module,
        rewrite_rule: target_module,
    }

    # Construct an ImportFrom AST node by unpacking the dict as both positional and keyword args
    import_from_node = ast3.ImportFrom(*import_args_dict, **import_args_dict)

    # Visit the ImportFrom node — verifies no exception is raised during dispatch
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_edge_case_string_arguments():
    """Tests that visit_ImportFrom handles an ImportFrom node built with non-printable and empty string arguments without error."""

    # Edge-case strings: one contains non-printable/whitespace characters, one is empty
    non_printable_str = "\x0bQbHzaZ?\tpM/wFtV"
    empty_str = ""

    # Intentionally uses duplicate keys and mixed empty/non-printable strings as edge-case input
    import_from_kwargs = {
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
    }

    # Construct an ImportFrom AST node using the edge-case dict as both positional and keyword args
    import_from_node = module_1.ImportFrom(*import_from_kwargs, **import_from_kwargs)

    # Instantiate the rewrite visitor with the constructed node
    rewrite_visitor = module_0.BaseImportRewrite(import_from_node)

    # Invoke the visitor method under test; verifies it runs without raising an exception
    visit_result = rewrite_visitor.visit_ImportFrom(import_from_node)

