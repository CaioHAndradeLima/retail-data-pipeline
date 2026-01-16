def consume_order_events():
    events = read_from_kafka("order-events")
    write_to_snowflake("BRONZE.ORDER_EVENTS", events)
