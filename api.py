from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI(
    title="AI Agent Calculator API",
    description="Python API used by n8n AI Agent",
    version="1.0"
)


# Request model
class CalculationRequest(BaseModel):
    operation: Literal[
        "add",
        "subtract",
        "multiply",
        "divide"
    ]

    a: float
    b: float


# Health check API
@app.get("/")
def home():
    return {
        "message": "Python Calculator API is running"
    }


# Calculator API
@app.post("/calculate")
def calculate(request: CalculationRequest):

    a = request.a
    b = request.b
    operation = request.operation

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":

        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )

        result = a / b

    return {
        "operation": operation,
        "number1": a,
        "number2": b,
        "result": result
    }
