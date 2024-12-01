all: venv

venv:
	python -m virtualenv --python python3.10 .venv-bootstrap
	./.venv-bootstrap/bin/pip install -r requirements-bootstrap.txt
	python -m virtualenv --python python3.10 venv


test: venv
	venv/bin/python tests/test_rectangle.py

clean:
	rm -rf .venv-bootstrap venv
