# Makefile for gendiff project

# Install dependencies and setup development environment
install:
	uv pip install -e .[dev]

# Build package distribution
build:
	uv build

# Install package globally
package-install:
	uv tool install dist/*.whl

# Run linter (Ruff)
lint:
	uv run ruff check .

# Combined check for CI: run linter and tests
check:
	make lint
	make test-coverage  

# Run tests (using pytest from virtual environment)
test:
	uv run pytest -v tests/

# Run tests with coverage report (for SonarQube)
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml tests/

# Run gendiff with example files
demo:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

# Clean build artifacts
clean:
	rm -rf dist
	rm -rf .venv
	rm -rf .pytest_cache
	rm -f coverage.xml
	rm -rf __pycache__
	rm -rf gendiff/__pycache__
	rm -rf gendiff/scripts/__pycache__
	rm -rf tests/__pycache__
