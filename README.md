# breweries-case
Breweries Case of Data Engineering

## Context

You work as a Data Engineer at a large brewing company, and your mission is to build a
resilient and scalable Data Lake from scratch. To accomplish this, you will consume
data from the Open Brewery DB API, which provides information about breweries and pubs
around the world.

## Instructions

0. Architecture: Describe how you would design the data architecture. Provide a
blueprint or documentation that represents your proposed solution and explains
the main components and data flow.
0. Data Lake Architecture: Your data lake must follow the medallion architecture
having a bronze, silver, and gold layer:
    * Bronze Layer: Persist the raw data from the API in its native format or any
format you find suitable.
    * Silver Layer: Transform the data to a columnar storage format such as
parquet or delta, and partition it by brewery location. Please explain any
other transformations you perform.
    * Gold Layer: Create an aggregated view with the quantity of breweries per
type and location.

0. Language: Use the language of your preference for the requests and data
transformation. Please include test cases for your code. Python and PySpark are
preferred.
0. Orchestration Tool: To monitor your pipelines and schedule executions
continuously choose the orchestration tool of your preference (Airflow, Luigi, Mage
etc.) to build a data pipeline. We're interested in seeing your ability to handle
scheduling, retries, and error handling in the pipeline.
0. Data Quality: Describe how you would design and implement data quality checks,
detailing the techniques or rules you would apply and what dimensions of data
quality these checks would help ensure.
0. Observability / Alerts: Describe how you would design monitoring and alerting
mechanisms to ensure pipeline reliability — including how you would track pipeline
performance, detect and diagnose failures, and notify the appropriate stakeholders
when incidents occur.



