import pytest

import base as base_module
import typed_ast._ast3 as typed_ast_ast3

def test_base_node_transformer_constructs_with_none():
    """Ensure BaseNodeTransformer can be instantiated with None without raising."""
    # Arrange
    none_input = None

    # Act
    transformer_instance = base_module.BaseNodeTransformer(none_input)

    # Assert: instantiation succeeded and returned an instance of the expected type
    assert isinstance(transformer_instance, base_module.BaseNodeTransformer)

def test_base_import_rewrite_visit_importfrom_behaviour():
    """Exercise BaseImportRewrite.visit_ImportFrom using an ImportFrom node."""
    # Create a MatMult AST node
    mat_mult = typed_ast_ast3.MatMult()

    # Instantiate the BaseImportRewrite visitor with the MatMult node
    base_import_rewrite = base_module.BaseImportRewrite(mat_mult)

    # Prepare the node sequence used to construct the ImportFrom node
    node_list = [base_import_rewrite, mat_mult, base_import_rewrite]

    # Construct an ImportFrom node from the prepared nodes
    import_from_node = typed_ast_ast3.ImportFrom(*node_list)

    # Invoke the visitor's ImportFrom handler (ensures no exceptions and exercises logic)
    base_import_rewrite.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_importfrom_no_error():
    """Ensure BaseImportRewrite.visit_ImportFrom accepts an ImportFrom node without raising."""
    # Create a MatMult node from the typed AST module (used as a positional arg).
    mat_mult_node = typed_ast_ast3.MatMult()

    # Use an explicit None value as in the original test.
    none_value = None

    # Instantiate the BaseImportRewrite visitor with the None value.
    base_import_rewriter = base_module.BaseImportRewrite(none_value)

    # Prepare positional args and keyword args for ImportFrom exactly as before.
    import_from_args = [none_value, mat_mult_node]
    import_from_kwargs = {}

    # Create the ImportFrom node using positional and keyword unpacking.
    import_from_node = typed_ast_ast3.ImportFrom(*import_from_args, **import_from_kwargs)

    # Invoke the visitor's ImportFrom handler (original test only ensured no exception).
    base_import_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_importfrom():
    """Ensure BaseImportRewrite can visit an ImportFrom node without error."""
    # Sample input text used to initialize the BaseImportRewrite instance.
    original_text = "\x0bQHzaZ?\tpM/wFtV"
    rewriter = base_module.BaseImportRewrite(original_text)

    # Another literal used as mapping values/keys in the test.
    alias_text = "%WE}A)"

    # Construct the same mapping as in the original test (duplicate keys intentionally present).
    mapping = {
        original_text: alias_text,
        alias_text: alias_text,
        alias_text: alias_text,
        original_text: alias_text,
    }

    # Create an ImportFrom node using the mapping both as positional and keyword args,
    # then invoke the visitor method. The test passes if no exception is raised.
    import_from_node = typed_ast_ast3.ImportFrom(*mapping, **mapping)
    rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_importfrom_with_duplicate_keys():
    """
    Invoke BaseImportRewrite.visit_ImportFrom on an ImportFrom node built from a
    mapping with duplicate keys to exercise that code path.
    """
    # A non-empty string used as a dict key/value (kept exactly as in original)
    import_key_text = "\x0bQbHzaZ?\tpM/wFtV"
    # An empty-string key (kept exactly as in original)
    empty_import_key = ""

    # Construct the mapping exactly as in the original test (including repeated entries).
    # Note: This literal composition is preserved to keep behaviour identical.
    import_args_map = {
        import_key_text: import_key_text,
        empty_import_key: import_key_text,
        import_key_text: import_key_text,
        empty_import_key: import_key_text,
        import_key_text: import_key_text,
    }

    # Build an ImportFrom node using typed_ast._ast3.ImportFrom (alias: typed_ast_ast3)
    importfrom_node = typed_ast_ast3.ImportFrom(*import_args_map, **import_args_map)

    # Create the BaseImportRewrite instance from base (alias: base_module)
    import_rewriter = base_module.BaseImportRewrite(importfrom_node)

    # Invoke the visit_ImportFrom method with the same node (preserves call order)
    result = import_rewriter.visit_ImportFrom(importfrom_node)

