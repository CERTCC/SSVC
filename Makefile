# Project-specific vars
MKDOCS_PORT=8765
DOCKER_DIR=docker
PROJECT_DIR = ./src
# Targets
.PHONY: all test docs docker_test clean help mdlint_fix up down regenerate_json

all: help

dev:
	@echo "Set up dev environment..."
	uv sync --dev --project $(PROJECT_DIR)

mdlint_fix:
	@echo "Running markdownlint..."
	markdownlint --config .markdownlint.yml --fix .

test:
	@echo "Running tests locally..."
	uv run --project $(PROJECT_DIR) pytest -v

docker_test:
	@echo "Building the latest test image..."
	pushd $(DOCKER_DIR) && docker-compose build test
	@echo "Running tests in Docker..."
	pushd $(DOCKER_DIR) && docker-compose run --rm test

docs:
	@echo "Building and running docs in Docker..."
	pushd $(DOCKER_DIR) && docker-compose up docs

up:
	@echo "Starting Docker services..."
	pushd $(DOCKER_DIR) && docker-compose up -d

down:
	@echo "Stopping Docker services..."
	pushd $(DOCKER_DIR) && docker-compose down

regenerate_json:
	@echo "Regenerating JSON files..."
	rm -rf data/json/decision_points
	export PYTHONPATH=$(PWD)/src && ./src/ssvc/doctools.py --jsondir=./data/json/decision_points --overwrite

clean:
	@echo "Cleaning up Docker resources..."
	pushd $(DOCKER_DIR) && docker-compose down --rmi local || true
	rm -rf $(PROJECT_DIR)/.venv $(PROJECT_DIR)/uv.lock
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
	@echo " up         - Start Docker services"
	@echo " down       - Stop Docker services"
	@echo " regenerate_json - Regenerate JSON files from python modules"
	@echo " clean      - Clean up Docker resources"
	@echo " help       - Display this help message"


