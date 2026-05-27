#!/bin/bash
#SBATCH --job-name=temp1_combined
#SBATCH --output=slurm_logs/slurm-%j.out
#SBATCH --error=slurm_logs/slurm-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=24:00:00
#SBATCH -p long

# =============================================================================
# Run ALL models × ALL modules with temperature=1, prompt-type=combined
#
# Usage (SLURM):   sbatch run_all_temp1_combined.sh
# Usage (direct):  bash  run_all_temp1_combined.sh
#
# Override defaults with environment variables:
#   MODELS="mini sonnet"  bash run_all_temp1_combined.sh
#   RUNS="1 2 3"          bash run_all_temp1_combined.sh
# =============================================================================

set -euo pipefail

# --- Configuration (override via env vars) -----------------------------------
TEMPERATURE=1
VERSION="functions"
PROMPT_TYPE="base"
MODELS="${MODELS:-deepseek-v3}"
RUNS="${RUNS:-1 2 3}"

# --- Timestamps & logging ----------------------------------------------------
timestamp=$(date +%Y%m%d_%H%M%S)
log_dir="slurm_logs/$timestamp"
mkdir -p "$log_dir"

echo "============================================"
echo "Job running on $(hostname)"
echo "Date: $(date)"
echo "Temperature: $TEMPERATURE"
echo "Prompt type: $PROMPT_TYPE"
echo "Version:     $VERSION"
echo "Models:      $MODELS"
echo "Runs:        $RUNS"
echo "============================================"

# --- Environment -----------------------------------------------   ---------------
export HF_HOME=${HOME}/.cache/huggingface

# GPU debug info (only meaningful on SLURM nodes with GPUs)
if command -v nvidia-smi &>/dev/null; then
    nvidia-smi || true
    echo "CUDA_VISIBLE_DEVICES: ${CUDA_VISIBLE_DEVICES:-not set}"
    echo "SLURM_JOB_GPUS: ${SLURM_JOB_GPUS:-not set}"
    python3 -c "import torch; print(f'Torch sees {torch.cuda.device_count()} GPUs')" 2>/dev/null || true
fi

# --- Auto-discover module ↔ test pairs from data/ ----------------------------
# Each subfolder in data/ (excluding "old") contains exactly one .py module file
# (not starting with test_) and one test file (starting with test_).

DATA_DIR="data"

declare -a MODULE_PATHS=()
declare -a TEST_PATHS=()
declare -a MODULE_NAMES=()

for module_dir in "$DATA_DIR"/*/; do
    dirname=$(basename "$module_dir")

    # Skip non-module directories
    [[ "$dirname" == "old" ]] && continue
    [[ "$dirname" == "__pycache__" ]] && continue

    # Find the module file (*.py, not test_*)
    module_file=""
    test_file=""
    for f in "$module_dir"*.py; do
        base=$(basename "$f")
        if [[ "$base" == test_* ]]; then
            test_file="$f"
        elif [[ "$base" != __* ]]; then
            module_file="$f"
        fi
    done

    if [[ -z "$module_file" || -z "$test_file" ]]; then
        echo "WARNING: Skipping $dirname — could not find module/test pair"
        continue
    fi

    MODULE_PATHS+=("$module_file")
    TEST_PATHS+=("$test_file")
    MODULE_NAMES+=("$dirname")
done

echo ""
echo "Discovered ${#MODULE_PATHS[@]} modules:"
for i in "${!MODULE_NAMES[@]}"; do
    echo "  [$i] ${MODULE_NAMES[$i]}"
    echo "       module: ${MODULE_PATHS[$i]}"
    echo "       test:   ${TEST_PATHS[$i]}"
done
echo ""

# --- Main loop: models × modules × runs --------------------------------------
total=0
failed=0

for model in $MODELS; do
    for i in "${!MODULE_PATHS[@]}"; do
        module_path="${MODULE_PATHS[$i]}"
        test_path="${TEST_PATHS[$i]}"
        module_name="${MODULE_NAMES[$i]}"

        for run in $RUNS; do
            total=$((total + 1))
            echo ""
            echo "================================================================"
            echo "[$total] Model: $model | Module: $module_name | Run: $run"
            echo "    module_path: $module_path"
            echo "    test_path:   $test_path"
            echo "    temperature: $TEMPERATURE | prompt: $PROMPT_TYPE | version: $VERSION"
            echo "================================================================"

            if python3 -m src.main \
                -p "$module_path" \
                -tp "$test_path" \
                -m "$model" \
                -t "$TEMPERATURE" \
                -v "$VERSION" \
                --prompt-type "$PROMPT_TYPE" \
                --run "$run"; then
                echo "✓ Finished: $model / $module_name / run$run"
            else
                echo "✗ FAILED:   $model / $module_name / run$run (exit code $?)"
                failed=$((failed + 1))
            fi
        done
    done
done

# --- Summary ------------------------------------------------------------------
echo ""
echo "============================================"
echo "ALL DONE — $(date)"
echo "Total runs:  $total"
echo "Succeeded:   $((total - failed))"
echo "Failed:      $failed"
echo "============================================"

# --- Move SLURM logs ---------------------------------------------------------
if [ -n "${SLURM_JOB_ID:-}" ]; then
    echo "Moving SLURM logs to $log_dir"
    cp "slurm_logs/slurm-${SLURM_JOB_ID}.out" "$log_dir/" 2>/dev/null || true
    cp "slurm_logs/slurm-${SLURM_JOB_ID}.err" "$log_dir/" 2>/dev/null || true
    rm -f "slurm_logs/slurm-${SLURM_JOB_ID}.out"
    rm -f "slurm_logs/slurm-${SLURM_JOB_ID}.err"
fi
