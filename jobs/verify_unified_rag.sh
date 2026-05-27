#!/bin/bash
#SBATCH -p long
#SBATCH -t 0-01:00:00
#SBATCH --gpus-per-node=1
#SBATCH -o jobs/out/verify_unified_rag_%j.log

echo "Starting verification job on $(hostname)"

# Tokens loaded automatically from .env

# Run verification command
python3 -m src.main \
    -p data/codetiming/codetiming_timer.py \
    -tp data/codetiming/test_codetiming__timer.py \
    -m deepseek-coder \
    -v functions \
    -t 1.0 \
    -s verification_run

echo "Job finished"
