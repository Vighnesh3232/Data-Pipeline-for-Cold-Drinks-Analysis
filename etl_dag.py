# Updated `etl_dag.py`
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from etl_script import (
    load_data_from_directory,
    analyze_age_vs_frequency,
    marketing_channels_by_age_group,
    packaging_preferences_health_concerns,
    taste_ratings_vs_price_range,
    reasons_new_brands_urban_rural,
)
import pandas as pd

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize the DAG
with DAG(
    'etl_dag',
    default_args=default_args,
    description='ETL Pipeline for Cold Drinks Analysis',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    def extract_and_load_data():
        # Load data from directory
        df = load_data_from_directory()
        df.to_csv('./airflow/extract_folder/extracted_data.csv', index=False)  # Save data for other tasks

    def transform_task(task_function):
        df = pd.read_csv('./airflow/extract_folder/extracted_data.csv')  # Load the data
        task_function(df)

    # Define the tasks
    extract_and_load_task = PythonOperator(
        task_id='extract_and_load_data',
        python_callable=extract_and_load_data,
    )

    analyze_age_vs_frequency_task = PythonOperator(
        task_id='analyze_age_vs_frequency',
        python_callable=lambda: transform_task(analyze_age_vs_frequency),
    )

    # Define other transformation tasks as before, using transform_task
    # Set the task dependencies
    extract_and_load_task >> [
        analyze_age_vs_frequency_task,
        # Add other tasks as needed
    ]