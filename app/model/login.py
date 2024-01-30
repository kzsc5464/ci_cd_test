from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Sequence

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Colu