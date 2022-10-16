from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from user_management.core.config import settings

engine: Engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
