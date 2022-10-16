#!/bin/bash

VENV=${1:-venv}

python -m venv $VENV && \
  source $VENV/bin/activate && \
  python -m pip install --upgrade pip && \
  pip install -e '.[build]'