#!/bin/bash

set -e

python src/manage.py migrate --no-input
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to migrate database: $status"
  exit $status
fi

python src/manage.py collectstatic --noinput --clear
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to collect staticfiles: $status"
  exit $status
fi

gunicorn src.unigram.wsgi:application \
  --name app \
  --bind 0.0.0.0:8000 \
  --workers 10 \
  --pythonpath "/usr/app/src" \
  --log-level=debug \
  --timeout 120 \
  --reload
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start gunicorn: $status"
  exit $status
fi
