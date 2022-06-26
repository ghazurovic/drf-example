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
---

### Apply Migrations
- Apply migrations: -> `make migrate`
- Create migrations for model changes -> `make makemigrations`
---

### Create superuser
- Create admin user to control Admin UI -> `make add_superuser`
  * Credentials: `admin` / `Ldexw74ngG`

### Load fixtures
- run command: `make load-fixtures`
- it will load test users and products

#### Available users
- Users: `test_user_1`, `test_user_2`, `test_user_3`, `test_user_4`, `test_user_5`,
- All user share same password: `Ldexw74ngG`
