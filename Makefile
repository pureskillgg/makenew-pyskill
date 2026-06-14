all: build

build:
	@rm -rf dist
	@uv build

format:
	@uv run black .

lint:
	@uv run pylint ./pureskillgg_makenew_pyskill
	@uv run black --check .

test:
	@uv run pytest --cov=./pureskillgg_makenew_pyskill

watch:
	@uv run ptw

notebook:
	@uv run jupyter notebook notebooks

version:
	@git add pyproject.toml uv.lock
	@git commit -m "$$(uv version --short)"
	@git tag --sign "v$$(uv version --short)" -m "$(uv version --short)"
	@git push --follow-tags

.PHONY: build format lint notebook test watch version
