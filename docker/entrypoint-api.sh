#!/bin/sh
set -e

python manage.py migrate_schemas --shared
python manage.py seed_tenants
python manage.py seed_roles
python manage.py seed_group_permissions

exec "$@"