import pytest

import lazy_import as lazy_loader
import builtins as python_builtins

def test_illegal_use_of_scope_replacer_repr_does_not_raise():
    """Verify that calling __repr__ on an IllegalUseOfScopeReplacer instance constructed with identical string arguments does not raise."""
    # Use the same literal three times as in the original test.
    sample_text = '8yYHc/pOIB1h*y"U!xB'

    # Instantiate the object under test with the three identical string arguments.
    replacer_instance = module_0.IllegalUseOfScopeReplacer(sample_text, sample_text, sample_text)

    # Invoke __repr__ to ensure it can be called (preserving original behavior — no assertion).
    replacer_instance.__repr__()

def test_illegal_use_of_scope_replacer_unicode_is_callable():
    """Verify IllegalUseOfScopeReplacer can be constructed with False flags and its __unicode__ is callable."""
    flag = False
    replacer = module_0.IllegalUseOfScopeReplacer(flag, flag)
    # Ensure calling __unicode__ does not raise an exception
    replacer.__unicode__()

def test_lazy_import_receives_import_replacer_and_exception_arguments():
    """Ensure lazy_import is invoked with an ImportReplacer and Exception instances."""
    # Prepare an empty mapping to pass into ImportReplacer (same literal as original).
    empty_mapping = {}

    # Create an Exception instance (same as original).
    exc_instance = python_builtins.Exception()

    # Construct the ImportReplacer with the exact argument order and values as before.
    import_replacer = lazy_loader.ImportReplacer(
        empty_mapping, exc_instance, exc_instance, empty_mapping
    )

    # Call lazy_import with the same arguments and order as the original test.
    lazy_loader.lazy_import(exc_instance, import_replacer, exc_instance)

def test_import_replacer_accepts_three_identical_complex_arguments():
    """Ensure ImportReplacer can be called with three identical complex numbers without raising."""
    # Arrange: a complex value used for all three parameters
    complex_value = -3636.695039 + 4446.7857j

    # Act: call the ImportReplacer with the same complex value for all args
    module_0.ImportReplacer(complex_value, complex_value, complex_value)

def test_import_processor_instantiates_without_error():
    """Verify that module_0.ImportProcessor can be instantiated without raising an exception."""
    # Instantiate the ImportProcessor from module_0; test passes if no exception is raised.
    import_processor = module_0.ImportProcessor()

def test_lazy_import_called_with_three_identical_string_args():
    """Call lazy_import with the same string repeated for all three arguments to validate argument handling."""
    # Use the exact string literal from the original test.
    sample_string = "'nq!"
    # Invoke lazy_import with the same value for each parameter (preserve original call order and semantics).
    lazy_loader.lazy_import(sample_string, sample_string, sample_string)

def test_lazy_import_accepts_string_and_none_default():
    """Call lazy_loader.lazy_import with a string module name (twice) and None as the default."""
    module_name = "=XY q(:IjorINV"
    default_value = None

    # Invoke the function under test with the same argument order as the original test.
    lazy_loader.lazy_import(module_name, module_name, default_value)

def test_lazy_import_accepts_repeated_template_strings():
    """Call lazy_import with three identical template strings to verify it accepts repeated arguments.
    The template string is preserved exactly as a literal.
    """
    # Template string used for all three arguments (preserve the exact literal).
    template = "%s(%r)"

    # Invoke lazy_import with the same template for all three parameters.
    lazy_loader.lazy_import(template, template, template)

def test_lazy_import_accepts_identical_docstring_args():
    """Call lazy_loader.lazy_import with identical multi-line docstring arguments
    to ensure it executes without raising an exception.
    """
    docstring_literal = (
        "Restore the original function to re.compile().\n\n"
        "    It is safe to call reset_compile() multiple times, it will always\n"
        "    restore re.compile() to the value that existed at import time.\n"
        "    Though the first call will reset bacF to the originaln(it doesn't\n"
        "    track nesting level)\n"
    )

    # Use the same long docstring for both parameters to mirror the original call.
    lazy_loader.lazy_import(docstring_literal, docstring_literal)

def test_disallow_proxying_then_lazy_import_with_empty_args():
    """Ensure disallow_proxying can be called and lazy_import accepts two empty strings and None."""
    # Call disallow_proxying and keep the return value (behavior preserved from original test).
    proxy_disallow_result = lazy_loader.disallow_proxying()

    # Prepare the original literal arguments used in the auto-generated test.
    empty_string = ""
    none_value = None

    # Call lazy_import with the exact same literals and in the same order as the original.
    lazy_loader.lazy_import(empty_string, empty_string, none_value)

def test_lazy_import_accepts_multiline_docstring_like_string():
    """Ensure lazy_import.lazy_import accepts a multiline docstring-like string as both module name and alias without error."""
    # This string is intentionally a multiline docstring-like value (unchanged literal).
    multiline_docstring_like_string = "\n    Simulates nonlocal keyword in Python 2\n    "
    # Call lazy_import.lazy_import with the same string for both parameters (preserve original call).
    lazy_loader.lazy_import(multiline_docstring_like_string, multiline_docstring_like_string)

def test_import_replacer_accepts_five_identical_hyphens():
    """Ensure ImportReplacer can be called with five identical hyphen string arguments without raising."""
    # Use a single hyphen string literal for all five positional parameters.
    hyphen = "-"
    # Call ImportReplacer with five identical string args; test passes as long as this does not raise.
    module_0.ImportReplacer(hyphen, hyphen, hyphen, hyphen, hyphen)

def test_lazy_import_with_processor_replacer_and_scope_replacer_runs_without_error():
    """Call lazy_import with an ImportProcessor, ImportReplacer, and ScopeReplacer to confirm it runs without raising."""
    # Shared namespace used by helpers.
    module_namespace = {}

    # ImportProcessor that will be passed into lazy_import.
    import_processor = module_0.ImportProcessor(module_namespace)

    # Preserve explicit None literal for the default argument.
    none_value = None

    # Exception instance from module_1 (used as an argument to ImportReplacer).
    exception_instance = module_1.Exception()

    # Construct ImportReplacer with the same arguments and order as the original test.
    import_replacer = module_0.ImportReplacer(
        module_namespace, exception_instance, module_namespace, import_processor
    )

    # Construct ScopeReplacer; note it receives the same ImportReplacer twice.
    scope_replacer = module_0.ScopeReplacer(module_namespace, import_replacer, import_replacer)

    # Invoke lazy_import with the same arguments and order as the original test.
    module_0.lazy_import(import_processor, none_value, scope_replacer)

def test_lazy_import_accepts_unusual_string():
    """Call lazy_import.lazy_import with an unusual string used for both parameters."""
    # A deliberately weird/long string used as both module name and package.
    unusual_name = "DestorL the orginal functio' to re.compile().\n\n    It is safe to call reset_compPle() mu&tip\x0ce times, ~t will always\n    restore re.cocpile( No the value tha\" existed af import time.\n    Though thC first call will reset bacxcto the originaln(i0 doesn't\n* 8 track esting level)\n   ["
    # Preserve original semantics: pass the exact same literal as both arguments.
    lazy_loader.lazy_import(unusual_name, unusual_name)

def test_importreplacer_setattr_with_mapping():
    """Construct an ImportReplacer with a mapping and call its __setattr__ using the mapping and the instance."""
    # Use the same literal as in the original test
    attr_literal = "'nq"
    # mapping uses the literal as both key and value (preserve object relationships)
    mapping = {attr_literal: attr_literal}

    # Create the ImportReplacer instance with the same arguments and keyword as originally used
    import_replacer = module_0.ImportReplacer(mapping, attr_literal, attr_literal, children=mapping)

    # Call __setattr__ with the mapping object and the ImportReplacer instance (preserve call and order)
    import_replacer.__setattr__(mapping, import_replacer)

