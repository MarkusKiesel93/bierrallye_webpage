from pathlib import Path
import yaml

PROJECT_ROOT = Path('.')
CONFIG = PROJECT_ROOT / 'configs.yml'

SECTIONS = ['general', 'production', 'development']
CONFIGS_GENERAL = ['project_name', 'app_name', 'version']
CONFIGS_PRODUCTION = ['backend_domain', 'frontend_domain', 'backend_port']
CONFIGS_DEVELOPMENT = ['frontend_domain', 'backend_port', 'frontend_port', 'server_port']


def load_config():
    with open(CONFIG, 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)
    return cfg


def test_sections():
    config = load_config()
    for section in config:
        assert section in SECTIONS


def test_configsl():
    config = load_config()
    for setting in config['general']:
        assert setting in CONFIGS_GENERAL
    for setting in config['production']:
        assert setting in CONFIGS_PRODUCTION
    for setting in config['development']:
        assert setting in CONFIGS_DEVELOPMENT
