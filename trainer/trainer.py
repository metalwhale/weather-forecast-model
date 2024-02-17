import datetime
import os
import sys

import psycopg2


# Env
database_host = os.environ["WP_INPUT_DATABASE_HOST"]
database_port = os.environ["WP_INPUT_DATABASE_PORT"]
database_db = os.environ["WP_INPUT_DATABASE_DB"]
database_user = os.environ["WP_INPUT_DATABASE_USER"]
database_password = os.environ["WP_INPUT_DATABASE_PASSWORD"]

conn = psycopg2.connect(
    f"host={database_host} port={database_port} user={database_user} password={database_password} dbname={database_db}"
)

# Input
input_start_date = os.environ.get("WP_INPUT_START_DATE", "")
print(input_start_date)

# Kubeflow
print(os.environ.get("WP_KFP_RUN_URL", ""))
print(os.environ.get("WP_KFP_PROFILE", ""))
print(os.environ.get("WP_KFP_RUN_ID", ""))
print(os.environ.get("WP_KFP_EXECUTION_ID", ""))

# Output
output_dir_path = sys.argv[1]
print(output_dir_path)
os.makedirs(output_dir_path, exist_ok=True)
with open(os.path.join(output_dir_path, "output.txt"), "w") as output_file:
    output_file.write("\n".join([
        input_start_date,
        str(datetime.datetime.now()),
    ]) + "\n")
