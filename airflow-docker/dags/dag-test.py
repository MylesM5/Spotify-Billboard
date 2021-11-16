from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime



#execution = start_date + schedule_interval, catchup = most recent non-triggered dag run
with DAG("spot_dag",start_date=datetime(2021,1,1),
         schedule_interval= "@daily",catchup=False) as dag:

    t1 = PythonOperator(
        task_id = "spotify_extract",
        python_callable = spotify_extract,
        dag=dag
    )

    t2 = BashOperator(
        task_id="cloud_transfer"
        "bq cd spot.csv my_gcp_bucket",
        dag=dag
    )

    t1 >> t2

