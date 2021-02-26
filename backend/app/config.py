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
        MAIL_USERNAME=os.getenv('EMAIL_ADDRESS'),
        MAIL_PASSWORD=os.getenv('EMAIL_PASSWORD'),
        MAIL_FROM=os.getenv('EMAIL_ADDRESS'),
        MAIL_PORT=587,
        MAIL_SERVER='mail.gmx.net',
        MAIL_FROM_NAME='Bierralley Irnfritz',
        MAIL_TLS=True,
        MAIL_SSL=False,
    )

    secret_key: str


settings = Settings()
