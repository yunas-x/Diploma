import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connection string
SQLALCHEMY_DATABASE_URL = os.getenv('POSTGRES_CONNECTION_STRING')

# Engine for DataBase Sessions
Engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Default Session Generator
# SessionMaker() -> Session
SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
