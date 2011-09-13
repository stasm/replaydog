#!/usr/bin/env bash

# Have the whole script fail if any individual command fails.
set -e

# Create the virtual environment and activate it.
virtualenv \
    --python=$(which python2.7) \
    --no-site-packages \
    --prompt="(replaydog) " \
    env
source env/bin/activate

# Install the requirements.
pip install -r requirements.txt

# Setup Django
./manage.py validate
./manage.py syncdb

echo "source env/bin/activate # To enter the virtual environment"
echo "./manage.py runserver # To start the development server"
