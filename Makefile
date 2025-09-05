# Makefile for ia-core-models - reproducible educational module
# Firma técnica: Develop Aguascalientes & Copilot Microsoft

# Licensed under the Apache License, Version 2.0 (2025)
# © Develop Aguascalientes & Copilot Microsoft

VENV := .venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

train:
	$(PYTHON) training/train_cnn.py --config configs/cnn_default.yaml

doc:
	mkdir -p docs
	$(PYTHON) -m pydoc training.train_cnn > docs/caso_estudio_cnn.md
	echo "\n\n## Firma técnica\nDevelop Aguascalientes & Copilot Microsoft" >> docs/caso_estudio_cnn.md

clean:
	sudo rm -rf __pycache__ */__pycache__ *.pt modelo_entrenado.pt docs

lock: venv
	$(PIP) install -r configs/requirements.txt

venv:
	test -d $(VENV) || python3 -m venv $(VENV)

verify:
	bash verifica-entorno.sh

docker:
	docker build -t ia-core-models .

all: lock clean train doc

.PHONY: train doc clean lock verify docker all venv

.PHONY: train doc clean lock verify docker all
