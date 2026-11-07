from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="DK Calculator API",
    description="Simple calculator built using FastAPI",
    version="1.0.0"
)


class CalculationRequest(BaseModel):
    num1: float
    num2: float


class CalculationResponse(BaseModel):
    num1: float
    num2: float
    operation: str
    result: float


@app.get("/")
def home():
    return {
        "message": "Calculator API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/add", response_model=CalculationResponse)
def add(data: CalculationRequest):
    return {
        "num1": data.num1,
        "num2": data.num2,
        "operation": "addition",
        "result": data.num1 + data.num2
    }


@app.post("/subtract", response_model=CalculationResponse)
def subtract(data: CalculationRequest):
    return {
        "num1": data.num1,
        "num2": data.num2,
        "operation": "subtraction",
        "result": data.num1 - data.num2
    }


@app.post("/multiply", response_model=CalculationResponse)
def multiply(data: CalculationRequest):
    return {
        "num1": data.num1,
        "num2": data.num2,
        "operation": "multiplication",
        "result": data.num1 * data.num2
    }


@app.post("/divide", response_model=CalculationResponse)
def divide(data: CalculationRequest):

    if data.num2 == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )

    return {
        "num1": data.num1,
        "num2": data.num2,
        "operation": "division",
        "result": data.num1 / data.num2
    }


@app.post("/modulus", response_model=CalculationResponse)
def modulus(data: CalculationRequest):

    if data.num2 == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot calculate modulus with zero"
        )

    return {
        "num1": data.num1,
        "num2": data.num2,
        "operation": "modulus",
        "result": data.num1 % data.num2
    }


@app.post("/power", response_model=CalculationResponse)
def power(data: CalculationRequest):
    return {
        "num1": data.num1,
        "num2": data.num2,
        "operation": "power",
        "result": data.num1 ** data.num2
    }# from typing import Literal

# from fastapi import FastAPI, HTTPException


# app = FastAPI(title="Calculator API")


# @app.get("/")
# def read_root():
# 	return {"message": "Calculator API", "documentation": "/docs"}


# @app.get("/calculate")
# def calculate(
# 	operation: Literal["add", "subtract", "multiply", "divide"],
# 	a: float,
# 	b: float,
# ):
# 	if operation == "add":
# 		result = a + b
# 	elif operation == "subtract":
# 		result = a - b
# 	elif operation == "multiply":
# 		result = a * b
# 	else:
# 		if b == 0:
# 			raise HTTPException(status_code=400, detail="Cannot divide by zero")
# 		result = a / b

# 	return {"operation": operation, "a": a, "b": b, "result": result}
