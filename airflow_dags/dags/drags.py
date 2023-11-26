from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.sensors import ExternalTaskSensor
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag1 = DAG('dag1', default_args=default_args, schedule_interval='@once')

start_task = DummyOperator(task_id='start_task', dag=dag1)
#1

dag2 = DAG('dag2', default_args=default_args, schedule_interval='@once')

sensor_task = ExternalTaskSensor(
    task_id='sensor_task',
    external_dag_id='dag1',
    external_task_id='end_task',
    timeout=600,
    dag=dag2,
)
#2

start_task >> sensor_task
