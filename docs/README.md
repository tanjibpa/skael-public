# Files

### docker-compose.yml

* `docker-compose.yml`: shared docker configuration between development and production
* `docker-compose.override.yml`: provides development configuration.
* `docker-compose.production.yml`: provides production configuration.

# Development configuration

In this configuration:
 * Angular app is ran with development server
 * Flask app is ran by flask debugger instead of uWSGI
 * Your code is mounted into container so code auto-reload works

### Changing the port

If the default port (http://localhost:4200) is inconvenient, open up docker-compose.override.yml.
Under frontend, find ports:

```
frontend:
  ports:
    - "4200:4200"
```

And change the first number to something different (leave the second at 4200).

# Docker Compose

You can use the standard docker compose commands to interact with the containers. Some examples below.

### Starting the app

Start the app with:

```
docker-compose up --build
```

You can also skip rebuilding:

```
docker-compose up
```

This is a little faster, but remember that you need to rebuild when:

- The Dockerfiles change
- The dependencies change

Be careful when you switch branches or pull in new code because some changes might have happened.

### Drop/delete everything, including database, for a fresh start

```
docker-compose down --rmi all -v --remove-orphans
```

### Entering a running container

The container names are frontend, backend, postgres, migrations

```
docker-compose exec frontend /bin/sh
```

### Running a one-off command in a spinoff container

This creates and starts a copy of the container you selected, and then deletes it when you are done.

```
docker-compose run --rm frontend /bin/sh
```

### Adding new dependencies

Frontend:

```
docker-compose run --rm frontend yarn add react
```

Backend:

```
docker-compose run --rm backend /bin/sh -c 'pip install aiohttp && pip freeze > requirements.txt'
```

You need to rebuild and restart the containers after updating dependencies.

```
docker-compose up --build
```

### Adding a migration

```
docker-compose run --rm migrations alembic revision -m "A new migration"
```

After you have updated the migration, you can upgrade and downgrade using the command

```
docker-compose run --rm migrations alembic upgrade head
```

```
docker-compose run --rm migrations alembic downgrade -1
```

### Running the nose tests

```
docker-compose run --rm backend nosetests
```

## Interacting with the database

The postgres container must be running.

```
docker-compose start postgres
```

### Connecting locally

In docker-compose.override.sql you can forward port 5432 to your local workstation. Then you can connect to it directly using your favorite postgres admin tool.

### Accessing the psql shell

```
docker-compose exec postgres psql -U postgres
```

### Creating a database dump

```
docker-compose exec postgres pg_dump -U postgres > dump.sql
```

### Clearing the database completely

```
docker-compose exec postgres psql -U postgres -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public; GRANT ALL ON SCHEMA public TO postgres; GRANT ALL ON SCHEMA public TO public;"
```

### Restoring a database dump

```
cat dump.sql | docker exec -i $(docker-compose ps -q postgres) psql -U postgres
```
