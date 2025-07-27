# FastAPI Tutorial

## Getting Started

Make sure you have [pyenv](https://github.com/pyenv/pyenv) on your system.

### 1. Create Virtual Environment

```sh
pyenv virtualenv 3.11.0 my_fastapi_env
```

### 2. Activate Environment & Install Dependencies

```sh
pyenv activate my_fastapi_env
pip install fastapi uvicorn
```

### 3. Run the Server

Make sure you are in the directory where `main.py` is located, then run:

```sh
uvicorn main:app --reload
```

### 4. Access the API

- Visit http://127.0.0.1:8000 to test the API.
- Visit http://127.0.0.1:8000/docs for the Swagger UI.
- Visit http://127.0.0.1:8000/redoc for the ReDoc documentation.
