from http import HTTPStatus

from fastapi import FastAPI

from learning_fast_api.schemas import Message, User, UserDB, UserPublic

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: User):
    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )
    database.append(user_with_id)

    return user_with_id
