from pathlib import Path
import yaml

PROJECT_ROOT = Path('.')
CONFIG = PROJECT_ROOT / 'configs.yml'
CONFIG_SECRET = PROJECT_ROOT.resolve().parent / 'secret_configs.yml'

SECTIONS = ['general', 'production', 'development']
CONFIGS_GENERAL = ['project_name', 'app_name', 'version']
CONFIGS_PRODUCTION = ['backend_domain', 'frontend_domain', 'backend_port']
CONFIGS_DEVELOPMENT = ['frontend_domain', 'backend_port', 'frontend_port', 'server_port']
CONFIGS_SECRET = ['email_address', 'email_password']


def load_config(config_path):
    with open(config_path, 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)
    return cfg


def test_sections():
    config = load_config(CONFIG)
    assert set(config.keys()) == set(SECTIONS)


def test_configs():
    config = load_config(CONFIG)
    assert set(config['general'].keys()) == set(CONFIGS_GENERAL)
    assert set(config['production'].keys()) == set(CONFIGS_PRODUCTION)
    assert set(config['development'].keys()) == set(CONFIGS_DEVELOPMENT)


def test_secret_configs():
    config = load_config(CONFIG)
    secret_config = load_config(CONFIG_SECRET)
    project_name = config['general']['project_name']
    assert project_name in secret_config.keys()
    assert set(secret_config[project_name].keys()) == set(CONFIGS_SECRET)
