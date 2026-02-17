
import requests as rq
from pyspark.sql import SparkSession
import pyarrow.parquet as pq


a = rq.get(url=r"https://api.openbrewerydb.org/v1/breweries").json()
##spark = SparkSession.builder.getOrCreate()


