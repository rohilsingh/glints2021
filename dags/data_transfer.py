from airflow import AirflowException, DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import psycopg2
import logging
from contextlib import closing

WORKFLOW_DAG_ID = 'data_transfer'
WORKFLOW_START_DATE = datetime.now() - timedelta(days = 1)
WORKFLOW_SCHEDULE_INTERVAL = "@once"
WORKFLOW_DEFAULT_ARGS = {
    'owner': 'airflow',
    'start_date': WORKFLOW_START_DATE,
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    dag_id = WORKFLOW_DAG_ID,
    catchup = False,
    schedule_interval = WORKFLOW_SCHEDULE_INTERVAL,
    default_args = WORKFLOW_DEFAULT_ARGS
)

def data_transfer(**context):

    source = "host=airflow_psql_source_1 user=postgres password=Glints2021 dbname=source_db"
    target = "host=airflow_psql_target_1 user=postgres password=Glints2021 dbname=target_db"

    with closing(psycopg2.connect(source)) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('select * from source_table')
            rows = cursor.fetchall()

    with closing(psycopg2.connect(target)) as conn:
        with closing(conn.cursor()) as cursor:
            insert_query = 'insert into target_table values %s'
            psycopg2.extras.execute_values(cursor, insert_query, rows)
        conn.commit()

transfer_data = PythonOperator(
    task_id='transfer_data',
    python_callable=data_transfer,
    provide_context=True,
    dag=dag
)
