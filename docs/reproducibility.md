### 🧪 Validación Condicional de Pruebas

El flujo `make.yml` incluye una verificación ética del entorno de pruebas. Si `tests/` existe, se ejecuta `pytest` dentro del entorno virtual `.venv`. Si no, se documenta la omisión sin interrumpir el flujo.

> Esto garantiza trazabilidad sin fallos innecesarios, y permite modularizar el desarrollo por etapas.
