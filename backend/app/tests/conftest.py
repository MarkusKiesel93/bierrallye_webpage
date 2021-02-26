from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from typing import Generator

from app.api import router

# from ..database import engine, SessionLocal
# from ..models import Base
# from ..main import app
# from ..config import Settings

# @pytest.fixture(scope="module")
# def client(monkeypatch):
#     monkeypatch.setenv('DATABASE', 'test.db')
#     from ..main import app
#     return TestClient(app)


# @pytest.fixture(scope='module')
# def settings() -> Settings:
#     settings = Settings()
#     settings.database = 'test.db'
#     return settings

# @pytest.fixture(scope="module")
# def get_db():
#     settings = Settings(
#         database='test.db',
#         app_name='TEST APP'
#     )
#     db = SessionLocal(engine(settings))
#     try:
#         yield db
#     finally:
#         db.close()


@pytest.fixture()
def client(monkeypatch) -> Generator:
    monkeypatch.setenv('DATABASE', 'test.db')

    app = FastAPI()
    app.include_router(router)

    with TestClient(app) as client:
        yield client
