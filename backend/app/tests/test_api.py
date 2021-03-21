from fastapi.testclient import TestClient
import pandas as pd
from pathlib import Path
import json
import random

from app.hashing import hash_email


TEST_DATA_PATH = Path(__file__).parent / 'data' / 'input.csv'
TEST_DATA = pd.read_csv(TEST_DATA_PATH)

# todo: read https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest


def chose_teams(n: int, max: int = 90):
    teams = []
    rows = []
    for i in range(n):
        row = -1
        while row == -1 or row in rows:
            row = random.choice(range(90))
        rows.append(row)
        teams.append(TEST_DATA.iloc[row].to_dict())
    return teams


def free_places(client: TestClient):
    response = client.get('/places/free/')
    assert response.status_code == 200
    return response.json()


def test_api(client: TestClient):
    assert free_places(client) == 90

    # create some teams
    test_teams = chose_teams(5)
    for team in test_teams:
        response = client.post('/team/', json=team)
        assert response.status_code == 201

    assert free_places(client) == 90 - 5

    # check for error on duplicate
    response = client.post('/team/', json=test_teams[0])
    assert response.status_code == 409

    # verify teams
    for team in test_teams:
        response = client.post(
            'team/verify',
            json={
                'email': team['email'],
                'hash': hash_email(team['email'])
            })
        assert response.status_code == 200
