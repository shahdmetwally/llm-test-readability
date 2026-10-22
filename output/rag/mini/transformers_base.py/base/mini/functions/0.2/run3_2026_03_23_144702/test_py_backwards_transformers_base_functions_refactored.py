import pytest

import base as base_module
import typed_ast._ast3 as ast3

def test_base_node_transformer_accepts_none_parent():
    """Constructing BaseNodeTransformer with a None parent should succeed."""
    parent_node = None  # represent no enclosing/parent node
    transformer = base_module.BaseNodeTransformer(parent_node)  # instantiate with None parent

def test_base_import_rewrite_visits_importfrom_with_matmult_and_rewriter():
    """Verify BaseImportRewrite.visit_ImportFrom is exercised with a constructed ImportFrom node.

    Constructs a MatMult node and a BaseImportRewrite (initialized with that MatMult),
    then builds an ImportFrom node from those objects and calls visit_ImportFrom to
    ensure the code path is executed.
    """
    # Create a MatMult AST/node instance (from the typed_ast._ast3 alias).
    mat_mult = ast3.MatMult()

    # Instantiate the BaseImportRewrite with the MatMult node (from base as base_module).
    base_rewriter = base_module.BaseImportRewrite(mat_mult)

    # Prepare the sequence of nodes passed to ImportFrom: rewriter, mat_mult, rewriter.
    nodes = [base_rewriter, mat_mult, base_rewriter]

    # Construct the ImportFrom node using the ast3 alias and the node sequence.
    import_from = ast3.ImportFrom(*nodes)

    # Invoke the visitor method under test with the constructed ImportFrom node.
    base_rewriter.visit_ImportFrom(import_from)

def test_base_importrewrite_visit_importfrom_with_none_and_matmult():
    """Verify BaseImportRewrite.visit_ImportFrom handles an ImportFrom built
    from a None value and a MatMult node without raising errors.
    """
    # Create a MatMult AST node (from typed_ast._ast3)
    mat_mult = ast3.MatMult()

    # Use an explicit None value as in the original test
    none_value = None

    # Instantiate the BaseImportRewrite visitor from the base module,
    # passing the None value (preserves original behaviour).
    rewrite_visitor = base_module.BaseImportRewrite(none_value)

    # Prepare the positional and keyword arguments for ImportFrom exactly
    # as the original test did.
    import_args = [none_value, mat_mult]
    import_kwargs = {}

    # Construct the ImportFrom node using the same args/kwargs and then
    # call the visitor method under test.
    import_from_node = ast3.ImportFrom(*import_args, **import_kwargs)
    rewrite_visitor.visit_ImportFrom(import_from_node)

def test_baseimportrewrite_visit_importfrom_with_duplicate_keys():
    """Exercise BaseImportRewrite.visit_ImportFrom with a mapping that contains duplicate keys.

    This reproduces the original call pattern where a dict with repeated keys is
    passed both as positional (*dict) and keyword (**dict) arguments to ImportFrom.
    """
    source_str = "\x0bQHzaZ?\tpM/wFtV"
    target_str = "%WE}A)"

    # Initialize the visitor with the source name.
    visitor = base_module.BaseImportRewrite(source_str)

    # The literal intentionally repeats keys (last occurrence wins in a dict).
    mapping_dict = {
        source_str: target_str,
        target_str: target_str,
        target_str: target_str,
        source_str: target_str
    }

    # Construct the ImportFrom node by passing the dict as both *args and **kwargs.
    import_node = ast3.ImportFrom(*mapping_dict, **mapping_dict)

    # Invoke the visitor method under test.
    visitor.visit_ImportFrom(import_node)

def test_baseimportrewrite_visit_importfrom_handles_unusual_input():
    """Ensure BaseImportRewrite.visit_ImportFrom can be invoked with the generated ImportFrom node."""
    # Construct two string values used as keys/values in the mapping (kept identical to original).
    weird_string = "\x0bQbHzaZ?\tpM/wFtV"
    empty_string = ""

    # Mapping with repeated keys/values exactly as in the generated test (preserve semantics).
    mapping_args = {
        weird_string: weird_string,
        empty_string: weird_string,
        weird_string: weird_string,
        empty_string: weird_string,
        weird_string: weird_string,
    }

    # Build an ImportFrom AST node by unpacking the mapping both as positional and keyword args
    # (preserves original call shape).
    import_from_node = ast3.ImportFrom(*mapping_args, **mapping_args)

    # Create the BaseImportRewrite instance and invoke the visit_ImportFrom method.
    import_rewriter = base_module.BaseImportRewrite(import_from_node)
    visited = import_rewriter.visit_ImportFrom(import_from_node)

