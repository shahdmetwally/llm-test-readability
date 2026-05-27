#!/bin/bash
#SBATCH -p long
#SBATCH -t 0-04:00:00
#SBATCH --gpus-per-node=1
#SBATCH -o jobs/out/deepseek_functions_%j.log

# Load modules (if needed, or rely on user environment)
# module load python  # Uncomment if python module is needed specific versions

# Ensure we are in the project root
# cd /path/to/project_root # Optional: if you submit from elsewhere

echo "Starting job on $(hostname)"
echo "Python: $(which python3)"

# Tokens loaded automatically from .env

# Run the command directly
python3 -m src.main -m deepseek-coder -t 1.0 -v functions

echo "Job finished"


# sbatch 117893 