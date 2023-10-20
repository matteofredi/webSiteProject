from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL: str = f'postgresql://user:abc@localhost:5000/stuff'

engine = create_engine(url=DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except exc.DatabaseError:
        db.rollback()
    finally:
        db.close()
