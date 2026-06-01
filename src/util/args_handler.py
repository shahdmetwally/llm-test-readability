import argparse
import os

def validate_version(version):
    """Ensure the version string matches one of the expected options."""
    valid_versions = ["mix", "mix-cleanup", "summarize", "summarize-cleanup", "functions", "functions-cleanup"]
    if version not in valid_versions:
        raise ValueError(f"Invalid version '{version}'. Expected one of {valid_versions}.")
    

def get_args():
    parser = argparse.ArgumentParser(description='Process some file paths.')
    # Default module path
    ''''
    default_module_paths = [
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/codetiming/codetiming_timer.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.decorators/decorators.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.namedtupleutils/namedtupleutils.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.packages/packages.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.setuputils.cmd/cmd.py"
    ]
    '''

    default_module_path = ["data/pymonet.immutable_list/immutable_list.py"]

    parser.add_argument(
        '-p', '--paths',
        dest='paths',
        default=default_module_path, 
        type=str, 
        nargs='+', 
        help='at least one file path'
        #,required=True
    )

    # Default test path
    ''''
    default_test_path = [
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/codetiming/test_codetiming__timer.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.decorators/test_flutils_decorators.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.namedtupleutils/test_flutils_namedtupleutils.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.packages/test_flutils_packages.py",
        "/cephyr/NOBACKUP/groups/llm-readability/readability/data/flutils.setuputils.cmd/test_flutils_setuputils_cmd.py"
    ]
    '''

    default_test_path = "data/pymonet.immutable_list/test_pymonet_immutable_list.py"

    parser.add_argument("-tp", "--testpath",
                        dest="testpath",
                        type=str,
                        default=default_test_path,
                        help="The path to the test class")

    parser.add_argument("-m", "--model", dest="model", type=str, default="mistral_debugger",
                        help="Set the model to use")

    parser.add_argument("-s", "--session", dest="session", type=str, default="session",
                        help="Customize session name")

    parser.add_argument("-j", "--job", dest="job", type=str, default="job",
                        help="Customize job name")
    

    # if "cleanup" in version, is used in refactorManager assetion_cleanup()
    parser.add_argument("-v", "--scriptversion", dest="version", type=str, default="mix",
                        help="Set the script to run, default is 'mix. Alternative: mix, summarize, summarize-cleanup, mix-cleanup, functions, functions-cleanup")

    parser.add_argument('-t', '--temperature', dest="temperature", type=float, default=0.7,
                        help='Set the temperature')
                        
    parser.add_argument("--no-rag", dest="no_rag", action="store_true", default=False,
                        help="Disable RAG functionality")

    parser.add_argument("--prompt-type", dest="prompt_type", type=str, default="base",
                        help="Select prompt strategy: 'base' (default) or 'self_critique'")

    parser.add_argument("--run", dest="run", type=int, default=1,
                        help="Run number for the experiment")

    args = parser.parse_args()

    # Post-processing of parsed arguments
    args.test_path = os.path.join(os.getcwd(), args.testpath) if args.testpath else None
    args.model = args.model.lower()
    args.session_name = f"{args.session}_temp{args.temperature}"
    args.version = args.version.lower()
    validate_version(args.version)
    
    return args


def test_arguments():
    args = get_args()
    print(args)
    print("Modules:", args.module)
    print("Test Files:", args.testpath)

def test_module():
    print("Executing script_arguments.py")

#test_arguments()