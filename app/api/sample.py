from fastapi import APIRouter

router = APIRouter(prefix="/sample", tags=["Sample"])

@router.get("/")
def get_sample():
    return {
        "topic": "FastAPI Basics",
        "description": "This is a sample GET endpoint returning json."
    }
