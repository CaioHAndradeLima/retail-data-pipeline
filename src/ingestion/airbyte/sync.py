from src.ingestion.airbyte.client import AirbyteClient

def sync_connection(client: AirbyteClient, connection_id: str):
    client.trigger_sync(connection_id)
