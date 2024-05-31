from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG("pool",
         description="Pool DAG",
         schedule_interval=None,
         start_date=datetime(2024, 5, 31),
         catchup=False,
         default_view="graph") as dag:

    task1 = BashOperator(
          task_id="task1",
          bash_command="sleep 5",
          pool="meupool"
      )
    task2 = BashOperator(
          task_id="task2",
          bash_command="sleep 5",
          pool="meupool",
          priority_weight=5
      )
    task3 = BashOperator(
          task_id="task3",
          bash_command="sleep 5",
          pool="meupool"
      )
    task4 = BashOperator(
          task_id="task4",
          bash_command="sleep 5",
          pool="meupool",
          priority_weight=10
      )
