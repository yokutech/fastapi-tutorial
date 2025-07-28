from fastapi import FastAPI
from pydantic import BaseModel

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


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"User ID is {user_id}"}


@app.get("/search")
def search_items(q: str, limit: int = 10):
    return {"query": q, "limit": limit}


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.post("/items")
def create_item(item: Item):
    return {"item": item}
