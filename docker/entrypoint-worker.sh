#!/bin/sh
set -e

celery -A config worker --loglevel=info