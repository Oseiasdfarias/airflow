from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import statistics as sts


def data_cleaner():
    dataset = pd.read_csv(
        "/opt/airflow/data/Churn.csv",
        sep=";")

    dataset.columns = ["Id", "Score", "Estado", "Genero",
                       "Idade", "Patrimonio", "Saldo",
                       "Produtos", "TemCartCredito",
                       "Ativo", "Salario", "Saiu"]
    mediana = sts.median(dataset["Salario"])
    dataset["Salario"].fillna(mediana, inplace=True)
    dataset["Genero"].fillna("Masculino", inplace=True)
    mediana = sts.median(dataset["Idade"])
    dataset.loc[(dataset["Idade"] < 0) | (dataset["Idade"] > 120), "Idade"] = mediana  # noqa: E501
    dataset.drop_duplicates(subset="Id", keep="first", inplace=True)
    dataset.to_csv("/opt/airflow/data/Churn_Clean.csv", sep=";", index=False)


with DAG("py_operator",
         description="Python Operator DAG",
         schedule_interval=None,
         start_date=datetime(2024, 6, 2),
         catchup=False,
         default_view="graph",
         tags=["PyOperator", "pipeline"]) as dag:

    t1 = PythonOperator(
        task_id='t1',
        python_callable=data_cleaner
    )
    t1
