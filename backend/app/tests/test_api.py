from fastapi.testclient import TestClient
import pandas as pd
from pathlib import Path


TEST_DATA = Path(__file__).parent / 'data' / 'input.csv'

# todo: read https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest


def free_places(client: TestClient):
    response = client.get('/places/free/')
    assert response.status_code == 200
    return response.json()


def test_places_free_initial(client: TestClient):
    fp = free_places(client)
    assert fp == 90


# def test_create_team(client: TestClient):
#     test_data = pd.read_csv(TEST_DATA)
#     for _, row in test_data.iterrows():
#         team = row.to_dict()
#         print(team)
#         response = client.post('/teams/', json=team)
#         print(response.json())
#         assert response.status_code == 201


