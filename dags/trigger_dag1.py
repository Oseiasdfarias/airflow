from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG("trigger_dag1",
         description="Trigger DAG1",
         schedule_interval=None,
         start_date=datetime(2024, 5, 27),
         catchup=False,
         default_view="graph") as dag:

    task1 = BashOperator(task_id="task1",
                         bash_command="sleep 5")
    task2 = BashOperator(task_id="task2",
                         bash_command="sleep 5")
    task3 = BashOperator(task_id="task3",
                         bash_command="sleep 5",
                         trigger_rule="one_failed")

    [task1, task2] >> task3
