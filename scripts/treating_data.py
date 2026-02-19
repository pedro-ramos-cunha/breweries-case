import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import json
import os
import sqlite3
from sqlalchemy import create_engine

## Setting configs ---------------------------------------------------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))                   # File Base directory
json_path = os.path.join(base_dir, "..", "data", "breweries_data.json") # Path to the raw JSON file (Bronze Layer)
data_path = os.path.join(base_dir, "..", "data") # Path to the output Parquet file (Silver Layer)

## Read the raw JSON file --------------------------------------------------------------------

with open(json_path, 'r') as f:
    data = json.load(f)

## Convert to DataFrame for easier transformation --------------------------------------------
## Due the size of data, pandas can handle it fine, but if the data was too big, 
## I would consider using Dask or PySpark for distributed processing.
df = pd.DataFrame(data)

## Basic transformations (Silver Layer requirements)--------------------------------------------
## * Accordin to API documentation, fields 'state' and 'street'
##   are deprecated, so I will drop than and use 'state_province' and 'address_1' instead.
df = df.drop(columns=['state', 'street'], errors='ignore')

## Convert Pandas DataFrame to PyArrow Table ---------------------------------------------------
table = pa.Table.from_pandas(df)

## Write to Parquet with Partitioning ----------------------------------------------------------
## After a preliminary analysis of the data, I decided to partition the Parquet file by 
## * Country
## * State/Province
## This will allow for more efficient querying and data retrieval based on these common dimensions.

pq.write_to_dataset(
    table,
    root_path=data_path+"/breweries_data_by_country_and_state.parquet",
    partition_cols=['country', 'state_province'],
    compression='snappy'
)
pq.write_to_dataset(
    table,
    root_path=data_path+"/breweries_data_by_type.parquet",
    partition_cols=['brewery_type'],
    compression='snappy'
)

engine = create_engine('sqlite:///'+data_path+'\\brewery_case.db', echo=False)
print(df.to_sql('breweries_semi_treated',engine, if_exists='replace', index=False))

connection = engine.raw_connection()
cursor = connection.cursor()

with open(f"{base_dir}\\database_scheme.sql", 'r', encoding='utf-8') as file:
        sql_query = file.read()
cursor.executescript(sql_query)

with open(f"{base_dir}\\database_integrity.sql", 'r', encoding='utf-8') as file:
        sql_query = file.read()
cursor.executescript(sql_query)
connection.commit()
