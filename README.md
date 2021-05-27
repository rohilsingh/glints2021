## Problem Set
A key part of a Data Engineer’s responsibilities is maintaining the serviceability of Data Warehouse. To achieve this, you will need to understand the set up and operation of a basic Data Warehouse.

In this technical assessment, you are required to submit the setup for the data pipeline of a basic data warehouse using Docker and Apache Airflow.

Your final setup should include the following:
- A source postgres database (Database X)
- A target postgres database (Database Y, which is not the same Docker container as Database X)
- Apache Airflow with webserver accessible from localhost:5884
- A Directed Acyclic Graph (DAG) for transferring the content of Source Database X to Target Database Y
- README.md detailing the usage of your submission

As the focus of this technical assessment is on the set up of a basic data pipeline using Airflow, the content of the table in Source Postgres Database X to be transferred can be determined by the candidate. It can be as basic as:

| id | creation_date | sale_value |
| -- | ------------- | ---------- |
| 0  | 12-12-21 | 1000 |
| 1  | 13-12-21 | 2000 |

## Setup

The setup consists of 3 files:

1) docker-compose.yaml : It consists of the configuration for running the airflow container, source postgre container & target postgre container.

2) run-airflow.sh : It conists of two commands, one for initialization of database and other for starting the containers, it calls docker-compose.yaml to start the required containers.

3) dags/data_transfer.py : This contains the DAG code for data transfer between the two database containers.

## Running the setup

1) Run the run-airflow.sh file to start all the required containers
2) Access the webserver at localhost:5884
3) Login using credentials:
    USERNAME : airflow
    PASSWORD : airflow
4) Activate the dag name data_transfer & run it.

## Inspecting database

**To check source**
- Access psql shell using command: psql -h localhost -p 5442 -U postgres
- On prompt enter password : Glints2021
- Switch to database: \c source_db;
- check table: select * from source_table;

**To check target**
- Access psql shell using command: psql -h localhost -p 5443 -U postgres
- On prompt enter password : Glints2021
- Switch to database: \c target_db;
- check table: select * from target_table;
