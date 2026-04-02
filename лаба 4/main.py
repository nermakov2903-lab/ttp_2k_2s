from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Pydantic-модель
class Feedback(BaseModel):
    name: str
    message: str


feedback_storage: list[Feedback] = []

@app.post("/feedback")
def receive_feedback(feedback: Feedback):
    # Сохраняем отзыв
    feedback_storage.append(feedback)

    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }