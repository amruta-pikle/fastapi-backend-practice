from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/taskmanager',
    tags=['Task Manager']
)

users = {
    'amruta': {
        'username': 'amruta',
        'password': 'password1234',
        'role': 'admin'
    },
    'abhay': {
        'username': 'abhay',
        'password': 'password1122',
        'role': 'user'
    }
}

oauth2_schema = OAuth2PasswordBearer('/taskmanager/token')


@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_name = users.get(form_data.username)
    if not user_name or user_name['password'] != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credential",
            headers={"WWW-Authenticate": "Bearer"}
        )


    return {"access_token": user_name["username"], "role": user_name['role'], "token_tyoe": "bearer"}


def get_current_user(token: str = Depends(oauth2_schema)):
    for user in users.values():
        if user['username'] == token:
            return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authorised token",
        headers={"WWW-Authenticate": "Bearer"}
    )
