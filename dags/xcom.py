from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def task_write(**kwargs):
    kwargs["ti"].xcom_push(
        key="valorXcom1",
        value=10200)


def task_read(**kwargs):
    valor = kwargs["ti"].xcom_pull(
        key="valorXcom1")
    print(f"Valor Recuperado: {valor}")


with DAG("gadXcom",
         description="Trigger DAG1",
         schedule_interval=None,
         start_date=datetime(2024, 5, 27),
         catchup=False,
         default_view="graph") as dag:

    task1 = PythonOperator(task_id="task1",
                           python_callable=task_write)
    task2 = PythonOperator(task_id="task2",
                           python_callable=task_read)

    task1 >> task2
