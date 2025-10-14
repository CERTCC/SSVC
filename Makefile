# Project-specific vars
MKDOCS_PORT=8765
DOCKER_DIR=docker
DOCKER_COMPOSE=docker-compose --project-directory $(DOCKER_DIR)
UV_RUN=uv run

# Targets
.PHONY: all test docs api docker_test clean help mdlint_fix up down regenerate_json


all: help

dev:
	@echo "Set up dev environment..."
	uv sync --dev

mdlint_fix:
	@echo "Running markdownlint..."
	markdownlint --config .markdownlint.yml --fix .

test:
	@echo "Running tests locally..."
	$(UV_RUN) pytest -v

docker_test:
	@echo "Building the latest test image..."
	$(DOCKER_COMPOSE) build test
	@echo "Running tests in Docker..."
	$(DOCKER_COMPOSE) run --rm test

docs_local:
	@echo "Building and running docs locally..."
	$(UV_RUN) mkdocs serve

docs:
	@echo "Building and running docs in Docker..."
	$(DOCKER_COMPOSE) up docs

api:
	@echo "Building and running API in Docker..."
	$(DOCKER_COMPOSE) up api

api_dev:
	$(UV_RUN) uvicorn ssvc.api.main:app --reload

up:
	@echo "Starting Docker services..."
	$(DOCKER_COMPOSE) up -d

down:
	@echo "Stopping Docker services..."
	$(DOCKER_COMPOSE) down

regenerate_json:
	@echo "Regenerating JSON files..."
	rm -rf data/json/decision_points
	export PYTHONPATH=$(PWD)/src && ./src/ssvc/doctools.py --datadir=./data --overwrite

clean:
	@echo "Cleaning up Docker resources..."
	$(DOCKER_COMPOSE) down --rmi local || true

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo " all         - Display this help message"

	@echo " dev        - Set up development environment"
	@echo " mdlint_fix  - Run markdownlint with fix"
	@echo " test       - Run tests locally"
	@echo " docker_test - Run tests in Docker"

	@echo " docs       - Build and run documentation in Docker"
	@echo " docs_local - Build and run documentation locally"

	@echo " api        - Build and run API in Docker"
	@echo " api_dev    - Run API locally with auto-reload"

	@echo " up         - Start Docker services"
	@echo " down       - Stop Docker services"

	@echo " regenerate_json - Regenerate JSON files from python modules"

	@echo " clean      - Clean up Docker resources"
	@echo " help       - Display this help message"


