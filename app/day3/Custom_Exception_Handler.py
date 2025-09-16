from fastapi import  Request, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/custom_exception",
    tags=["Custom Exception"]
)
class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something wrong."}
    )

@router.get("/custom/{name}")
def get_custom(name: str):
    if name == "bad":
        raise CustomException(name)
    return {"name": name}