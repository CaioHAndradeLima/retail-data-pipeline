import os
from datetime import datetime

from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.models.param import Param
from dotenv import load_dotenv

from src.ingestion.airbyte.client import AirbyteClient
from src.ingestion.airbyte.discovery import discover_connections
from src.ingestion.airbyte.sync import sync_connection

load_dotenv()


@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["bronze", "airbyte"],
    max_active_tasks=2,
    params={
        "tables": Param(
            default=[],
            type="array",
            description="List of table names to sync (empty = all tables)",
        )
    },
)
def postgres_to_snowflake_bronze():

    @task
    def list_connections(params=None):
        tables = params.get("tables") if params else []

        client = AirbyteClient(
            base_url=os.getenv("AIRBYTE_API_URL"),
            workspace_id=os.getenv("WORKSPACE_ID"),
        )

        connections = discover_connections(client, tables)
        return [c["connectionId"] for c in connections]

    @task
    def sync(connection_id: str):
        client = AirbyteClient(
            base_url=os.getenv("AIRBYTE_API_URL"),
            workspace_id=os.getenv("WORKSPACE_ID"),
        )
        sync_connection(client, connection_id)

    sync.expand(connection_id=list_connections())


dag = postgres_to_snowflake_bronze()
