FROM python:3.12-slim-bookworm AS base
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip uv
WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN python -m venv "${VIRTUAL_ENV}"
FROM base AS dependencies

ARG BASE_DIR=..
ARG SRC_DIR=${BASE_DIR}/src

# Copy the files we need
COPY ${BASE_DIR}/ /app
# Set the environment variable
ENV PYTHONPATH=/app/src
COPY ${SRC_DIR}/pyproject.toml /app/src/pyproject.toml
COPY ${SRC_DIR}/uv.lock /app/src/uv.lock

# install requirements
RUN uv sync --project=/app/src --frozen


FROM dependencies AS test
ENV PYTHONPATH=/app/src
# Install pytest and dev dependencies
RUN uv sync --project=/app/src --frozen --dev
# Run the unit tests
CMD ["uv", "run", "--project=/app/src", "pytest"]

FROM dependencies AS docs
CMD ["uv", "run", "--project=/app/src", "mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]

FROM dependencies AS registry_api
CMD ["uv", "run", "--project=/app/src", "uvicorn", "ssvc.api.main:app", "--host", "0.0.0.0", "--port", "8000"]