from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config.env_variables import get_env_vars

env = get_env_vars()

class NotFoundError(Exception):
    pass


class Base(DeclarativeBase):
    pass


engine = create_engine(env.DB_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    database = session_local()
    try:
        return database
    finally:
        database.close()
