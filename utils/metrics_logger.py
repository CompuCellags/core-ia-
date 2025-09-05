# metrics_logger.py

import json, os
from datetime import datetime

def save_log(action, config, metrics=None):
    os.makedirs("logs", exist_ok=True)
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "model": config['model']['name'],
        "parameters": config['training'],
        "metrics": metrics or {}
    }
    filename = f"{action}_{config['model']['name']}.json"
    path = os.path.join("logs", filename)
    with open(path, 'w') as f:
        json.dump(log, f, indent=2)
    print(f"📝 Log guardado en: {path}")
