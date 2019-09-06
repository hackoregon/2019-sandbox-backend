#! /bin/bash

# -e  Exit immediately if a command exits with a non-zero status:
# (http://linuxcommand.org/lc3_man_pages/seth.html)
set -e

if [ -z ${DEBUG+x} ]; then 
  echo "DEBUG var is unset, setting to False" && export DEBUG=false ; 
else 
  echo "var is set to '$DEBUG'";
fi

echo Debug: $DEBUG

if [ -z ${TRAVIS+x} ]; then 
  echo "TRAVIS var is unset, setting to False" && export TRAVIS=false ; 
else 
  echo "var is set to '$TRAVIS'";
fi

echo Travis: $TRAVIS

# Pull in environment variables values from AWS Parameter Store, and preserve the exports
# source usage per https://stackoverflow.com/q/14742358/452120 (iff running on travis-ci)
if [ $DEBUG = "false" ] && [ $TRAVIS = "false" ]; then
  source /code/src_files/scripts/deploy/get-ssm-parameters.sh
fi

>&2 echo "Postgres is up"

chmod +x *.py

#echo "Make migrations"
#python -Wall manage.py makemigrations api

echo "Migrate..."
python -Wall manage.py migrate --noinput api

# Collect static files
echo "Collect static files..."
python -Wall manage.py collectstatic --noinput

echo "Run server..."
gunicorn backend.wsgi -c gunicorn_conf.py
