from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint

from core import database


class User(database.Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True)
    username = Column(String(length=50), nullable=False, unique=True)
    hashed_password = Column(String, nullable=False, unique=True)
    salt = Column(String, nullable=False, unique=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='id_primary_key_constraint'),
    )
