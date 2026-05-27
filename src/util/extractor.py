import re
import os

def extract_test_cases(test_file_path):
    """
    Extracts imports and test cases from a pytest file.
    """
    with open(test_file_path, 'r') as f:
        content = f.read()

    # Simple import extraction (everything before the first def)
    import_match = re.search(r'^(.*?)def ', content, re.DOTALL | re.MULTILINE)
    imports = import_match.group(1).strip() if import_match else ""

    # Test cases extraction (all def test_*)
    test_cases = re.findall(r'(def test_.*?)(?=\ndef test_|\Z)', content, re.DOTALL)
    
    return imports, [tc.strip() for tc in test_cases]

def extract_functions_from_files(file_paths):
    """
    Extracts all function definitions from a list of python files.
    """
    functions = {}
    for path in file_paths:
        with open(path, 'r') as f:
            content = f.read()
            # Find all top-level functions
            matches = re.finditer(r'^def (\w+)\(.*\):.*?\n(?=\S|\Z)', content, re.DOTALL | re.MULTILINE)
            # This is a bit simplified, but works for basic extraction
            # Re-read with a more robust pattern if needed
            all_funcs = re.findall(r'(def \w+\(.*\):.*?\n)(?=\S|\Z)', content, re.DOTALL | re.MULTILINE)
            # Actually use ast for better extraction if possible
            import ast
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions[node.name] = ast.get_source_segment(content, node)
    return functions

def extract_function_names(file_path):
    """
    Extracts function names from a python file.
    """
    with open(file_path, 'r') as f:
        content = f.read()
    import ast
    tree = ast.parse(content)
    return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

def extract_response(response):
    """
    Extracts code from a response string using a prioritized strategy:
    1. Content inside <final_code> tags (highest priority).
    2. The LAST markdown code block (to avoid intermediate drafts).
    3. Raw text if it looks like code (e.g. starts with import/def).
    4. Truncated markdown blocks.
    """
    if not response:
        return ""

    # Priority 1: Check for <final_code> tags
    final_code_match = re.search(r'<final_code>(.*?)</final_code>', response, re.DOTALL | re.IGNORECASE)
    if final_code_match:
        content = final_code_match.group(1).strip()
        # Even inside tags, the model might include backticks
        markdown_match = re.search(r'```(?:[\w\s]*?)?\n([\s\S]*?)\n?```', content, re.IGNORECASE)
        if markdown_match:
             return markdown_match.group(1).strip()
        return content

    # Priority 2: Check for markdown code blocks (Return the LAST one)
    pattern = r'```(?:[\w\s]*?)?\n([\s\S]*?)\n?```'
    matches = re.findall(pattern, response, re.IGNORECASE)
    
    if matches:
        valid_matches = [m.strip() for m in matches if m.strip()]
        if valid_matches:
            return valid_matches[-1] # Return the LAST block

    # Priority 3: Check if the response itself looks like pure code
    lines = response.strip().splitlines()
    if lines:
        first_line = lines[0].strip()
        if first_line.startswith("import ") or first_line.startswith("from ") or first_line.startswith("def ") or first_line.startswith("@"):
            return response.strip()

    # Priority 4: Look for truncated blocks
    truncated_pattern = r'```(?:[\w\s]*?)?\n([\s\S]*)$'
    truncated_match = re.search(truncated_pattern, response, re.IGNORECASE)
    if truncated_match:
         return truncated_match.group(1).strip() + "\n# (Truncated by extractor)"

    # Fallback: Comment out the entire response
    commented_response = "\n".join([f"# {line}" for line in response.splitlines()])
    return f"# *** EXTRACTION FAILED: NO CODE BLOCK FOUND ***\n{commented_response}"
