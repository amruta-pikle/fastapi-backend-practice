from fastapi import APIRouter
import time

router = APIRouter(
    prefix="/middleware", tags=["Middleware"]
)

@router.get("/")
async def home():
    return {"msg": "Hello from middleware router"}

@router.get("/slow")
async def slow():
    time.sleep(2)
    return {"msg": "This took time"}