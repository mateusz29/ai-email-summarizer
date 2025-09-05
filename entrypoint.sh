#!/bin/sh

# wait-for-it.sh should be in your app image
/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Postgres is up"

alembic upgrade head

exec "$@"
