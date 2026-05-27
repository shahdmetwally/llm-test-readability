import pytest

import base as base_module
import typed_ast._ast3 as ast3

def test_base_node_transformer_initializes_with_none_parent():
    """Ensure BaseNodeTransformer constructs correctly when parent AST node is None."""
    parent_node = None  # represent missing/absent parent node
    transformer = base_module.BaseNodeTransformer(parent_node)  # instantiate with None parent
    assert transformer is not None
    assert isinstance(transformer, base_module.BaseNodeTransformer)

def test_base_import_rewrite_handles_importfrom():
    """Ensure BaseImportRewrite visits an ImportFrom node created from MatMult and rewriter instances."""
    # Create a MatMult node (from the ast3 alias)
    mat_mult_node = ast3.MatMult()
    # Instantiate the BaseImportRewrite with the MatMult node (from base_module alias)
    base_rewriter = base_module.BaseImportRewrite(mat_mult_node)
    # Prepare the arguments list for ImportFrom: rewriter, node, rewriter (preserve original order)
    import_args = [base_rewriter, mat_mult_node, base_rewriter]
    # Construct the ImportFrom node using ast3
    import_from_node = ast3.ImportFrom(*import_args)
    # Invoke the visitor method (this is the behaviour under test)
    base_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visits_importfrom_with_none_and_matmult():
    """Call BaseImportRewrite.visit_ImportFrom with an ImportFrom built from None and a MatMult."""
    # Create a MatMult node instance from the AST helper module.
    mat_mult = ast3.MatMult()

    # Use an explicit None value as the first argument (matches the original test input).
    none_value = None

    # Instantiate the BaseImportRewrite visitor with the None value.
    base_rewriter = base_module.BaseImportRewrite(none_value)

    # Prepare positional and keyword arguments for constructing the ImportFrom node.
    args = [none_value, mat_mult]
    kwargs = {}

    # Construct the ImportFrom node and invoke the visitor method under test.
    import_from_node = ast3.ImportFrom(*args, **kwargs)
    base_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_importfrom_with_duplicate_mappings():
    """Ensure BaseImportRewrite.visit_ImportFrom can be called with a mapping
    that contains duplicate keys and values (simulating odd import metadata)."""
    # Source module/name string used to initialize the rewrite visitor.
    source_name = "\x0bQHzaZ?\tpM/wFtV"
    # Create the BaseImportRewrite instance from the 'base' module.
    rewrite_visitor = base_module.BaseImportRewrite(source_name)

    # Alias string used in the mapping.
    alias_name = "%WE}A)"
    # Construct a mapping with duplicated entries (duplicates preserved as in original).
    mapping = {
        source_name: alias_name,
        alias_name: alias_name,
        alias_name: alias_name,
        source_name: alias_name,
    }

    # Create an ImportFrom AST node by unpacking the mapping both positionally and as keywords.
    import_from_node = ast3.ImportFrom(*mapping, **mapping)

    # Invoke the visitor method for ImportFrom nodes.
    rewrite_visitor.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_importfrom_with_redundant_mapping():
    """Call BaseImportRewrite.visit_ImportFrom with a specially-crafted mapping."""
    sample_text = "\x0bQbHzaZ?\tpM/wFtV"
    empty_text = ""
    # Intentionally duplicated keys/values to mirror the original test's mapping.
    mapping = {
        sample_text: sample_text,
        empty_text: sample_text,
        sample_text: sample_text,
        empty_text: sample_text,
        sample_text: sample_text,
    }

    # Build an ImportFrom node using the mapping both as positional and keyword args,
    # then pass it to BaseImportRewrite and invoke the visitor method.
    import_from_node = ast3.ImportFrom(*mapping, **mapping)
    importer = base_module.BaseImportRewrite(import_from_node)
    result_node = importer.visit_ImportFrom(import_from_node)

