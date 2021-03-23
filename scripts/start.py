from pathlib import Path
import subprocess as sp
import argparse as ap
import sys

from config_loader import load_configs
from deploy_preparation import create_env_file, create_vue_env_file, create_nginx_conf


PATH_REPO = Path('.').resolve()
PATH_CONFIGS = PATH_REPO / 'configs.yml'
PATH_CONFIGS_SECRET = PATH_REPO.parent / 'secret_configs.yml'
PATH_DOCKER_ENV = PATH_REPO / '.env'
PATH_VUE_ENV = PATH_REPO / 'frontend' / '.env'
PATH_SERVICES = {
    'backend': PATH_REPO / 'backend',
    'frontend': PATH_REPO / 'frontend',
}


parser = ap.ArgumentParser(prog='Run Webpage', description='Script to run development or production server')
parser.add_argument('-dev', '--development', action='store_true', help='run development server')
parser.add_argument('-prod', '--production', action='store_true', help='run production server')
parser.add_argument('-b', '--backend', action='store_true', help='run backend seperately')
parser.add_argument('-f', '--frontend', action='store_true', help='run frontend seperately')
parser.add_argument('-s', '--stop', action='store_true', help='stop all docker containers')

args = parser.parse_args()
num_args = sum(vars(args).values())

if num_args != 1:
    raise Exception('Select exactly one option.')

deploy_mode = 'production'
if not args.production:
    deploy_mode = 'development'

configs = load_configs(deploy_mode, PATH_CONFIGS, PATH_CONFIGS_SECRET)
create_env_file(configs, PATH_DOCKER_ENV)
create_vue_env_file(configs, PATH_VUE_ENV)
for service_path in PATH_SERVICES.values():
    create_nginx_conf(configs, service_path)


try:
    if args.production:
        print(f'RUN PRODUCTION SERVER FOR: {configs["project_name"]}')
        sp.run(['docker-compose', '--env-file', '.env', 'up', '--build', '--detach'])
    elif args.development:
        print(f'RUN DEVELOPMENT SERVER FOR: {configs["project_name"]}')
        sp.run(['npm', 'install'], cwd='./frontend/')
        sp.run(['docker-compose', '--file', 'docker-compose.dev.yml', '--env-file', '.env', 'up', '--build'])
    elif args.backend:
        print(f'RUN BACKEND FOR: {configs["project_name"]}')
        sp.run(['docker-compose', '--file', 'docker-compose.backend.yml', '--env-file', '.env', 'up', '--build'])
    elif args.frontend:
        print(f'RUN FRONTEND FOR: {configs["project_name"]}')
        sp.run(['docker-compose', '--file', 'docker-compose.frontend.yml', '--env-file', '.env', 'up', '--build'])
    elif args.stop:
        print(f'STOP CONTAINERS FOR: {configs["project_name"]}')
        containers = ['frontend', 'server', 'backend']
        for container in containers:
            sp.run(['docker', 'container', 'stop', f'{configs["project_name"]}_{container}'])
except KeyboardInterrupt:
    print(f'shutting down {deploy_mode} server')
    sys.exit(1)
