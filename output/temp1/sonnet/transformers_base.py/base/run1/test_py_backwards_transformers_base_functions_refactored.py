import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as the tree argument."""
    tree = None
    # Instantiate the transformer with a None AST tree
    transformer = base.BaseNodeTransformer(tree)

def test_visit_import_from_with_rewrite_node_as_argument():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles the case where
    a BaseImportRewrite instance is passed as an argument within an
    ImportFrom node (alongside a MatMult node), without raising an error.
    """
    # Create a MatMult AST node to use as a positional argument
    mat_mult_node = ast3.MatMult()

    # Create a BaseImportRewrite transformer seeded with the MatMult node
    import_rewrite = base.BaseImportRewrite(mat_mult_node)

    # Build an ImportFrom node where the rewrite transformer itself appears
    # as one of the arguments, simulating a self-referential import structure
    import_from_args = [import_rewrite, mat_mult_node, import_rewrite]
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Visit the ImportFrom node through the rewrite transformer
    import_rewrite.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_mat_mult_alias():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles an ImportFrom node
    where the alias is a MatMult node and the module name is None.
    Verifies that the visitor method can be called without error in this edge case.
    """
    # Create a MatMult AST node to use as an alias in the import statement
    mat_mult_alias = ast3.MatMult()

    none_type = None

    # Instantiate the rewriter with no initial configuration (None)
    import_rewriter = base.BaseImportRewrite(none_type)

    # Build an ImportFrom node with None as the module and MatMult as the alias
    import_from_args = [none_type, mat_mult_alias]
    import_from_kwargs = {}
    import_from_node = ast3.ImportFrom(*import_from_args, **import_from_kwargs)

    # Visit the ImportFrom node using the rewriter
    import_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_dict_unpacking():
    """
    Test that BaseImportRewrite.visit_ImportFrom can be called with
    an ImportFrom node constructed via keyword argument unpacking from a dict.
    """
    rewrite_source = "some.module"
    rewrite_target = "other.module"

    base_import_rewrite = base.BaseImportRewrite(rewrites={rewrite_source: rewrite_target})

    import_from_kwargs = {
        "module": rewrite_source,
        "names": [ast3.alias(name="something", asname=None)],
        "level": 0,
    }
    import_from_node = ast3.ImportFrom(**import_from_kwargs)

    result = base_import_rewrite.visit_ImportFrom(import_from_node)
    assert result is not None

def test_base_import_rewrite_visit_import_from_with_mixed_keys():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles an ImportFrom node
    constructed with duplicate and empty string keys in the argument dict.
    Verifies that the visitor method can be called without raising an error
    under these degenerate input conditions.
    """
    # A non-empty string with whitespace/control characters, used as a dict key
    non_empty_key = "\x0bQbHzaZ?\tpM/wFtV"
    # An empty string, also used as a dict key (duplicates will collapse in the dict)
    empty_key = ""

    # Build a dict with duplicate keys; Python will retain only the last value per key
    node_kwargs = {
        non_empty_key: non_empty_key,
        empty_key: non_empty_key,
        non_empty_key: non_empty_key,
        empty_key: non_empty_key,
        non_empty_key: non_empty_key,
    }

    # Construct an ImportFrom AST node using both positional and keyword arguments from the dict
    import_from_node = ast3.ImportFrom(*node_kwargs, **node_kwargs)

    # Instantiate the rewriter with the ImportFrom node as its subject
    rewriter = base.BaseImportRewrite(import_from_node)

    # Visit the ImportFrom node through the rewriter
    var_0 = rewriter.visit_ImportFrom(import_from_node)

