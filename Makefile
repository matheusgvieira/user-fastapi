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

install-dev:
	pip3 install -e ."[dev]"

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
	black app/*.py
	black app/config/*.py
	black app/database/*.py
	black tests/unit/*.py

mypy:
	mypy tests
	mypy src

lint:
	pylint src/*.py

check:
	black app/*.py
	black app/config/*.py
	black app/database/*.py
	black app/services/*.py
	black tests/integration/*.py
	black tests/unit/*.py
	isort app/*.py
	isort app/config/*.py
	isort app/database/*.py
	isort app/services/*.py
	isort tests/integration/*.py
	isort tests/unit/*.py
	flake8 app/*.py
	flake8 tests/integration/*.py
	flake8 tests/unit/*.py
	mypy tests
	mypy app

tdd:
	pytest -m "usuarios" --disable-pytest-warnings

run-uvicorn:
	uvicorn main:app --reload

run:
	skaffold dev --port-forward

install-nginx:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.2.0/deploy/static/provider/cloud/deploy.yaml