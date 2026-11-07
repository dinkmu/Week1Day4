from fastapi import FastAPI

app = FastAPI(
    title="DK's First FastAPI",
    description="A simple beginner FastAPI project",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DK's First FastAPI!"
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!",
        "name": name
    }