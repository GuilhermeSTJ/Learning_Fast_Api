from http import HTTPStatus

from fastapi.testclient import TestClient

from learning_fast_api.app import app


def test_read_root_return_ok_and_hW():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert

    assert response.json() == {'message': 'Hello, World!'}  # Assert    
