from base import BaseNodeTransformer
from typed_ast._ast3 import Node
import helpers as utils

def test_base_node_transformer_initialization_with_none():
    none_type = None
    base_node_transformer = BaseNodeTransformer(none_type)
    assert base_node_transformer.value is None

def test_base_import_rewrite_initialization():
    import_base as base
    import typed_ast._ast3 as ast

    mat_mult = utils.MatMult()
    base_import = base.BaseImportRewrite(mat_mult)
    
    rewrite_list = [base_import, mat_mult, base_import]
    
    import_from_module_1 = import_module_1.ImportFrom(*rewrite_list)
        
    base_import.visit_ImportFrom(import_from_module_1)