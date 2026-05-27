from dotenv import load_dotenv
from .util.model_lib import Session
from .util import file_handler as helper
from .util import verify_response as validate
import argparse
import os 
import json

#############################################
# Handle input arguments
#############################################
load_dotenv()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define default paths relative to the script directory
default_module_file_path = os.path.join(script_dir, '../data/queue_example/queue_example.py')
default_test_file_path = os.path.join(script_dir, '../data/queue_example/test_queue_example.py')


# Mistral-7B as default for debugging
default_model = "../.cache/models--mistralai--Mistral-7B-Instruct-v0.2/snapshots/cf47bb3e18fe41a5351bc36eef76e9c900847c89"

# Creating Argument Parser object
parser = argparse.ArgumentParser(description="Process file information.")

# Adding arguments
parser.add_argument("-m", "--model", dest="model", type=str, default= "mistral_debugger",
                    help="Set the model to use")

parser.add_argument("-s", "--session", dest="session", type=str, default="session",
                    help="Customize session name")

parser.add_argument('-pt', '--path_test', dest="path_test", type=str, default=default_test_file_path,
                    help='Path to the test suite file')

parser.add_argument('-pm', '--path_module', dest="path_module", type=str, default=default_module_file_path,
                    help='Path to the module file')
parser.add_argument('-t', '--temperature', dest="temperature", type=str, default=0.7,
                    help='Path to the module file')

args = parser.parse_args()

model: str = args.model.lower()
session: str = args.session
test_file_path = args.path_test
module_file_path = args.path_module
temperature = args.temperature #Default 0.7

session_name: str = f"{session}_temp{temperature}"

#############################################
# Setup output directory and files
#############################################

# Generate a timestamp
timestamp = helper.generate_timestamp()

#Create a new test file name
base_name= os.path.basename(test_file_path)
name, extension = os.path.splitext(base_name)
directory = f"./output/{model}/{session_name}/{timestamp}/"
new_test_file= f"{name}_refactored"
test_path = directory + new_test_file


#Create a new json file name
json_path = f"{directory}{session_name}" 

#############################################
# Extract imports and test cases
#############################################

# Extract imports and test cases from a test suite file
imports,test_cases = helper.extract_tests(test_file_path)
module_under_test = helper.read_python_file(module_file_path)

import_statements = '\n'.join(imports) + '\n'

#############################################
# Load model
#############################################
if model == "mixtral":
        model_path = os.getenv("MIXTRAL")
        max_new_tokens = int(os.getenv("TOKEN_LIMIT"))
elif model == "llama":
        model_path = os.getenv("LLAMA")
        max_new_tokens = int(os.getenv("TOKEN_LIMIT")) 
else: 
    model_path = default_model
    max_new_tokens = int(os.getenv("TOKEN_LIMIT"))
    

system_prompt: str = "You are a system that improve code readaility."


session: Session = Session.create(
    session_name,
    model_path,
    max_new_tokens,
    system_prompt,
    temperature
)

print("Session created: ", session_name)
print("\n")

def save_log(comment, system_prompt, user_prompt, response):
    response_data = [{
    "comment": comment,
    "system prompt": system_prompt,
    "user prompt": user_prompt,
    "response": response
    }]

    return response_data


#############################################
# Imports
#############################################

user_prompt = f"""I will provide you imports name and you will improve the the variable names and formatting to use meaningful variable names and format the code according to PEP 8.

The response MUST follow this format:
```
    [insert new import statements]
```
I will parse the response, therefore, ONLY ANSWER IN THE FORM I GAVE YOU.
Here are the import statements from the test suite file:
{import_statements}
"""

response = session.prompt(user_prompt, True)
#response = "```python\nimport pytest\nimport queue_example as queue_module\n```"

import_data = [{
    "system prompt": system_prompt,
    "user prompt": user_prompt,
    "response": response
}]


helper.create_json_file(directory, session_name, import_data)

#Start creating the file
helper.create_python_file(directory, new_test_file, response)

#############################################
# Test cases
#############################################

# test_case = test_cases[0]
length = len(test_cases)
print("\n" + str(length) + "\n")


new_test_cases = []


counter = 0

test_case_log_directory = f"{directory}/test_case_logs/"

for test_case in test_cases:
    counter += 1
    print(f"Test case: {counter} \n")

    user_prompt_v1 = f'''
    Here is the module: {module_under_test}

    I will provide you with a test case from the test suite file and rename the test and variables with informative names, add constants and separate setup, execution and assertion and remove type checking assertions. Then add comments to explain the test case and actions taken and code coverage achived  by the modified test case.
    Here are the test file new imports to used: {response}    
    Here is the test case to improve:
    {test_case}

    The response SHOULD ONLY contain the refactored test case in a  python code block. 
    '''

    new_test_v1 = session.prompt(user_prompt_v1, True)
    #new_test_v1 = "```python\n First response\n```"
    
    print("Model response: \n")
    print(new_test_v1)

    log_data = save_log(f"prompt_v1 constants_{counter}",system_prompt, user_prompt_v1, new_test_v1)
    
    helper.append_json_file(f"{directory}{session_name}", log_data)

    #new_test_v1 = validate.check_correct_format(new_test_v1)
    

    #############################################
    # Third change
    #############################################

    refactored_test_file = helper.read_python_file(test_path + ".py")

    print("\n Current test file")
    print(refactored_test_file)
    
    #session.clear_history()

    user_prompt_v3 = f'''
    Here is a test case: {new_test_v1}
    Add the test case to this file: {refactored_test_file}
    If there is a test case with the same name, change the name of the test case to another meaningful name.

    Provide the new test suite file in a python code block. DONT add any additional text since the file will be executed to verify the correctness of the test cases.
    '''

    test_suite= session.prompt(user_prompt_v3, True)

    #test_suite = f"```python\n New Test Suite response{counter} \n```"
    print(test_suite)
    log_data = save_log(f"Final test_{counter}",system_prompt, user_prompt_v3, test_suite)
    helper.append_json_file(f"{directory}{session_name}", log_data)
   # test_suite = validate.check_correct_format(test_suite)

    #Start creating the file
    test_file_version = f"{new_test_file}_v{counter}"
    print(test_file_version)


    helper.create_python_file(test_case_log_directory, test_file_version, test_suite)
    helper.create_python_file(directory, new_test_file ,test_suite)

    














