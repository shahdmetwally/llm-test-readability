import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as the tree argument."""

    # Use None as the tree argument to verify the transformer accepts it without error
    none_argument = None

    # Instantiate the transformer — this should succeed without raising an exception
    transformer_instance = base.BaseNodeTransformer(none_argument)

def test_visit_import_from_with_mat_mult_and_rewrite_args():
    """Test that visit_ImportFrom handles an ImportFrom node built with MatMult and BaseImportRewrite arguments without error."""

    # Create a MatMult AST node to serve as part of the ImportFrom arguments
    mat_mult_node = module_1.MatMult()

    # Create a BaseImportRewrite transformer using the MatMult node
    import_rewrite = module_0.BaseImportRewrite(mat_mult_node)

    # Build the positional argument list for ImportFrom:
    # [rewrite_instance, mat_mult_node, rewrite_instance] (rewrite appears at positions 0 and 2)
    import_from_args = [import_rewrite, mat_mult_node, import_rewrite]

    # Construct the ImportFrom node by unpacking the argument list
    import_from_node = module_1.ImportFrom(*import_from_args)

    # Invoke the visitor method — verifies it executes without raising an exception
    import_rewrite.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_none_module_and_mat_mult_names():
    """Test that visit_ImportFrom handles an ImportFrom node with a None module and a MatMult node as names without error."""

    # Build an AST MatMult node to serve as the 'names' argument
    mat_mult_node = module_1.MatMult()

    # Use None as the module name to represent a missing/anonymous module
    none_module = None

    # Create the rewrite visitor, initialised with no source module
    rewrite_visitor = module_0.BaseImportRewrite(none_module)

    # Construct positional args: module=None, names=[None, mat_mult_node]
    import_from_args = [none_module, mat_mult_node]

    # No keyword arguments are passed to ImportFrom
    import_from_kwargs = {}

    # Build the ImportFrom AST node using the prepared args
    import_from_node = module_1.ImportFrom(*import_from_args, **import_from_kwargs)

    # Invoke the visitor on the constructed ImportFrom node
    rewrite_visitor.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_dict_unpacked_args_does_not_raise():
    """Test that visit_ImportFrom handles an ImportFrom node constructed via dict unpacking without raising."""

    # Construct a BaseImportRewrite instance with an arbitrary rule string
    rewrite_rule = "\x0bQHzaZ?\tpM/wFtV"
    rewriter = base.BaseImportRewrite(rewrite_rule)

    # Build a dict used to unpack both positional and keyword args into ImportFrom
    # Note: duplicate keys are intentional (last value wins in Python)
    target_name = "%WE}A)"
    import_from_kwargs = {
        rewrite_rule: target_name,
        target_name: target_name,
    }

    # Construct an ImportFrom AST node using dict unpacking for both args and kwargs
    import_from_node = ast3.ImportFrom(*import_from_kwargs, **import_from_kwargs)

    # Invoke the visitor method — verifies it does not raise
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_edge_case_string_arguments():
    """Test that visit_ImportFrom handles an ImportFrom node built from edge-case strings without error."""

    # Edge-case strings: one with control/special characters, one empty
    control_char_string = "\x0bQbHzaZ?\tpM/wFtV"
    empty_string = ""

    # Build a dict with duplicate keys (Python retains last value per key);
    # used as both positional (*args) and keyword (**kwargs) for ImportFrom
    import_from_kwargs = {
        control_char_string: control_char_string,
        empty_string: control_char_string,
        control_char_string: control_char_string,
        empty_string: control_char_string,
        control_char_string: control_char_string,
    }

    # Construct an ImportFrom AST node using the edge-case arguments
    import_from_node = ast3.ImportFrom(*import_from_kwargs, **import_from_kwargs)

    # Instantiate the rewrite visitor with the constructed node
    rewrite_visitor = base.BaseImportRewrite(import_from_node)

    # Invoke visit_ImportFrom and capture the result
    visit_result = rewrite_visitor.visit_ImportFrom(import_from_node)

