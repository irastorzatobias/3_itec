FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD your_password
ENV MYSQL_DATABASE your_database
ENV MYSQL_USER your_username
ENV MYSQL_PASSWORD your_password
COPY test.sql /docker-entrypoint-initdb.d/
