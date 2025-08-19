from typing import List

from fastapi import APIRouter, HTTPException
from app.day1.models import ItemOut, ItemIn

router = APIRouter(
    prefix="/day1",
    tags=["Model examples"]
)

#In-memory "database"
fake_db = {}
id_counter = 1

@router.post("/items",response_model=ItemOut)
def create_item(item : ItemIn):
    """
        Create a new item and store it in the fake database.
    """
    global id_counter
    fake_db[id_counter] = item
    return ItemOut(id=id_counter, **item.model_dump())

@router.get("/items", response_model=List[ItemOut])
def get_all_items():
    """
        Get a list of all items in the fake database
    """
    return [ItemOut(id=id_counter,**item.model_dump()) for item_id, item in fake_db.items()]

@router.get("/items/{item_id}", response_model=ItemOut)
def get_Item(item_id : int):
    """
        Get a single item by its ID
    """
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemOut(id=item_id, **fake_db[item_id].dict())

@router.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item : ItemIn):
    """
        Update an existing item by ID.
    """
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return ItemOut(id=item_id, **item.model_dump())

@router.delete("/items/{item_id}")
def delete_item(item_id : int):
    """
        Delete an item by ID.
    """

    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": f"item{item_id} deleted successfully"}

