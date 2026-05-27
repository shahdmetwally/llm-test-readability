import os
import csv
import json
from datetime import datetime

class TestRunDataCollector:
    def __init__(self, output_dir, module_name):
        self.module = module_name
        self.timestamp = datetime.now().isoformat()
        self.llm_info = {}
        self.run_number = 1
        self.test_summary = {}
        self.coverage = {}
        self.test_results = {
            "before_refactoring": {},
            "after_refactoring": {}
        }
        self.diff_metrics = {} # To store test counts and coverage diffs
        self.output_path = os.path.join(output_dir, "test_run_report.csv")

    def set_llm_metadata(self, model_name, version, temperature, prompt_style="base", run_number=1):
        self.llm_info = {
            "model": model_name,
            "version": version,
            "temperature": temperature,
            "prompt_style": prompt_style
        }
        self.run_number = run_number

    def set_test_summary(self, test_summary):
        # Extract raw data for differences BEFORE converting to strings
        orig = test_summary.get("Original Test Results")
        ref = test_summary.get("Refactored Test Results")
        
        if isinstance(orig, dict) and isinstance(ref, dict):
            self.diff_metrics["diff_total_tests"] = ref.get("total", 0) - orig.get("total", 0)
            self.diff_metrics["diff_passing_tests"] = ref.get("pass", 0) - orig.get("pass", 0)
            self.diff_metrics["diff_failing_tests"] = ref.get("fail", 0) - orig.get("fail", 0)

        # Ensure values are strings for test_summary dict (existing behavior)
        self.test_summary = {
            key: str(val) if not isinstance(val, (str, int, float)) else val
            for key, val in test_summary.items()
        }


    def set_coverage_data(self, original_coverage, refactored_coverage):
        self.coverage = {
            "before_refactoring": original_coverage,
            "after_refactoring": refactored_coverage
        }
        if isinstance(original_coverage, (int, float)) and isinstance(refactored_coverage, (int, float)):
            self.diff_metrics["diff_coverage"] = round(refactored_coverage - original_coverage, 2)
    
    def set_test_results(self, stage: str, results: dict):
        # Remove any _captured_output entries
        filtered_results = {k: v for k, v in results.items() if k != "_captured_output"}
        self.test_results[stage] = filtered_results

    def set_dan_scores(self, original_score, refactored_score):
        self.test_results["dan_score_before"] = original_score
        self.test_results["dan_score_after"] = refactored_score

        avg_orig = None
        avg_ref = None

        if isinstance(original_score, dict) and original_score:
            vals = [v for v in original_score.values() if isinstance(v, (int, float))]
            if vals:
                avg_orig = round(sum(vals) / len(vals), 6)
                self.test_results["avg_dan_score_before"] = avg_orig

        if isinstance(refactored_score, dict) and refactored_score:
            vals = [v for v in refactored_score.values() if isinstance(v, (int, float))]
            if vals:
                avg_ref = round(sum(vals) / len(vals), 6)
                self.test_results["avg_dan_score_after"] = avg_ref

        if avg_orig is not None and avg_ref is not None:
            self.diff_metrics["dan_score_diff"] = round(avg_orig - avg_ref, 6)

    def save(self):
        row = {
            "module": self.module,
            "timestamp": self.timestamp,
            "llm_model": self.llm_info.get("model", ""),
            "llm_version": self.llm_info.get("version", ""),
            "llm_temperature": self.llm_info.get("temperature", ""),
            "prompt_style": self.llm_info.get("prompt_style", ""),
            "run_number": self.run_number,
            
            # Coverage
            "original_coverage": self.coverage.get("before_refactoring", ""),
            "refactored_coverage": self.coverage.get("after_refactoring", ""),
            "diff_coverage": self.diff_metrics.get("diff_coverage", ""),

            # Test counts differences
            "diff_total_tests": self.diff_metrics.get("diff_total_tests", ""),
            "diff_passing_tests": self.diff_metrics.get("diff_passing_tests", ""),
            "diff_failing_tests": self.diff_metrics.get("diff_failing_tests", ""),

            # DAN Scores - serialize dict to json for CSV
            "dan_score_before": json.dumps(self.test_results.get("dan_score_before", {})),
            "dan_score_after": json.dumps(self.test_results.get("dan_score_after", {})),
            "avg_dan_score_before": self.test_results.get("avg_dan_score_before", ""),
            "avg_dan_score_after": self.test_results.get("avg_dan_score_after", ""),
            "dan_score_diff": self.diff_metrics.get("dan_score_diff", ""),
        }

        # Flatten test_summary instead of dumping
        if isinstance(self.test_summary, dict):
            for key, val in self.test_summary.items():
                # convert objects like ExitCode.TESTS_FAILED into strings
                if not isinstance(val, (str, int, float)):
                    val = str(val)
                row[f"summary_{key}"] = val

        # Optional: add detailed results as JSON (one column per run)
        row["results_before"] = json.dumps(self.test_results["before_refactoring"])
        row["results_after"] = json.dumps(self.test_results["after_refactoring"])

        write_header = not os.path.exists(self.output_path)

        with open(self.output_path, mode="a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            if write_header:
                writer.writeheader()
            writer.writerow(row)

        print(f"Test run data saved to: {self.output_path}")

    def save_json(self):
        json_path = self.output_path.replace(".csv", ".json")
        data = {
            "module": self.module,
            "timestamp": self.timestamp,
            "llm_info": self.llm_info,
            "run_number": self.run_number,
            "diff_metrics": self.diff_metrics,
            "test_summary": self.test_summary,
            "coverage": self.coverage,
            "test_results": self.test_results,
        }
        with open(json_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Test run JSON data saved to: {json_path}")


