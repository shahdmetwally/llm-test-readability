import pytest
import os
import sys
import re
import subprocess
import json
from io import StringIO

BASE_PATH_TO_STRIP = "/cephyr/NOBACKUP/groups/llm-readability/readability"


WORKER_SCRIPT = """
import os
os.environ["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
import sys
import coverage
import pytest

test_path = sys.argv[1]
module_path = sys.argv[2]
run_dir = sys.argv[3]
extra_target = sys.argv[4] if len(sys.argv) > 4 else None

if run_dir not in sys.path:
    sys.path.insert(0, run_dir)

candidates = [os.path.realpath(module_path)]
if extra_target and os.path.exists(extra_target):
    candidates.append(os.path.realpath(extra_target))

cov = coverage.Coverage(include=candidates)
cov.start()
try:
    ret = pytest.main([test_path, "-p", "no:langsmith", "-q"])
except Exception:
    ret = -1
cov.stop()

measured = [os.path.realpath(m) for m in cov.get_data().measured_files()]
target = candidates[0]
for candidate in candidates:
    if candidate in measured:
        target = candidate
        break

try:
    _, statements, missing, _ = cov.analysis(target)
    total = len(statements)
    executed = total - len(missing)
    percent = round((executed / total) * 100, 2) if total > 0 else 0.0
except Exception:
    percent, executed, total = 0.0, 0, 0

print(json.dumps({
    "percent": percent,
    "executed": executed,
    "total": total,
    "exit_code": int(ret)
}))
"""


def run_pytest_with_coverage(test_files, output_dir, modules_under_test=None, label=None):
    """
    Run pytest with the canonical coverage calculation used by
    recalculate_coverage.py.
    """
    test_list = test_files if isinstance(test_files, list) else [test_files]
    test_list = [os.path.abspath(str(f)) for f in test_list if os.path.exists(str(f))]
    if not test_list:
        return "N/A"

    candidates = []
    if output_dir and os.path.exists(output_dir):
        for filename in os.listdir(output_dir):
            if filename.endswith(".py") and not filename.startswith("test_") and "_refactored" not in filename:
                candidate = os.path.abspath(os.path.join(output_dir, filename))
                if candidate not in candidates:
                    candidates.append(candidate)

    if not candidates and modules_under_test:
        module_list = modules_under_test if isinstance(modules_under_test, list) else [modules_under_test]
        candidates.extend(
            os.path.abspath(str(module))
            for module in module_list
            if module and os.path.exists(str(module))
        )

    if not candidates:
        return "N/A"

    extra_target = None
    if "plugins_base" in os.path.abspath(output_dir):
        try:
            import httpie.plugins.base
            extra_target = os.path.realpath(httpie.plugins.base.__file__)
        except ImportError:
            pass

    run_dir = os.path.abspath(output_dir)
    args = [sys.executable, "-c", WORKER_SCRIPT, test_list[0], candidates[0], run_dir]
    if extra_target:
        args.append(extra_target)

    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=run_dir,
            check=False,
        )
        for line in reversed(result.stdout.strip().splitlines()):
            if line.startswith("{") and line.endswith("}"):
                return json.loads(line).get("percent", 0.0)
        if result.stderr:
            print(f"Coverage collection failed for {test_list[0]}: {result.stderr.strip()[:300]}")
        return 0.0
    except subprocess.TimeoutExpired:
        print(f"Coverage collection timed out for {test_list[0]}")
        return 0.0


def run_pytest_and_collect_results(test_files, modules_under_test):
    """
    Run pytest on single or multiple test files and return detailed results
    including collection errors.
    Returns: dict(label -> {test_name -> status})
    """
    detailed_results = {}

    items = test_files.items() if isinstance(test_files, dict) else [("Tests", test_files)]

    for label, files in items:
        test_list = [os.path.abspath(str(f)) for f in (files if isinstance(files, list) else [files])]

        results_for_label = {}

        for test_file in test_list:
            if not os.path.exists(test_file):
                results_for_label[test_file] = "error: file not found"
                continue

            try:
                # Insert modules into sys.path
                for module_path in modules_under_test:
                    abs_module_path = os.path.abspath(module_path)
                    if abs_module_path not in sys.path:
                        sys.path.insert(0, abs_module_path)

                    captured_output = StringIO()
                    sys.stdout = captured_output
                    sys.stderr = captured_output
                    try:
                        pytest.main([test_file, "-q", "--tb=short"], plugins=[ResultCollector(results_for_label)])
                    finally:
                        sys.stdout = sys.__stdout__
                        sys.stderr = sys.__stderr__

                    # Save captured output
                    results_for_label["_captured_output"] = captured_output.getvalue()

            except Exception as e:
                results_for_label[test_file] = f"error: {str(e)}"

            if not results_for_label:
                results_for_label["Collection Error"] = "Test collection failed"

        detailed_results[label] = results_for_label

    return detailed_results

def extract_failed_tests(pytest_output, file_path):
    """
    Extract failed test cases from pytest output.
    Returns a dictionary like:
    {
        file_path: {
            "test_name": "failure details",
            ...
        }
    }
    """
    failures = {}
    current_test = None
    failure_details = []

    for line in pytest_output.splitlines():
        match = re.match(r"^(.*::.*)\s+FAILED", line)
        if match:
            if current_test and failure_details:
                failures[current_test] = "\n".join(failure_details)
                failure_details = []
            current_test = match.group(1)

        elif current_test:
            if line.startswith("=" * 10):
                failures[current_test] = "\n".join(failure_details)
                current_test = None
            else:
                failure_details.append(line)

    if current_test and failure_details:
        failures[current_test] = "\n".join(failure_details)

    return {file_path: failures} if failures else None


class ResultCollector:
    """
    Pytest plugin to collect individual test outcomes.
    """
    def __init__(self, results_dict):
        self.results = results_dict
        self.collection_failed = False

    def pytest_collectreport(self, report):
        if report.failed:
            self.collection_failed = True
            self.results["Collection Error"] = "Test collection failed"

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            test_name = report.nodeid.split("::")[-1] if "::" in report.nodeid else report.nodeid
            outcome = "pass" if report.passed else "fail" if report.failed else "error"
            self.results[test_name] = outcome


def run_pytest_and_log_results(test_files, modules_under_test, output_dir, combined=False):
    """
    Run pytest on provided test files, log outputs, compute coverage.
    Returns:
        failed_tests (dict),
        test_summary (dict),
        coverage_summary (dict),
        test_ran_status (dict),
        detailed_results (dict)
    """
    os.makedirs(output_dir, exist_ok=True)
    failed_tests = {}
    test_summary = {}
    test_ran_status = {}

    # Normalize test file paths
    normalized_test_files = {
        label: [os.path.abspath(str(f)) for f in (files if isinstance(files, list) else [files])]
        for label, files in (test_files.items() if isinstance(test_files, dict) else [("Tests", test_files)])
    }
    coverage_summary = {}

    detailed_results = run_pytest_and_collect_results(normalized_test_files, modules_under_test)

    # Coverage per test set
    for label, files in normalized_test_files.items():
        coverage_summary[label] = run_pytest_with_coverage(
            files, output_dir, modules_under_test=modules_under_test, label=label
        )

    # Build summary and logs
    for label, results in detailed_results.items():
        collection_failed = "Collection Error" in results
        if not collection_failed:
            captured_output = results.get("_captured_output", "")
            exit_code = results.get("_exit_code", 1)
            if exit_code != 0 and "collected 0 items / 1 error" in captured_output:
                results["Collection Error"] = True
                collection_failed = True

        real_tests = {k: v for k, v in results.items() if k != "Collection Error"}

        total = len(real_tests)
        passed = sum(1 for v in real_tests.values() if v == "pass")
        failed = sum(1 for v in real_tests.values() if v == "fail")
        errors = sum(1 for v in real_tests.values() if v == "error")

        test_summary[label] = {"total": total, "pass": passed, "fail": failed, "error": errors}
        test_ran_status[label] = (not collection_failed and total > 0)
        failed_tests[label] = {k: v for k, v in real_tests.items() if v in ("fail", "error")}

        clean_results = {
            (k.replace(BASE_PATH_TO_STRIP, "") if BASE_PATH_TO_STRIP in k else k): v
            for k, v in real_tests.items()
        }
        log_file_path = os.path.join(output_dir, f"{label.replace(' ', '_').lower()}_pytest.log")
        with open(log_file_path, "w") as f:
            json.dump({"collection_failed": collection_failed, "tests": clean_results}, f, indent=2)

    return failed_tests, test_summary, coverage_summary, test_ran_status, detailed_results
