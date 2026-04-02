from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import re

app = FastAPI()

# Хранилище отзывов
feedbacks = []


class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def check_bad_words(cls, value):
        bad_words = ["дурак", "лох", "идиот"]

        for word in bad_words:
            if re.search(word, value.lower()):
                raise ValueError("Использование недопустимых слов")

        return value


@app.post("/feedback")
def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)

    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }


@app.get("/feedback")
def get_feedbacks():
    return feedbacks