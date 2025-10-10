# SSVC API Readme

This directory contains source code for the SSVC API.

## Prerequisites

- `uv` CLI tool installed. You can install it via pip:

```shell
pip install uv
```

We recommend using `uv` to manage your Python environment and dependencies,
so you don't need to manually create and activate virtual environments or
worry about Python versions.

## Running a local instance in development mode

From the project root, run:

```shell
uv --project=src run uvicorn ssvc.api.main:app --reload --port=7777
```

> [!TIP]
> Adjust the port as needed.

> [!NOTE]
> We're planning to move our `pyproject.toml` to the top level of the project,
> so in the future you may be able to run this command without the `--project` flag.

This will start the FastAPI server with auto-reload enabled, allowing you to
see changes immediately.

## Running a local instance in production mode

From the project root, run:

```shell
cd docker
docker-compose up api
```

This will start the FastAPI server in a Docker container.

> [!NOTE]
> Docker and Docker Compose must be installed on your machine to use this method.
> Make sure to adjust the `docker-compose.yml` file if you want to change
> the port or other settings.

> [!TIP]
> The `api` docker target copies the code into the container at build time.
> If you make changes to the code, you'll need to rebuild the Docker image
> using `docker-compose build api` before restarting the container. Or else
> use `docker-compose up --build api` to build and start in one command.

