from sqlalchemy import Column, Integer, String
from database.database import Base
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    username = Column(String,
                      unique=True)
    password = Column(String)
    tokens = relationship("TokenModel", 
                          back_populates="user")
    


