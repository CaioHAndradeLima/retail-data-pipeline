# Retail Data Pipeline – End-to-End Analytics Platform

## Overview

This project implements a modern retail data pipeline using industry-standard tools and patterns to ingest, transform, and analyze data from a transactional database into analytics-ready datasets.

The pipeline follows a Bronze → Silver → Gold architecture and is designed to answer real business questions such as revenue, conversion rates, cancellations, and fulfillment performance.

---

## Architecture Overview

Postgres (OLTP)
- CDC (Orders) → Kafka → Airflow
- Incremental Reads (Payments, Shipments, Reference Data)
        ↓
   Snowflake (Bronze)
        ↓
       dbt
        ↓
   Snowflake (Silver)
        ↓
   Snowflake (Gold)

Key principles:
- Bronze: Raw, append-only data (events and snapshots)
- Silver: Clean, current-state, entity-level tables
- Gold: Business metrics and KPIs ready for dashboards

---

## Data Sources

Postgres (Simulated Production):
- orders (CDC enabled via Debezium)
- payments (incremental via updated_at)
- shipments (incremental via updated_at)
- customers (daily snapshot)
- products (daily snapshot)

---

## Bronze Layer (Raw Data)

Bronze tables are created and managed via Terraform and represent ingestion contracts.

Tables:
- ORDER_EVENTS – Order CDC events from Kafka
- PAYMENT_EVENTS – Incremental payment events
- SHIPMENT_EVENTS – Incremental shipment events
- CUSTOMERS_SNAPSHOT – Full snapshot per day
- PRODUCTS_SNAPSHOT – Full snapshot per day

Characteristics:
- Append-only
- No transformations
- Includes metadata (timestamps, source system, offsets)
- Designed for traceability and replay

---

## Silver Layer (Clean, Current State)

Silver models are managed entirely by dbt and represent the latest state of each business entity.

Silver models:

- orders_current: Latest state of each order (CDC collapsed)
- payments_current: Latest state of each payment
- shipments_current: Latest state of each shipment
- customers_current: Latest customer snapshot
- products_current: Latest product snapshot
- orders_enriched: Orders joined with customers, payments, and shipments

Why “current”:
Models with the _current suffix represent a single row per entity containing the latest known state. Historical data remains preserved in Bronze.

Why orders_enriched:
This model provides an analytics-friendly view of orders with contextual information, without aggregation.

---

## Gold Layer (Business Metrics)

Gold models answer specific business questions and are designed for dashboards and reporting.

Business questions and models:

1. How many orders are created per day?
Model: gold.orders.orders_daily
Provides daily order volume trends.

2. How much revenue are we generating?
Model: gold.revenue.revenue_daily
Provides daily revenue, excluding canceled and refunded orders.

3. What is the order conversion rate?
Model: gold.orders.orders_conversion
Defines conversion as orders with successful payment.

4. Which products generate the most revenue?
Deferred until order_items modeling is added.

5. What percentage of orders are canceled or refunded?
Model: gold.orders.orders_cancellation_rate
Provides cancellation and refund rates over time.

6. How long does it take for an order to move from created to shipped or delivered?
Model: gold.orders.orders_fulfillment_time
Provides fulfillment duration metrics for operational analysis.

---

## Data Quality and Testing

dbt tests enforce:
- Primary key uniqueness
- Not-null constraints
- Referential integrity
- Timestamp availability for freshness

These tests ensure reliability and trust in downstream analytics.

---

## Tooling Summary

- Postgres: Source transactional database
- Kafka and Debezium: CDC for orders
- Airflow: Orchestration
- Snowflake: Analytical data warehouse
- Terraform: Infrastructure and Bronze contracts
- dbt: Silver and Gold transformations

---

## Key Design Decisions

- CDC applied only to high-value transactional tables
- Snapshots used for slowly changing reference data
- dbt owns all analytical transformations
- Terraform manages infrastructure and raw ingestion contracts
- Clear separation of responsibilities across layers

---

## Future Improvements

- Add order_items modeling
- Introduce dbt snapshots for customers and products
- Add CI/CD for dbt
- Integrate BI tools (Looker, Power BI, Tableau)
- Add data freshness and volume monitoring

---

## Conclusion

This project demonstrates a production-grade analytics pipeline with correct ingestion patterns, clean modeling, business-aligned metrics, and strong testing practices. It mirrors real-world data engineering architectures used in modern analytics platforms.
