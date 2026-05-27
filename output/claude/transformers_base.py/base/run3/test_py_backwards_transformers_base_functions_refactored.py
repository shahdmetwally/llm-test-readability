import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as the source tree argument."""
    source_tree = None

    # Instantiate the transformer with no AST tree (None), verifying basic construction
    base_node_transformer = base.BaseNodeTransformer(source_tree)

def test_visit_import_from_with_mat_mult_nodes():
    """Test that BaseImportRewrite.visit_ImportFrom processes an ImportFrom node
    where the module and alias arguments are MatMult AST nodes."""

    # Create a MatMult AST node to serve as the module reference
    mat_mult_node = ast3.MatMult()

    # Instantiate the rewriter with the MatMult node as its target
    rewriter = base.BaseImportRewrite(mat_mult_node)

    # Build an ImportFrom node using the rewriter and MatMult node as arguments
    import_from_args = [rewriter, mat_mult_node, rewriter]
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Visit the ImportFrom node to trigger the rewrite logic
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_none_module_and_mat_mult_alias():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles an ImportFrom node
    where the module is None and the names list contains a MatMult node.
    This exercises the rewrite visitor with a minimal/degenerate import statement.
    """
    # Create a MatMult AST node to use as an alias entry in the import names
    mat_mult_node = ast3.MatMult()

    none_module = None

    # Instantiate the rewrite visitor with no module context
    rewriter = base.BaseImportRewrite(none_module)

    # Build the argument list: module=None, names=[None, mat_mult_node]
    import_from_args = [none_module, mat_mult_node]
    import_from_kwargs = {}

    # Construct an ImportFrom node with the given arguments
    import_from_node = ast3.ImportFrom(*import_from_args, **import_from_kwargs)

    # Visit the ImportFrom node using the rewrite visitor
    rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_dict_unpacking():
    """
    Test that BaseImportRewrite.visit_ImportFrom can be called when an
    ImportFrom node is constructed by unpacking a dictionary as both
    positional and keyword arguments. This exercises the visitor method
    with an unconventional (dict-unpacked) ImportFrom node.
    """
    # An arbitrary string used as a key/value in the argument dictionary
    raw_key = "\x0bQHzaZ?\tpM/wFtV"

    # Instantiate the rewriter with the raw key as its configuration string
    rewriter = base.BaseImportRewrite(raw_key)

    # A second arbitrary string used as the value in the argument dictionary
    raw_value = "%WE}A)"

    # Build a dict whose keys and values will be unpacked into ImportFrom's
    # positional (*dict_args) and keyword (**dict_kwargs) parameters
    node_args = {raw_key: raw_value, raw_value: raw_value, raw_value: raw_value, raw_key: raw_value}

    # Construct the ImportFrom AST node using dict unpacking for both
    # positional and keyword arguments
    import_from_node = ast3.ImportFrom(*node_args, **node_args)

    # Invoke the visitor method under test
    rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_unusual_strings():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles an ImportFrom node
    constructed from unusual/non-standard string values (including whitespace
    and empty strings) without raising an unexpected error.
    """
    # Unusual string with whitespace and special characters as a module name
    unusual_str = "\x0bQbHzaZ?\tpM/wFtV"
    empty_str = ""

    # Build a dict with these strings as keys/values (duplicate keys collapse naturally)
    node_args = {unusual_str: unusual_str, empty_str: unusual_str}

    # Construct an ImportFrom AST node using the unusual strings as positional/keyword args
    import_from_node = ast3.ImportFrom(*node_args, **node_args)

    # Instantiate the rewriter with the constructed ImportFrom node
    rewriter = base.BaseImportRewrite(import_from_node)

    # Visit the ImportFrom node — verifying the method runs without error
    result = rewriter.visit_ImportFrom(import_from_node)

