# Project-specific vars
PFX=ssvc
DOCKER=docker
DOCKER_BUILD=$(DOCKER) build
DOCKER_RUN=$(DOCKER) run --tty --rm
PROJECT_VOLUME=--volume $(shell pwd):/app
MKDOCS_PORT=8765

# docker names
TEST_DOCKER_TARGET=test
TEST_IMAGE = $(PFX)_test
DOCS_DOCKER_TARGET=docs
DOCS_IMAGE = $(PFX)_docs

# Targets
.PHONY: all dockerbuild_test dockerrun_test dockerbuild_docs dockerrun_docs docs docker_test clean help

all: help

mdlint_fix:
	@echo "Running markdownlint..."
	markdownlint --config .markdownlint.yml --fix .

dockerbuild_test:
	@echo "Building the test Docker image..."
	$(DOCKER_BUILD) --target $(TEST_DOCKER_TARGET) --tag $(TEST_IMAGE) .

dockerrun_test:
	@echo "Running the test Docker image..."
	$(DOCKER_RUN) $(PROJECT_VOLUME) $(TEST_IMAGE)

dockerbuild_docs:
	@echo "Building the docs Docker image..."
	$(DOCKER_BUILD) --target $(DOCS_DOCKER_TARGET) --tag $(DOCS_IMAGE) .

dockerrun_docs:
	@echo "Running the docs Docker image..."
	$(DOCKER_RUN) --publish $(MKDOCS_PORT):8000 $(PROJECT_VOLUME) $(DOCS_IMAGE)


docs: dockerbuild_docs dockerrun_docs
docker_test: dockerbuild_test dockerrun_test

clean:
	@echo "Cleaning up..."
	$(DOCKER) rmi $(TEST_IMAGE) $(DOCS_IMAGE) || true

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo " all         - Display this help message"
	@echo " mdlint_fix  - Run markdownlint with --fix"
	@echo " docs        - Build and run the docs Docker image"
	@echo " docker_test - Build and run the test Docker image"
	@echo ""
	@echo " dockerbuild_test - Build the test Docker image"
	@echo " dockerrun_test   - Run the test Docker image"
	@echo " dockerbuild_docs - Build the docs Docker image"
	@echo " dockerrun_docs   - Run the docs Docker image"
	@echo ""
	@echo " clean - Remove the Docker images"
	@echo " help  - Display this help message"



