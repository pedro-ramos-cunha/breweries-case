
import sqlite3
import os
## Setting configs ---------------------------------------------------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))                   # File Base directory
database_path = os.path.join(base_dir, "..", "data", "brewery_case.db") # Path to the output Parquet file (Silver Layer)
with sqlite3.connect(database_path) as connection:
    cursor = connection.cursor()

    with open(f"{base_dir}\\database_calculated_tables.sql", 'r', encoding='utf-8') as file:
        sql_query = file.read()
    cursor.executescript(sql_query)
    connection.commit()