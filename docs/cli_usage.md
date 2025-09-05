```plaintext
╔════════════════════════════╗
║  IA-CORE MODULE DOCS       ║
╚════════════════════════════╝

# CLI USAGE GUIDE

# Licensed under the Apache License, Version 2.0 (2025)
# © Develop Aguascalientes & Copilot Microsoft

## Purpose
This document explains how to use the IA-CORE CLI to train models, validate datasets, and log metrics with ethical traceability. Each command integrates modular components documented in this repository.

## Basic Execution
```bash
python cli/ia-core-cli.py --train --config configs/cnn_default.yaml

##Available Flags

--------------------------------------------------------------------
||       Flag         |             Description                    |
||--------------------|--------------------------------------------|
|| --train	          | Trains the model using the provided config |
||--------------------|--------------------------------------------|
|| --validate-dataset | Runs ethical validation on the dataset     |
||--------------------|--------------------------------------------|
||--log-train	      | Saves training metrics and config snapshot |
||--------------------|--------------------------------------------|
||--ascii	          | Displays banner from banner.txt            |
||--------------------|--------------------------------------------|
||--help	          | Shows available commands and usage         |
||--------------------|--------------------------------------------|

##Example Workflow

```bash

python cli/ia-core-cli.py --ascii
python cli/ia-core-cli.py --validate-dataset
python cli/ia-core-cli.py --train --config configs/cnn_default.yaml
python cli/ia-core-cli.py --log-train

##Ethical Notes

Each command is modular and traceable.

Dataset validation prevents unethical training.

Logs ensure reproducibility and auditability.

--------------------------------------------------------------------------------------------------

GUÍA DE USO DEL CLI

##Propósito

Este documento explica cómo usar el CLI de IA-CORE para entrenar modelos, validar datasets y registrar métricas con trazabilidad ética. Cada comando integra componentes modulares documentados en este repositorio.

#Ejecución básica

```bash

python cli/ia-core-cli.py --train --config configs/cnn_default.yaml

##Flags disponibles

|   Flag	                           Descripción
|-----------------!-----------------------------------------------------------|
|--train          |	 Entrena el modelo usando la configuración proporcionada  |
|-----------------|-----------------------------------------------------------|
|--validate-dataset	| Ejecuta validación ética sobre el dataset               |
|-------------------|
|--log-train	Guarda  métricas de entrenamiento y snapshot de configuración

|--ascii	            Muestra el banner desde banner.txt

|--help	            Muestra los comandos disponibles y su uso


##Flujo de trabajo ejemplo

```bash

python cli/ia-core-cli.py --ascii
python cli/ia-core-cli.py --validate-dataset
python cli/ia-core-cli.py --train --config configs/cnn_default.yaml
python cli/ia-core-cli.py --log-train

##Notas éticas

Cada comando es modular y trazable.

La validación del dataset previene entrenamientos no éticos.

Los logs garantizan reproducibilidad y auditabilidad.
