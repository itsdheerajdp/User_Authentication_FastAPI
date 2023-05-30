from database import Base
from sqlalchemy import Column,String,Integer 
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,index=True,primary_key=True)
    name = Column(String)
    email = Column(String,unique=True)
    password=Column(String)
