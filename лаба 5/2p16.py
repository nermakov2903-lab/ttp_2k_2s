# проверка в endpoint
#/////////////////////////

# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class User(BaseModel):
#     name: str
#     age: int
#
# @app.post("/user")
# def create_user(user: User):
#     is_adult = user.age >= 18
#     return {
#         "name": user.name,
#         "age": user.age,
#         "is_adult": is_adult
#     }
#

#Отдельная функция проверки
#//////////////////////////


# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class User(BaseModel):
#     name: str
#     age: int
#
# def is_user_adult(age: int) -> bool:
#     return age >= 18
#
# @app.post("/user")
# def create_user(user: User):
#     return {
#         "name": user.name,
#         "age": user.age,
#         "is_adult": is_user_adult(user.age)
#     }


#Использование Response Model
#///////////////////////////////

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

class UserResponse(User):
    is_adult: bool

@app.post("/user", response_model=UserResponse)
def create_user(user: User):
    return UserResponse(
        name=user.name,
        age=user.age,
        is_adult=user.age >= 18
    )