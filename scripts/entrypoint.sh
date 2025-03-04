#!/bin/bash
set -e

echo "Waiting for database to be ready..."
python manage.py wait_for_db

echo "Create migrations..."
python manage.py makemigrations
python manage.py makemigrations src

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Loading initial data..."
python manage.py load_initial_data

echo "Starting server..."
gunicorn src.config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120 \
    --reload