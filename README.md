# Setup
- Short example of fully functional RESTful API created with DRF.
---
### Configuring Project
- `backend.env` -> used for configuring Django instance
- `postgres.env`-> used for configuring Postgres instance
- If left unchanged it will run server with default conf:
  * http://localhost:8000/api/
----
### Running Project with Makefile
- run project with command:
  * `make docker-run` -> has 2 optional named args
    - `BACKEND_CONF=${path_to_file}`
    - `PGSQL_CONF=${path_to_file}`
  * without args default conf is used
---
- If Makefile isn't available run app with `docker-compose`
  * BACKEND_CONF -> path to backend conf or use default `backend.env`
  * PGSQL_CONF -> path to pgsql conf or default `postgres.env`
  * `env_file=${BACKEND_CONF} pg_env_file=${PGSQL_CONF} docker-compose up`
