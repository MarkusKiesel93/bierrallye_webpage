import re

from app.config import settings


def test_settings_exist():
    assert len(settings.deploy_mode) >= 3
    assert len(settings.app_name) >= 3
    assert len(settings.frontend_domain) >= 5
    assert len(settings.cors_allowed_origins) >= 1
    assert len(settings.cors_allowed_headers) >= 1
    assert len(settings.cors_allowed_methods) >= 1
    assert len(settings.database) >= 3
    assert len(settings.secret_key) >= 10


def test_settings():
    assert settings.deploy_mode in ['production', 'development']
    assert settings.database.endswith('.db')


def test_settings_mail():
    mail_regex = r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$'
    assert re.match(mail_regex, settings.mail_config.MAIL_USERNAME)
    assert re.match(mail_regex, settings.mail_config.MAIL_FROM)
    assert settings.mail_config.MAIL_TLS in [True, False]
    assert settings.mail_config.MAIL_SSL in [True, False]
    assert len(settings.mail_config.MAIL_SERVER) >= 3
