from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_mail import FastMail
import pytest
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api import router
from app.mail import fast_mail
from app.database import Base, get_db

# todo: how do I need different scopes ?
# monkeypatch and scope module cant be used


@pytest.fixture(scope='module')
def client() -> Generator:
    database_url = 'sqlite:///database/test.db'
    engine = create_engine(database_url, connect_args={'check_same_thread': False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app = FastAPI()
    app.dependency_overrides[get_db] = override_get_db
    app.include_router(router)

    with TestClient(app) as client:
        yield client
    # todo remove database


@pytest.fixture(scope='module')
def fm() -> FastMail:
    fm = fast_mail
    fm.config.SUPPRESS_SEND = 1
    yield fm
