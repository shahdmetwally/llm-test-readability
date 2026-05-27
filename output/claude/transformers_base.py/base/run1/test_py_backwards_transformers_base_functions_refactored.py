import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as the tree argument."""
    tree = None
    # Instantiate the transformer with no AST tree (None), verifying basic construction
    transformer = base.BaseNodeTransformer(tree)

def test_visit_import_from_with_rewrite_node_as_module():
    """
    Test that BaseImportRewrite.visit_ImportFrom processes an ImportFrom node
    where the rewrite transformer itself is used as the module argument,
    verifying that the visitor handles this structural configuration without error.
    """
    # Create a MatMult AST node to serve as the module reference in the import
    mat_mult_node = ast3.MatMult()

    # Instantiate the import rewrite transformer with the MatMult node as its target
    import_rewriter = base.BaseImportRewrite(mat_mult_node)

    # Build an ImportFrom node using the rewriter and mat_mult_node as positional args
    import_from_args = [import_rewriter, mat_mult_node, import_rewriter]
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Invoke the visitor method to process the constructed ImportFrom node
    import_rewriter.visit_ImportFrom(import_from_node)

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
    rewrite_visitor = base.BaseImportRewrite(none_module)

    # Build an ImportFrom node with None as the module and MatMult as the name entry
    import_names = [none_module, mat_mult_node]
    import_kwargs = {}
    import_from_node = ast3.ImportFrom(*import_names, **import_kwargs)

    # Visit the ImportFrom node — exercises the rewrite logic on a degenerate import
    rewrite_visitor.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_dict_unpacking():
    """
    Test that BaseImportRewrite.visit_ImportFrom can be called when an
    ImportFrom node is constructed by unpacking a dictionary as both
    positional and keyword arguments. This exercises the visitor method
    with an unconventional (dict-unpacked) AST node instantiation.
    """
    # An arbitrary string used as the rewrite rule/source for BaseImportRewrite
    rewrite_rule = "\x0bQHzaZ?\tpM/wFtV"
    base_import_rewrite = base.BaseImportRewrite(rewrite_rule)

    # A second arbitrary string used as the mapped target value
    target_value = "%WE}A)"

    # Build a dict whose keys/values will be unpacked into ImportFrom's
    # positional and keyword arguments, simulating an edge-case construction
    node_args = {rewrite_rule: target_value, target_value: target_value}

    # Construct an ImportFrom AST node using dict unpacking for both args and kwargs
    import_from_node = ast3.ImportFrom(*node_args, **node_args)

    # Invoke the visitor method under test with the unconventionally constructed node
    base_import_rewrite.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_mixed_keys():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles an ImportFrom node
    constructed with unusual/non-identifier string keys (including empty string
    and non-printable characters) passed as both positional and keyword arguments.
    Verifies that visit_ImportFrom can be called without raising under these inputs.
    """
    # A string containing non-printable and special characters, used as dict keys
    non_printable_key = "\x0bQbHzaZ?\tpM/wFtV"
    empty_key = ""

    # Build a dict with duplicate keys (last value wins); used as both *args and **kwargs
    mixed_key_dict = {
        non_printable_key: non_printable_key,
        empty_key: non_printable_key,
        non_printable_key: non_printable_key,
        empty_key: non_printable_key,
        non_printable_key: non_printable_key,
    }

    # Construct an ImportFrom AST node using the mixed-key dict for both args and kwargs
    import_from_node = ast3.ImportFrom(*mixed_key_dict, **mixed_key_dict)

    # Wrap the node in a BaseImportRewrite transformer
    rewriter = base.BaseImportRewrite(import_from_node)

    # Invoke the visitor method under test
    result = rewriter.visit_ImportFrom(import_from_node)

