#!/bin/bash
set -e

echo "Creating Airflow connections..."

airflow connections delete airbyte_conn || true

airflow connections add airbyte_conn \
  --conn-type http \
  --conn-host "http://host.docker.internal:8001"

echo "Airflow connections created successfully."
