from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='Un simple DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 6, 14, 18, 0, 0),
    catchup=False,
)
start = DummyOperator(
    task_id='start',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)
start >> end
