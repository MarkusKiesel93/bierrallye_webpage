from pathlib import Path
import yaml

PROJECT_ROOT = Path('.')
CONFIG = Path(__file__).parent / 'setup.yml'


def load_config(section):
    with open(CONFIG, 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)
    cfg = cfg[section]
    return cfg


def test_strucutre():
    config = load_config('folders')
    for folder in config:
        main_folder = PROJECT_ROOT / folder
        assert main_folder.is_dir()
        for sub_folder in config[folder]:
            assert (main_folder / sub_folder).is_dir()


def test_files_exist():
    config = load_config('files')
    for folder in config:
        if folder == 'root':
            main_folder = PROJECT_ROOT
        else:
            main_folder = PROJECT_ROOT / folder
        for file in config[folder]:
            assert (main_folder / file).is_file()


def test_deploy():
    config = load_config('deploy')
    for folder in config:
        if folder == 'root':
            main_folder = PROJECT_ROOT
        else:
            main_folder = PROJECT_ROOT / folder / 'deploy'
        for file in config[folder]:
            assert (main_folder / file).is_file()
