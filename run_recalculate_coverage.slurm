#!/bin/bash
#SBATCH --job-name=recalc_cov
#SBATCH --output=slurm_logs/recalc_cov_%j.out
#SBATCH --error=slurm_logs/recalc_cov_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH -A naiss2026-3-104-gpu
#SBATCH -p gpu
#SBATCH --gpus=1
#SBATCH --mem=32G
#SBATCH --time=02:00:00

cd /nobackup/proj/disk/llm-readability/shared/thesis/llm-test-readability
mkdir -p slurm_logs

echo "========================================="
echo "Starting coverage recalculation on $(hostname) at $(date)"
echo "Python: $(which python3)"
echo "========================================="

source /nobackup/proj/disk/llm-readability/shared/llm-test-readability/venv_gpu/bin/activate

python3 -u recalculate_coverage.py output

echo "========================================="
echo "Finished execution at $(date)"
echo "========================================="
