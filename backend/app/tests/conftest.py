from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_mail import FastMail
import pytest
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from app.api import router
from app.database import Base, get_db
from app.mail import get_fm
from app.config import settings

# todo: how do I need different scopes ?
# monkeypatch and scope module cant be used


@pytest.fixture(scope='module')
def client() -> Generator:
    database_url = 'sqlite:///db/test.db'
    engine = create_engine(database_url, connect_args={'check_same_thread': False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    def override_get_fm():
        fast_mail = FastMail(settings.mail_config)
        fast_mail.config.SUPPRESS_SEND = 1
        yield fast_mail

    app = FastAPI()
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_fm] = override_get_fm
    app.include_router(router)

    try:
        with TestClient(app) as client:
            yield client
    finally:
        os.remove('./db/test.db')


@pytest.fixture(scope='module')
def fm() -> FastMail:
    fast_mail = FastMail(settings.mail_config)
    fast_mail.config.SUPPRESS_SEND = 1
    fast_mail.config.SUPPRESS_SEND = 1
    yield fast_mail
