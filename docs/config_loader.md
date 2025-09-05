```plaintext
╔════════════════════════════╗
║  IA-CORE MODULE DOCS       ║
╚════════════════════════════╝

# CONFIG_LOADER MODULE

# Licensed under the Apache License, Version 2.0 (2025)
# © Develop Aguascalientes & Copilot Microsoft

## Purpose
This module loads and validates YAML configuration files used in model training and deployment. It ensures the presence of required keys and prevents execution with incomplete parameters.

## Usage
```python
from configs.config_loader import load_config
config = load_config("configs/cnn_default.yaml")

##Example Output

##json

{
  "model": {...},
  "training": {...},
  "dataset": {...}
}

##Ethical Notes
Prevents silent failures due to missing parameters.

Encourages explicit configuration and reproducibility.

----------------------------------------------------------------------------------------

##Propósito
Este módulo carga y valida archivos de configuración YAML utilizados en el entrenamiento y despliegue de modelos. Asegura la presencia de claves requeridas y evita ejecuciones con parámetros incompletos.

##Uso
python
from configs.config_loader import load_config
config = load_config("configs/cnn_default.yaml")

##Ejemplo de salida

##json

{
  "model": {...},
  "training": {...},
  "dataset": {...}
}

##Notas éticas
Previene fallos silenciosos por falta de parámetros.

Promueve configuración explícita y reproducibilidad.
