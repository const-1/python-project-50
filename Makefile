# Makefile for gendiff project

# Virtual environment paths
VENV = .venv
PYTHON = $(VENV)/bin/python
RUFF = $(VENV)/bin/ruff
PYTEST = $(VENV)/bin/pytest
GENDIFF = $(VENV)/bin/gendiff
UV = $(VENV)/bin/uv

# Default target
all: install test

# Install dependencies and setup development environment
install:
	@echo "Creating virtual environment..."
	python -m uv venv $(VENV)
	$(UV) pip install -e .[dev]

# Build package distribution
build:
	$(UV) build

# Run linter (Ruff)
lint:
	$(RUFF) check gendiff tests

# Combined check for CI: run linter and tests
check: lint test-coverage

# Run all tests
test:
	$(PYTEST) -v tests/

# Run gendiff with example files
demo:
	$(GENDIFF) tests/fixtures/file1.json tests/fixtures/file2.json

# Test JSON files
test-json:
	$(GENDIFF) tests/fixtures/file1.json tests/fixtures/file2.json

# Test YAML files
test-yaml:
	$(GENDIFF) tests/fixtures/file1.yml tests/fixtures/file2.yml

# Test recursive structures
test-recursive:
	$(PYTEST) -v tests/test_recursive.py

# Run all tests
test-all: test-json test-yaml test-recursive

# Run tests with coverage report
test-coverage:
	$(PYTEST) --cov=gendiff --cov-report=xml tests/

# Clean build artifacts
clean:
	rm -rf dist
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -f coverage.xml
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -delete

# Phony targets
.PHONY: all install build lint check test demo test-json test-yaml test-recursive test-all test-coverage clean
