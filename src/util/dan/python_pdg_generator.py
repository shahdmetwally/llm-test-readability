import ast
import networkx as nx

class PythonPDGGenerator(ast.NodeVisitor):
    def __init__(self):
        self.graphs = []
        self.current_graph = None
        self.counter = 0
        
        # Per-function state
        self.var_defs = {} 
        self.last_control_nodes = []
        self.method_entry_node = None
        self.method_return_node = None

    def _add_node(self, label, shape='ellipse'):
        if self.current_graph is None:
            return None
        node_id = str(self.counter)
        self.counter += 1
        self.current_graph.add_node(node_id, label=label, shape=shape)
        return node_id

    def _add_edge(self, u, v, style='solid', label=''):
        if self.current_graph is None:
            return
        if u and v:
            self.current_graph.add_edge(u, v, style=style, label=label)

    def build(self, code_content):
        tree = ast.parse(code_content)
        self.visit(tree)
        return self.graphs

    def visit_FunctionDef(self, node):
        # Start new graph for this function
        prev_graph = self.current_graph
        prev_state = (self.var_defs, self.last_control_nodes, self.method_entry_node, self.method_return_node)
        
        self.current_graph = nx.DiGraph()
        self.current_graph.name = node.name
        self.var_defs = {}
        self.last_control_nodes = []
        
        # Create Method Entry
        label = f"METHOD {node.name}"
        self.method_entry_node = self._add_node(label, shape='box')
        self.last_control_nodes = [self.method_entry_node]
        
        # Args definitions
        for arg in node.args.args:
            arg_node = self._add_node(f"PARAM {arg.arg}")
            self._add_edge(self.method_entry_node, arg_node, style='solid')
            self.var_defs[arg.arg] = [arg_node]

        # Body
        for stmt in node.body:
            self.visit(stmt)

        # Method Return
        self.method_return_node = self._add_node("METHOD_RETURN")
        for p in self.last_control_nodes:
            self._add_edge(p, self.method_return_node)
            
        # Save and restore
        self.graphs.append(self.current_graph)
        self.current_graph = prev_graph
        self.var_defs, self.last_control_nodes, self.method_entry_node, self.method_return_node = prev_state

    def visit_Assign(self, node):
        if self.current_graph is None: return
        
        code_segment = ast.get_source_segment(self.code_source, node) if hasattr(self, 'code_source') else "Assign"
        label = f"ASSIGN {code_segment}"
        node_id = self._add_node(label)
        
        # Control Flow
        for p in self.last_control_nodes:
            self._add_edge(p, node_id)
        self.last_control_nodes = [node_id]

        # Data Flow (Targets)
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.var_defs[target.id] = [node_id]
        
        # Data Flow (Value - usages)
        self._visit_expr(node.value, node_id)

    def visit_Expr(self, node):
        if self.current_graph is None: return
        
        # Call or other expression
        label = "EXPR"
        if isinstance(node.value, ast.Call):
            func_name = "func"
            if isinstance(node.value.func, ast.Name):
                func_name = node.value.func.id
            elif isinstance(node.value.func, ast.Attribute):
                func_name = node.value.func.attr
            label = f"CALL {func_name}"
            
        node_id = self._add_node(label)
        
        # Control Flow
        for p in self.last_control_nodes:
            self._add_edge(p, node_id)
        self.last_control_nodes = [node_id]

        # Usage
        self._visit_expr(node.value, node_id)

    def _visit_expr(self, node, current_node_id):
        # Recursive helper to find variable usages in expressions
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Load):
                if node.id in self.var_defs:
                    for def_node in self.var_defs[node.id]:
                        self._add_edge(def_node, current_node_id, style='dashed', label='data_dep')
        
        for child in ast.iter_fields(node):
            child_val = child[1]
            if isinstance(child_val, list):
                for item in child_val:
                    if isinstance(item, ast.AST):
                        self._visit_expr(item, current_node_id)
            elif isinstance(child_val, ast.AST):
                self._visit_expr(child_val, current_node_id)

    def visit_If(self, node):
        if self.current_graph is None: return
        
        cond_id = self._add_node("IF_COND")
        for p in self.last_control_nodes:
            self._add_edge(p, cond_id)
        
        # Usage in condition
        self._visit_expr(node.test, cond_id)

        # Branching
        original_defs = {k: v[:] for k, v in self.var_defs.items()}
        
        # True Branch
        self.last_control_nodes = [cond_id]
        for stmt in node.body:
            self.visit(stmt)
        end_true = self.last_control_nodes

        # False Branch
        self.var_defs = original_defs # Restore for else
        self.last_control_nodes = [cond_id]
        for stmt in node.orelse:
            self.visit(stmt)
        end_false = self.last_control_nodes

        # Merge
        self.last_control_nodes = end_true + end_false
    
    def generic_visit(self, node):
        super().generic_visit(node)

def generate_pdg(file_path):
    with open(file_path, 'r') as f:
        source = f.read()
    
    gen = PythonPDGGenerator()
    gen.code_source = source # helper for snippets
    return gen.build(source)
