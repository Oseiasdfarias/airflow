from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


dag = DAG("teste_bash", description="Nossa primeira DAG",
          schedule_interval=None, start_date=datetime(2024, 5, 27),
          catchup=False)


task1 = BashOperator(task_id="task1", bash_command="""
                     ls -la;
                     pwd;
                     python --version""",
                     dag=dag)

task1
