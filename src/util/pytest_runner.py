import pytest
import os
import sys
import re
import coverage
import json
from io import StringIO

BASE_PATH_TO_STRIP = "/cephyr/NOBACKUP/groups/llm-readability/readability"


def run_pytest_with_coverage(test_files, output_dir):
    """
    Run pytest with coverage tracking using coverage.Coverage API directly.
    Returns the coverage percentage as a float or "N/A" if failed.
    """
    try:
        # Normalize input to a list of absolute test file paths
        test_list = test_files if isinstance(test_files, list) else [test_files]
        test_list = [os.path.abspath(str(f)) for f in test_list if os.path.exists(str(f))]

        if not test_list:
            return "N/A"

        # Initialize coverage tracking
        cov = coverage.Coverage()
        cov.start()

        # Run pytest programmatically with absolute paths
        exit_code = pytest.main(test_list)

        # Stop and save coverage data
        cov.stop()
        cov.save()

        # Generate report data
        cov.json_report(outfile=os.path.join(output_dir, "coverage.json"))
        cov.report(file=open(os.devnull, "w"))  # Silent console report

        # Compute overall coverage percentage
        total_statements = 0
        total_executed = 0

        for filename in cov.get_data().measured_files():
            _, statements, missing, _ = cov.analysis(filename)
            total_statements += len(statements)
            total_executed += len(statements) - len(missing)

        return round((total_executed / total_statements) * 100, 2) if total_statements > 0 else "N/A"

    except Exception as e:
        print(f"Coverage collection failed: {e}")
        return "N/A"


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
    coverage_summary = {}
    test_ran_status = {}

    # Normalize test file paths
    normalized_test_files = {
        label: [os.path.abspath(str(f)) for f in (files if isinstance(files, list) else [files])]
        for label, files in (test_files.items() if isinstance(test_files, dict) else [("Tests", test_files)])
    }

    detailed_results = run_pytest_and_collect_results(normalized_test_files, modules_under_test)

    # Coverage per test set
    for label, files in normalized_test_files.items():
        coverage_summary[label] = run_pytest_with_coverage(files, output_dir)

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
