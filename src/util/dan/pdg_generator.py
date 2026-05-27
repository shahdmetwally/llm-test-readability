import ast
import networkx as nx
import logging

logger = logging.getLogger(__name__)

class PDGGenerator(ast.NodeVisitor):
    def __init__(self, source_code):
        self.source_code = source_code
        self.method_graphs = {} # name -> nx.DiGraph
        self.current_graph = None
        self.current_control_node = None
        self.variable_defs = {}  # var_name -> node_id
        self.node_counter = 0

    def build(self):
        try:
            tree = ast.parse(self.source_code)
            self.visit(tree)
            return self.method_graphs
        except Exception as e:
            logger.error(f"Failed to parse or build PDG: {e}")
            return {}

    def _add_node(self, node, label, node_type="STATEMENT"):
        if self.current_graph is None:
            return None
            
        node_id = str(self.node_counter)
        self.node_counter += 1
        lineno = getattr(node, 'lineno', 0) if node else 0
        self.current_graph.add_node(node_id, label=label, type=node_type, lineno=lineno)
        return node_id

    def visit_Module(self, node):
        # Handle top-level code as a pseudo-function called __main__
        self.current_graph = nx.DiGraph()
        self.current_graph.name = "__main__"
        self.current_control_node = None
        self.variable_defs = {}
        
        # Entry Node
        label = "METHOD: __main__"
        entry_id = self._add_node(node, label, "METHOD")
        self.current_control_node = entry_id

        # Process non-function statements at top level
        for stmt in node.body:
            if not isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                self._process_statement(stmt)
            
        # Exit Node
        exit_id = self._add_node(None, "METHOD_RETURN", "METHOD_RETURN")
        if self.current_control_node:
            self.current_graph.add_edge(self.current_control_node, exit_id, type="CONTROL")

        # Save graph
        self.method_graphs["__main__"] = self.current_graph
        
        # Reset context
        self.current_graph = None
        self.current_control_node = None
        self.variable_defs = {}

        # Continue to visit other nodes (e.g., FunctionDefs)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Start a new graph for this function
        func_name = node.name
        self.current_graph = nx.DiGraph()
        self.current_graph.name = func_name
        
        # Reset context for new graph
        self.current_control_node = None
        self.variable_defs = {}
        # We keep node_counter global or per-graph? 
        # Per-graph is cleaner for independent DOT files, but global is fine too.
        # Let's keep global unique IDs to avoid confusion if we ever merge.
        
        # Entry Node
        label = f"METHOD: {func_name}"
        entry_id = self._add_node(node, label, "METHOD")
        self.current_control_node = entry_id

        # Arguments
        for arg in node.args.args:
            arg_name = arg.arg
            arg_id = self._add_node(arg, f"param: {arg_name}", "PARAM")
            
            self.current_graph.add_edge(self.current_control_node, arg_id, type="CONTROL")
            self.variable_defs[arg_name] = arg_id
            self.current_control_node = arg_id

        # Body
        for stmt in node.body:
            self._process_statement(stmt)
            
        # Exit Node
        exit_id = self._add_node(None, "METHOD_RETURN", "METHOD_RETURN")
        if self.current_control_node:
            self.current_graph.add_edge(self.current_control_node, exit_id, type="CONTROL")

        # Save graph
        self.method_graphs[func_name] = self.current_graph
        
        # Reset current graph so we don't accidentally add top-level code or other stuff to it
        self.current_graph = None
        self.current_control_node = None
        self.variable_defs = {}

    def _process_statement(self, stmt):
        if self.current_graph is None:
            return

        # Determine label
        try:
            raw_source = ast.unparse(stmt)
            label = raw_source.split('\n')[0]
            if len(label) > 60:
                label = label[:57] + "..."
        except:
            label = f"Stmt line {getattr(stmt, 'lineno', '?')}"

        stmt_id = self._add_node(stmt, label)

        # Control Flow Edge
        if self.current_control_node:
            self.current_graph.add_edge(self.current_control_node, stmt_id, type="CONTROL")
        
        self.current_control_node = stmt_id

        # Data Flow Edges
        for child in ast.walk(stmt):
            if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                if child.id in self.variable_defs:
                    def_node = self.variable_defs[child.id]
                    self.current_graph.add_edge(def_node, stmt_id, type="DATA", var=child.id)

        # Update Definitions
        if isinstance(stmt, ast.Assign):
            for target in stmt.targets:
                if isinstance(target, ast.Name):
                    self.variable_defs[target.id] = stmt_id
        elif isinstance(stmt, ast.AnnAssign):
            if isinstance(stmt.target, ast.Name):
                self.variable_defs[stmt.target.id] = stmt_id
        elif isinstance(stmt, ast.AugAssign):
            if isinstance(stmt.target, ast.Name):
                self.variable_defs[stmt.target.id] = stmt_id

        # Recurse
        if isinstance(stmt, (ast.If, ast.For, ast.While, ast.With, ast.Try, ast.AsyncWith, ast.AsyncFor)):
             for child_stmt in stmt.body:
                 self._process_statement(child_stmt)
             if hasattr(stmt, 'orelse'):
                 for child_stmt in stmt.orelse:
                     self._process_statement(child_stmt)
             if hasattr(stmt, 'finalbody'):
                 for child_stmt in stmt.finalbody:
                     self._process_statement(child_stmt)

    def save_to_dot(self, graph, file_path):
        """
        Export a specific graph to DOT format manually.
        """
        try:
            with open(file_path, "w") as f:
                f.write(f'digraph "{graph.name}" {{\n')
                f.write('  node [shape="rect"];\n')
                
                # Nodes
                for node, data in graph.nodes(data=True):
                    label = data.get('label', '').replace('"', '\\"')
                    node_line = f'  "{node}" [label = "{label}"];\n'
                    f.write(node_line)
                
                # Edges
                for u, v, data in graph.edges(data=True):
                    edge_type = data.get('type', '')
                    var = data.get('var', '')
                    label = f"{edge_type}: {var}" if var else edge_type
                    edge_line = f'  "{u}" -> "{v}" [ label = "{label}"];\n'
                    f.write(edge_line)
                    
                f.write('}\n')
        except Exception as e:
            logger.error(f"Failed to save DOT file: {e}")
