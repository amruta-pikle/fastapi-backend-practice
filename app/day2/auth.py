from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/day2",
    tags=["Token_Generation"]
)

# In-memory user store (for demo)
fake_users_db={
    "amruta" : {
        "username": "amruta",
        "password": "password123"
    }
}

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/day2/token")

# Route to generate token
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict or user_dict["password"]!= form_data.password:
        raise  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

    #For demo: token = username
    return {"access_token": user_dict["username"], "token_tyoe": "bearer"}