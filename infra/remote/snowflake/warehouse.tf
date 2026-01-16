
resource "snowflake_warehouse" "retail_wh" {
  name           = "RETAIL_WH"
  warehouse_size = "XSMALL"

  auto_suspend = 60
  auto_resume  = true

  initially_suspended = true

  comment = "Warehouse for retail data pipeline (ingestion + analytics)"
}