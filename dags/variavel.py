from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime


def print_variabe(**context):
    minha_var = Variable.get("minhaVar")
    print(f"Valor da variável minha_var: {minha_var}")


with DAG("Variaveis",
         description="Variaveis DAG",
         schedule_interval=None,
         start_date=datetime(2024, 5, 31),
         catchup=False,
         default_view="graph") as dag:

    task1 = PythonOperator(task_id="task1",
                           python_callable=print_variabe)
    task1
