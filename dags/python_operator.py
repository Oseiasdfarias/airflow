from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import statistics import sts


def data_cleaner():
    dataset = pd.read_csv(
        "/opt/airflow/data/Churn.csv",
        sep=";")
    


with DAG("pytho_operator",
         description="Python Operator DAG",
         schedule_interval=None,
         start_date=datetime(2024, 5, 31),
         catchup=False,
         default_view="graph") as dag:
    
