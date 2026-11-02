import os
import sys
import glob
import json
import csv
import subprocess
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

WORKER_SCRIPT = """
import os
os.environ["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
import sys
import json
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
except Exception as e:
    ret = -1
cov.stop()

measured = [os.path.realpath(m) for m in cov.get_data().measured_files()]
target = candidates[0]
for c in candidates:
    if c in measured:
        target = c
        break

try:
    _, stmts, missing, _ = cov.analysis(target)
    total = len(stmts)
    executed = total - len(missing)
    pct = round((executed / total) * 100, 2) if total > 0 else 0.0
except Exception as e:
    pct, executed, total = 0.0, 0, 0

print(json.dumps({
    "percent": pct,
    "executed": executed,
    "total": total,
    "exit_code": int(ret)
}))
"""

def run_single_coverage(test_path, module_path, run_dir, extra_target=None, timeout=30):
    try:
        args = [sys.executable, "-c", WORKER_SCRIPT, test_path, module_path, run_dir]
        if extra_target:
            args.append(extra_target)
        proc = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=run_dir
        )
        # Parse last line of stdout
        lines = [line.strip() for line in proc.stdout.strip().splitlines() if line.strip()]
        for line in reversed(lines):
            if line.startswith("{") and line.endswith("}"):
                data = json.loads(line)
                return data.get("percent", 0.0), data.get("executed", 0), data.get("total", 0)
        if proc.stderr:
            print(f"  [STDERR] {test_path}:\n{proc.stderr.strip()[:300]}")
        return 0.0, 0, 0
    except subprocess.TimeoutExpired:
        print(f"  [TIMEOUT] {test_path} exceeded {timeout}s")
        return 0.0, 0, 0
    except Exception as e:
        print(f"  [ERROR] {test_path}: {e}")
        return 0.0, 0, 0

def process_report(report_path):
    report_path = os.path.abspath(report_path)
    run_dir = os.path.abspath(os.path.dirname(report_path))
    try:
        with open(report_path, "r") as f:
            report = json.load(f)
            
        py_files = [f for f in os.listdir(run_dir) if f.endswith(".py")]
        module_files = [f for f in py_files if not f.startswith("test_") and "_refactored" not in f]
        orig_test_files = [f for f in py_files if f.startswith("test_") and "_refactored" not in f]
        ref_test_files = [f for f in py_files if "_refactored" in f]
        
        if not module_files or not orig_test_files or not ref_test_files:
            return report_path, False, "Missing required .py files in run directory"
            
        module_path = os.path.abspath(os.path.join(run_dir, module_files[0]))
        orig_test_path = os.path.abspath(os.path.join(run_dir, orig_test_files[0]))
        ref_test_path = os.path.abspath(os.path.join(run_dir, ref_test_files[0]))

        extra_target = None
        if "plugins_base" in run_dir:
            try:
                import httpie.plugins.base
                extra_target = os.path.realpath(httpie.plugins.base.__file__)
            except ImportError:
                pass
        
        orig_pct, orig_exec, orig_tot = run_single_coverage(orig_test_path, module_path, run_dir, extra_target=extra_target)
        ref_pct, ref_exec, ref_tot = run_single_coverage(ref_test_path, module_path, run_dir, extra_target=extra_target)
        
        diff_pct = round(ref_pct - orig_pct, 2)
        
        # Update JSON report
        if "coverage" not in report:
            report["coverage"] = {}
        report["coverage"]["before_refactoring"] = orig_pct
        report["coverage"]["after_refactoring"] = ref_pct
        
        if "diff_metrics" not in report:
            report["diff_metrics"] = {}
        report["diff_metrics"]["diff_coverage"] = diff_pct
        
        with open(report_path, "w") as f:
            json.dump(report, f, indent=4)
            
        # Update CSV report if it exists
        csv_path = report_path.replace(".json", ".csv")
        if os.path.exists(csv_path):
            rows = []
            fieldnames = []
            with open(csv_path, "r", newline="") as cf:
                reader = csv.DictReader(cf)
                fieldnames = reader.fieldnames
                for row in reader:
                    row["original_coverage"] = orig_pct
                    row["refactored_coverage"] = ref_pct
                    row["diff_coverage"] = diff_pct
                    rows.append(row)
            if rows and fieldnames:
                with open(csv_path, "w", newline="") as cf:
                    writer = csv.DictWriter(cf, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                    
        return report_path, True, f"Orig: {orig_pct}% -> Ref: {ref_pct}% (Diff: {diff_pct}%)"
    except Exception as e:
        return report_path, False, str(e)

def main():
    base_dir = sys.argv[1] if len(sys.argv) > 1 else "output"
    pattern = f"{base_dir}/*/*/*/*/*/test_run_report.json"
    reports = sorted(glob.glob(pattern))
    
    # If standard 5-level pattern didn't match all, try recursive fallback
    if not reports:
        reports = sorted(glob.glob(f"{base_dir}/**/test_run_report.json", recursive=True))
        
    print(f"Found {len(reports)} reports to process in '{base_dir}'.")
    if not reports:
        print("No reports found. Exiting.")
        return

    start_time = time.time()
    num_workers = min(16, os.cpu_count() or 4)
    print(f"Processing with {num_workers} parallel workers...\n")
    
    success_count = 0
    fail_count = 0
    
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(process_report, r): r for r in reports}
        for i, fut in enumerate(as_completed(futures)):
            rep_path, ok, msg = fut.result()
            rel_path = os.path.relpath(rep_path, base_dir)
            if ok:
                success_count += 1
                print(f"[{i+1}/{len(reports)}] OK: {rel_path} | {msg}")
            else:
                fail_count += 1
                print(f"[{i+1}/{len(reports)}] FAIL: {rel_path} | {msg}")
                
    elapsed = round(time.time() - start_time, 2)
    print(f"\n==========================================")
    print(f"Finished recalculating coverage in {elapsed}s.")
    print(f"Total reports: {len(reports)}")
    print(f"Successful updates: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"==========================================")

if __name__ == "__main__":
    main()
