import yaml


# return one dict with all configs for deploy_mode
def load_configs(deploy_mode, config_path, secret_config_path):
    configs = {}
    configs['deploy_mode'] = deploy_mode

    with open(config_path, 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)

    # general configs
    for config in cfg['general']:
        configs[config] = cfg["general"][config]

    # configs for deploy mode
    for config in cfg[deploy_mode]:
        configs[config] = cfg[deploy_mode][config]

    # secret configs
    with open(secret_config_path, 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)
        cfg = cfg[configs['project_name']]
    for config in cfg:
        configs[config] = cfg[config]

    return configs
