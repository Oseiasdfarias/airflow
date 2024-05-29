from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime


dag = DAG("dag_run_dag1",
          description="DAG Group 1",
          schedule_interval=None,
          start_date=datetime(2024, 5, 27),
          catchup=False,
          default_view="graph")

task1 = BashOperator(
  task_id="task1",
  bash_command="sleep 5",
  dag=dag
  )
task2 = TriggerDagRunOperator(
  task_id="task2",
  trigger_dag_id="dag_run_dag2",
  dag=dag
  )

task1 >> task2
