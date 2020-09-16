from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()N 

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@router.get("/", tags=["items"])
def read_root():
    return {"msg": "Hello World"}

@router.get("/items/{item_id}", tags=["items"])
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
