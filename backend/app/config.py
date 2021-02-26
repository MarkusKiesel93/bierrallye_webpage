import os
from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings


class Settings(BaseSettings):
    deploy_mode: str
    app_name: str
    frontend_domain: str

    cors_allowed_origins: list = [
        os.getenv('FRONTEND_DOMAIN'),
        f'www.{os.getenv("FRONTEND_DOMAIN")}',
    ]
    cors_allowed_methods: list = ['POST', 'DELETE']
    cors_allowed_headers: list = ['*']

    if os.getenv('DEPLOY_MODE') == 'development':
        cors_allowed_origins: list = ['*']

    database: str

    mail_config: object = ConnectionConfig(
        MAIL_USERNAME='markuskiesel@gmx.at',
        # Todo import password from secret in os 
        MAIL_PASSWORD='',
        MAIL_FROM='markuskiesel@gmx.at',
        MAIL_PORT=587,
        MAIL_SERVER='mail.gmx.net',
        MAIL_FROM_NAME='Bierralley Irnfritz',
        MAIL_TLS=True,
        MAIL_SSL=False,
    )

    secret_key: str


settings = Settings()
