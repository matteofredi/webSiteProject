import secrets
from typing import Type

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import user_model
from schemas import user_schema


def get_user_by_username(username: str, db: Session) -> Type[user_model.User]:
    user = db.get(user_model.User, {'username': username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return user


def create_user(user_data: user_schema.UserCreate, db: Session) -> user_model.User:
    random_salt: str = secrets.token_hex(12)
    hashed_password: str = user_data.password + 'fake_hashed_password'

    user_obj = user_model.User(username=user_data.username, hashed_password=hashed_password, salt=random_salt)

    db.add(user_obj)

    return user_obj


def delete_user(username: str, db: Session) -> Type[user_model.User]:
    user = get_user_by_username(username=username, db=db)

    db.delete(user)

    return user
