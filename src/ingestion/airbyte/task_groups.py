from datetime import timedelta
from airflow.decorators import task_group
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor


@task_group
def airbyte_connection_group(
    connection_id: str,
    connection_name: str,
):
    sync = AirbyteTriggerSyncOperator(
        task_id="sync_airbyte_connection",
        airbyte_conn_id="airbyte_default",
        connection_id=connection_id,
        asynchronous=True,
        pool="airbyte_sequential",
        doc_md=f"### Airbyte sync for `{connection_name}`",
    )

    sensor = AirbyteJobSensor(
        task_id="sensor_airbyte_connection",
        airbyte_conn_id="airbyte_default",
        airbyte_job_id=sync.output,
        pool="airbyte_sequential",
        poke_interval=30,
        timeout=60 * 60 * 60,
        retries=5,
        retry_delay=timedelta(minutes=5),
        doc_md=f"### Airbyte sensor for `{connection_name}`",
    )

    sync >> sensor
