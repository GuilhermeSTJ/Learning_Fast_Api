from http import HTTPStatus

from fastapi import FastAPI

from learning_fast_api.schemas import (
    Count,
    CountSaida,
    Message,
    User,
    UserDB,
    UserPublic,
)

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


@app.post('/count', status_code=HTTPStatus.CREATED)
def conta_valores(conta: Count):
    conta_valores = CountSaida(
        out_value=conta.in_value1 + conta.in_value2,
        **conta.model_dump()
    )
    return conta_valores

@app.get('/users', status_code=HTTPStatus.OK)	
def read_users():    
    return {'users': database}