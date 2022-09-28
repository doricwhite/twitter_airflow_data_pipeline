# Imports
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl

# DAG default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": 'False',
    "start_date": datetime[2020,11,8],
    "email": ['doricwhite@gmail.com'],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

# Create DAG
dag = DAG(
    dag_id="twitter_dag",
    default_args=default_args,
    description="ETL Twitter DAG"
)

# Python Operator to execute ETL
run_etl = PythonOperator (
    task_id="complete_twitter_etl",
    python_callable=run_twitter_etl,
    dag=dag
)

run_etl