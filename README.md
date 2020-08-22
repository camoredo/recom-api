# Recom

## Database set up

Make sure to have [PostgreSQL](https://www.postgresql.org/) installed on the local machine as the application will require credentials that will be set to the Django application.  

Enter the psql console:

```bash
psql
```

Create a database and user:

```sql
CREATE DATABASE recomdb;
CREATE USER recomuser WITH PASSWORD 'free123';
```

Alter the parameters of the database:

```sql
ALTER ROLE recomuser SET client_encoding TO 'utf-8';
ALTER ROLE recomuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE recomuser SET timezone TO 'UTC';
```

Grant the user access priviliges to the database:

```sql
GRANT ALL PRIVILEGES ON DATABASE recomdb TO recomuser;
```