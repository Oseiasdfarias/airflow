from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

with DAG("dummy_dag",
         description="Dummy DAG",
         schedule_interval=None,
         start_date=datetime(2024, 5, 31),
         catchup=False,
         default_view="graph") as dag:

    task1 = BashOperator(
        task_id="task1",
        bash_command="sleep 1"
    )
    task2 = BashOperator(
        task_id="task2",
        bash_command="sleep 1"
    )
    task3 = BashOperator(
        task_id="task3",
        bash_command="sleep 1"
    )
    task4 = BashOperator(
        task_id="task4",
        bash_command="sleep 1"
    )
    task5 = BashOperator(
        task_id="task5",
        bash_command="sleep 1"
            )
    taskdummy = DummyOperator(
        task_id="taskdummy")

    [task1, task2, task3] >> taskdummy >> [task4, task5]
