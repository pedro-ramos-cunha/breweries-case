# breweries-case repo
Breweries Case of Data Engineering. This repo concerns to a sample case data engineering data extraction according to instructions and context below.

### Menu

*   [Context](#context)
*   [Instructions](#instructions)
*   [Hardware Informations](#hardware-information)
*   [Software Information](#tools-version)
    *   [Python Dependencies](#python-dependencies)
*   [Problem Solving](#problem-solving) 
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

## Enviroment Information

Due the lack of hardware resources the explanation will be mainly theorical. The code will try to example the proposition in scale.

### Hardware information
| Column                                                | Value                                                                                        |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------|
| OS Name                                               | Microsoft Windows 10 Home                                                                    |
| Version                                               | 10.0.19045 Build 19045                                                                       |
| Other OS Description                                  | Not available                                                                                |
| OS Manufacturer                                       | Microsoft Corporation                                                                        |
| System Name                                           | HP                                                                                           |
| System Manufacturer                                   | HP                                                                                           |
| System Model                                          | HP Notebook                                                                                  |
| System Type                                           | x64-based PC                                                                                 |
| System SKU                                            | X7T74UAR#ABA                                                                                 |
| Processor                                             | AMD A10-9600P RADEON R5, 10 COMPUTE CORES 4C+6G, 2400 Mhz, 4 Core(s), 4 Logical Processor(s) |
| BIOS Version/Date                                     | Insyde F.24, 07/06/2017                                                                      |
| SMBIOS Version                                        | 2.8                                                                                          |
| Embedded Controller Version                           | 67.40                                                                                        |
| BIOS Mode                                             | UEFI                                                                                         |
| BaseBoard Manufacturer                                | HP                                                                                           |
| BaseBoard Product                                     | 81F9                                                                                         |
| BaseBoard Version                                     | 67.40                                                                                        |
| Platform Role                                         | Mobile                                                                                       |
| Secure Boot State                                     | Enabled                                                                                      |
| PCR7 Configuration                                    | Elevation Required for View                                                                  |
| Windows Directory                                     | C:\Windows                                                                                   |
| System Directory                                      | C:\Windows\system32                                                                          |
| Boot Device                                           | \Device\HarddiskVolume1                                                                      |
| Locale                                                | Brazil                                                                                       |
| Hardware Abstraction Layer                            | Version = "10.0.19041.6456"                                                                  |
| User Name                                             | HP\Pedro                                                                                     |
| Time Zone                                             | E. South America Standard Time                                                               |
| Installed Physical Memory (RAM)                       | 16.0 GB                                                                                      |
| Total Physical Memory                                 | 15.0 GB                                                                                      |
| Available Physical Memory                             | 7.24 GB                                                                                      |
| Total Virtual Memory                                  | 17.2 GB                                                                                      |
| Available Virtual Memory                              | 8.53 GB                                                                                      |
| Page File Space                                       | 2.25 GB                                                                                      |
| Page File                                             | C:\pagefile.sys                                                                              |
| Kernel DMA Protection                                 | Disabled                                                                                     |
| Virtualization-based Security                         | Not enabled                                                                                  |
| Device Encryption Support                             | Elevation Required for View                                                                  |
| Hyper-V - VM Monitor Mode Extensions                  | Yes                                                                                          |
| Hyper-V - Second Level Address Translation Extensions | Yes                                                                                          |
| Hyper-V - Virtualization Enabled in Firmware          | No                                                                                           |
| Hyper-V - Data Execution Protection                   | Yes                                                                                          |

### Tools version 

 python -m pipreqs.pipreqs "C:\Users\Pedro\Documents\breweries-case\"


| Software | Version |
|----------|---------|
| Python   | 3.13.12 |

#### Python dependencies

Read [requirements.txt](requirements.txt)

## Problem Solving
