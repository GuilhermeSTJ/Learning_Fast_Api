from http import HTTPStatus

import pytest

from fastapi.testclient import TestClient

from learning_fast_api.app import app

@pytest.fixture()
def client():
    return TestClient(app)

def test_read_root_return_ok_and_helloWord(client):

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert

    assert response.json() == {'message': 'Hello, World!'}  # Assert


def test_create_user(client):

    response = client.post('/users', json={
        'username': 'test',
        'email': 'test@test.com',
        'password': 'test1234'
    })  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert

    assert response.json() == {
        'username': 'test',
        'email': 'test@test.com',
        'id': 1
    }  # Assert
