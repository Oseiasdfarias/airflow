from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG("trigger_dag3",
         description="Trigger DAG3",
         schedule_interval=None,
         start_date=datetime(2024, 5, 27),
         catchup=False) as dag:

    task1 = BashOperator(
          task_id="task1",
          bash_command="sleep 5; exit 1"
      )
    task2 = BashOperator(
          task_id="task2",
          bash_command="sleep 5; exit 1"
      )
    task3 = BashOperator(
          task_id="task3",
          bash_command="sleep 5",
          trigger_rule="all_failed"
      )

    [task1, task2] >> task3
