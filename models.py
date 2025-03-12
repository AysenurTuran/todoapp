from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class ToDo(Base):
    __tablename__='todos'

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    description = Column(String(1000))
    priority = Column(Integer)
    completed = Column(Boolean,default=False)
    owner_id = Column(Integer,ForeignKey('users.id'))

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True,index=True)
    username = Column(String,unique=True)
    hashed_password = Column(String)
    email=Column(String,unique=True)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean,default=True)
    role = Column(String)
    phone_number = Column(String)