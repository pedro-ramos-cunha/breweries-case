import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

base_dir = os.path.dirname(os.path.abspath(__file__))                   # File Base directory
data_path = os.path.join(base_dir, "..", "data") # Path to the output Parquet file (Silver Layer)
db_path = os.path.join(base_dir, "..", "data", "brewery_case.db")
