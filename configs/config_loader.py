# config_loader.py

import yaml

REQUIRED_KEYS = ['model', 'training', 'dataset']

def load_config(path):
    try:
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        raise ValueError(f"❌ Error al leer config: {e}")

    for key in REQUIRED_KEYS:
        if key not in config:
            raise ValueError(f"❌ Configuración inválida: falta '{key}'")

    return config

# Licensed under the Apache License, Version 2.0 (2025)
# © Develop Aguascalientes & Copilot Microsoft
