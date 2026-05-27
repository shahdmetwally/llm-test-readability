import pytest
import lazy_import as lazy
import builtins as builtin

def test_illegal_use_of_scope_replacer():
    str_0 = '8yYHc/pOIB1h*y"U!'
    var_0 = lazy.IllegalUseOfScopeReplacer(str_0, str_0, str_0)
    var_0.__repr__()

def test_illegal_use_of_scope_replacer_0():
    bool_0 = False
    illegal_use_of_scope_replacer_0 = lazy.IllegalUseOfScopeReplacer(bool_0, bool_0)
    result = illegal_use_of_scope_replacer_0.__unicode__()
    assert result == builtin.str(bool_0)

def test_lazy_import_with_import_replacer():
    import_mapping = {}
    exception = builtin.Exception()
    import_replacer = lazy.ImportReplacer(
        import_mapping, exception, exception, import_mapping
    )
    lazy.lazy_import(exception, import_replacer, exception)

def test_import_replacer_complex_values():
    complex_value = -3636.695039 + 4446.7857j
    module_0.ImportReplacer(complex_value, complex_value, complex_value)

def test_illegal_use_of_scope_replacer_1():
    pass

def test_lazy_import_functionality_0():
    module_name = "module_0"
    function_name = "lazy_import"
    alias = "module_0"
    module_0.lazy_import(module_name, function_name, alias)
    assert module_0.lazy_import == module_0.lazy_import

def test_disallow_proxying_0():
    expected_value = lazy.module_0.disallow_proxying()
    actual_value = builtin.module_0.disallow_proxying()
    assert actual_value == expected_value

def test_illegal_use_of_scope_replacer_2():
    bool_0 = True
    illegal_use_of_scope_replacer_0 = lazy.IllegalUseOfScopeReplacer(bool_0, bool_0)
    illegal_use_of_scope_replacer_0.__repr__()

def test_lazy_import_functionality_1():
    module_name = "Q'!"
    alias = "Q'!"
    module_0.lazy_import(module_name, alias)
    assert module_0.is_imported(alias)

def test_illegal_use_of_scope_replacer_equality_and_unicode_0():
    bool_0 = False
    illegal_use_of_scope_replacer = lazy.IllegalUseOfScopeReplacer(bool_0, bool_0)
    var_0 = illegal_use_of_scope_replacer.__eq__(bool_0)
    assert var_0 is True
    illegal_use_of_scope_replacer.__unicode__()

def test_illegal_use_of_scope_replacer_equality_and_unicode_representation_1():
    bool_0 = False
    illegal_use_of_scope_replacer_0 = lazy.IllegalUseOfScopeReplacer(bool_0, bool_0)
    var_0 = illegal_use_of_scope_replacer_0.__eq__(illegal_use_of_scope_replacer_0)
    illegal_use_of_scope_replacer_0.__unicode__()
    assert var_0 is True

def test_lazy_import_functionality_2():
    module_name = "=XY q(:IjorINV"
    alias = "=XY q(:IjorINV"
    fromlist = None
    module_0.lazy_import(module_name, alias, fromlist)
    assert module_0.lazy_import(module_name, alias, fromlist) is None

def test_lazy_import_functionality_3():
    str_0 = "%s(%r)"
    str_1 = "module_0"
    str_2 = "lazy_import"
    module_0.lazy_import(str_0, str_1, str_2)
    assert module_0.lazy_import == str_0

def test_reset_compile_restores_original_function():
    original_compile = re.compile
    lazy.lazy_import("Restore the original function to re.compile().", "Restore the original function to re.compile().")
    lazy.reset_compile()
    assert re.compile == original_compile

def test_disallow_proxying_and_lazy_import():
    disallow_proxying_result = module_0.disallow_proxying()
    module_name = ""
    package_name = ""
    level = None
    module_0.lazy_import(module_name, package_name, level)
    assert disallow_proxying_result == ""
    assert module_0.sys.modules.get(module_name) is not None

def test_lazy_import_simulation_0():
    nonlocal_keyword = "\n    Simulates nonlocal keyword in Python 2\n    "
    lazy.lazy_import(nonlocal_keyword, nonlocal_keyword)
    assert module_0.lazy_import == builtin.lazy_import

def test_lazy_import_functionality_3():
    import_name = "&HR#2M#O\x0b_y\rx9("
    module_0.lazy_import(import_name, import_name, import_name)

def test_import_replacer_initialization_0():
    str_0 = "-"
    str_1 = "."
    str_2 = "*"
    str_3 = "|"
    str_4 = "\\"
    import_replacer = lazy.ImportReplacer(str_0, str_1, str_2, str_3, str_4)
    assert isinstance(import_replacer, lazy.ImportReplacer)

def test_lazy_import_with_import_replacer_0():
    import_name = "'nq"
    import_mapping = {}
    import_replacer = lazy.ImportReplacer(import_mapping, import_name, import_mapping, import_mapping)
    lazy.lazy_import(import_mapping, import_replacer)

def test_lazy_import_functionality_4():
    import_dict = {}
    import_processor = module_0.ImportProcessor(import_dict)
    none_type = None
    exception = module_1.Exception()
    import_replacer = module_0.ImportReplacer(import_dict, exception, import_dict, import_processor)
    scope_replacer = module_0.ScopeReplacer(import_dict, import_replacer, import_replacer)
    module_0.lazy_import(import_processor, none_type, scope_replacer)

def test_lazy_import_functionality_1():
    original_function = "DestorL the orginal functio' to re.compile().\n\n    It is safe to call reset_compPle() mu&tip\x0ce times, ~t will always\n    restore re.cocpile( No the value tha\" existed af import time.\n    Though thC first call will reset bacxcto the originaln(i0 doesn't\n* 8 track esting level)\n   ["
    module_0.lazy_import(original_function, original_function)
    module_0.reset_compile()
    assert module_0.lazy_import(original_function, original_function) == module_0.re.compile(original_function)

def test_import_replacer_initialization_1():
    str_0 = "'nq"
    dict_0 = {str_0: str_0}
    import_replacer_0 = lazy.ImportReplacer(dict_0, str_0, str_0, children=dict_0)
    import_replacer_0.__setattr__(dict_0, import_replacer_0)
    assert isinstance(import_replacer_0, lazy.ImportReplacer)
    assert import_replacer_0.dict == dict_0
    assert import_replacer_0.name == str_0
    assert import_replacer_0.asname == str_0
    assert import_replacer_0.children == dict_0