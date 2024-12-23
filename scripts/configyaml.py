import yaml
import os

def load_config():
    """Carrega o arquivo config.yaml e retorna as configurações."""
    # Diretório base é o local deste arquivo Python
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "../config/config.yaml")  # Caminho relativo à pasta do script

    # Verificar se o arquivo existe
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Arquivo config.yaml não encontrado: {config_path}")

    # Carregar o arquivo config.yaml
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
