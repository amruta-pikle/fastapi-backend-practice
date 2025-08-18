from fastapi import Depends,HTTPException,status,APIRouter
from .auth import oauth2_schema

router = APIRouter(
    prefix="/day2",
    tags=["Token_Generation"]
)

# Protected Route
@router.get("/secured-data")
def read_secure_date(token: str = Depends(oauth2_schema)):
    if token!= "amruta":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return {"message": "This is protected data accessible only with a valid token"}