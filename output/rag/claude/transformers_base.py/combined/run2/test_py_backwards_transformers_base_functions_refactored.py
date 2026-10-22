import pytest
import base as base
import typed_ast._ast3 as ast3

def test_base_node_transformer_instantiation_with_none():
    """Test that BaseNodeTransformer can be instantiated with None as its argument."""
    # Use None as the constructor argument to verify it is accepted
    none_argument = None

    # Instantiate the transformer — should not raise
    transformer_instance = base.BaseNodeTransformer(none_argument)

def test_visit_import_from_with_mat_mult_node_does_not_raise():
    """Test that visit_ImportFrom processes an ImportFrom node built with a MatMult node without error."""

    # Create a MatMult AST node to serve as the base argument
    mat_mult_node = ast3.MatMult()

    # Wrap the MatMult node in a BaseImportRewrite transformer
    import_rewriter = base.BaseImportRewrite(mat_mult_node)

    # Build the positional args for ImportFrom: rewriter appears as first and third args
    import_from_args = [import_rewriter, mat_mult_node, import_rewriter]

    # Construct the ImportFrom node using the prepared arguments
    import_from_node = ast3.ImportFrom(*import_from_args)

    # Invoke the visitor method on the constructed ImportFrom node
    import_rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_none_module_and_mixed_names():
    """Test that visit_ImportFrom handles an ImportFrom node with a None module and mixed name list (None + MatMult node) without error."""

    # Build a MatMult AST node to use as one of the import names
    mat_mult_node = ast3.MatMult()

    # Use None as the module name to simulate a missing/relative module
    none_module = None

    # Create the rewriter with no initial configuration
    rewriter = base.BaseImportRewrite(none_module)

    # Construct the names list: a None entry and a MatMult node
    import_names = [none_module, mat_mult_node]

    # No additional keyword arguments
    extra_kwargs = {}

    # Build an ImportFrom node using the mixed names list
    import_from_node = ast3.ImportFrom(*import_names, **extra_kwargs)

    # Invoke the visitor method under test
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_dict_unpacked_args_does_not_raise():
    """Test that visit_ImportFrom handles an ImportFrom node constructed via dict unpacking without error."""

    # An unusual string used as both a module name key and dict key
    module_name = "\x0bQHzaZ?\tpM/wFtV"
    rewriter = base.BaseImportRewrite(module_name)

    # A second string used as alias/value in the arguments dict
    alias_name = "%WE}A)"

    # Build a dict with duplicate keys (last value wins for duplicate str_1 key);
    # this dict is unpacked as both positional and keyword args into ImportFrom
    import_args_dict = {module_name: alias_name, alias_name: alias_name, alias_name: alias_name, module_name: alias_name}

    # Construct an ImportFrom AST node using dict unpacking for both *args and **kwargs
    import_from_node = ast3.ImportFrom(*import_args_dict, **import_args_dict)

    # Invoke the visitor method — verifies it does not raise an exception
    rewriter.visit_ImportFrom(import_from_node)

def test_visit_import_from_with_dict_unpacked_string_keys():
    """Test that visit_ImportFrom handles an ImportFrom node built via dict unpacking of string keys without error."""

    # Define string values used as both keys and values in the argument dict
    non_printable_string = "\x0bQbHzaZ?\tpM/wFtV"
    empty_string = ""

    # Construct a dict with repeated keys (duplicate keys are intentional — last value wins per Python semantics)
    string_args_dict = {
        non_printable_string: non_printable_string,
        empty_string: non_printable_string,
        non_printable_string: non_printable_string,
        empty_string: non_printable_string,
        non_printable_string: non_printable_string,
    }

    # Build an ImportFrom AST node by unpacking the dict as both positional and keyword arguments
    import_from_node = ast3.ImportFrom(*string_args_dict, **string_args_dict)

    # Instantiate the rewrite visitor with the constructed import node
    rewrite_visitor = base.BaseImportRewrite(import_from_node)

    # Invoke visit_ImportFrom and capture the result
    visit_result = rewrite_visitor.visit_ImportFrom(import_from_node)