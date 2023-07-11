FROM postgres:14.4

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB payroll

# Database creation file
COPY 01_setup.sql /docker-entrypoint-initdb.d/
COPY 02_insert_employees.sql /docker-entrypoint-initdb.d/
COPY 03_insert_entries.sql /docker-entrypoint-initdb.d/

RUN apt-get install -y postgresql-contrib-14

