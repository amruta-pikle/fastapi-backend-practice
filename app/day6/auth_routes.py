from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from .auth_utils import create_access_token, decode_access_token
from .schemas import LoginRequest, TokenResponse

router = APIRouter(
    prefix="/auth-example",
    tags = ["Authentication Example"]
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl= "/auth-example/login")

fake_user = {
    'username' :'amruta',
    'password' : 'test123'
}

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    if request.username == fake_user['username'] and request.password == fake_user['password']:
        token = create_access_token({"sub" : request.username})
        return {"access_token": token}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

@router.get("/protected")
def protected_route(token: str = Depends(oauth2_schema)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or Expired token")
    return {"message": f"Hello {payload['sub']}, you accessed a protected route!"}
