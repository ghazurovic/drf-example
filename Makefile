.PHONY: docker-run makemigrations migrate

# if arg is not provided, fallback to default conf
BACKEND_CONF := $(or $(BACKEND_CONF), backend.env)
PGSQL_CONF := $(or $(PGSQL_CONF), postgres.env)

docker-run:
	@echo "*** Starting PGSQL using ${PGSQL_CONF}...*** "
	@echo "*** Staring backend service using ${BACKEND_CONF}... ***"
	env_file=${BACKEND_CONF} pg_env_file=${PGSQL_CONF} docker-compose up

makemigrations:
	docker exec -it drf-example_backend_1 python3 opt/backend/manage.py makemigrations

migrate:
	docker exec -it drf-example_backend_1 python3 opt/backend/manage.py migrate
