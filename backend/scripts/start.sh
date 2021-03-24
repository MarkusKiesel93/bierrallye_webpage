#! /usr/bin/env bash

set -e

pytest --cov -v ./app

if [ ${DEPLOY_MODE} = "production" ]; then
    gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers 4 app.main:app
else
    uvicorn app.main:app --reload --host 0.0.0.0 --port ${BACKEND_PORT}
fi