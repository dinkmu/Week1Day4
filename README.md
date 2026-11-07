# DK Calculator

DK Calculator is a simple REST API built with FastAPI. It uses a single `/calculate` endpoint so you can test addition, subtraction, multiplication, and division easily from Postman.

## Features

- Addition, subtraction, multiplication, and division
- Single Postman-friendly calculation endpoint
- JSON request and response
- Request validation with Pydantic
- Division-by-zero handling
- Invalid-operation handling
- Health-check endpoint
- Interactive Swagger UI documentation
- ReDoc API documentation

## Technologies

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- Postman

## Project Structure

```text
dk-calculator/
├── main.py
├── README.md
└── requirements.txt
```

## Requirements

Verify that Python 3 is installed:

```bash
python3 --version
```

## Installation

### 1. Open the project directory

```bash
cd dk-calculator
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

#### macOS or Linux

```bash
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
fastapi
uvicorn[standard]
```

## Run DK Calculator

Start the development server from the folder containing `main.py`:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Keep the terminal open while testing the API.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Returns application information |
| `GET` | `/health` | Checks the API health status |
| `POST` | `/calculate` | Performs a calculation |

## Test with Postman

### Request settings

- Method: `POST`
- URL: `http://127.0.0.1:8000/calculate`
- Body type: `raw`
- Content type: `JSON`

In Postman, select **Body > raw > JSON**, paste one of the sample requests below, and select **Send**.

## Supported Operations

| Operation | JSON value | Example | Result |
|---|---|---|---|
| Addition | `add` | 10 + 5 | 15 |
| Subtraction | `subtract` | 10 - 5 | 5 |
| Multiplication | `multiply` | 10 x 5 | 50 |
| Division | `divide` | 10 / 5 | 2 |

Operation values are case-insensitive. For example, `add`, `Add`, and `ADD` are accepted.

## Addition Example

### Request

```json
{
  "number1": 10,
  "number2": 5,
  "operation": "add"
}
```

### Response

```json
{
  "number1": 10.0,
  "number2": 5.0,
  "operation": "add",
  "result": 15.0
}
```

## Subtraction Example

### Request

```json
{
  "number1": 100,
  "number2": 25,
  "operation": "subtract"
}
```

### Response

```json
{
  "number1": 100.0,
  "number2": 25.0,
  "operation": "subtract",
  "result": 75.0
}
```

## Multiplication Example

### Request

```json
{
  "number1": 20,
  "number2": 5,
  "operation": "multiply"
}
```

### Response

```json
{
  "number1": 20.0,
  "number2": 5.0,
  "operation": "multiply",
  "result": 100.0
}
```

## Division Example

### Request

```json
{
  "number1": 100,
  "number2": 4,
  "operation": "divide"
}
```

### Response

```json
{
  "number1": 100.0,
  "number2": 4.0,
  "operation": "divide",
  "result": 25.0
}
```

## Error Handling

### Division by zero

Request:

```json
{
  "number1": 100,
  "number2": 0,
  "operation": "divide"
}
```

Response with HTTP status `400 Bad Request`:

```json
{
  "detail": "Cannot divide by zero"
}
```

### Invalid operation

Request:

```json
{
  "number1": 10,
  "number2": 5,
  "operation": "hello"
}
```

Response with HTTP status `400 Bad Request`:

```json
{
  "detail": "Invalid operation. Use add, subtract, multiply, or divide."
}
```

### Invalid request body

FastAPI validates incoming data with Pydantic. Missing fields or invalid number values return HTTP status `422 Unprocessable Entity`.

## API Documentation

After starting the server, open the following pages in a browser:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Swagger UI also provides a **Try it out** button for testing the API without Postman.

## Health Check

Send:

```http
GET http://127.0.0.1:8000/health
```

Response:

```json
{
  "status": "healthy"
}
```

## Author

Dineshkumar K

## License

This project is intended for learning and demonstration purposes.
