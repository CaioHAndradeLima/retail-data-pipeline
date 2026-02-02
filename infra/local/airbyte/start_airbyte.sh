#!/bin/bash

abctl local install \
  --chart-version 2.0.19 \
  --host airbyte.local \
  --insecure-cookies \
  --values airbyte-values.yaml \
  --port=8000
