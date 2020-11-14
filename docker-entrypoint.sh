#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python Dunno/manage.py migrate

# Start server
echo "Starting server"
python Dunno/manage.py runserver https://test-task-django.herokuapp.com/