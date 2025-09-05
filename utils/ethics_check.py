# ethics_check.py

def validate_dataset(dataset):
    labels = [label for _, label in dataset]
    unique = set(labels)
    if len(unique) < 2:
        print("⚠️ Dataset no tiene clases suficientes")
    if len(labels) < 100:
        print("⚠️ Dataset demasiado pequeño para entrenamiento ético")
    print(f"✅ Dataset validado: {len(labels)} muestras, {len(unique)} clases")

# Licensed under the Apache License, Version 2.0 (2025)
# © Develop Aguascalientes & Copilot Microsoft
