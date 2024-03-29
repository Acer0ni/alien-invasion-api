#!/bin/bash
set -euo pipefail #unofficial strict mode
git pull
docker build -t alien_invasion_api .
docker kill alien_invasion_api
docker rm alien_invasion_api
docker run --name alien_invasion_api -p 127.0.0.1:8001:8000 --env-file .env -d alien_invasion_api
