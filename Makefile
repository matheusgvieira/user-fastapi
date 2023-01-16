API_URL := https://api.com.br
API_TOKEN := e4545c16-0768-11ed-b939-0242ac120002

export API_URL
export API_TOKEN


env:
	pip3 install virtualenv
	virtualenv venv
	source venv/bin/activate

envs:
	@echo $(API_URL)
	@echo $(API_TOKEN)

avenv:
	source venv/bin/activate

nvenv:
	deactivate

install:
	pip3 install -e .

clean:
	rm -rf pytest
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf docs/_build
	rm -rf *_cache

flake:
	flake8 src/*.py
	flake8 tests/unit/*.py

black:
	black src/*.py
	black tests/unit/*.py

mypy:
	mypy tests
	mypy src

lint:
	pylint src/*.py

check:
	black src/*.py
	black tests/integration/*.py
	black tests/unit/*.py
	isort src/*.py
	isort tests/integration/*.py
	isort tests/unit/*.py
	flake8 src/*.py
	flake8 tests/integration/*.py
	flake8 tests/unit/*.py
	mypy tests
	mypy src

tdd:
	pytest -m "usuarios" --disable-pytest-warnings

run:
	uvicorn main:app --reload