#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python Dunno/manage.py migrate

# Start server
echo "Starting server"
python Dunno/manage.py runserver 0.0.0.0:8000