from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task

with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    first_task = BashOperator(task_id='firs_task', bash_command=f"echo test 1")

    @task()
    def second_task():
        print("test 2")

    second_task = second_task()

    first_task >> second_task