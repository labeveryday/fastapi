from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Run the app - uvicorn main:app --reload

# http://127.0.0.1:8000

# http://127.0.0.1:8000/items/5?q=somequery

# Read Docs: http://127.0.0.1:8000/docs#/

# Additional docs: http://127.0.0.1:8000/redoc
