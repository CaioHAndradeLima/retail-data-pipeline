from airflow.datasets import Dataset

RETAIL_BRONZE = Dataset("snowflake://Retail/Bronze")
RETAIL_SILVER = Dataset("snowflake://Retail/Silver")
RETAIL_GOLD = Dataset("snowflake://Retail/Gold")
