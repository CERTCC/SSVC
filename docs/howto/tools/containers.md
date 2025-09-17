# SSVC Docker Containers

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose

Then clone the repository:

```shell
git clone https://github.com/CERTCC/SSVC.git
cd SSVC
```

!!! tip "Quick Start"

    To quickly start all the containers, run:

    ```shell
    docker-compose --project-directory=docker up
    ```

## Test

We provide a containerized environment to run the SSVC test suite.

```shell
docker-compose --project-directory=docker up test
```

## Docs

We provide a containerized environment to build and serve the SSVC documentation (this website).

```shell
docker-compose --project-directory=docker up docs
```

Then browse to `http://localhost:8000/docs` to access the docs site.

## SSVC Object Registry API Container

We provide containerized FastAPI server that allows you to run a local instance
of the SSVC Object Registry API.

```shell
docker-compose --project-directory=docker up api
```

Then browse to `http://localhost:8001/docs` to access the API documentation.
