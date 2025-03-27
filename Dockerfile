########### BASE STAGE ###########
FROM python:3.12-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

# Set app directory
WORKDIR app/

# Install dependencies
RUN pip install poetry
COPY pyproject.toml poetry.lock .
RUN poetry install --only main --no-interaction --no-ansi

EXPOSE 8000

# Copy src files
COPY ./app /app/

# Execute app
CMD uvicorn app:app --host 0.0.0.0 --port 8000 ${APP_RUN_PARAMS}
