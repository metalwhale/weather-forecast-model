import os

import psycopg2

def fetch_data():
    database_host = os.environ["WP_INPUT_DATABASE_HOST"]
    database_port = os.environ["WP_INPUT_DATABASE_PORT"]
    database_db = os.environ["WP_INPUT_DATABASE_DB"]
    database_user = os.environ["WP_INPUT_DATABASE_USER"]
    database_password = os.environ["WP_INPUT_DATABASE_PASSWORD"]
    cursor: psycopg2.extensions.cursor = psycopg2.connect(
        f"host={database_host} port={database_port} user={database_user} password={database_password} dbname={database_db}"
    ).cursor()
    input_start_date = os.environ.get("WP_INPUT_START_DATE", "")
    cursor.execute(f"SELECT count(*) FROM historical_weather_daily_records WHERE date >= '{input_start_date}'")
    print(cursor.fetchone())
