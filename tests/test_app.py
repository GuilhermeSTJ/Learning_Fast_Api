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


def test_read_users(client):

    response = client.get('/users',)

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': [
        {
        'username': 'test',
        'email': 'test@test.com',
        'id': 1}
    ]}


def test_update_user(client):

    response = client.put('/users/1', json={
        'username': 'testou',
        'email': 'testou@test.com',
        'password': 'test1234'
    })

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'id': 1,
        'username': 'testou',
        'email': 'testou@test.com',
    }  # Assert


def test_update_user_not_found(client):

    response = client.put('/users/2', json={
        'username': 'testou',
        'email': 'testou@test.com',
        'password': 'test1234'
    })

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):

    response = client.delete('/users/1')

    response2 = client.delete('/users/10')

    assert response.status_code == HTTPStatus.OK

    assert response2.status_code == HTTPStatus.NOT_FOUND
