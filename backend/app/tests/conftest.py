import pytest
import os
from typing import Generator
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_mail import FastMail
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from twilio.rest import Client

from app.api import router
from app.database import Base, get_db
from app.notify import get_fm, get_twilio_client
from app.config import settings


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

    def override_get_twilio_client() -> Client:
        client = Client(settings.twilio_test_sid, settings.twilio_test_token)
        yield client

    app = FastAPI()
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_fm] = override_get_fm
    app.dependency_overrides[get_twilio_client] = override_get_twilio_client
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


@pytest.fixture(scope='module')
def twilio_client() -> Client:
    client = Client(settings.twilio_test_sid, settings.twilio_test_token)
    yield client
