# main.py

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()
data = [
    {
        "name": "item1",
        "description": "description items1",
        "price": 8900,
        "tax": 12.30
    },
    {
        "name": "item2",
        "description": "description items2",
        "price": 8000,
        "tax": 11.30
    },
    {
        "name": "item3",
        "description": "description items3",
        "price": 9900,
        "tax": 15.30
    },
]


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/{item_id}")
async def root(item_id):
    result = data[int(item_id)]
    return {"message": "Hello World", "result": result}
