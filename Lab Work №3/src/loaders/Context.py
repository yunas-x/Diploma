from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./logs.db"

# Engine for DataBase Sessions
Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Default Session Generator
# SessionMaker() -> Session
SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
