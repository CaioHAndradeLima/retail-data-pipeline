#!/bin/bash

./stop_airflow.sh
./start_airflow.sh

docker compose exec airflow-scheduler bash /opt/airflow/validation/validate_dags.sh