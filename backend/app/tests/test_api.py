from fastapi.testclient import TestClient
import pandas as pd
from pathlib import Path


TEST_DATA = Path(__file__).parent / 'data' / 'input.csv'

# todo: read https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest

# maby use a in memory database for testing
# look if this is possible for sqlalchemy


# def test_settings(settings: Settings):
#     print(type(settings))
#     assert settings.database == 'test.db'


# def test_create_team(client: TestClient):
#     test_data = pd.read_csv(TEST_DATA)
#     for _, row in test_data.iterrows():
#         team = row.to_dict()
#         print(team)
#         response = client.post('/teams/', json=team)
#         print(response.json())
#         assert response.status_code == 201
