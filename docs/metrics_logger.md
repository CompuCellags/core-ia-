```plaintext
╔════════════════════════════╗
║  IA-CORE MODULE DOCS       ║
╚════════════════════════════╝

# METRICS_LOGGER MODULE

## Purpose
This module records training metrics and configuration parameters in structured JSON logs. It ensures traceability, reproducibility, and ethical transparency in model development.

## Usage
```python
from utils.metrics_logger import save_log
save_log("train", config, {"final_loss": 0.034})

##Example Output

##json

{ "timestamp": "2025-09-04T18:45:00Z", "action": "train", "model": "cnn_v1", "parameters": { "epochs": 10, "batch_size": 32 }, "metrics": { "final_loss": 0.034 } }

##Ethical Notes Creates a verifiable record of model behavior and training conditions.

Supports auditability and responsible experimentation.

--------------------------------------------------------------------------------------------------

##Propósito Este módulo registra métricas de entrenamiento y parámetros de configuración en logs JSON estructurados. Garantiza trazabilidad, reproducibilidad y transparencia ética en el desarrollo de modelos.

##Uso

##Python

from utils.metrics_logger import save_log
save_log("train", config, {"final_loss": 0.034})

##Ejemplo de salida

##json

{ "timestamp": "2025-09-04T18:45:00Z", "action": "train", "model": "cnn_v1", "parameters": { "epochs": 10, "batch_size": 32 }, "metrics": { "final_loss": 0.034 } }

##Notas éticas Genera un registro verificable del comportamiento del modelo y condiciones de entrenamiento.

Apoya la auditabilidad y la experimentación responsable.

