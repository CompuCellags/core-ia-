#!/usr/bin/env python3
# ia-core-cli.py

import argparse
import shutil
import os
import yaml
import json
from datetime import datetime

# === Funciones de comandos ===

def deploy_model(args):
    print_ascii_art('deploy')
    print(f"🚀 Desplegando modelo '{args.model}' en entorno '{args.env}' con configuración '{args.config}'")

def list_models(args):
    if getattr(args, 'banner', None) == 'full':
        print_ascii_art('list')
    else:
        print("📦 Modelos disponibles:")
    print("- ia-customer-service")
    print("- ia-automation")
    print("- ia-integration")

def train_model(args):
    print_ascii_art('train')
    print(f"🧠 Entrenando modelo '{args.model}' con dataset '{args.dataset}'")

    # Cargar configuración YAML
    try:
        with open(args.config, 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error al leer config: {e}")
        return

    # Validación de claves requeridas
    required_keys = ['model', 'training', 'dataset']
    for key in required_keys:
        if key not in config:
            print(f"❌ Configuración inválida: falta '{key}'")
            return

    # Simulación de entrenamiento
    total_loss = 0.1234  # ← Aquí puedes integrar entrenamiento real más adelante
    print(f"📈 Entrenamiento simulado completado — Loss final: {total_loss}")

    # Guardar log ético
    save_log("train", config, {"final_loss": total_loss})

# === Banner principal ===

def print_banner():
    width = shutil.get_terminal_size((80, 20)).columns
    title = "IA Core CLI — Ethical by Design"
    print(title.center(width, "="))
    script_dir = os.path.dirname(os.path.abspath(__file__))
    banner_path = os.path.join(script_dir, 'banner.txt')
    try:
        with open(banner_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("IA Core Models — Ethical by Design")

# === Arte ASCII por módulo ===

def print_ascii_art(module):
    if module == 'list':
        print(r"""
        _________
       /         \
      /___________\
      ||  MODELOS ||
      ||_________||
      |___________|
        """)
    elif module == 'deploy':
        print(r"""
        ╔════════════╗
        ║  DEPLOY IA ║
        ╚════════════╝
        """)
    elif module == 'train':
        print(r"""
        ╔════════════╗
        ║  TRAIN IA  ║
        ╚════════════╝
        """)

# === Guardar log ético ===

def save_log(action, config, metrics=None):
    os.makedirs("logs", exist_ok=True)
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "model": config['model']['name'],
        "parameters": config['training'],
        "metrics": metrics or {}
    }
    log_path = f"logs/{action}_{config['model']['name']}.json"
    with open(log_path, 'w') as f:
        json.dump(log, f, indent=2)
    print(f"📝 Log guardado en: {log_path}")

# === Main ===

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        prog='ia-core-cli',
        description='CLI para gestionar modelos IA preentrenados del proyecto ia-core-models',
        epilog="""
Ejemplos de uso:
  ia-core-cli deploy --model ia-customer-service --env azure --config config.yaml
  ia-core-cli list --banner full
  ia-core-cli train --model ia-automation --dataset ./data/train.csv --config configs/cnn_default.yaml
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    subparsers = parser.add_subparsers(title='Comandos disponibles', dest='command')

    # Comando: deploy
    deploy = subparsers.add_parser(
        'deploy',
        help='Desplegar un modelo en Azure, Kubernetes o local',
        description="""
Despliega un modelo IA en el entorno especificado.

Ejemplo:
  ia-core-cli deploy --model ia-customer-service --env azure --config config.yaml
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    deploy.add_argument('--model', required=True, help='Nombre del modelo a desplegar')
    deploy.add_argument('--env', choices=['azure', 'kubernetes', 'local'], default='local', help='Entorno de despliegue')
    deploy.add_argument('--config', help='Archivo de configuración YAML/JSON')
    deploy.set_defaults(func=deploy_model)

    # Comando: list
    list_cmd = subparsers.add_parser(
        'list',
        help='Listar modelos disponibles',
        description="""
Muestra los modelos IA disponibles en el repositorio.

Ejemplo:
  ia-core-cli list --banner full
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    list_cmd.add_argument('--banner', choices=['full', 'compact'], help='Mostrar arte ASCII')
    list_cmd.set_defaults(func=list_models)

    # Comando: train
    train = subparsers.add_parser(
        'train',
        help='Entrenar un modelo con dataset personalizado',
        description="""
Entrena un modelo IA usando un dataset local y configuración YAML.

Ejemplo:
  ia-core-cli train --model ia-automation --dataset ./data/train.csv --config configs/cnn_default.yaml
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    train.add_argument('--config', required=True, help='Ruta al archivo YAML de configuración')
    train.add_argument('--model', required=True, help='Nombre del modelo a entrenar')
    train.add_argument('--dataset', required=True, help='Ruta al dataset CSV')
    train.set_defaults(func=train_model)

    # Ejecutar
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
