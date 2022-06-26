.PHONY: docker-run makemigrations migrate showmigrations-app makemigrations-app add-admin load-fixtures run-tests

# if arg is not provided, fallback to default conf
BACKEND_CONF := $(or $(BACKEND_CONF), backend.env)
PGSQL_CONF := $(or $(PGSQL_CONF), postgres.env)

docker-run:
	@echo "*** Starting PGSQL using ${PGSQL_CONF}...*** "
	@echo "*** Staring backend service using ${BACKEND_CONF}... ***"
	env_file=${BACKEND_CONF} pg_env_file=${PGSQL_CONF} docker-compose up

showmigrations:
	docker exec -it drf-example_backend_1 python3 opt/backend/manage.py showmigrations

makemigrations:
	docker exec -it drf-example_backend_1 python3 opt/backend/manage.py makemigrations

migrate:
	docker exec -it drf-example_backend_1 python3 opt/backend/manage.py migrate

add-admin:
	docker exec -it drf-example_backend_1 python3 opt/backend/manage.py add_superuser

load-fixtures:
	docker exec -it drf-example_backend_1 python3 opt/backend/manage.py loaddata users.json products.json

run-tests:
	docker exec -it drf-example_backend_1 pytest
