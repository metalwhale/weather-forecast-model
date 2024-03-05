import sys

from .data import fetch_data
from .train import train_model

# Data
fetch_data()

# Training
output_dir_path = sys.argv[1]
train_model(output_dir_path)
