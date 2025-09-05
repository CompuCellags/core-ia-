```plaintext
╔════════════════════════════╗
║  IA-CORE MODULE DOCS       ║
╚════════════════════════════╝

# ETHICS_CHECK MODULE

# Licensed under the Apache License, Version 2.0 (2025)
# © Develop Aguascalientes & Copilot Microsoft

## Purpose
This module performs basic ethical validation on datasets before training. It checks for minimum sample size and class diversity to ensure responsible and meaningful model development.

## Usage
```python
from utils.ethics_check import validate_dataset
validate_dataset(dataloader.dataset)

##Example Output

##plaintext

✅ Dataset validated: 120 samples, 3 classes

⚠️ Dataset too small for ethical training

⚠️ Dataset lacks sufficient class diversity

##Ethical Notes Helps prevent biased or meaningless training runs.

Encourages responsible dataset curation and transparency.

-------------------------------------------------------------------------------------------

##Propósito Este módulo realiza una validación ética básica sobre datasets antes del entrenamiento. Verifica el tamaño mínimo de muestra y la diversidad de clases para asegurar un desarrollo de modelos responsable y significativo.

##Uso

##Python

from utils.ethics_check import validate_dataset
validate_dataset(dataloader.dataset)

##Ejemplo de salida

##plaintext

✅ Dataset validado: 120 muestras, 3 clases

⚠️ Dataset demasiado pequeño para entrenamiento ético

⚠️ El dataset no tiene suficiente diversidad de clases

##Notas éticas Ayuda a prevenir entrenamientos sesgados o sin significado.

Promueve la curación responsable de datasets y la transparencia.
