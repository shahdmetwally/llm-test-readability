import pytest

import base as base_module
import typed_ast._ast3 as typed_ast_ast3

def test_base_node_transformer_accepts_none():
    """Ensure BaseNodeTransformer can be instantiated with None (no AST node)."""
    none_value = None  # represent absence of a node
    transformer = base_module.BaseNodeTransformer(none_value)  # should construct without error

def test_base_import_rewrite_visits_importfrom_with_matmult():
    """Ensure BaseImportRewrite correctly handles visiting an ImportFrom node containing MatMult."""
    # Create a MatMult node from the typed_ast._ast3 module.
    mat_mult = typed_ast_ast3.MatMult()

    # Instantiate the BaseImportRewrite visitor, providing the MatMult node.
    visitor = base_module.BaseImportRewrite(mat_mult)

    # Prepare the children for the ImportFrom node.
    # Note: the original test deliberately includes the visitor twice in the list.
    children = [visitor, mat_mult, visitor]

    # Construct an ImportFrom node with the prepared children.
    import_from = typed_ast_ast3.ImportFrom(*children)

    # Invoke the visitor's ImportFrom handler (preserves original call order and behaviour).
    visitor.visit_ImportFrom(import_from)

def test_base_import_rewrite_handles_importfrom_with_matmult_node():
    """Ensure BaseImportRewrite.visit_ImportFrom is exercised using an ImportFrom containing a MatMult node."""
    # Create a MatMult AST node (from typed_ast._ast3)
    matmult_node = typed_ast_ast3.MatMult()

    # Use an explicit None value as the placeholder argument (kept identical to original test)
    none_placeholder = None

    # Instantiate the BaseImportRewrite visitor with the None placeholder
    rewriter = base_module.BaseImportRewrite(none_placeholder)

    # Prepare positional and keyword arguments for constructing ImportFrom
    args = [none_placeholder, matmult_node]
    kwargs = {}

    # Construct an ImportFrom AST node using the typed_ast._ast3 alias
    import_from_node = typed_ast_ast3.ImportFrom(*args, **kwargs)

    # Invoke the visitor's ImportFrom handler (this is the behaviour under test)
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_importfrom_with_duplicate_mappings():
    """Verify BaseImportRewrite.visit_ImportFrom handles an ImportFrom built from a dict with repeated entries."""
    # Original string literals retained exactly to preserve behavior.
    source_name = "\x0bQHzaZ?\tpM/wFtV"
    alias_name = "%WE}A)"

    # Create the BaseImportRewrite visitor with the exact same argument as before.
    visitor = base_module.BaseImportRewrite(source_name)

    # Construct a dict that intentionally repeats the same key/value pairs (duplicates as in the original test).
    mapping = {source_name: alias_name, alias_name: alias_name, alias_name: alias_name, source_name: alias_name}

    # Build an ImportFrom node by expanding the mapping as positional (*mapping -> keys) and keyword (**mapping -> items) args.
    import_node = typed_ast_ast3.ImportFrom(*mapping, **mapping)

    # Invoke the visitor on the constructed ImportFrom node.
    visitor.visit_ImportFrom(import_node)

def test_visit_importfrom_with_redundant_dict_args():
    """Ensure BaseImportRewrite.visit_ImportFrom can be called with the same dict used as both *args and **kwargs."""
    source_str = "\x0bQbHzaZ?\tpM/wFtV"
    empty_str = ""

    # Construct the mapping used twice below (literal duplicates in the source are collapsed by Python dict rules).
    arg_mapping = {
        source_str: source_str,
        empty_str: source_str,
        source_str: source_str,
        empty_str: source_str,
        source_str: source_str,
    }

    # Create the ImportFrom node by passing the mapping as both positional (keys) and keyword arguments.
    import_from_node = typed_ast_ast3.ImportFrom(*arg_mapping, **arg_mapping)

    # Initialize the BaseImportRewrite and invoke the visit_ImportFrom method with the node.
    base_rewriter = base_module.BaseImportRewrite(import_from_node)
    result = base_rewriter.visit_ImportFrom(import_from_node)

