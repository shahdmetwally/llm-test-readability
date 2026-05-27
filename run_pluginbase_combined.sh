#!/bin/bash
#SBATCH --job-name=pluginbase_combined
#SBATCH --output=slurm_logs/slurm-%j.out
#SBATCH --error=slurm_logs/slurm-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=02:00:00
#SBATCH -p long

# =============================================================================
# Run sonnet on httpie.plugins.base (prompt-type: combined) for all 3 runs
#
# Usage (SLURM):   sbatch run_pluginbase_combined.sh
# Usage (Direct):  bash run_pluginbase_combined.sh
# =============================================================================

set -euo pipefail

# Environment
export HF_HOME=${HOME}/.cache/huggingface

# Run for all 3 runs sequentially
for run in 1 2 3; do
    echo ""
    echo "================================================================"
    echo "Starting: httpie.plugins.base | sonnet | combined | Run $run"
    echo "================================================================"
    
    python3 -m src.main \
        -p data/httpie.plugins.base/base.py \
        -tp data/httpie.plugins.base/test_httpie_plugins_base.py \
        -m sonnet \
        -t 1 \
        -v functions \
        --prompt-type combined \
        --run "$run"
done

echo ""
echo "============================================"
echo "ALL DONE!"
echo "============================================"
