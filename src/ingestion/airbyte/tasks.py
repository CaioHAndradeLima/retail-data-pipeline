import os
from airflow.decorators import task

from src.ingestion.airbyte.client import AirbyteClient
from src.ingestion.airbyte.discovery import discover_connections


@task
def list_connections(params=None):
    tables = params.get("tables") if params else []

    client = AirbyteClient(
        base_url=os.getenv("AIRBYTE_API_URL"),
        workspace_id=os.getenv("WORKSPACE_ID"),
    )

    connections = discover_connections(client, tables)

    return [
        {
            "connection_id": c["connectionId"],
            "connection_name": c["name"],
        }
        for c in connections
    ]
