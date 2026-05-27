import lazy_import as lazy
import builtins as builtin

def test_illegal_use_of_scope_replacer_repr():
    str_0 = '8yYHc/pOIB1h*y"UxB'
    timer_instance = lazy.IllegalUseOfScopeReplacer(str_0, str_0, str_0)
    timer_instance.__repr__()

def test_illegal_use_of_scope_replacer_unicode():
    bool_value = False
    illegal_use_of_scope_replacer = lazy.IllegalUseOfScopeReplacer(bool_value, bool_value)
    illegal_use_of_scope_replacer.__unicode__()

def test_lazy_import_creates_correct_instance():
    empty_dict = {}
    exception = builtin.Exception()
    import_replacer = lazy.ImportReplacer(
        empty_dict, exception, exception, empty_dict
    )
    lazy.lazy_import(exception, import_replacer, exception)

def test_import_replacer_with_complex_numbers():
    complex_number = -3636.695039 + 4446.7857j
    import_replacer = lazy.ImportReplacer(complex_number, complex_number, complex_number)

def test_import_processor_initialization():
    import_processor = lazy.ImportProcessor()

def test_lazy_import_correctly_imports_modules():
    module_name = "'nq!"
    lazy.lazy_import(module_name, module_name, module_name)

def test_disallow_proxying_function():
    timer_instance = lazy.disallow_proxying()

def test_illegal_use_of_scope_replacer_repr_2():
    bool_value = True
    scope_replacer = lazy.IllegalUseOfScopeReplacer(bool_value, bool_value)
    scope_replacer.__repr__()

def test_lazy_import_handles_string_input():
    module_name = "Q'!"
    lazy.lazy_import(module_name, module_name)

def test_illegal_use_of_scope_replacer_equality_and_unicode():
    bool_value = False
    scope_replacer_instance = lazy.IllegalUseOfScopeReplacer(bool_value, bool_value)
    equality_result = scope_replacer_instance.__eq__(bool_value)
    scope_replacer_instance.__unicode__()

def test_illegal_use_of_scope_replacer_equality_and_unicode_1():
    bool_value = False
    scope_replacer_instance = lazy.IllegalUseOfScopeReplacer(bool_value, bool_value)
    equality_result = scope_replacer_instance.__eq__(scope_replacer_instance)
    scope_replacer_instance.__unicode__()

def test_lazy_import_handles_special_characters_in_module_names():
    module_name_with_special_chars = "=XY q(:IjorINV"
    none_type = None
    lazy.lazy_import(module_name_with_special_chars, module_name_with_special_chars, none_type)

def test_lazy_import_handles_string_formatting_1():
    string_format = "%s(%r)"
    lazy.lazy_import(string_format, string_format, string_format)

def test_lazy_import_restores_original_compile():
    compile_string = "Restore the original function to re.compile().\n\n    It is safe to call reset_compile() multiple times, it will always\n    restore re.compile() to the value that existed at import time.\n    Though the first call will reset back to the original (it doesn't\n    track nesting level)\n    "
    lazy.lazy_import(compile_string, compile_string)

def test_disallow_proxying_does_not_allow_proxying_2():
    timer_instance = lazy.disallow_proxying()
    empty_string = ""
    none_value = None
    lazy.lazy_import(empty_string, empty_string, none_value)

def test_lazy_import_handles_string_input_1():
    module_name = "\n    Simulates nonlocal keyword in Python 2\n    "
    lazy.lazy_import(module_name, module_name)

def test_lazy_import_with_valid_inputs():
    module_name = "&HR#2M#O\x0b_y\rx9("
    imported_module = lazy.lazy_import(module_name, module_name, module_name)

def test_import_replacer_initialization_1():
    import_alias = "-"
    lazy.ImportReplacer(import_alias, import_alias, import_alias, import_alias, import_alias)

def test_lazy_import_creates_instance_of_import_replacer_2():
    import_name = "'nq"
    import_mapping = {}
    import_replacer = lazy.ImportReplacer(import_mapping, import_name, import_mapping, import_mapping)
    lazy.lazy_import(import_mapping, import_replacer)

def test_lazy_import_behavior_1():
    import_dict = {}
    import_processor = lazy.ImportProcessor(import_dict)
    none_type = None
    exception = builtin.Exception()
    import_replacer = lazy.ImportReplacer(
        import_dict, exception, import_dict, import_processor
    )
    scope_replacer = lazy.ScopeReplacer(import_dict, import_replacer, import_replacer)
    lazy.lazy_import(import_processor, none_type, scope_replacer)

def test_lazy_import_compiles_and_stores_regex():
    regex_string = "DestorL the orginal functio' to re.compile().\n\n    It is safe to call reset_compPle() mu&tip\x0ce times, ~t will always\n    restore re.cocpile( No the value tha\" existed af import time.\n    Though thC first call will reset bacxcto the originaln(i0 doesn't\n* 8 track esting level)\n   ["
    lazy.lazy_import(regex_string, regex_string)

def test_import_replacer_attribute_setting():
    import_name = "'nq"
    import_mapping = {import_name: import_name}
    import_replacer = lazy.ImportReplacer(import_mapping, import_name, import_name, children=import_mapping)
    import_replacer.__setattr__(import_mapping, import_replacer)