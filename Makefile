.PHONY: rust-version format lint test run release all create read update delete

rust-version:
	@echo "Rust command-line utility versions:"
	@rustc --version
	@cargo --version
	@rustfmt --version
	@rustup --version
	@clippy-driver --version

lint:
	@cargo clippy --quiet

test:
	@cargo test --quiet

run:
	@cargo run

release:
	@cargo build --release

all: format lint test run

# CRUD operation targets
create:
	@cargo run -- create

read:
	@cargo run -- read

update:
	@cargo run -- update

delete:
	@cargo run -- delete

extract:
	@cargo run -- extract

load:
	@cargo run -- load


# Install dependencies
python_install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run tests using pytest and generate coverage
python_test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

# Run unittests directly
python_unittest:
	python -m unittest discover -s . -p "test_*.py"


# Format code with black
python_format:
	black *.py mylib/*.py

# Lint code with ruff (for faster linting)
python_lint:
	# Disable comment to test speed
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

# Lint Dockerfile with hadolint
python_container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

# Refactor: run format and lint
python_refactor: format lint

# Deploy target (implementation needed)
python_deploy:
	# deploy goes here

# Run all steps (install, lint, test, format, deploy)
python_all: python_install python_lint python_test python_format python_deploy
