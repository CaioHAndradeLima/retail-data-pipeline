resource "snowflake_table" "bronze_customers_snapshot" {
  database = snowflake_database.retail_analytics.name
  schema   = snowflake_schema.bronze.name
  name     = "CUSTOMERS_SNAPSHOT"

  column {
    name     = "CUSTOMER_ID"
    type     = "STRING"
    nullable = false
  }
  column {
    name = "NAME"
    type = "STRING"
  }
  column {
    name = "EMAIL"
    type = "STRING"
  }
  column {
    name = "COUNTRY"
    type = "STRING"
  }
  column {
    name = "CREATED_AT"
    type = "TIMESTAMP_TZ"
  }

  column {
    name = "SNAPSHOT_DATE"
    type = "DATE"
  }
  column {
    name = "INGESTED_AT"
    type = "TIMESTAMP_TZ"
  }
}

resource "snowflake_table" "bronze_products_snapshot" {
  database = snowflake_database.retail_analytics.name
  schema   = snowflake_schema.bronze.name
  name     = "PRODUCTS_SNAPSHOT"

  column {
    name     = "PRODUCT_ID"
    type     = "STRING"
    nullable = false
  }
  column {
    name = "PRODUCT_NAME"
    type = "STRING"
  }
  column {
    name = "CATEGORY"
    type = "STRING"
  }
  column {
    name = "PRICE"
    type = "NUMBER(10,2)"
  }
  column {
    name = "ACTIVE"
    type = "BOOLEAN"
  }

  column {
    name = "SNAPSHOT_DATE"
    type = "DATE"
  }
  column {
    name = "INGESTED_AT"
    type = "TIMESTAMP_TZ"
  }
}
