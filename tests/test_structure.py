from pathlib import Path
import yaml

PROJECT_ROOT = Path('.')
CONFIG = Path(__file__).parent / 'structure.yml'


def test_strucutre():
    with open(CONFIG, 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)

    for folder in cfg:
        main_folder = (PROJECT_ROOT / folder)
        assert main_folder.is_dir()
        for sub_folder in cfg[folder]:
            assert (main_folder / sub_folder).is_dir()
