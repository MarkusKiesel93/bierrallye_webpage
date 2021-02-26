from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_mail import FastMail
import pytest
from typing import Generator

from app.api import router
from app.mail import fast_mail

# todo: how do I need different scopes ?
# monkeypatch and scope module cant be used

@pytest.fixture()
def client(monkeypatch) -> Generator:
    monkeypatch.setenv('DATABASE', 'test.db')

    app = FastAPI()
    app.include_router(router)

    with TestClient(app) as client:
        yield client


@pytest.fixture(scope='module')
def fm() -> FastMail:
    fm = fast_mail
    fm.config.SUPPRESS_SEND = 1
    yield fm
