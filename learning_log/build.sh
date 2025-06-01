#!/bin/bash
# Apply database migrations
python manage.py migrate

# Collect static files (needed for admin panel or CSS/JS)
python manage.py collectstatic --noinput
