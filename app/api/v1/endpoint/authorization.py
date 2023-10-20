# AUTHORIZATION MODULE
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from models import user_model
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password, salt):
    return pwd_context.verify(plain_password + salt, hashed_password)


def get_password_hash(password: str, salt: str):
    return pwd_context.hash(password + salt)


def verify_user(username: str, password: str):
    user: user_model.User | None = None
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')

    if not verify_password(plain_password=password, hashed_password=user.hashed_password, salt=user.salt):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Credentials')

