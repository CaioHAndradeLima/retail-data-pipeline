from typing import List, Optional
from src.ingestion.airbyte.client import AirbyteClient


def discover_connections(
    client: AirbyteClient,
    table_filter: Optional[List[str]] = None,
) -> List[dict]:
    connections = client.list_connections()

    connections = [
        c for c in connections if c["name"].endswith("_postgres_to_snowflake")
    ]

    if table_filter:
        connections = [
            c for c in connections if any(t in c["name"] for t in table_filter)
        ]

    return connections
