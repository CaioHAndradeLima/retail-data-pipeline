#!/bin/bash
set -e

./start_airflow.sh
echo "Initializing Airflow metadata database"
echo "Creating admin user (admin / admin)"

docker compose exec airflow-scheduler bash -c "airflow db migrate &&
      airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com;"

./stop_airflow.sh

echo "Airflow initialization completed successfully"
