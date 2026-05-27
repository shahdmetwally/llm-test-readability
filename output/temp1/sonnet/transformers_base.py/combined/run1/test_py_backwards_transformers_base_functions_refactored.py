import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as the tree argument."""
    # Use None to represent the absence of an AST tree node
    none_argument = None

    # Verify that instantiation succeeds without raising an error
    transformer_instance = base.BaseNodeTransformer(none_argument)

def test_visit_import_from_with_mat_mult_node_does_not_raise():
    """Verify that visit_ImportFrom handles an ImportFrom node built from MatMult arguments without error."""

    # Create a MatMult AST node to use as constructor arguments
    mat_mult_node = ast3.MatMult()

    # Instantiate the rewriter with the MatMult node as its target
    import_rewriter = base.BaseImportRewrite(mat_mult_node)

    # Build the argument list: rewriter appears as first and third element (mirrors original structure)
    import_from_args = [import_rewriter, mat_mult_node, import_rewriter]

    # Construct an ImportFrom node using the unpacked argument list
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Invoke the visitor method — primary behaviour under test
    import_rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_none_module_and_mat_mult_name():
    """Test that visit_ImportFrom handles an ImportFrom node with a None module and a MatMult node as a name entry."""

    # Build a MatMult AST node to serve as an entry in the import names list
    mat_mult_node = ast3.MatMult()

    # Use None as the module name to simulate a missing/anonymous module
    none_module = None

    # Instantiate the rewrite visitor with a None source module
    rewrite_visitor = base.BaseImportRewrite(none_module)

    # Construct positional args: [None module, MatMult name node]
    import_from_args = [none_module, mat_mult_node]

    # No additional keyword arguments for ImportFrom construction
    import_from_kwargs = {}

    # Build the ImportFrom node using unpacked args and kwargs
    import_from_node = ast3.ImportFrom(*import_from_args, **import_from_kwargs)

    # Invoke the visitor on the constructed ImportFrom node
    rewrite_visitor.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_dict_unpacked_args_does_not_raise():
    """Verify that visit_ImportFrom handles an ImportFrom node constructed via dict unpacking without raising."""

    # Create a BaseImportRewrite instance with an arbitrary rewrite rule string
    rewrite_rule = "\x0bQHzaZ?\tpM/wFtV"
    rewriter = base.BaseImportRewrite(rewrite_rule)

    # Build a dict to be unpacked as both positional and keyword args into ImportFrom
    # Note: duplicate keys are intentional — this mirrors the original auto-generated test
    target_name = "%WE}A)"
    import_args_dict = {
        rewrite_rule: target_name,
        target_name: target_name,
        target_name: target_name,
        rewrite_rule: target_name,
    }

    # Construct the ImportFrom AST node using dict unpacking for both args and kwargs
    import_from_node = ast3.ImportFrom(*import_args_dict, **import_args_dict)

    # Invoke the visitor method — the test passes if no exception is raised
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_edge_case_string_keys():
    """Test that visit_ImportFrom handles an ImportFrom node built with edge-case strings (empty and non-printable) without error."""

    # Edge-case string containing a non-printable vertical-tab character and a tab
    non_printable_str = "\x0bQbHzaZ?\tpM/wFtV"
    # Empty string used as an additional key/value in the argument dict
    empty_str = ""

    # Dict with intentionally repeated keys (Python keeps last value for each key);
    # used as both positional-unpack args and keyword-unpack args for ImportFrom
    import_from_kwargs = {
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
        empty_str: non_printable_str,
        non_printable_str: non_printable_str,
    }

    # Construct an AST ImportFrom node using the edge-case dict as both args and kwargs
    import_from_node = ast3.ImportFrom(*import_from_kwargs, **import_from_kwargs)

    # Construct a BaseImportRewrite visitor with the ImportFrom node
    rewrite_visitor = base.BaseImportRewrite(import_from_node)

    # Invoke visit_ImportFrom and capture the result — verifies no exception is raised
    visit_result = rewrite_visitor.visit_ImportFrom(import_from_node)