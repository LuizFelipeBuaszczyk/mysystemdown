FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

WORKDIR /app

COPY pyproject.toml .
RUN pip install .


FROM builder

WORKDIR /app

COPY ./src .

COPY /docker/entrypoint-api.sh /entrypoint-api.sh
COPY /docker/entrypoint-worker.sh /entrypoint-worker.sh

RUN chmod +x /entrypoint-*.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]