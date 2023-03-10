ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}

ENV ENV="development"

# Setup the Python package manager
RUN export POETRY_HOME=/opt/poetry && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry

# Setup the app directory
RUN mkdir -p /app
WORKDIR /app

# Install Python dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main

# Copy the rest of the app
COPY . .

EXPOSE 8000

CMD ["poetry", "run", "gunicorn", "--bind", ":8000", "--workers", "2", "callsign_alert.wsgi"]
