from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import (PythonOperator,
                                               BranchPythonOperator)
from datetime import datetime
import random


def gera_naleatorio():
    return random.randint(1, 100)


def avalia_naleatorio(**context):
    n_aleatorio = (context["task_instance"]
                   .xcom_pull(
                       task_ids="gera_naleatorio_task"))
    if n_aleatorio % 2 == 0:
        return "par_task"
    else:
        return "impar_task"


with DAG("branch_test",
         description="Branch Test DAG",
         schedule_interval=None,
         start_date=datetime(2024, 5, 31),
         catchup=False,
         default_view="graph") as dag:

    gera_naleatorio_task = PythonOperator(
        task_id="gera_naleatorio_task",
        python_callable=gera_naleatorio
    )

    branch_task = BranchPythonOperator(
        task_id="branch_task",
        python_callable=avalia_naleatorio,
        provide_context=True
    )

    par_task = BashOperator(
        task_id="par_task",
        bash_command="echo 'Número Par'"
    )
    impar_task = BashOperator(
        task_id="impar_task",
        bash_command="echo 'Número Impar'"
    )

    gera_naleatorio_task >> branch_task
    branch_task >> par_task
    branch_task >> impar_task
