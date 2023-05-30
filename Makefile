checkfiles = gema/ tests/ conftest.py
py_warn = PYTHONDEVMODE=1

up:
	@poetry update

deps:
	@poetry install

style: deps
	@isort -src $(checkfiles)
	@black $(checkfiles)

check: deps
	@black --check $(black_opts) $(checkfiles) || (echo "Please run 'make style' to auto-fix style issues" && false)
	@ruff $(checkfiles) --fix
	@mypy $(checkfiles)

test: deps
	$(py_warn) pytest --cov-append --cov-report=

build: deps
	@poetry build

publish: deps
	@poetry publish --build

ci: check test
