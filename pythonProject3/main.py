from fastapi import FastAPI
from models import User

app = FastAPI()

# Создаём экземпляр пользователя
user = User(
    name="John Doe",
    id=1
)

# Маршрут для получения данных пользователя
@app.get("/users")
def get_user():
    return user