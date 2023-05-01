#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt

pip install --upgrade --no-cache-dir git+https://github.com/StreamAlpha/tvdatafeed.git

pip install TA-Lib

python manage.py collectstatic --no-input
python manage.py migrate