from sqlalchemy import Column, Integer, String

from db import Base


class Users(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String)
