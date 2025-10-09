VENV := venv
PYTHON := $(VENV)/bin/python

.PHONY: venv
venv:
	python3 -m venv $(VENV)

.PHONY: install
install: venv
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: test
test: install
	$(PYTHON) -m pytest