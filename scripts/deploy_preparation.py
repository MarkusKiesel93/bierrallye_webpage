# environment file to use with docker
def create_env_file(configs, env_path):
    with open(env_path, 'w') as env_file:
        for config, value in configs.items():
            env_file.write(f'{config.upper()}={value}\n')


# environment file to use with vue
# 'VUE_APP_' needed to be used by process.env
# todo: is there a better way to do this ?
# todo: secrets should not be leaked to vue !!
def create_vue_env_file(configs, env_path):
    with open(env_path, 'w') as env_file:
        for config, value in configs.items():
            env_file.write(f'VUE_APP_{config.upper()}={value}\n')


def create_nginx_conf(configs, service_path):
    for service in ['backend', 'frontend']:
        for template_file in (service_path / 'deploy').glob(f'**/*nginx.conf_{configs["deploy_mode"]}'):
            fill_template(configs, template_file)


def fill_template(configs, template_file):
    with open(template_file, 'r') as t_file:
        template = t_file.read()
        for config, value in configs.items():
            template = template.replace(f'{{{{{config}}}}}', str(value))
    with open(template_file.parent / 'nginx.conf', 'w') as new_file:
        new_file.write(template)
