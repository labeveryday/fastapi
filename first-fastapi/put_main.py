# Receive body from PUT
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


# Load fastapi
app = FastAPI()

# Write a comment about this code block:
# This code block is used to define a Pydantic model for the Item class. The Pydantic model defines the fields of the Item class, their data types, and any validation rules.
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "Family"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    curl -X 'PUT' \
    'http://127.0.0.1:8000/items/7' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{ \
    "name": "string", \
    "price": 0, \
    "is_offer": true \
    }'
    """
    item.
    return {"item_name": item.name, "item_id": item_id}
