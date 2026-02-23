from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Pydantic-модель для обратной связи
class Feedback(BaseModel):
    name: str
    message: str

# 4. Хранилище для всех полученных отзывов (в памяти)
feedback_storage: list[Feedback] = []

# 2–3. POST-конечная точка для приёма отзывов
@app.post("/feedback")
def receive_feedback(feedback: Feedback):
    # Сохраняем отзыв
    feedback_storage.append(feedback)

    # Возвращаем сообщение об успешном приёме
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }