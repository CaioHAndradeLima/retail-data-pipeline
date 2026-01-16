resource "snowflake_database" "retail_analytics" {
  name = "RETAIL_ANALYTICS"
}

resource "snowflake_schema" "bronze" {
  database = snowflake_database.retail_analytics.name
  name     = "BRONZE"
}

resource "snowflake_schema" "silver" {
  database = snowflake_database.retail_analytics.name
  name     = "SILVER"
}

resource "snowflake_schema" "gold" {
  database = snowflake_database.retail_analytics.name
  name     = "GOLD"
}