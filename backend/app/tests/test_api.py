from fastapi.testclient import TestClient
from pathlib import Path
import random
import pandas as pd

from app.hashing import hash_email


TEST_DATA_PATH = Path('./app/tests/data/input.csv')
TEST_DATA = pd.read_csv(TEST_DATA_PATH)


def test_create_verify_delete(client: TestClient):
    assert free_places(client) == 90
    check_options_block(client, 90)

    test_teams = chose_teams(5)

    # create team wrong drink pref player 1
    team_wrong_dring = test_teams[0].copy()
    team_wrong_dring['drink_pref_player_1'] = 'Sturm'
    response = client.post('/team/', json=team_wrong_dring)
    assert response.status_code == 422

    # create team wrong drink pref player 2
    team_wrong_dring = test_teams[0].copy()
    team_wrong_dring['drink_pref_player_2'] = 'Schnaps'
    response = client.post('/team/', json=team_wrong_dring)
    assert response.status_code == 422

    team_wrong_block = test_teams[0].copy()
    team_wrong_block['start_block'] = 'X'
    response = client.post('/team/', json=team_wrong_block)
    assert response.status_code == 422

    # create some teams
    for team in test_teams:
        print(team)
        response = client.post('/team/', json=team)
        assert response.status_code == 201
        # todo: test if email or sms correct

    assert free_places(client) == 90 - 5
    check_options_block(client, 90 - 5)

    # check for error on duplicate
    response = client.post('/team/', json=test_teams[0])
    assert response.status_code == 409

    # check registerd csv
    response = client.get('/registered/csv/')
    assert response.status_code == 200
    check_csv(5, 7)

    # deregister wrong email
    response = client.delete('team/not_exising@test.com/ASDFJK')
    assert response.status_code == 400

    # deregister wrog hash
    response = client.delete(f'team/{test_teams[0]["contact"]}/WRONG!')
    assert response.status_code == 400

    # deregistration
    for team in test_teams:
        contact = team['contact']
        response = client.delete(f'team/{contact}/{hash_email(contact)}')
        assert response.status_code == 200
        # todo: test if email or sms correct


def test_options_drink(client: TestClient):
    response = client.get('/options/drinks/')
    assert response.status_code == 200
    assert len(response.json()) == 5


def check_options_block(client: TestClient, places_free):
    response = client.get('/options/blocks/')
    assert response.status_code == 200
    assert len(response.json()) == 6
    free_overall = 0
    for block in response.json():
        free_overall += block['free']
    assert free_overall == places_free


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


def check_csv(rows, cols):
    CSV_PATH = Path('./static/registrierte_nutzer.csv')
    df = pd.read_csv(CSV_PATH)
    assert df.shape[0] == rows
    assert df.shape[1] == cols
