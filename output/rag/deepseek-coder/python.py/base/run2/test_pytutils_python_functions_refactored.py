import ast
import astunparse


class AliasFixer(ast.NodeTransformer):
    aliases = {
        'module_0': 'python',
        # you can add more alias->module mappings here
    }

    def visit_Call(self, node):
        self.generic_visit(node)
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            if node.func.value.id in self.aliases:
                # The call belongs to the correct module
                node.func.value.id = self.aliases[node.func.value.id]
        return node


# test code to fix
code = '''
import pytest
import python as module_0

def test_py_info_creation():
    """
    Tests if PyInfo object is properly created.
    """
    # Create py_info object
    info = py_info.PyInfo()
    
    # Assert the creation of PyInfo object
    assert isinstance(info, py_info.PyInfo)

'''

tree = ast.parse(code)
tree_fixed = AliasFixer().visit(tree)
fixed_code = astunparse.unparse(tree_fixed)

print(fixed_code)