import re

#################################################
#  System Prompts
#################################################

def get_system_prompt_summary():
    return """You are a helpful AI assistant that will make CONCISE summaries of function to improve testing. The summary should include:
    1. The Functions Signature
    2. The Functions behavior description
    3. The Functions expected inputs and output
    4. Edge cases and constraints
    5. Dependencies and Side effects
    6. Error Handling"""

def get_system_prompt_further_summarization():
    return """"You are a helpful AI assistant that will create a HIGHLY CONCISE summary of a previously summarized function. Please condense the information further by including ONLY the following key details:
    1. The Function's core purpose in one sentence
    2. The Function's expected inputs and outputs in minimal detail
    3. Any critical edge cases or constraints that directly impact the function
Omit redundant information and focus on providing a summary that is as short as possible while still capturing the essence of the function.
"""

def get_system_prompt_readability():
    return """You are a helpful AI assistant that will help improve the readability of the test cases."""

def get_system_prompt_readability_simple():
    return "You are a system that improve code readaility."

def get_system_prompt_self_critique():
    return """You are an expert Python developer and software testing specialist.

Your task is to improve the readability of an automatically generated unit test while preserving its exact semantic behaviour.

The test was generated automatically and may contain poor naming, unclear structure, or missing explanatory comments.

You must perform a structured rewrite with self-critique and revision before producing the final answer."""


#################################################
#  Self_critique_prompt //With removed readability guidelines
#################################################
def get_self_critique_user_prompt(rag_context, original_test, imports):
    return f"""
### Context (Retrieved via RAG)

The following information describes the code under test and domain context:

{rag_context}

Use this information to understand the intent of the test and avoid semantic drift.


---

UPDATED FILE IMPORTS (The file header uses these now):
<imports>
{imports}
</imports>

### Original Test

```python
{original_test}
```

---

## TASK

Perform the following steps:

---

### Step 1 — Readability Rewrite

Rewrite the test to improve readability by:

* Renaming the test method to clearly describe the behaviour under test
* Renaming variables for clarity and domain alignment
* Adding a concise docstring or one-sentence summary comment
* Improving formatting and structural clarity where needed

STRICT REQUIREMENTS:
1. **IMPORT ALIASES**: You MUST use the exact import names provided in the `<imports>` block above.
   *   **EXAMPLE**: If original had `import pandas as pd` and used `pd.DataFrame`, but new import is `import pandas as pandas_lib`, you MUST change `pd.DataFrame` to `pandas_lib.DataFrame`.
2. **MISSING SYMBOLS**: If the test references constants or helper functions from the original test that are NOT in the module context, you MUST include their definitions within the refactored test or define them locally.
3. **PYTEST FIXTURES**: You MUST NOT remove or change any arguments from the original function signature. If you introduce new `pytest` fixtures (like `capsys` or `tmp_path`), you MUST add them to the function arguments.
4. **NO HALLUCINATION**: Preserve the EXACT logic branch and edge case from the original test. Do NOT replace it with a "better" generic test from your bank of knowledge.

Do NOT:

* Change assertions
* Modify expected values
* Modify input values
* Change control flow
* Add or remove function calls
* Add or remove fixtures from the code logic (though you must list them in the signature if used)
* Change imports (except to match the provided aliases)
* Generalize literals
* Alter execution order

Semantic behaviour must remain identical.

---

### Step 2 — Self-Critique

Evaluate your rewritten test against the following criteria:

#### A. Semantic Preservation Check

* Are all assertions identical in logic and expected values?
* Are all function calls preserved?
* Are all literals unchanged?
* Is execution order identical?
* Are fixtures unchanged?
* Has any behaviour been added or removed?

If any semantic deviation exists, describe it precisely.

#### B. Readability Evaluation

* Is the test name behaviour-focused and specific?
* Are variable names descriptive and domain-aligned?
* Is the purpose of the test immediately clear?
* Is the structure easy to follow?
* Are comments concise and helpful?

Identify weaknesses in your rewrite.

---

### Step 3 — Revision

If the critique identified:

* Semantic deviation → Fix it immediately.
* Readability weaknesses → Improve them without breaking semantics.

---

## FINAL OUTPUT REQUIREMENT

You MUST output two sections:

### Section 1: Self-Critique & Fix Plan
1.  **Alias Check**: List all imports from `<imports>`. Check if the Refactored Test uses the *exact* new aliases. If an incorrect alias from the original code is still present, explicitly state: "Found [old alias], replacing with [new alias]".
2.  **Semantic Check**: Verify assertions and logic are preserved.

### Section 2: Final Code
Output the final, corrected code wrapped in `<final_code>` tags.

<final_code>
```python
[Final Refactored Code Here]
```
</final_code>
"""

#################################################
#  Loose Self_critique_prompt
#################################################
def get_loose_self_critique_user_prompt(rag_context, original_test, imports):
    return f"""
### Context (Retrieved via RAG)

The following information describes the code under test and domain context:

{rag_context}

Use this information to understand the intent of the test and avoid semantic drift.

Do NOT use helper functions or constants from the Context unless you define them yourself.
---

UPDATED FILE IMPORTS (The file header uses these now):
<imports>
{imports}
</imports>

### Original Test

```python
{original_test}
```

---

## TASK

Perform the following steps:

---

### Step 1 — Readability Rewrite

Rewrite the test to improve readability by:

* Renaming the test method to clearly describe the behaviour under test
* Renaming variables for clarity and domain alignment
* Adding a concise docstring or one-sentence summary comment
* Improving formatting and structural clarity where needed

STRICT REQUIREMENTS:
1. **IMPORT ALIASES**: You MUST use the exact import names provided in the `<imports>` block above (e.g., if `module_0` is now imported as `timer`, you must use `timer.Timer()` instead of `module_0.Timer()`).
2. **MISSING SYMBOLS**: If the test references constants or helper functions from the original test that are NOT in the module context, you MUST include their definitions within the refactored test or define them locally.
3. **PYTEST FIXTURES**: You MUST NOT remove or change any arguments from the original function signature. If you introduce new `pytest` fixtures (like `capsys` or `tmp_path`), you MUST add them to the function arguments.
4. **NO HALLUCINATION**: Preserve the EXACT logic branch and edge case from the original test. Do NOT replace it with a "better" generic test from your bank of knowledge.

PERMITTED STRUCTURAL CHANGES (LOOSER CONSTRAINTS):
* You **MAY replace manual context manager calls** (`__enter__`, `__exit__`) with idiomatic `with` statements.
* You **MAY remove redundant function calls** that are superseded by language features (e.g., if you use a `with` statement, do NOT manually call `__enter__` inside it).
* You **MAY improve variable names** even if the original names were generic ().

Do NOT:

* Change assertions
* Modify expected values
* Modify input values
* Change control flow (except for context managers)
* Add or remove function calls (except for context managers)
* Add or remove fixtures from the code logic (do NOT add `capsys` or other pytest fixtures if not present)
* Change imports (except to match the provided aliases)
* Add NEW imports or dependencies (standard library is okay if absolutely needed, but avoid new frameworks)
* Convert standard assertions to framework-specific ones (e.g. keep `assert` usage simple)
* Generalize literals
* Alter execution order

Semantic behaviour must remain identical.

---

### Step 2 — Self-Critique

Evaluate your rewritten test against the following criteria:

#### A. Semantic Preservation Check

* Are all assertions identical in logic and expected values?
* Are all function calls preserved?
* Are all literals unchanged?
* Is execution order identical?
* Are fixtures unchanged?
* Has any behaviour been added or removed?

If any semantic deviation exists, describe it precisely.

#### B. Readability Evaluation

* Is the test name behaviour-focused and specific?
* Are variable names descriptive and domain-aligned?
* Is the purpose of the test immediately clear?
* Is the structure easy to follow?
* Are comments concise and helpful?

Identify weaknesses in your rewrite.

---

### Step 3 — Revision

If the critique identified:

* Semantic deviation → Fix it immediately.
* Readability weaknesses → Improve them without breaking semantics.

---

## FINAL OUTPUT REQUIREMENT

Output ONLY the final revised test.

Do NOT include:

* The critique
* Explanations
* Reasoning steps
* Any commentary outside the final test code

Return only valid Python test code.
"""

def get_system_prompt_constrained_instruction():
    return """You are an expert Python developer and software testing specialist.

Your task is to improve the readability of an automatically generated unit test while strictly preserving its semantic behaviour.

This is a constrained code-modification task. You must follow the allowed and prohibited modification rules exactly."""

#################################################
#  Constrained Instruction Prompt //With removed readability guidelines
#################################################
def get_constrained_instruction_user_prompt(rag_context, original_test, imports):
    return f"""
### Context (Retrieved via RAG)

The following information describes the code under test and relevant domain concepts:

{rag_context}

Use this information to better understand the intent of the test.
You may use it only to improve naming clarity and descriptive comments.
You must not introduce new behaviour.

---

UPDATED FILE IMPORTS (The file header uses these now):
<imports>
{imports}
</imports>

### Original Test

```python
{original_test}
```

---

## OBJECTIVE

Improve the readability and clarity of this test while preserving identical execution behaviour.

## ALLOWED MODIFICATIONS

You MAY perform only the following changes:

* Rename the test function to clearly describe the behaviour under test.
* Rename local variables for clarity and domain alignment.
* Add a concise docstring or a single summary comment explaining the purpose of the test.
* Improve formatting (spacing, line breaks) for readability.
* Add inline comments that clarify intent (without changing logic).
* **CRITICAL**: Update usages of imported modules to match the aliases in the `UPDATED FILE IMPORTS` block above.

## PROHIBITED MODIFICATIONS

You must NOT:

* Change assertions.
* Modify expected values.
* Modify input values.
* Change control flow.
* Add or remove function calls.
* Add or remove fixtures.
* Change imports (except to match the provided aliases).
* Generalize literals.
* Alter execution order.

Semantic behaviour must remain identical.

## FINAL OUTPUT REQUIREMENT

Output ONLY the final revised test case in a Python code block.
Do not include any other text, explanations, or commentary.

```python
[revised test code]
```
"""
#################################################
#  Base Prompt
#################################################
def base_user_prompt(rag_context, original_test, imports):
    return f"""
    ### Context (Retrieved via RAG)

The following information describes the code under test and relevant domain concepts:

{rag_context}

Use this information to better understand the intent of the test.
You may use it only to improve naming clarity and descriptive comments.
You must not introduce new behaviour.

---

UPDATED FILE IMPORTS (The file header uses these now):
<imports>
{imports}
</imports>

### Original Test

```python
{original_test}
```

---

## OBJECTIVE

Improve the readability and clarity of this test while preserving identical execution behaviour.

## ALLOWED MODIFICATIONS

ONLY perform the following modifications to the test to improve readability:

* Rename the test function to clearly describe the behaviour under test.
* Rename local variables for clarity and domain alignment.
* Add a concise docstring or a single summary comment explaining the purpose of the test.
* Improve formatting (spacing, line breaks) for readability.
* Add inline comments that clarify intent (without changing logic).
* **CRITICAL**: Update usages of imported modules to match the aliases in the `UPDATED FILE IMPORTS` block above.

## PROHIBITED MODIFICATIONS

You must NOT:

* Change assertions.
* Modify expected values.
* Modify input values.
* Change control flow.
* Add or remove function calls.
* Add or remove fixtures.
* Change imports (except to match the provided aliases).
* Generalize literals.
* Alter execution order.

Semantic behaviour must remain identical.

## FINAL OUTPUT REQUIREMENT

Output ONLY the final revised test case in a Python code block.

```python
[revised test code]
```
"""


#################################################
#  Combined Prompts
#################################################
def combined_user_prompt(rag_context, original_test, imports):
    return f"""
### Context (Retrieved via RAG)

The following information describes the code under test and domain context:

{rag_context}

Use this information to understand the intent of the test and avoid semantic drift.


---

UPDATED FILE IMPORTS (The file header uses these now):
<imports>
{imports}
</imports>

### Original Test

```python
{original_test}
```

---

## TASK

Perform the following steps:

---

### Step 1 — Readability Rewrite and Chain of Thought Analysis
You must improve the readability of this test using a strict sequential reasoning process.
Do NOT output the code immediately. You must "think" first.

1.  **Analyze Intent**: What is this test actually testing? (1 sentence)
2.  **Identify Improvements**:
    *   **Function Name**: Propose a new name that reflects the behavior (e.g., `test_timer_start_stops_correctly`).
    *   **Variables**: List mapping of old cryptic names (e.g., `var_0`) to new descriptive names (e.g., `timer_instance`).
    *   **Docstring**: Draft a concise 1-sentence docstring.
3.  **Safety Check**:
    *   Are we adding any new libraries? (Must be NO)
    *   **CRITICAL**: Did we rename any import aliases? If yes, we MUST update ALL references in the code to use the new alias. usage of the old alias will cause a crash.
        *   **EXAMPLE**: If original had `import pandas as pd` and used `pd.DataFrame`, but new import is `import pandas as pandas_lib`, you MUST change `pd.DataFrame` to `pandas_lib.DataFrame`.
    *   Are we changing assertions? (Must be NO)
    *   Are new variables defined or hallucinated? (Must ensure definition)



Rewrite the test to improve readability by:

* Rename the test function to clearly describe the behaviour under test.
* Rename local variables for clarity and domain alignment.
* Add a concise docstring or a single summary comment explaining the purpose of the test.
* Improve formatting (spacing, line breaks) for readability.
* Add inline comments that clarify intent (without changing logic).

## PROHIBITED MODIFICATIONS

You must NOT:

* Change assertions
* Modify expected values
* Modify input values
* Change control flow
* Add or remove function calls
* Add or remove fixtures from the code logic (though you must list them in the signature if used)
* Change imports (except to match the provided aliases)
* Generalize literals
* Alter execution order

Semantic behaviour must remain identical.

---

### Step 2 — Self-Critique

Evaluate your rewritten test against the following criteria:

#### A. Semantic Preservation Check

* Are all assertions identical in logic and expected values?
* Are all function calls preserved?
* Are all literals unchanged?
* Is execution order identical?
* Are fixtures unchanged?
* Has any behaviour been added or removed?

If any semantic deviation exists, describe it precisely.

#### B. Readability Evaluation

* Is the test name behaviour-focused and specific?
* Are variable names descriptive and domain-aligned?
* Is the purpose of the test immediately clear?
* Is the structure easy to follow?
* Are comments concise and helpful?

Identify weaknesses in your rewrite.

---

### Step 3 — Revision

If the critique identified:

* Semantic deviation → Fix it immediately.
* Readability weaknesses → Improve them without breaking semantics.

---

## FINAL OUTPUT REQUIREMENT

After your analysis, you MUST output two sections:

### Section 1: Self-Critique & Fix Plan
1.  **Alias Check**: List all imports from `<imports>`. Check if the Refactored Test uses the *exact* new aliases. If an incorrect alias from the original code is still present, explicitly state: "Found [old alias], replacing with [new alias]".
2.  **Semantic Check**: Verify assertions and logic are preserved.

### Section 2: Final Code
Output the final, corrected code wrapped in `<final_code>` tags.

<final_code>
```python
[Final Refactored Code Here]
```
</final_code>
"""

#################################################
#  Chain of Thought (CoT) Prompt
#################################################
def get_cot_user_prompt(rag_context, original_test, imports):
    return f"""
### Context (Retrieved via RAG)

The following information describes the code under test and domain context:

{rag_context}

Use this information to understand the intent of the test.

---

UPDATED FILE IMPORTS (The file header uses these now):
<imports>
{imports}
</imports>

### Original Test

```python
{original_test}
```

---

## TASK: Chain-of-Thought Refactoring

You must improve the readability of this test using a strict sequential reasoning process.
Do NOT output the code immediately. You must "think" first.

### Step 1: Analyze & Plan (Mental Sandbox)

1.  **Analyze Intent**: What is this test actually testing? (1 sentence)
2.  **Identify Improvements**:
    *   **Function Name**: Propose a new name that reflects the behavior (e.g., `test_timer_start_stops_correctly`).
    *   **Variables**: List mapping of old cryptic names (e.g., `var_0`) to new descriptive names (e.g., `timer_instance`).
    *   **Docstring**: Draft a concise 1-sentence docstring.
3.  **Safety Check**:
    *   Are we adding any new libraries? (Must be NO)
    *   **CRITICAL**: Did we rename any import aliases? If yes, we MUST update ALL references in the code to use the new alias. usage of the old alias will cause a crash.
        *   **EXAMPLE**: If original had `import pandas as pd` and used `pd.DataFrame`, but new import is `import pandas as pandas_lib`, you MUST change `pd.DataFrame` to `pandas_lib.DataFrame`.
    *   Are we changing assertions? (Must be NO)
    *   Are new variables defined or hallucinated? (Must ensure definition)

### Step 2: Refactoring Execution

Apply the plan from Step 1 to generate the code.

**STRICT RULES:**
1.  **NO NEW DEPENDENCIES**: Do not add `pytest`, `unittest`, or `mock` unless they are already imported.
2.  **NO SEMANTIC CHANGE**: Logic must remain identical.
3.  **NO HALLUCINATIONS**: Do not use helper functions from the RAG context unless you define them inside the test.
4.  **CONSISTENT IMPORTS**: Use the NEW import aliases you defined. Do NOT use the old aliases.

---

## FINAL OUTPUT

After your analysis, providing the final code in a single Python block.

```python
[Final Refactored Code Here]
```
"""


#################################################
#  RAG Base Prompt
#################################################

def get_rag_base_prompt(readability_guidelines, context, imports, test_code):
    return f"""You are an expert Python developer refactoring existing pytest tests to improve readability.

[IMPORTANT]
Your goal is to IMPROVE CLARITY, NOT TO CHANGE LOGIC.
You MUST preserve all assertions and the exact behavior of the test.
The input code is FUNCTIONAL. Do not break it.
You are only meant to improve READABILITY, such as renaming variables to something meaningful, adding comments, renaming function names and so on 
[/IMPORTANT]

[READABILITY GUIDELINES]
{readability_guidelines}
[/READABILITY GUIDELINES]


REPO CONTEXT (Reference only):
<context>
{context}
</context>

UPDATED FILE IMPORTS (The file header uses these now):
<imports>
{imports}
</imports>

CODE TO REFACTOR:
<test>
{test_code}
</test>

STRICT GUIDELINES:
1. **PRESERVE LOGIC (CRITICAL)**: You must NOT change the behavior of the test. If the original test fails, yours must fail. If it passes, yours must pass.
2. **KEEP QUIRKS & BUGS**: If the original test does something "weird" or "wrong" (like calling a private method `_start_time` directly, or testing `__exit__`), PRESERVE IT. Do not "fix" the test logic.
3. **RENAME & FIX IMPORTS**: Rename variables to be meaningful. CRITICALLY, you MUST update usage of imported modules to match the `UPDATED FILE IMPORTS` block.
   *   **EXAMPLE**: If original had `import pandas as pd` and used `pd.DataFrame`, but new import is `import pandas as pandas_lib`, you MUST change `pd.DataFrame` to `pandas_lib.DataFrame`.
4. **PYTEST & FIXTURES**: Keep the original function signature. If you use `capsys`, `tmp_path`, or other fixtures, they MUST be present in the function arguments.
5. **LOCATE MISSING SYMBOLS**: If the test uses constants (like `RE_TIME_MESSAGE`), ensure they are defined within the block or used consistently with the aliases.
6. **NO NEW ASSERTIONS**: Do NOT add assertions that were not present in the input.
7. **NO CONVERSATIONAL FILLER**: Output ONLY valid Python code inside a markdown code block.
8. **FINAL OUTPUT**: You MUST wrap the final python code in `<final_code>` tags.

<final_code>
```python
[refactored test code]
```
</final_code>

```python
"""

#################################################
#  Global User Prompts
#################################################

def get_import_user_prompt(imports):
    return f"""I will provide you with import statements from a test file. Your task is to:
    1. Improve the variable names (aliases) to be meaningful and descriptive.
    2. Format the code according to PEP 8.
    3. MANDATORY: ALWAYS include `import pytest` on its own line at the top.
    4. STRICT: DO NOT change the module names themselves. Only change the names after the `as` keyword (the aliases).

    Example:
    Original: `import codetiming_timer as module_0`
    Good: `import codetiming_timer as timer`
    Bad: `import pytest_codetiming_timer as timer` (DO NOT DO THIS)

    The response MUST follow this format:
    ```python
    [insert new import statements]
    ```
    I will parse the response, therefore, ONLY ANSWER IN THE FORM I GAVE YOU.
    
    Original import statements:
    {imports}
    """

def get_cleanup_user_prompt(refactored_test_case):
    return f"""
    
    Given the following test case refactor the test case to retain its core purpose and functionality while removing any redundant or unnecessary assertions.
    
    Here is a test case: \n 
    {refactored_test_case}

     Ensure that the test still verifies the intended behavior without checking obvious or guaranteed properties (such as default values or type checks). Keep the assertions that directly contribute to validating the logic or specific conditions the test is designed to check.

    Then add comments to explain the test case and actions taken and code coverage achived  by the modified test case. The response SHOULD ONLY contain the refactored test case in a  python code block. Dont add the imports since they are already added to the file.
    """

#################################################
#  Full module User Prompts
#################################################


def full_first_prompt(imports,test_case,modules):
    module_under_test = ''
    if len(modules) == 1:
        module_under_test = modules[0]
    else:
        module_under_test = '\n'.join(modules)

    return f'''
    Here is the module: {module_under_test}

    I will provide you with a test case from the test suite file and rename the test and variables with informative names, add constants and separate setup, execution and assertion and remove type checking assertions. Then add comments to explain the test case and actions taken and code coverage achived  by the modified test case.
    Here are the test file new imports to used: {imports}    
    Here is the test case to improve:
    {test_case}
    \n
    The response SHOULD ONLY contain the refactored test case in a  python code block. 
    '''

#################################################
#  Functions
#################################################

def functions_first_prompt(imports, test_case, all_found_functions):
    return f"""I will provide you with a test case from the test suite file and rename the test and variables with informative names, add constants and separate setup, execution and assertion. Then add comments to explain the core purpose of the test case and actions taken.
    Here are the test file new imports to used: {imports}    
    Here is the test case to improve: \n

    {test_case}
    \n
    The modules functions used in this test case are:"\n" {all_found_functions}

    The response SHOULD ONLY contain the refactored test case in a  python code block. Dont add the imports since they are already added to the file.
    """

def sum_first_prompt(imports, test_case, all_found_functions):
    return f"""I will provide you with a test case from the test suite file and rename the test and variables with informative names, add constants and separate setup, execution and assertion. Then add comments to explain the core purpose of the test case and actions taken.
    Here are the test file new imports to used: {imports}    
    Here is the test case to improve: \n

    {test_case}
    \n
    Here are the summary of the modules functions used in this test case are:"\n" {all_found_functions}

    The response SHOULD ONLY contain the refactored test case in a  python code block. Dont add the imports since they are already added to the file.
    """


def final_prompt(functions_names, refactored_test_case):
    return f'''
    Here is a test case: {refactored_test_case}
    And here are the names of the current test in the file: {functions_names}
    If there is a test case with the same name, change the name of the test case to another meaningful name.

    Provide the test case in a python code block. DONT add the imports or any additional text since the file will be executed to verify the correctness of the test cases.

    Response format:
    ```Python
    [insert test case]
    ```
    
    '''

#################################################
#  Prompt template generation functions
#################################################

def generate_first_all_prompts_with_functions(imports, test_cases, functions, version):
    method_call_pattern = re.compile(r'\b(\w+)\(')
    test_case_prompts = []

    for test_case in test_cases:
        used_functions = set(method_call_pattern.findall(test_case))
        temp_functions = []
        for function_name in used_functions:
            if function_name in functions:
                temp_functions.append(functions[function_name])
        
        # Join the found functions into a single string
        all_found_functions = '\n'.join(temp_functions) + '\n'

        if "sum" in version.lower():
            temp_prompt = sum_first_prompt(imports, test_case, all_found_functions)
        else:
            temp_prompt = functions_first_prompt(imports, test_case, all_found_functions)

        test_case_prompts.append(temp_prompt)

    return test_case_prompts

def generate_first_prompt_for_one_test_case_functions(imports, test_case, all_found_functions, version ="functions"):
        """
        Generate the first prompt for a single test case, version can be functions or summarize
        """
        
        if "sum" in version.lower():
            prompt = sum_first_prompt(imports, test_case, all_found_functions)
        else:
            prompt = functions_first_prompt(imports, test_case, all_found_functions)

        return prompt


def generate_first_prompts_with_module(imports, test_cases, modules):
    test_case_prompts = []
    #LLama3.1 context window
    context_window = 128000

    for test_case in test_cases:
        temp_promp =full_first_prompt(imports, test_case, modules)
        test_case_prompts.append(temp_promp)
    
    return test_case_prompts

#################################################
#  Pytest-Specific Prompts
#################################################

def get_system_prompt_pytest_fixer():
    return """You are an helpful AI assistant that will fixing pytest failures. Your responses must:
    1. Preserve the original test's intent
    2. Follow pytest best practices
    3. Maintain existing test coverage
    4. Provide only the corrected test code in a Python block
    5. Include brief comments explaining fixes"""

def get_import_error_prompt(error_info):
    return f"""Fix these Python imports that caused a ModuleNotFoundError:
    
    Error Details:
    - Missing module: {error_info.get('module')}
    - File: {error_info.get('file')}
    - Original error: {error_info.get('message')}

    Provide solutions that either:
    1. Replace with equivalent alternative imports, OR
    2. Add necessary mocks/patching

    Include brief comments explaining your changes. Respond ONLY with the corrected import block:

    ```Python
    [corrected imports]
    ```"""

def get_syntax_error_prompt(error_info):
    return f"""Fix this Python syntax error while preserving functionality:

    File: {error_info.get('file')}
    Line: {error_info.get('line')}
    Error: {error_info.get('message')}

    Problematic Code:
    {error_info.get('context')}

    Provide ONLY the corrected code block with brief comments:

    ```Python
    [corrected code]
    ```"""

def get_test_failure_prompt(test_name, test_content, failed_module, failure_type=None):
    base_prompt = f"""Fix this failing pytest test while maintaining its original purpose:

    Test Name: {test_name}
    Failure Type: {failure_type if failure_type else 'Unknown'}

    Original Test:
    {test_content}
    """

    if failed_module:
        base_prompt += f"""
        Module Under Test (for reference):
        {failed_module}
    """
        
    base_prompt += """
    Provide the complete corrected test function with:
    1. Clear variable names
    2. Proper setup/teardown
    3. Focused assertions
    4. Brief comments explaining fixes

    Respond ONLY with the corrected test in a Python block:

    ```Python
    [corrected test]
    ```"""
    
    # Add specific guidance for common failure types
    if failure_type == "AssertionError":
        base_prompt += "\nPay special attention to the assertion logic - verify the actual behavior matches expectations."
    elif failure_type == "Timeout":
        base_prompt += "\nConsider optimizing performance or adding reasonable timeouts."
    elif failure_type == "AttributeError":
        base_prompt += "\nVerify the test and module have matching attribute/method names."
    
    return base_prompt

''''
def get_flaky_test_prompt(test_name, test_content):
    return f"""This test appears flaky (sometimes passes/sometimes fails). Make it reliable:

    Test Name: {test_name}

    Original Test:
    {test_content}

    Provide a robust version that:
    1. Handles race conditions
    2. Uses proper waiting/retries
    3. Has deterministic assertions
    4. Includes necessary synchronization

    Respond ONLY with the corrected test:

    ```Python
    [corrected test]
    ```"""
'''




