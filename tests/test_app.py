from http import HTTPStatus


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


def test_conta_valores(client):

    response = client.post('/count', json={
        'in_value1': 2,
        'in_value2': 3
    })  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert

    assert response.json() == {
        'in_value1': 2,
        'in_value2': 3,
        'out_value': 5
    }  # Assert
