#!/bin/bash
set -e

# permission to execute airbyte scripts
chmod +x ./airbyte/create_connections.sh
chmod +x ./airbyte/setup_postgres_source.sh
chmod +x ./airbyte/setup_snowflake_destination.sh
chmod +x ./airbyte/generate_tables_json.sh
chmod +x ./airbyte/start_airbyte.sh

./airbyte/start_airbyte.sh

# Starting postgres and CDC connectors
docker compose \
  --env-file ../../.env \
  -f postgres/docker-compose.yml \
  up -d

# airbyte set up
cd airbyte;

./create_postgres_source.sh
./create_snowflake_connection.sh
./generate_tables_json.sh
./create_connections.sh

cd ..;

docker compose \
  --env-file ../../.env \
  -f airflow/docker-compose.yml \
  up -d

# Logging airflow user
echo "Airflow user: admin password: admin"

