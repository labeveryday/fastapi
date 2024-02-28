from enum import Enum

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel



app = FastAPI()


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


# Normally this would be a database
items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Screwdriver", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}


# Function parameters that are not path parameters can be specified as query parameters 
# Here we can query items like this /items?count=20
Selection = dict[
    str, str | int | float | Category | None
]  # dictionary containing the user's query arguments

# FastAPI handles JSON serialization and deserialization for us.
# We can simply use built-in python and Pydantic types, in this case dict[int, Item]
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

# Lookup an item by its id. If it's not found, raise an HTTPException with a 404 status code and a detail message.
@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} was not found")
    return items[item_id]

# Using query parameters to filter items by category. If no category is provided, return all items.
@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None, 
    price: float | None = None, 
    count: int | None = None, 
    category: Category | None = None
) -> dict[str, Selection]:
    # Helper function
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )
    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }
