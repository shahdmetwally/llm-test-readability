import pytest

import base as base_module
import typed_ast._ast3 as ast3

def test_base_node_transformer_initializes_with_none():
    """Ensure BaseNodeTransformer can be instantiated with None as the initializer."""
    # Use None as the initializer (exactly as in the original test).
    initializer = None

    # Construct the transformer using the module alias provided in imports.
    transformer_instance = base_module.BaseNodeTransformer(initializer)

def test_base_import_rewrite_visit_importfrom_handles_matmult_children():
    """Ensure BaseImportRewrite.visit_ImportFrom can handle ImportFrom nodes
    whose children include a MatMult node and a BaseImportRewrite instance
    without raising an exception.
    """
    # Create a MatMult node instance (from typed_ast._ast3)
    mat_mult_node = ast3.MatMult()

    # Create a BaseImportRewrite instance bound to the MatMult node
    rewriter = base_module.BaseImportRewrite(mat_mult_node)

    # Prepare positional args for ImportFrom (intentionally using these objects
    # to simulate unusual child nodes)
    import_from_args = [rewriter, mat_mult_node, rewriter]

    # Construct the ImportFrom node using those arguments
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Invoke the visitor; the test passes if no exception is raised
    rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visits_import_from_without_error():
    """Ensure BaseImportRewrite.visit_ImportFrom accepts an ImportFrom node without raising."""
    # Create a MatMult instance (used as one of the constructor args for ImportFrom).
    mat_mult = module_1.MatMult()

    # Use explicit None value to match the original None literal.
    none_value = None

    # Instantiate BaseImportRewrite with None (same as original).
    base_import_rewrite = module_0.BaseImportRewrite(none_value)

    # Prepare positional and keyword arguments for ImportFrom construction.
    import_from_args = [none_value, mat_mult]
    import_from_kwargs = {}

    # Construct the ImportFrom node with the same arguments as before.
    import_from_node = module_1.ImportFrom(*import_from_args, **import_from_kwargs)

    # Invoke the visitor method; the test succeeds if no exception is raised.
    base_import_rewrite.visit_ImportFrom(import_from_node)

def test_baseimportrewrite_visit_importfrom_handles_duplicate_mappings():
    """Ensure BaseImportRewrite.visit_ImportFrom accepts an ImportFrom node built from duplicate-key mappings."""
    # The original weird string values are preserved exactly (intentional test inputs).
    module_name = "\x0bQHzaZ?\tpM/wFtV"
    alias_value = "%WE}A)"

    # Construct a mapping with duplicate keys/entries intentionally (mirrors original test).
    mapping_dict = {
        module_name: alias_value,
        alias_value: alias_value,
        alias_value: alias_value,
        module_name: alias_value,
    }

    # Instantiate the rewriter with the same first argument as the original test.
    base_import_rewriter = base_module.BaseImportRewrite(module_name)

    # Create an ImportFrom AST node by unpacking the same mapping both positionally and as keywords,
    # exactly as done in the original test to preserve behavior.
    import_from_node = ast3.ImportFrom(*mapping_dict, **mapping_dict)

    # Invoke the visitor method under test (same call and order as original).
    base_import_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_importfrom_handles_repeated_keys():
    """Exercise BaseImportRewrite.visit_ImportFrom with an ImportFrom built from repeated keys (should not raise)."""
    # Two string keys (including special characters) used in the original generated mapping
    key_a = "\x0bQbHzaZ?\tpM/wFtV"
    key_b = ""

    # Mapping intentionally includes repeated entries (duplicates were present in the original test).
    mapping = {key_a: key_a, key_b: key_a, key_a: key_a, key_b: key_a, key_a: key_a}

    # Construct the ImportFrom node using the same call pattern as the original test.
    import_from_node = ast3.ImportFrom(*mapping, **mapping)

    # Create the BaseImportRewrite and invoke the visit method (preserve call order and behavior).
    rewrite = base_module.BaseImportRewrite(import_from_node)
    result = rewrite.visit_ImportFrom(import_from_node)

