#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt

pip3 install tvdatafeed

python manage.py collectstatic --no-input
python manage.py migrate