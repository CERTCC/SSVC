FROM python:3.12-slim-bookworm AS base
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip uv
WORKDIR /app

FROM base AS dependencies

# Copy the files we need
COPY . /app
# Set the environment variable
ENV PYTHONPATH=/app/src

# install requirements
RUN uv sync --frozen

FROM dependencies AS test

ENV PYTHONPATH=/app/src
# Install pytest and dev dependencies
RUN uv sync --frozen --dev
# Run the unit tests
CMD ["uv", "run", "pytest"]

FROM dependencies AS docs
CMD ["uv", "run", "mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]

FROM dependencies AS registry_api
CMD ["uv", "run", "uvicorn", "ssvc.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
