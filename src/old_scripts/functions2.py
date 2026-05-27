"""
Scripts:
- summarize the functions into text 
- extract the test cases
- send the summarized functions and each test case to the model
- uses the test cases name to ensure that the test cases name are unique

"""


import argparse
import os
from dotenv import load_dotenv
from .util import file_handler as helper
from .util.verify_response import check_correct_format
import re
from datetime import datetime 

load_dotenv()

parser = argparse.ArgumentParser(description='Process some file paths.')
parser.add_argument(
    '-p','--paths',
    dest='paths', 
    type=str, 
    nargs='+', 
    help='at least one file path',
    required=True
)

parser.add_argument("-tp","--testpath",
                    dest="testpath",
                    type=str,
                    help="The path to the test class")

parser.add_argument("-m", "--model", dest="model", type=str, default= "mistral_debugger",
                    help="Set the model to use")

parser.add_argument("-s", "--session", dest="session", type=str, default="session",
                    help="Customize session name")

parser.add_argument("-j", "--job", dest="job", type=str, default="job",
                    help="Customize session name")

parser.add_argument('-t', '--temperature', dest="temperature", type=str, default=0.7,
                    help='Path to the module file')

args = parser.parse_args()
paths = args.paths
test_path = os.path.join(os.getcwd(), args.testpath)
model: str = args.model.lower()
session: str = args.session
temperature = args.temperature #Default 0.7
job: str = args.job
session_name: str = f"session{session}_temp{temperature}"

timestamp = helper.generate_timestamp()
# Create the directory

output_dir = f"./output/{model}/{job}/{session}-{temperature}/{timestamp}"
os.makedirs(output_dir, exist_ok=True)

if len(paths) == 0:
    parser.error("The script must have at least one file path as an argument.")

# Print the paths
def print_paths(paths):
    for i, path in enumerate(paths, start=1):
        path = os.path.join(os.getcwd(), path)
        print(f'Path {i}: {path}')

print_paths(paths)

###########################################################
# Extract functions name and code
###########################################################
inside_function = False
current_functions = []
functions = {}
class_name = None

for path in paths:
    path = os.path.join(os.getcwd(), path)
    with open(path, 'r') as file:
        for line in file:
            if line.strip().startswith('class '):
                class_name = line.strip().split()[1].split('(')[0].rstrip(':')
            if line.strip().startswith('def'):
                # Save the previous function if any
                if current_functions:
                    function_name = current_functions[0].split('(')[0][4:].strip()
                    # Check if the function is __init__ and use class name as key
                    if function_name == '__init__' and class_name:
                        functions[class_name] = '\n'.join(current_functions)
                    else:
                        functions[function_name] = '\n'.join(current_functions)
                    current_functions = []
                
                inside_function = True
                current_functions.append(line.strip())
            elif inside_function:
                if line.strip() == '':
                    inside_function = False
                    function_name = current_functions[0].split('(')[0][4:].strip()
                    # Check if the function is __init__ and use class name as key
                    if function_name == '__init__' and class_name:
                        functions[class_name] = '\n'.join(current_functions)
                    else:
                        functions[function_name] = '\n'.join(current_functions)
                    current_functions = []
                else:
                    current_functions.append(line.strip())

# Save the last function if the file ends with a function
if current_functions:
    function_name = current_functions[0].split('(')[0][4:].strip()
    if function_name == '__init__' and class_name:
        functions[class_name] = '\n'.join(current_functions)
    else:
        functions[function_name] = '\n'.join(current_functions)

def print_functions(functions):
    for name, func in functions.items():
        print(f"{name}")
        #print(f"Function Code:\n{func}\n")

#print_functions(functions)

#############################################
# Load model
#############################################
from .util.model_lib import Session

# Mistral-7B as default for debugging
default_model = "../.cache/models--mistralai--Mistral-7B-Instruct-v0.2/snapshots/cf47bb3e18fe41a5351bc36eef76e9c900847c89"

if model == "mixtral":
        model_path = os.getenv("MIXTRAL")
        max_new_tokens = int(os.getenv("TOKEN_LIMIT"))
elif model == "llama":
        model_path = os.getenv("LLAMA")
        max_new_tokens = int(os.getenv("TOKEN_LIMIT")) 
else: 
    model_path = default_model
    max_new_tokens = int(os.getenv("TOKEN_LIMIT"))


system_prompt: str = """You are a helpful AI assistant that will make CONCICE summaries of function to improve testing. The summary should include:
    1. The Functions Signature
    2. The Functions behavior description
    3. The Functions expected inputs and output
    4. Edge cases and constraints
    5. Dependencies and Side effects
    6. Error Handling"""


model_session: Session = Session.create(
    session_name,
    model_path,
    max_new_tokens,
    system_prompt,
    temperature
)


###########################################################
# Extract Test cases
###########################################################
def extract_tests(file_path):
    # Initialize variables
    imports = []
    test_cases = []
    inside_test_case = False
    current_test_case = []
    # Read the file and process lines
    with open(file_path, 'r') as file:
        for line in file:
            # Check for imports
            if line.startswith('import') or line.startswith('from'):
                imports.append(line.strip())
            # Check for start of a test case
            elif line.strip().startswith('def test') or line.strip().startswith('@pytest'):
                inside_test_case = True
                current_test_case.append(line.strip())
            # Check for end of a test case
            elif line.strip() == '' and inside_test_case:
                inside_test_case = False
                test_cases.append('\n'.join(current_test_case))
                current_test_case = []
            # Collect lines of a test case
            elif inside_test_case:
                current_test_case.append(line.strip())

        # Catch any test case not followed by a blank line
        if current_test_case:
            test_cases.append('\n'.join(current_test_case))
        
    return imports, test_cases


# Extract imports and test cases from a test suite file
imports,test_cases = extract_tests(test_path)

###########################################################
# Identify and print functions used in each test case
###########################################################
def generate_test_cases_prompt_with_function_data(test_cases, functions):
    method_call_pattern = re.compile(r'\b(\w+)\(')
    test_case_prompts = []
    
    for i, test_case in enumerate(test_cases):
        used_functions = set(method_call_pattern.findall(test_case))
        #print(f"\nTest Case {i}:")
        temp_functions = []
        for function_name in used_functions:
            if function_name in functions:
                #print(f"\nFunction '{function_name}' used in Test Case {i}:\n{functions[function_name]}")
                temp_functions.append(functions[function_name])
        
        all_found_functions = '\n'.join(temp_functions) + '\n'

        temp_prompt = f"""
        Here is the test case:\n {test_case}. \n
        The modules functions used in this test case are: \n {all_found_functions}. \n
    
        """
        #print(temp_prompt,"\n")

        test_case_prompts.append(temp_prompt)

    return test_case_prompts


    

test_cases_prompts = generate_test_cases_prompt_with_function_data(test_cases, functions)


#############################################
# Imports
#############################################
import_statements = '\n'.join(imports) + '\n'

user_prompt = f"""I will provide you imports name and you will improve the the variable names and formatting to use meaningful variable names and format the code according to PEP 8.

The response MUST follow this format:
```Python
    [insert new import statements]
```
I will parse the response, therefore, ONLY ANSWER IN THE FORM I GAVE YOU.
Here are the import statements from the test suite file:
{import_statements}
"""
print("import prompt: ",user_prompt)

#Send imports to model
import_response = model_session.prompt(user_prompt, True)
print("Before checking format: ", import_response)
import_checked_response = check_correct_format(import_response)
print("\nChecked:\n",import_checked_response)
print("*************************************************\n\n")
#Save the import data

file_log_file_path = os.path.join(output_dir, f'File_creation_logs-{session_name}.txt')

import_store_summary= f''' 
###########################################################
# Imports 
###########################################################\n
System promp: \n
{system_prompt} \n 
User prompt:\n
{user_prompt}
\n
***********************************************************
* Model Response 
***********************************************************
{import_checked_response} \n\n  '''

with open(file_log_file_path, 'w') as file:
    file.write(import_store_summary)

#Create a new test file name
base_name= os.path.basename(test_path)
name, extension = os.path.splitext(base_name)
new_test_file= f"{name}_refactored"

#Start creating the file
new_python_file_path = helper.create_python_file(output_dir, new_test_file, import_checked_response)

#Set new system prompt
model_session.system_prompt = "You are a system that improve code readaility."

#create test case logs
test_case_log = f"{output_dir}test_case_logs.txt"

def extract_function_names(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    # Regular expression to match function definitions
    function_pattern = re.compile(r'^\s*def\s+(\w+)\s*\(', re.MULTILINE)
    
    # Find all matches
    function_names = function_pattern.findall(file_content)
    
    # Format the function names as a string that looks like a list
    formatted_function_names = str(function_names)
    
    return formatted_function_names


counter = 0
for test_case_prompt in test_cases_prompts:

    user_prompt_1 =  f"""I will provide you with a test case from the test suite file and rename the test and variables with informative names, add constants and separate setup, execution and assertion. Then add comments to explain the core purpose of the test case and actions taken.
    Here are the test file new imports to used: {import_checked_response}    
    Here is the test case to improve:
    {test_case_prompt}
    The response SHOULD ONLY contain the refactored test case in a  python code block. Dont add the imports since they are already added to the file.
    """
    
    response = model_session.prompt(user_prompt_1, True)
    checked_response1 = check_correct_format(response)
    print(response)
    test_case_info= f''' 
###########################################################
# Test case -   {counter}
###########################################################\n
System promp: \n
{system_prompt}\n
User prompt:\n
{user_prompt}
\n
***********************************************************
* Model Response 
***********************************************************
{response} \n\n  '''
    
    #Save the test case data
    with open(f'{test_case_log}', 'a') as file:
        file.write(test_case_info)

    user_prompt_2 =  f'''

    Here is a test case: {checked_response1}

    Given the following test case and the information about the functions used, refactor the test case to retain its core purpose and functionality while removing any redundant or unnecessary assertions. Ensure that the test still verifies the intended behavior without checking obvious or guaranteed properties (such as default values or type checks). Keep the assertions that directly contribute to validating the logic or specific conditions the test is designed to check.

    Then add comments to explain the test case and actions taken and code coverage achived  by the modified test case. The response SHOULD ONLY contain the refactored test case in a  python code block. Dont add the imports since they are already added to the file.
    
    '''
    response = model_session.prompt(user_prompt_2, True)
    checked_response2 = check_correct_format(response)
    print("\n Remove assertions: \n",checked_response2)
        #Save the test case data
    
    test_case_info_ref= f''' 
###########################################################
# Test case Refinement- {counter}
###########################################################\n
System promp: \n
{system_prompt}\n
User prompt:\n
{user_prompt_2}
\n
***********************************************************
* Model Response 
***********************************************************
{response} 

Post processing: 
{checked_response2} \n\n  '''

    with open(test_case_log, 'a') as file:
        file.write(test_case_info_ref)

###########################################################
# Test case Refinement
###########################################################
    function_names = extract_function_names(new_python_file_path)

    user_prompt_3 =  f'''
    Here is a test case: {checked_response2}
    And here are the names of the current test in the file: {function_names}
    If there is a test case with the same name, change the name of the test case to another meaningful name.

    Provide the test case in a python code block. DONT add any additional text since the file will be executed to verify the correctness of the test cases.
    '''
    response = model_session.prompt(user_prompt_3, True)
    new_test_case = check_correct_format(response)
    print("\n function name check: \n",response)
        #Save the test case data
    
    test_case_info_ref= f''' 
###########################################################
# Test case Refinement- {counter}
###########################################################\n
System promp: \n
{system_prompt}\n
User prompt:\n
{user_prompt_2}
\n
***********************************************************
* Model Response 
***********************************************************
{response} 

Post processing: 
{new_test_case} \n\n  '''

    with open(test_case_log, 'a') as file:
        file.write(test_case_info_ref)

    helper.append_test_case(new_python_file_path, new_test_case)

