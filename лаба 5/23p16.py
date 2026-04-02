from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
import re

app = FastAPI()

# Хранилище отзывов
feedbacks = []

# Запрещённые слова
BAD_WORDS = ["дурак", "лох", "идиот"]


class Contact(BaseModel):
    email: EmailStr
    phone: Optional[str] = None

    @validator("phone")
    def validate_phone(cls, value):
        if value is None:
            return value
        if not re.fullmatch(r"\d{7,15}", value):
            raise ValueError("Phone must contain only digits (7-15)")
        return value


class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    contact: Contact

    @validator("message")
    def check_bad_words(cls, value):
        lower_message = value.lower()
        for word in BAD_WORDS:
            if word in lower_message:
                raise ValueError("Сообщение содержит запрещённые слова")
        return value


@app.post("/feedback")
def create_feedback(
    feedback: Feedback,
    is_premium: bool = Query(False)
):

    feedbacks.append(feedback)

    response_message = f"Спасибо, {feedback.name}! Ваш отзыв сохранён."

    if is_premium:
        response_message += " Ваш отзыв будет рассмотрен в приоритетном порядке."

    return {"message": response_message}


@app.get("/feedback")
def get_feedbacks() -> List[Feedback]:
    return feedbacks