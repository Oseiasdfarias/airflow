from airflow import DAG, Dataset
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd


mydataset = Dataset("/opt/airflow/data/Churn_new.csv")


def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/Churn_new.csv", sep=";")


with DAG("producer",
         description="Python Producer DAG",
         schedule_interval=None,
         start_date=datetime(2024, 6, 2),
         catchup=False,
         default_view="graph",
         tags=["PyOperator", "pipeline"]) as dag:

    t1 = PythonOperator(
        task_id="t1",
        python_callable=my_file,
        outlets=[mydataset])
    t1
