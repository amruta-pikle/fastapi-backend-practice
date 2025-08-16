from pydantic import BaseModel
from typing import Optional

# Request model for creating/updating an item
class ItemIn(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# Response model for sending item details back
class ItemOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float