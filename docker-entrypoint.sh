#!/bin/sh
python3 -m pip install -r opt/backend/requirements.txt
python3 opt/backend/manage.py migrate
python3 opt/backend/manage.py runserver 0.0.0.0:8000
