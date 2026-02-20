from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/calculate")
def calculate(data: Numbers):
    return {"result": data.num1 + data.num2}