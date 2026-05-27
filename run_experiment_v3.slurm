#!/bin/bash
#SBATCH --job-name=llm_refactor_v3
#SBATCH --output=slurm_logs/slurm-%j.out
#SBATCH --error=slurm_logs/slurm-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=4
#SBATCH --time=08:00:00
#SBATCH -p long

# Create logs directory if it doesn't exist
# Create timestamped directory for logs
timestamp=$(date +%Y%m%d_%H%M%S)
log_dir="slurm_logs/$timestamp"
mkdir -p "$log_dir"

# Print some node info
echo "Job running on $(hostname)"
echo "Date: $(date)"

llm-test-readability/slurm_logs# Set environment variables for Hugging Face
export HF_HOME=${HOME}/.cache/huggingface
# Debugging Info
echo "Running debug checks..."
nvidia-smi
echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
echo "SLURM_JOB_GPUS: $SLURM_JOB_GPUS"
echo "SLURM_GPUS_ON_NODE: $SLURM_GPUS_ON_NODE"
python3 -c "import torch; print(f'Torch sees {torch.cuda.device_count()} GPUs')"

# Run the pipeline
echo "Starting execution..."

python3 -m src.main -m deepseek-v3 -t 1 -v functions --prompt-type combined --run 1

echo "Execution finished at $(date)"

# Move SLURM logs to the timestamped directory
if [ -n "$SLURM_JOB_ID" ]; then
    echo "Moving SLURM logs to $log_dir"
    # Copy to timestamped dir
    cp "slurm_logs/slurm-${SLURM_JOB_ID}.out" "$log_dir/"
    cp "slurm_logs/slurm-${SLURM_JOB_ID}.err" "$log_dir/"
    
    # Remove originals (clean up)
    rm "slurm_logs/slurm-${SLURM_JOB_ID}.out"
    rm "slurm_logs/slurm-${SLURM_JOB_ID}.err"
fi
