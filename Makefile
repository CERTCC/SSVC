# Project-specific vars
MKDOCS_PORT=8765
DOCKER_DIR=docker

# Targets
.PHONY: all test docs docker_test clean help

all: help

mdlint_fix:
	@echo "Running markdownlint..."
	markdownlint --config .markdownlint.yml --fix .

test:
	@echo "Running tests locally..."
	pytest -v src/test

docker_test:
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

clean:
	@echo "Cleaning up Docker resources..."
	pushd $(DOCKER_DIR) && docker-compose down --rmi local || true

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo " all         - Display this help message"
	@echo " mdlint_fix  - Run markdownlint with --fix"
	@echo " test        - Run the tests in a local shell"
	@echo " docs        - Build and run the docs Docker service"
	@echo " docker_test - Run the tests in a Docker container"
	@echo " clean       - Remove Docker containers and images"
	@echo " help        - Display this help message"
