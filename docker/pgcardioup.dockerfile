FROM postgres:16.2-alpine
LABEL authors="Emanuel Severino <emanuelsmseverino@gmail.com>"
ENV POSTGRES_USER=cardioup_user
ENV POSTGRES_PASSWORD=cardioup123
ENV POSTGRES_DB=cardioup_db
EXPOSE 5432