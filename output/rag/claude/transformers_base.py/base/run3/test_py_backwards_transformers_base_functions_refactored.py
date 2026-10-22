import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as the tree argument."""
    # Pass None as the AST tree, representing an empty/absent syntax tree
    tree = None
    base_node_transformer = base.BaseNodeTransformer(tree)

def test_visit_import_from_with_rewrite_node_as_argument():
    """
    Test that BaseImportRewrite.visit_ImportFrom can be called with an
    ImportFrom node whose arguments include the rewriter itself, verifying
    that the visitor handles self-referential import structures without error.
    """
    # Create a MatMult AST node to act as a placeholder/target for rewriting
    mat_mult_node = ast3.MatMult()

    # Instantiate the import rewriter with the MatMult node as its base
    import_rewriter = base.BaseImportRewrite(mat_mult_node)

    # Build an ImportFrom node using the rewriter and MatMult node as arguments,
    # with the rewriter appearing at both the first and third positions
    import_from_args = [import_rewriter, mat_mult_node, import_rewriter]
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Visit the ImportFrom node through the rewriter
    import_rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_mat_mult_alias():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles an ImportFrom node
    whose alias is a MatMult node, with a None module name.
    """
    # Create a MatMult AST node to use as the alias in the ImportFrom
    mat_mult_alias = ast3.MatMult()

    none_module = None

    # Initialise the rewriter with no configuration
    rewriter = base.BaseImportRewrite(none_module)

    # Build an ImportFrom node with a None module and MatMult as the alias
    import_from_args = [none_module, mat_mult_alias]
    import_from_kwargs = {}
    import_from_node = ast3.ImportFrom(*import_from_args, **import_from_kwargs)

    # Visit the ImportFrom node — exercise the rewrite logic
    rewriter.visit_ImportFrom(import_from_node)

def test_base_import_rewrite_visit_import_from_with_dict_unpacking():
    """
    Test that BaseImportRewrite.visit_ImportFrom does not raise an unexpected
    exception when called with an ImportFrom node constructed via dictionary
    unpacking of positional and keyword arguments.
    """
    rewrite_target = "\x0bQHzaZ?\tpM/wFtV"
    base_import_rewrite = base.BaseImportRewrite(rewrite_target)

    replacement_name = "%WE}A)"

    # Note: duplicate keys mean only the last value for each key is retained
    node_args = {
        rewrite_target: replacement_name,
        replacement_name: replacement_name,
    }
    import_from_node = ast3.ImportFrom(*node_args, **node_args)

    base_import_rewrite.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_invalid_dict_unpacking():
    """
    Test that BaseImportRewrite.visit_ImportFrom handles an ImportFrom node
    constructed with invalid/malformed dict unpacking arguments without raising
    an unexpected error. This exercises the rewrite visitor with a node built
    from mixed positional and keyword arguments derived from arbitrary strings.
    """
    # Arbitrary string values used as constructor arguments (including non-printable chars)
    arbitrary_key = "\x0bQbHzaZ?\tpM/wFtV"
    empty_str = ""

    # Dict with duplicate keys; effectively reduces to fewer unique entries at runtime
    malformed_args = {
        arbitrary_key: arbitrary_key,
        empty_str: arbitrary_key,
        arbitrary_key: arbitrary_key,
        empty_str: arbitrary_key,
        arbitrary_key: arbitrary_key,
    }

    # Construct an ImportFrom AST node using unpacked dict as both positional and keyword args
    import_from_node = ast3.ImportFrom(*malformed_args, **malformed_args)

    # Wrap the node in a BaseImportRewrite visitor
    rewrite_visitor = base.BaseImportRewrite(import_from_node)

    # Invoke the visitor method under test
    result = rewrite_visitor.visit_ImportFrom(import_from_node)