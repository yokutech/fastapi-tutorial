from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {
    "message": "Hello, FastAPI!"
  }

@app.get("/greet")
def greet(name: str = "Guest"):
  return {
    "message": f"Hello, ${name}!"
  }
