import requests

class AirbyteClient:
    def __init__(self, base_url: str, workspace_id: str):
        self.base_url = base_url.rstrip("/")
        self.workspace_id = workspace_id

    def list_connections(self):
        r = requests.post(
            f"{self.base_url}/connections/list",
            json={"workspaceId": self.workspace_id},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()["connections"]

    def trigger_sync(self, connection_id: str):
        r = requests.post(
            f"{self.base_url}/connections/sync",
            json={"connectionId": connection_id},
            timeout=30,
        )
        # already running
        if r.status_code == 409:
            return

        r.raise_for_status()
