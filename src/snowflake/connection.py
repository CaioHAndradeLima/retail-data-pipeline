import os
from typing import Optional

from snowflake.connector import connect
from snowflake.connector.connection import SnowflakeConnection

from dotenv import load_dotenv

# Load environment variables from .env (safe to call multiple times)
load_dotenv()


def get_snowflake_connection(
    warehouse: Optional[str] = None,
    database: Optional[str] = None,
    schema: Optional[str] = None,
) -> SnowflakeConnection:
    """
    Create and return a Snowflake connection using environment variables.

    Environment variables required:
      - SNOWFLAKE_ACCOUNT
      - SNOWFLAKE_USER
      - SNOWFLAKE_PASSWORD
      - SNOWFLAKE_ROLE

    Optional (can be overridden by function args):
      - SNOWFLAKE_WAREHOUSE
      - SNOWFLAKE_DATABASE
      - SNOWFLAKE_SCHEMA
    """

    account = os.getenv("SNOWFLAKE_ACCOUNT")
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    role = os.getenv("SNOWFLAKE_ROLE")

    if not all([account, user, password, role]):
        raise RuntimeError(
            "Missing required Snowflake environment variables. "
            "Check SNOWFLAKE_ACCOUNT, USER, PASSWORD, ROLE."
        )

    conn = connect(
        account=account,
        user=user,
        password=password,
        role=role,
        warehouse=warehouse or os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=database or os.getenv("SNOWFLAKE_DATABASE"),
        schema=schema or os.getenv("SNOWFLAKE_SCHEMA"),
    )

    return conn
