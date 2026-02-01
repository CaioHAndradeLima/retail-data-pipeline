import re


def sanitize_task_id(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "_", value)
