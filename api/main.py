from fastapi import FastAPI
import torch
from models.simple_cnn import SimpleCNN

app = FastAPI(title="Servidor IA Educativo")

# Cargar modelo entrenado (simulado)
model = SimpleCNN()
model.eval()

@app.get("/")
def read_root():
    return {"mensaje": "Servidor IA activo — Develop Aguascalientes"}

@app.get("/predict")
def predict():
    # Simulación de entrada
    dummy_input = torch.randn(1, 3, 32, 32)
    output = model(dummy_input)
    predicted_class = torch.argmax(output, dim=1).item()
    return {"predicción": predicted_class}
