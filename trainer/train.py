import os

import aim

def train_model(output_dir_path):
    print(output_dir_path)
    os.makedirs(output_dir_path, exist_ok=True)
    run = aim.Run(repo=os.environ["WP_AIM_REPO"])
    print(run.hash)
