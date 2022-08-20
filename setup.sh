#!/bin/bash

VENV=${1:-venv}

python3.8 -m venv $VENV && \
  source $VENV/bin/activate && \
  python3.8 -m pip install --upgrade pip && \
  pip install -e '.[build]' && \
  pip install openapi_definition/v1/client