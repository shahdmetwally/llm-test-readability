import pytest

import base as base_module
import typed_ast._ast3 as typed_ast_ast3

def test_base_node_transformer_constructs_with_none():
    """Ensure BaseNodeTransformer can be constructed with a None node without raising."""
    none_node = None
    transformer = base_module.BaseNodeTransformer(none_node)
    assert isinstance(transformer, base_module.BaseNodeTransformer)

def test_base_import_rewrite_visits_importfrom_node():
    """Ensure BaseImportRewrite.visit_ImportFrom can be invoked with an ImportFrom node constructed from a MatMult instance."""
    # Create a MatMult AST node instance
    mat_mult = typed_ast_ast3.MatMult()
    # Instantiate the BaseImportRewrite visitor with the MatMult instance
    base_import_rewriter = base_module.BaseImportRewrite(mat_mult)
    # Prepare the arguments for ImportFrom: (base_import_rewriter, mat_mult, base_import_rewriter)
    import_from_args = [base_import_rewriter, mat_mult, base_import_rewriter]
    # Construct an ImportFrom AST node using the prepared arguments
    import_from_node = typed_ast_ast3.ImportFrom(*import_from_args)
    # Invoke the visitor method for ImportFrom nodes; ensure no exceptions are raised
    base_import_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visits_importfrom_with_matmult():
    """Ensure BaseImportRewrite.visit_ImportFrom can be invoked on an ImportFrom node containing None and a MatMult."""
    # Create a MatMult AST node instance.
    mat_mult = typed_ast_ast3.MatMult()

    # None is used as the constructor argument to BaseImportRewrite (preserve original behavior).
    none_value = None

    # Instantiate the visitor.
    base_rewriter = base_module.BaseImportRewrite(none_value)

    # Construct the ImportFrom node containing None and the MatMult node.
    import_from_node = typed_ast_ast3.ImportFrom(none_value, mat_mult)

    # Invoke the visitor method under test.
    base_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visits_importfrom_with_duplicate_keys_passed_as_args_and_kwargs():
    """
    Ensure BaseImportRewrite.visit_ImportFrom can be invoked with a mapping
    that contains duplicate keys and is passed via both *mapping and **mapping.
    """
    # Source string passed to BaseImportRewrite (unchanged literal)
    source_string = "\x0bQHzaZ?\tpM/wFtV"
    # Create the visitor as in the original test
    visitor = base_module.BaseImportRewrite(source_string)

    # Alias/value used in the mapping (unchanged literal)
    alias_string = "%WE}A)"

    # Preserve the original dict literal (duplicate keys; last occurrence wins)
    mapping_dict = {
        source_string: alias_string,
        alias_string: alias_string,
        alias_string: alias_string,
        source_string: alias_string,
    }

    # Construct the ImportFrom node by passing the dict as both *args and **kwargs
    import_node = typed_ast_ast3.ImportFrom(*mapping_dict, **mapping_dict)

    # Invoke the visitor method
    visitor.visit_ImportFrom(import_node)

def test_base_import_rewrite_visits_importfrom_node_with_unusual_keys():
    """Construct an ImportFrom node from a mapping with unusual keys and invoke BaseImportRewrite.visit_ImportFrom."""
    # A non-empty key with control and punctuation characters (unchanged literal).
    weird_key = "\x0bQbHzaZ?\tpM/wFtV"
    # An explicit empty-string key (unchanged literal).
    empty_key = ""

    # Mapping constructed exactly as in the original test. Note: duplicate keys are intentional;
    # later entries overwrite earlier ones, which matches the original behavior.
    mapping = {
        weird_key: weird_key,
        empty_key: weird_key,
        weird_key: weird_key,
        empty_key: weird_key,
        weird_key: weird_key,
    }

    # Construct an ImportFrom node using the mapping as both positional and keyword args,
    # preserving the original call pattern and argument order.
    import_from_node = typed_ast_ast3.ImportFrom(*mapping, **mapping)

    # Instantiate the BaseImportRewrite visitor with the ImportFrom node (same as original).
    rewrite_visitor = base_module.BaseImportRewrite(import_from_node)

    # Invoke the visitor method on the ImportFrom node, preserving the original call and assignment.
    result = rewrite_visitor.visit_ImportFrom(import_from_node)

